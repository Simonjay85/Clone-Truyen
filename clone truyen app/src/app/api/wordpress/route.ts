/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable @typescript-eslint/ban-ts-comment */
// @ts-nocheck
import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  try {
    const { wpUrl, wpUser, wpAppPassword, endpoint, method = 'POST', payload } = await req.json();

    if (!wpUrl || !wpUser || !wpAppPassword || !endpoint) {
      return NextResponse.json({ error: 'Missing WordPress Connection Settings' }, { status: 400 });
    }

    const cleanUrl = wpUrl.replace(/\/$/, "");
    const fetchUrl = `${cleanUrl}/wp-json/wp/v2/${endpoint}`;
    
    const authHeaders = new Headers();
    if (wpAppPassword.startsWith('M-CORE-')) {
      authHeaders.set('X-Mac-Core-Token', wpAppPassword);
    } else {
      authHeaders.set('Authorization', 'Basic ' + Buffer.from(wpUser + ":" + wpAppPassword).toString('base64'));
    }
    authHeaders.set('Content-Type', 'application/json');

    // Nếu payload chứa the_loai (array tên), resolve sang IDs
    let finalPayload = payload;
    if (payload && Array.isArray(payload.the_loai) && payload.the_loai.length > 0 && method !== 'GET') {
      const termIds: number[] = [];
      for (const termName of payload.the_loai) {
        try {
          // Tìm term theo tên
          const searchRes = await fetch(
            `${cleanUrl}/wp-json/wp/v2/the_loai?search=${encodeURIComponent(termName)}&per_page=5`,
            { headers: authHeaders }
          );
          if (searchRes.ok) {
            const terms = await searchRes.json();
             
            const found = Array.isArray(terms) && terms.find((t: unknown) =>
              t.name?.toLowerCase() === termName.toLowerCase() || t.slug === termName.toLowerCase()
            );
            if (found) {
              termIds.push(found.id);
            } else {
              // Tạo term mới nếu chưa có
              const createRes = await fetch(`${cleanUrl}/wp-json/wp/v2/the_loai`, {
                method: 'POST',
                headers: authHeaders,
                body: JSON.stringify({ name: termName }),
              });
              if (createRes.ok) { const newTerm = await createRes.json(); termIds.push(newTerm.id); }
            }
          }
        } catch {}
      }
      finalPayload = { ...payload, the_loai: termIds };
    }

    const options: RequestInit = { method, headers: authHeaders };
    if (finalPayload && method !== 'GET') {
      options.body = JSON.stringify(finalPayload);
    }

    const response = await fetch(fetchUrl, options);
    
    if (!response.ok) {
      const respText = await response.text();
      throw new Error(`WP API Error ${response.status}: ${respText}`);
    }

    const data = await response.json();
    return NextResponse.json(data);
  } catch (error: any) {
    console.error('WP API Error:', error);
    return NextResponse.json({ error: (error as any).message || 'Unknown WP Error' }, { status: 500 });
  }
}
