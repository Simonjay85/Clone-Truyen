import { NextResponse } from 'next/server';
import fs from 'fs/promises';
import path from 'path';

// Luôn đảm bảo mcore_db.json nằm ở thư mục root/data
const DB_PATH = path.join(process.cwd(), 'data', 'mcore_db.json');

export const dynamic = 'force-dynamic';

// Write lock đơn giản: ngăn GET đọc file lúc POST đang ghi atomic (tmp → rename)
let isWriting = false;

export async function GET() {
  // Nếu engine đang ghi → đợi 300ms rồi mới đọc, tránh đọc file rỗng/corrupt
  if (isWriting) {
    await new Promise(r => setTimeout(r, 300));
  }

  try {
    // Đảm bảo thư mục "data" tồn tại
    try {
      await fs.access(path.join(process.cwd(), 'data'));
    } catch {
      await fs.mkdir(path.join(process.cwd(), 'data'), { recursive: true });
    }

    try {
      const data = await fs.readFile(DB_PATH, 'utf-8');
      if (!data.trim()) throw new Error('File rỗng cục bộ');
      return NextResponse.json({ success: true, data: JSON.parse(data) });
    } catch (e: unknown) {
      if (e instanceof Error && (e as NodeJS.ErrnoException).code === 'ENOENT') {
        return NextResponse.json({ success: true, data: null });
      }
      return NextResponse.json({ success: false, error: e instanceof Error ? e.message : String(e) }, { status: 500 });
    }
  } catch (error: unknown) {
    return NextResponse.json({ success: false, error: error instanceof Error ? error.message : String(error) }, { status: 500 });
  }
}

export async function POST(req: Request) {
  isWriting = true;
  try {
    const body = await req.json();

    try {
      await fs.access(path.join(process.cwd(), 'data'));
    } catch {
      await fs.mkdir(path.join(process.cwd(), 'data'), { recursive: true });
    }

    const tmpPath = DB_PATH + '.' + Date.now() + Math.random() + '.tmp';
    await fs.writeFile(tmpPath, JSON.stringify(body, null, 2), 'utf-8');
    await fs.rename(tmpPath, DB_PATH);

    return NextResponse.json({ success: true });
  } catch (error: unknown) {
    return NextResponse.json({ success: false, error: error instanceof Error ? error.message : String(error) }, { status: 500 });
  } finally {
    // Luôn release lock dù thành công hay lỗi
    isWriting = false;
  }
}
