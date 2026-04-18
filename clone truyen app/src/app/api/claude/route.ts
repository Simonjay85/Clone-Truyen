import { NextResponse } from 'next/server';

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const { apiKey, systemPrompt, userPrompt, temperature = 0.7, model = 'claude-3-5-sonnet-20241022' } = body;

    if (!apiKey) return NextResponse.json({ error: 'Missing Claude API Key' }, { status: 400 });

    let fallbackChain = [model];
    if (model.includes('sonnet')) {
       fallbackChain = [
           'claude-sonnet-4-5',
           'claude-3-7-sonnet-20250219',
           'claude-3-5-sonnet-20241022',
           'claude-3-5-sonnet-20240620',
       ];
    } else if (model.includes('haiku')) {
       fallbackChain = ['claude-haiku-4-5', 'claude-3-5-haiku-20241022'];
    }

    let lastError: any = null;
    let data: any = null;
    let ok = false;

    for (let m of fallbackChain) {
        console.log("[Claude API] Trying model:", m);
        const response = await fetch('https://api.anthropic.com/v1/messages', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-api-key': apiKey,
            'anthropic-version': '2023-06-01'
          },
          body: JSON.stringify({
            model: m,
            max_tokens: 8192,
            temperature: temperature,
            system: systemPrompt,
            messages: [
              { role: 'user', content: userPrompt }
            ]
          })
        });

        data = await response.json();
        if (response.ok) {
            ok = true;
            break;
        } else {
            const msg = data.error?.message || JSON.stringify(data);
            console.warn(`[Claude API] ❌ model=${m} failed: ${msg}`);
            lastError = data;
            
            // If it's authentication or credit error, stop trying
            if (msg.includes('credit') || msg.includes('balance') || msg.includes('authentication')) {
                break;
            }
        }
    }

    if (!ok) {
        const errMsg = lastError?.error?.message || JSON.stringify(lastError);
        console.error('[Claude API] All models failed. Last error:', errMsg);
        return NextResponse.json({ error: `model: ${fallbackChain[fallbackChain.length-1]} — ${errMsg}` }, { status: 400 });
    }

    // Claude returns an array of content blocks
    const usage = data.usage ? {
        promptTokens: data.usage.input_tokens || 0,
        completionTokens: data.usage.output_tokens || 0,
        totalTokens: (data.usage.input_tokens || 0) + (data.usage.output_tokens || 0)
    } : undefined;

    return NextResponse.json({ text: data.content?.[0]?.text || '', usage, chosenModel: fallbackChain[fallbackChain.length-1] });
  } catch (error: any) {
    console.error('Claude Route Error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
