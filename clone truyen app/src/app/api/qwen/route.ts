/* eslint-disable @typescript-eslint/no-explicit-any */
import { NextResponse } from 'next/server';

export async function POST(req: Request) {
  try {
    const { apiKey, systemPrompt, userPrompt, model, jsonMode, temperature } = await req.json();

    if (!apiKey) {
      return NextResponse.json({ error: 'Missing Qwen API Key' }, { status: 400 });
    }

     
    const payload: any = {
      model: model || 'qwen-plus-character',
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt }
      ],
      temperature: temperature !== undefined ? temperature : 0.8,
      max_tokens: 8192,
    };

    if (jsonMode) {
      payload.response_format = { type: 'json_object' };
    }

    let response;
    let retries = 3;
    let lastError = null;

    while (retries > 0) {
      try {
        response = await fetch('https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
          },
          body: JSON.stringify(payload)
        });
        
        if (response.ok || response.status === 400 || response.status === 401 || response.status === 403 || response.status === 429) {
           break; // Stop retrying if successful or if it's a definitive Auth/Quota/Bad-Request error
        }
      } catch (err) {
        lastError = err;
      }
      retries--;
      if (retries > 0) await new Promise(resolve => setTimeout(resolve, 2000)); // wait 2s before retry
    }

    if (!response) {
       throw lastError || new Error('Network failure after 3 retries');
    }

    if (!response.ok) {
      let errorData;
      try { errorData = await response.json(); } catch { errorData = { error: response.statusText }; }
      return NextResponse.json({ error: errorData }, { status: response.status });
    }

    const data = await response.json();
    const content = data.choices[0]?.message?.content || '';

    const usage = data.usage ? {
        promptTokens: data.usage.prompt_tokens || 0,
        completionTokens: data.usage.completion_tokens || 0,
        totalTokens: data.usage.total_tokens || 0
    } : undefined;

    return NextResponse.json({ text: content, usage, chosenModel: payload.model });

  } catch (err: unknown) {
    console.error("[Qwen POST Error]:", err);
    return NextResponse.json({ error: err instanceof Error ? err.message : 'Internal Server Error' }, { status: 500 });
  }
}
