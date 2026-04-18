import { NextResponse } from 'next/server';

export async function POST(req: Request) {
  try {
    const { apiKey, systemPrompt, userPrompt, model, jsonMode, temperature } = await req.json();

    if (!apiKey) {
      return NextResponse.json({ error: 'Missing OpenAI API Key' }, { status: 400 });
    }

    const payload: any = {
      model: model || 'gpt-4o-mini',
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt }
      ],
      temperature: temperature !== undefined ? temperature : 0.8,
      max_tokens: 16000,
    };

    if (jsonMode) {
      payload.response_format = { type: 'json_object' };
    }

    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const errorData = await response.json();
      return NextResponse.json({ error: errorData }, { status: response.status });
    }

    const data = await response.json();
    const content = data.choices[0]?.message?.content || '';

    return NextResponse.json({ text: content });

  } catch (err: any) {
    console.error("[OpenAI POST Error]:", err);
    return NextResponse.json({ error: err.message || 'Internal Server Error' }, { status: 500 });
  }
}
