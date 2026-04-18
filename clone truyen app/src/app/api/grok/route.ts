import { NextResponse } from 'next/server';

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const { apiKey, systemPrompt, userPrompt, temperature = 0.9, jsonMode = false, model = 'grok-beta' } = body;

    if (!apiKey) return NextResponse.json({ error: 'Missing Grok API Key' }, { status: 400 });

    const response = await fetch('https://api.x.ai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        model: model,
        temperature: temperature,
        messages: [
          { role: 'system', content: systemPrompt },
          { role: 'user', content: userPrompt }
        ],
        response_format: jsonMode ? { type: "json_object" } : undefined
      })
    });

    const data = await response.json();

    if (!response.ok) {
        return NextResponse.json({ error: data.error?.message || JSON.stringify(data) }, { status: response.status });
    }

    return NextResponse.json({ text: data.choices[0].message.content });
  } catch (error: unknown) {
    console.error('Grok Route Error:', error);
    const errorMessage = error instanceof Error ? error.message : 'Internal Server Error';
    return NextResponse.json({ error: errorMessage }, { status: 500 });
  }
}
