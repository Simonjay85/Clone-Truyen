import { NextResponse } from 'next/server';
import fs from 'fs/promises';
import path from 'path';

// Luôn đảm bảo mcore_db.json nằm ở thư mục root/data
const DB_PATH = path.join(process.cwd(), 'data', 'mcore_db.json');

export async function GET() {
  try {
    // Đảm bảo thư mục "data" tồn tại
    try {
      await fs.access(path.join(process.cwd(), 'data'));
    } catch {
      await fs.mkdir(path.join(process.cwd(), 'data'), { recursive: true });
    }

    try {
      const data = await fs.readFile(DB_PATH, 'utf-8');
      return NextResponse.json({ success: true, data: JSON.parse(data) });
    } catch {
      // Nếu file chưa tồn tại, trả về rỗng không lỗi
      return NextResponse.json({ success: true, data: null });
    }
  } catch (error: any) {
    return NextResponse.json({ success: false, error: error.message }, { status: 500 });
  }
}

export async function POST(req: Request) {
  try {
    const body = await req.json();
    
    try {
      await fs.access(path.join(process.cwd(), 'data'));
    } catch {
      await fs.mkdir(path.join(process.cwd(), 'data'), { recursive: true });
    }

    await fs.writeFile(DB_PATH, JSON.stringify(body, null, 2), 'utf-8');
    return NextResponse.json({ success: true });
  } catch (error: any) {
    return NextResponse.json({ success: false, error: error.message }, { status: 500 });
  }
}
