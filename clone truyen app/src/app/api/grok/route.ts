import { NextResponse } from 'next/server';

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const { apiKey, systemPrompt, userPrompt, temperature = 0.9, jsonMode = false, model = 'grok-beta' } = body;

    if (!apiKey) return NextResponse.json({ error: 'Missing Grok API Key' }, { status: 400 });

    let finalSystemPrompt = systemPrompt || '';
    if (jsonMode) {
      const hasJsonKeyword = finalSystemPrompt.toLowerCase().includes('json') || (userPrompt || '').toLowerCase().includes('json');
      if (!hasJsonKeyword) {
          finalSystemPrompt += '\n\nPlease return JSON.';
      }
    }

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
          { role: 'system', content: finalSystemPrompt },
          { role: 'user', content: userPrompt }
        ],
        response_format: jsonMode ? { type: "json_object" } : undefined
      })
    });

    const data = await response.json();

    if (!response.ok) {
        return NextResponse.json({ error: data.error?.message || JSON.stringify(data) }, { status: response.status });
    }

    const usage = data.usage ? {
        promptTokens: data.usage.prompt_tokens || 0,
        completionTokens: data.usage.completion_tokens || 0,
        totalTokens: data.usage.total_tokens || 0
    } : undefined;

    return NextResponse.json({ text: data.choices[0].message.content, usage, chosenModel: model });
  } catch (error: unknown) {
    console.error('Grok Route Error:', error);
    const errorMessage = error instanceof Error ? error.message : 'Internal Server Error';
    return NextResponse.json({ error: errorMessage }, { status: 500 });
  }
}
