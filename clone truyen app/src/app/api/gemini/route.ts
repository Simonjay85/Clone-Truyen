import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  try {
    const { apiKey, apiKey2, apiKey3, systemPrompt, userPrompt, jsonMode, temperature = 0.7, model } = await req.json();

    if (!apiKey) {
      return NextResponse.json({ error: 'Missing Gemini API Key' }, { status: 400 });
    }

    const apiKeys = [apiKey, apiKey2, apiKey3].filter(k => !!k);
    
    let fallbackChain: string[] = [];
    const chosenModel = model || 'gemini-2.5-flash';
    
    if (chosenModel === 'gemini-2.5-pro' || chosenModel.includes('pro')) {
       fallbackChain = ['gemini-2.5-pro'];
    } else {
       fallbackChain = ['gemini-2.5-flash'];
    }
    
    let sysInstText = systemPrompt;
    if (jsonMode) {
      sysInstText += "\n\nCRITICAL RULE: YOU MUST RETURN A VALID JSON OBJECT OR ARRAY ONLY. DO NOT WRAP WITH MARKDOWN ```json. JUST RAW JSON FORMAT.";
    }

    let outText = '';
    let lastError: any = null;
    let lastData: any = null;

    outerLoop:
    for (let m = 0; m < fallbackChain.length; m++) {
        const currentModel = fallbackChain[m];
        for (let k = 0; k < apiKeys.length; k++) {
            const currentKey = apiKeys[k];
            try {
                console.log(`[Gemini API] Thử model=${currentModel} key=${k + 1}/${apiKeys.length}`);
                
                const url = `https://generativelanguage.googleapis.com/v1beta/models/${currentModel}:generateContent?key=${currentKey}`;
                
                const payload: any = {
                    contents: [{ role: 'user', parts: [{ text: userPrompt }] }],
                    generationConfig: {
                        temperature: temperature,
                        responseMimeType: jsonMode && currentModel !== 'gemini-pro' ? 'application/json' : 'text/plain',
                    }
                };

                // gemini-pro (1.0) does not support systemInstruction, so we append to user string or only send if not gemini-pro
                if (currentModel !== 'gemini-pro') {
                    payload.systemInstruction = { parts: [{ text: sysInstText }] };
                } else {
                    payload.contents[0].parts[0].text = `System Warning: ${sysInstText}\n\nUser Request: ${userPrompt}`;
                    delete payload.generationConfig.responseMimeType; // gemini-pro does not support JSON mode
                }

                const response = await fetch(url, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                
                const data = await response.json();
                lastData = data;
                
                if (response.ok && data.candidates && data.candidates[0]?.content?.parts?.[0]?.text) {
                    outText = data.candidates[0].content.parts[0].text;
                    console.log(`[Gemini API] ✅ Thành công với model=${currentModel} key=${k + 1}`);
                    break outerLoop;
                } else {
                    const errorMsg = data.error?.message || JSON.stringify(data);
                    console.warn(`[Gemini API] ❌ model=${currentModel} key=${k+1}: ${errorMsg.substring(0, 80)}...`);
                    lastError = data.error;
                    
                    if (errorMsg.includes('404') || errorMsg.includes('not found') || errorMsg.includes('support')) {
                        continue outerLoop; // Try next model
                    }
                    if (errorMsg.includes('400') && !errorMsg.includes('API key')) {
                        break outerLoop; 
                    }
                    // Quota or unavailable -> try next key (inner loop)
                }
            } catch (err: any) {
                lastError = err;
            }
        }
    }

    if (!outText) {
      let availableModels = "";
      try {
          const listRes = await fetch(`https://generativelanguage.googleapis.com/v1beta/models?key=${apiKeys[0]}`);
          const listData = await listRes.json();
          if (listData.models) {
              availableModels = "\\n🔥 BẤM OK RỒI CHỤP LẠI MÀN HÌNH NÀY GỬI CHO AI NHÉ \\nModel API Key hỗ trợ: " + listData.models.map((m: any) => m.name.replace('models/', '')).filter((n: string) => n.includes('gemini')).join(', ');
          } else {
             availableModels = "\\nLỗi lấy danh sách Model: " + JSON.stringify(listData);
          }
      } catch (e) {}
      
      const errOut = lastError?.message || lastError || "Failed";
      return NextResponse.json({ error: (typeof errOut === 'string' ? errOut : JSON.stringify(errOut)) + availableModels }, { status: 400 });
    }

    if (jsonMode) {
       outText = outText.replace(/```(?:json)?|```/g, '').trim();
    }

    return NextResponse.json({ text: outText, usage: lastData?.usageMetadata });
  } catch (error: any) {
    console.error('Gemini Route Error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
