import { NextRequest, NextResponse } from 'next/server';

const BYPASS_TOKEN = "ZEN_TRUYEN_2026_BYPASS";

async function callBypass(cleanUrl: string, method: string, endpoint: string, payload: any, signal?: AbortSignal) {
  const fetchUrl = `${cleanUrl}/api_truyen_bypass.php`;
  
  const options: RequestInit = {
    method: 'POST', // Luôn dùng POST khi gọi file PHP này để giấu dữ liệu
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      secret_token: BYPASS_TOKEN,
      method: method, // Phương thức thực sự của REST API (POST, GET, PUT)
      endpoint: endpoint,
      payload: payload
    })
  };
  
  if (signal) {
    options.signal = signal;
  }

  const res = await fetch(fetchUrl, options);
  
  if (!res.ok) {
    let errorText = await res.text();
    // Bắt trường hợp file PHP chưa được upload (trả về 404 HTML)
    if (res.status === 404 && errorText.includes('<html')) {
        errorText = "CHƯA UPLOAD FILE api_truyen_bypass.php lên host! Vui lòng upload file này lên thư mục gốc website.";
    }
    throw new Error(`Bypass API Error ${res.status}: ${errorText}`);
  }
  return res.json();
}

export async function POST(req: NextRequest) {
  try {
    const { wpUrl, endpoint, method = 'POST', payload } = await req.json();

    if (!wpUrl || !endpoint) {
      return NextResponse.json({ error: 'Missing WordPress Connection Settings' }, { status: 400 });
    }

    const cleanUrl = wpUrl.replace(/\/$/, "");

    // Xử lý tạo và ánh xạ thể loại (the_loai) sang ID
    let finalPayload = payload;
    if (payload && Array.isArray(payload.the_loai) && payload.the_loai.length > 0 && method !== 'GET') {
      const termIds: number[] = [];
      for (const termName of payload.the_loai) {
        try {
          const catController = new AbortController();
          const catTimeout = setTimeout(() => catController.abort(), 15000);
          
          // Gửi GET request qua file bypass để tìm thể loại
          const terms = await callBypass(
              cleanUrl, 
              'GET', 
              `the_loai?search=${encodeURIComponent(termName)}&per_page=5`, 
              null, 
              catController.signal
          );
          clearTimeout(catTimeout);
          
          const found = Array.isArray(terms) && terms.find((t: any) =>
            t.name?.toLowerCase() === termName.toLowerCase() || t.slug === termName.toLowerCase()
          );
          
          if (found) {
            termIds.push(found.id);
          } else {
            // Gửi POST request qua file bypass để tạo mới thể loại
            const createController = new AbortController();
            const createTimeout = setTimeout(() => createController.abort(), 15000);
            const newTerm = await callBypass(cleanUrl, 'POST', 'the_loai', { name: termName }, createController.signal);
            clearTimeout(createTimeout);
            
            if (newTerm && newTerm.id) {
                termIds.push(newTerm.id);
            }
          }
        } catch (e) {
          console.warn('WP Category Bypass Fetch Error:', e);
        }
      }
      finalPayload = { ...payload, the_loai: termIds };
    }

    // Gửi request thực sự (đăng truyện) qua bypass
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 30000); // 30 seconds

    const data = await callBypass(cleanUrl, method, endpoint, method !== 'GET' ? finalPayload : null, controller.signal);
    clearTimeout(timeoutId);

    return NextResponse.json(data);
  } catch (error: any) {
    console.error('WP Bypass API Error:', error);
    return NextResponse.json({ error: error.message || 'Unknown WP Error' }, { status: 500 });
  }
}
