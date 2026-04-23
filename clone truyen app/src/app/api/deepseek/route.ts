/* eslint-disable @typescript-eslint/no-explicit-any */
import { NextResponse } from 'next/server';

export const maxDuration = 300; // 5 minutes
export const dynamic = 'force-dynamic';
export async function POST(req: Request) {
  try {
    const { apiKey, systemPrompt, userPrompt, model, jsonMode, temperature } = await req.json();

    if (!apiKey) {
      return NextResponse.json({ error: 'Missing DeepSeek API Key' }, { status: 400 });
    }

    const payload: any = {
      model: model || 'deepseek-chat',
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt }
      ],
      temperature: temperature !== undefined ? temperature : 0.8,
      max_tokens: 8000,
    };

    if (jsonMode) {
      payload.response_format = { type: 'json_object' };
      const hasJsonKeyword = (systemPrompt || '').toLowerCase().includes('json') || (userPrompt || '').toLowerCase().includes('json');
      if (!hasJsonKeyword) {
        payload.messages[0].content = (payload.messages[0].content || '') + '\n\nPlease return JSON.';
      }
    }

    let response;
    let retries = 3;
    let lastError = null;

    while (retries > 0) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 120000); // 2 minutes timeout per request

        response = await fetch('https://api.deepseek.com/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
          },
          body: JSON.stringify(payload),
          signal: controller.signal
        });
        
        clearTimeout(timeoutId);
        
        if (response.ok || response.status === 400 || response.status === 401 || response.status === 403 || response.status === 429) {
           break;
        }
      } catch (err) {
        lastError = err;
      }
      retries--;
      if (retries > 0) await new Promise(resolve => setTimeout(resolve, 2000));
    }

    if (!response) {
       throw lastError || new Error('Network failure after 3 retries (Timeout or disconnect)');
    }

    if (!response.ok) {
      let errorData;
      try { errorData = await response.json(); } catch { errorData = { error: response.statusText }; }
      return NextResponse.json({ error: errorData }, { status: response.status });
    }

    const data = await response.json();
    
    if (!data) {
      throw new Error('DeepSeek returned an empty response (null)');
    }
    
    if (!data.choices || !Array.isArray(data.choices)) {
      throw new Error(`DeepSeek API Error: ${data.error ? JSON.stringify(data.error) : JSON.stringify(data)}`);
    }

    const content = data.choices[0]?.message?.content || '';

    const usage = data.usage ? {
        promptTokens: data.usage.prompt_tokens || 0,
        completionTokens: data.usage.completion_tokens || 0,
        totalTokens: data.usage.total_tokens || 0
    } : undefined;

    return NextResponse.json({ text: content, usage, chosenModel: payload.model });

  } catch (err: unknown) {
    console.error("[DeepSeek POST Error]:", err);
    return NextResponse.json({ error: err instanceof Error ? err.message : 'Internal Server Error' }, { status: 500 });
  }
}
