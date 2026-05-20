import { NextResponse } from 'next/server';

export async function POST(req: Request) {
  try {
    const { apiKey, prompt } = await req.json();

    if (!apiKey) {
      return NextResponse.json({ error: 'Missing OpenAI API Key' }, { status: 400 });
    }

    if (!prompt) {
      return NextResponse.json({ error: 'Missing prompt' }, { status: 400 });
    }

    // Call OpenAI DALL-E 3
    const response = await fetch('https://api.openai.com/v1/images/generations', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'dall-e-3',
        prompt: prompt,
        n: 1,
        size: '1792x1024',
        quality: 'standard',
        response_format: 'url'
      }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      return NextResponse.json({ error: errorData }, { status: response.status });
    }

    const data = await response.json();

    if (data.data && data.data.length > 0 && data.data[0].url) {
      return NextResponse.json({ imageUrl: data.data[0].url });
    } else {
      return NextResponse.json({ error: 'Không thể tạo ảnh từ OpenAI' }, { status: 500 });
    }

  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
