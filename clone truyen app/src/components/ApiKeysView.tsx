/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable @typescript-eslint/ban-ts-comment */
// @ts-nocheck
import React from 'react';
import { useStore } from '../store/useStore';
import { Key } from 'lucide-react';

export function ApiKeysView() {
  const {
    geminiKey, geminiKey2, geminiPaidKey, usePaidAPI, isFreeApiExhausted, 
    openAIKey, grokKey, claudeKey, qwenKey, deepseekKey, openRouterKey,
    setSettings 
  } = useStore();

  const [testResults, setTestResults] = React.useState<Record<string, string>>({});
  const [mounted, setMounted] = React.useState(false);

  React.useEffect(() => {
    setTimeout(() => setMounted(true), 0);
  }, []);

  const testKey = async (key: string, label: string) => {
    if (!key) return alert(`Chưa nhập ${label}!`);
    setTestResults(r => ({ ...r, [label]: '⏳ Đang kiểm tra...' }));
    try {
      const res = await fetch('/api/gemini', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          apiKey: key,
          systemPrompt: 'Be concise.',
          userPrompt: 'Say "OK" only.',
          model: 'gemini-2.0-flash'
        })
      });
      const data = await res.json();
      if (res.ok && data.text) {
        setTestResults(r => ({ ...r, [label]: '✅ HOẠT ĐỘNG - Key này còn quota!' }));
      } else {
        const msg = typeof data.error === 'object' ? JSON.stringify(data.error) : data.error;
        if (msg?.includes('429') || msg?.includes('quota')) {
          setTestResults(r => ({ ...r, [label]: '⛔ HẾT QUOTA hôm nay!' }));
        } else {
          setTestResults(r => ({ ...r, [label]: `❌ Lỗi: ${msg?.substring(0,60)}` }));
        }
      }
    } catch {
      setTestResults(r => ({ ...r, [label]: `❌ Không kết nối được` }));
    }
  };

  const testOpenAI = async () => {
    if (!openAIKey) return alert(`Chưa nhập OpenAI Key!`);
    setTestResults(r => ({ ...r, openai: '⏳ Đang kiểm tra OpenAI...' }));
    try {
      const res = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${openAIKey}`
        },
        body: JSON.stringify({
          model: 'gpt-4o-mini',
          messages: [{ role: 'user', content: 'Say OK' }],
          max_tokens: 5
        })
      });
      const data = await res.json();
      if (res.ok && data.choices) {
        setTestResults(r => ({ ...r, openai: '✅ HOẠT ĐỘNG (Valid Key)' }));
      } else {
        const msg = data.error?.message || JSON.stringify(data.error);
        if (msg.includes('quota') || msg.includes('insufficient')) {
          setTestResults(r => ({ ...r, openai: '⛔ HẾT TÀI KHOẢN (Out of Credits)' }));
        } else {
          setTestResults(r => ({ ...r, openai: `❌ Lỗi: ${msg.substring(0,60)}` }));
        }
      }
    } catch {
      setTestResults(r => ({ ...r, openai: `❌ Mất kết nối API` }));
    }
  };

  const testGrok = async () => {
    if (!grokKey) return alert(`Chưa nhập xAI (Grok) Key!`);
    setTestResults(r => ({ ...r, grok: '⏳ Đang kiểm tra Grok...' }));
    try {
      const res = await fetch('https://api.x.ai/v1/chat/completions', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${grokKey}`
        },
        body: JSON.stringify({
          model: 'grok-beta',
          messages: [{ role: 'user', content: 'Say OK' }],
          max_tokens: 5
        })
      });
      const data = await res.json();
      if (res.ok && data.choices) {
        setTestResults(r => ({ ...r, grok: '✅ HOẠT ĐỘNG (Valid Key)' }));
      } else {
        const msg = data.error?.message || JSON.stringify(data.error);
        if (msg.includes('quota') || msg.includes('balance') || msg.includes('insufficient')) {
          setTestResults(r => ({ ...r, grok: '⛔ HẾT TÀI KHOẢN (Out of Credits)' }));
        } else {
          setTestResults(r => ({ ...r, grok: `❌ Lỗi: ${msg.substring(0,60)}` }));
        }
      }
    } catch {
      setTestResults(r => ({ ...r, grok: `❌ Mất kết nối API` }));
    }
  };

  const testQwen = async () => {
    if (!qwenKey) return alert(`Chưa nhập Alibaba (Qwen) Key!`);
    setTestResults(r => ({ ...r, qwen: '⏳ Đang kiểm tra Qwen...' }));
    try {
      const res = await fetch('/api/qwen', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          apiKey: qwenKey,
          systemPrompt: 'Be concisce.',
          userPrompt: 'Say OK',
          model: 'qwen-max'
        })
      });
      if (res.ok) {
        setTestResults(r => ({ ...r, qwen: '✅ Kết nối Qwen DashScope thành công!' }));
      } else {
        const err = await res.json();
        setTestResults(r => ({ ...r, qwen: '❌ Lỗi: ' + (typeof err.error === 'string' ? err.error : (err.error?.message || err.message || JSON.stringify(err.error) || res.statusText)) }));
      }
    } catch {
      setTestResults(r => ({ ...r, qwen: '❌ Mất kết nối API' }));
    }
  };

  const testClaude = async () => {
    if (!claudeKey) return alert(`Chưa nhập Anthropic (Claude) Key!`);
    setTestResults(r => ({ ...r, claude: '⏳ Đang kiểm tra Claude...' }));
    try {
      const res = await fetch('/api/claude', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          apiKey: claudeKey,
          systemPrompt: 'Be concisce.',
          userPrompt: 'Say OK',
          model: 'claude-3-5-sonnet-20241022'
        })
      });
      const data = await res.json();
      if (res.ok && data.text) {
        setTestResults(r => ({ ...r, claude: '✅ HOẠT ĐỘNG (Valid Key)' }));
      } else {
        const msg = data.error?.message || data.error || JSON.stringify(data);
        if (typeof msg === 'string' && (msg.includes('balance') || msg.includes('credit') || msg.includes('billing'))) {
          setTestResults(r => ({ ...r, claude: '⛔ HẾT TÀI KHOẢN (Out of Credits)' }));
        } else {
          setTestResults(r => ({ ...r, claude: `❌ Lỗi: ${typeof msg === 'string' ? msg.substring(0,60) : 'Invalid Request'}` }));
        }
      }
    } catch {
      setTestResults(r => ({ ...r, claude: `❌ Mất kết nối API` }));
    }
  };

  const testDeepSeek = async () => {
    if (!deepseekKey) return alert(`Chưa nhập DeepSeek Key!`);
    setTestResults(r => ({ ...r, deepseek: '⏳ Đang kiểm tra DeepSeek...' }));
    try {
      const res = await fetch('/api/deepseek', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          apiKey: deepseekKey,
          systemPrompt: 'Be concisce.',
          userPrompt: 'Say OK',
          model: 'deepseek-chat'
        })
      });
      const data = await res.json();
      if (res.ok && data.text) {
        setTestResults(r => ({ ...r, deepseek: '✅ HOẠT ĐỘNG (Valid Key)' }));
      } else {
        let errorMsg = '';
        if (data.error && data.error.error && typeof data.error.error.message === 'string') {
           errorMsg = data.error.error.message;
        } else if (data.error && typeof data.error.message === 'string') {
           errorMsg = data.error.message;
        } else if (typeof data.error === 'string') {
           errorMsg = data.error;
        } else {
           errorMsg = JSON.stringify(data);
        }
        
        if (errorMsg.includes('balance') || errorMsg.includes('insufficient') || errorMsg.includes('payment')) {
           setTestResults(r => ({ ...r, deepseek: '❌ Lỗi: Cạn tiền (Hết quota)' }));
        } else {
           setTestResults(r => ({ ...r, deepseek: `❌ Lỗi: ${errorMsg.substring(0, 70)}` }));
        }
      }
    } catch {
      setTestResults(r => ({ ...r, deepseek: `❌ Mất kết nối API` }));
    }
  };

  const testOpenRouter = async () => {
    if (!openRouterKey) return alert(`Chưa nhập OpenRouter Key!`);
    setTestResults(r => ({ ...r, openrouter: '⏳ Đang kiểm tra OpenRouter...' }));
    try {
      const res = await fetch('/api/openrouter', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          apiKey: openRouterKey,
          systemPrompt: 'Be concise.',
          userPrompt: 'Say OK',
          model: 'liquid/lfm-40b:free'
        })
      });
      const data = await res.json();
      if (res.ok && data.text) {
        setTestResults(r => ({ ...r, openrouter: '✅ HOẠT ĐỘNG (Valid Key)' }));
      } else {
        let errorMsg = '';
        if (data.error && data.error.error && typeof data.error.error.message === 'string') {
           errorMsg = data.error.error.message;
        } else if (data.error && typeof data.error.message === 'string') {
           errorMsg = data.error.message;
        } else if (typeof data.error === 'string') {
           errorMsg = data.error;
        } else {
           errorMsg = JSON.stringify(data);
        }
        
        if (errorMsg.includes('balance') || errorMsg.includes('insufficient') || errorMsg.includes('payment') || errorMsg.includes('credits')) {
           setTestResults(r => ({ ...r, openrouter: '❌ Lỗi: Cạn tiền (Hết quota)' }));
        } else {
           setTestResults(r => ({ ...r, openrouter: `❌ Lỗi: ${errorMsg.substring(0, 70)}` }));
        }
      }
    } catch {
      setTestResults(r => ({ ...r, openrouter: `❌ Mất kết nối API` }));
    }
  };

  const { apiLogs = [], clearApiLogs } = useStore();
  const totalCost = apiLogs.reduce((acc, log) => acc + (log.cost || 0), 0);
  const totalTokens = apiLogs.reduce((acc, log) => acc + (log.totalTokens || 0), 0);
  const deepSeekCacheHitTokens = apiLogs.reduce((acc, log) => acc + ((log as any).promptCacheHitTokens || 0), 0);
  const deepSeekCacheMissTokens = apiLogs.reduce((acc, log) => acc + ((log as any).promptCacheMissTokens || 0), 0);
  const deepSeekCacheTotal = deepSeekCacheHitTokens + deepSeekCacheMissTokens;
  const deepSeekCacheRate = deepSeekCacheTotal > 0 ? deepSeekCacheHitTokens / deepSeekCacheTotal : 0;
  
  const modelStats = apiLogs.reduce((acc: unknown, log) => {
      (acc as any)[log.model] = ((acc as any)[log.model] || 0) + log.cost;
      return acc;
  }, {});
  const topModel = Object.keys(modelStats as object).sort((a,b) => (modelStats as any)[b] - (modelStats as any)[a])[0] || "None";
  
  const [activeTab, setActiveTab] = React.useState('dashboard');

  if (!mounted) return <div className="p-8 text-slate-500 font-medium h-full flex items-center justify-center">Đang nạp dữ liệu...</div>;

  return (
    <div className="max-w-7xl mx-auto py-10 animation-fade-in flex flex-col h-full px-4 border-none">
      <div className="mb-8 flex justify-between items-end flex-shrink-0">
        <div>
          <h2 className="text-3xl font-bold bg-gradient-to-r from-orange-500 to-rose-500 bg-clip-text text-transparent tracking-tight">Trạm Kế Toán API</h2>
          <p className="text-slate-400 mt-2">Dữ liệu Token, biểu giá và nơi điền chìa khóa các mô hình AI.</p>
        </div>
        <div className="flex gap-2">
            <button onClick={() => setActiveTab('dashboard')} className={`px-4 py-2 rounded-xl text-sm font-bold ${activeTab==='dashboard'? 'bg-rose-500/20 text-rose-400 border-rose-500/40' : 'bg-slate-800 text-slate-400'} border`}>📊 Dashboard Quota</button>
            <button onClick={() => setActiveTab('keys')} className={`px-4 py-2 rounded-xl text-sm font-bold ${activeTab==='keys'? 'bg-blue-500/20 text-blue-400 border-blue-500/40' : 'bg-slate-800 text-slate-400'} border`}>🔑 Cấu Hình Keys</button>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto space-y-8 custom-scrollbar pr-2 pb-20">
        {activeTab === 'dashboard' && (
           <div className="space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                 <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl relative overflow-hidden group">
                    <div className="absolute top-0 right-0 w-32 h-32 bg-emerald-500/10 rounded-full blur-3xl group-hover:bg-emerald-500/20 transition-all"></div>
                    <h4 className="text-slate-400 text-sm font-bold uppercase tracking-wider mb-2">Tổng Tổn Thất</h4>
                    <div className="text-4xl font-black text-emerald-400">${totalCost.toFixed(5)}</div>
                 </div>
                 <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl relative overflow-hidden group">
                    <div className="absolute top-0 right-0 w-32 h-32 bg-purple-500/10 rounded-full blur-3xl group-hover:bg-purple-500/20 transition-all"></div>
                    <h4 className="text-slate-400 text-sm font-bold uppercase tracking-wider mb-2">Tổng Tokens Đã Nạp</h4>
                    <div className="text-4xl font-black text-purple-400">{totalTokens.toLocaleString()}</div>
                 </div>
                 <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl relative overflow-hidden group">
                    <div className="absolute top-0 right-0 w-32 h-32 bg-amber-500/10 rounded-full blur-3xl group-hover:bg-amber-500/20 transition-all"></div>
                    <h4 className="text-slate-400 text-sm font-bold uppercase tracking-wider mb-2">Mô Hình Khát Máu Nhất</h4>
                    <div className="text-4xl font-black text-amber-400 truncate">{topModel}</div>
                 </div>
              </div>
              {deepSeekCacheTotal > 0 && (
                <div className="bg-slate-900 border border-cyan-500/20 rounded-2xl p-5 shadow-xl">
                  <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-3">
                    <div>
                      <h4 className="text-cyan-300 text-sm font-bold uppercase tracking-wider">DeepSeek Context Cache</h4>
                      <p className="text-slate-400 text-xs mt-1">Cache Hit / Miss tokens từ usage API DeepSeek.</p>
                    </div>
                    <div className="text-right">
                      <div className="text-3xl font-black text-cyan-300">{(deepSeekCacheRate * 100).toFixed(1)}%</div>
                      <div className="text-xs text-slate-500 font-mono">{deepSeekCacheHitTokens.toLocaleString()} hit / {deepSeekCacheMissTokens.toLocaleString()} miss</div>
                    </div>
                  </div>
                </div>
              )}

              <div className="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden flex flex-col">
                 <div className="p-4 border-b border-slate-800 flex justify-between items-center bg-slate-950">
                    <h3 className="font-bold tracking-wide text-rose-400">📜 Sổ Sao Kê Chi Tiết (1500 Gọi Gần Nhất)</h3>
                    <button onClick={() => confirm('Xóa sạch sổ?') && clearApiLogs()} className="text-xs bg-red-500/10 text-red-400 px-3 py-1.5 rounded uppercase font-bold hover:bg-red-500/20">Xóa Lịch Sử</button>
                 </div>
                 <div className="overflow-x-auto max-h-[500px]">
                    <table className="w-full text-left text-sm text-slate-300">
                       <thead className="bg-slate-900 text-slate-400 sticky top-0 z-10 shadow-md">
                          <tr>
                             <th className="px-4 py-3 font-medium">Thời Gian</th>
                             <th className="px-4 py-3 font-medium">Model</th>
                             <th className="px-4 py-3 font-medium text-right">Tokens (In/Out)</th>
                             <th className="px-4 py-3 font-medium text-right">Cache</th>
                             <th className="px-4 py-3 font-medium text-right">Chi Phí</th>
                          </tr>
                       </thead>
                       <tbody className="divide-y divide-slate-800 flex-1">
                          {apiLogs.length === 0 ? (
                            <tr><td colSpan={5} className="px-4 py-8 text-center text-slate-500">Chưa có giao dịch API nào.</td></tr>
                          ) : apiLogs.map((l: unknown) => (
                             <tr key={(l as any).id} className="hover:bg-slate-800/50 transition-colors">
                                <td className="px-4 py-3 font-mono text-xs">{new Date((l as any).timestamp).toLocaleTimeString()}</td>
                                <td className="px-4 py-3 font-bold text-rose-300">{(l as any).model}</td>
                                <td className="px-4 py-3 text-right font-mono text-xs text-slate-400">{(l as any).promptTokens} / {(l as any).completionTokens} <span className="text-white bg-slate-800 px-1 rounded">{(l as any).totalTokens}</span></td>
                                <td className="px-4 py-3 text-right font-mono text-xs text-cyan-300">
                                  {((l as any).promptCacheHitTokens || (l as any).promptCacheMissTokens)
                                    ? `${Math.round(((l as any).cacheHitRate || 0) * 100)}%`
                                    : '-'}
                                </td>
                                <td className="px-4 py-3 text-right font-bold text-emerald-400">${((l as any).cost || 0).toFixed(6)}</td>
                             </tr>
                          ))}
                       </tbody>
                    </table>
                 </div>
              </div>
           </div>
        )}

        <div className={activeTab === 'keys' ? 'block' : 'hidden'}>
          <div className="max-w-2xl mx-auto py-10 animation-fade-in pb-20">
            <div className="mb-8">
              <h2 className="text-3xl font-bold text-white tracking-tight">Cấu Hình Lõi</h2>
              <p className="text-slate-400 mt-2">Cài đặt kết nối M-Core với các API thông minh Google, OpenAI, Qwen...</p>
            </div>

            <div className="space-y-6">
              {/* GEMINI ENGINE CARD */}
              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl">
                <div className="flex justify-between items-center mb-6 border-b border-slate-800 pb-4">
                  <h3 className="text-lg font-semibold text-white flex items-center gap-2">
                    <Key className="text-blue-400" size={20} />
                    AI Engine (Google Gemini)
                  </h3>
                  
                  <div className="flex items-center gap-3 bg-slate-950 px-4 py-2 rounded-lg border border-slate-800">
                    <span className={`text-sm font-bold ${!usePaidAPI ? 'text-emerald-400' : 'text-slate-500'}`}>MIỄN PHÍ</span>
                    <button 
                      onClick={() => setSettings({ usePaidAPI: !usePaidAPI })}
                      className={`w-12 h-6 rounded-full transition-colors relative flex items-center ${usePaidAPI ? 'bg-amber-500' : 'bg-slate-700'}`}
                    >
                      <div className={`w-4 h-4 bg-white rounded-full absolute transition-transform ${usePaidAPI ? 'translate-x-7' : 'translate-x-1'}`}></div>
                    </button>
                    <span className={`text-sm font-bold ${usePaidAPI ? 'text-amber-400' : 'text-slate-500'}`}>TRẢ PHÍ</span>
                  </div>
                </div>
                
                {isFreeApiExhausted && !usePaidAPI && (
                  <div className="mb-6 p-4 bg-red-500/10 border border-red-500/30 rounded-xl flex gap-3 text-red-400 text-sm">
                    <div className="text-xl">⚠️</div>
                    <div>
                      <strong className="block mb-1">Cảnh báo: Tài khoản Free đã cạn kiệt (Quota Exceeded)!</strong>
                      Hệ thống M-Core đã tự động tạm ngưng trạm Auto-Pilot. Vui lòng bật sang luồng <strong>TRẢ PHÍ</strong> để tiếp tục cày cuốc.
                    </div>
                  </div>
                )}

                <div className="space-y-6">
                  <div className={`p-4 rounded-xl border transition-colors ${!usePaidAPI ? 'bg-emerald-900/10 border-emerald-500/30' : 'bg-slate-950 border-slate-800 opacity-50 grayscale'}`}>
                    <div className="flex justify-between items-center mb-2">
                      <label className="text-sm font-bold text-emerald-400">API Key 1 - Miễn Phí (Gmail chính)</label>
                      <button onClick={() => testKey(geminiKey, 'key1')} className="text-xs bg-slate-700 hover:bg-slate-600 px-3 py-1 rounded-lg text-slate-300 transition-all">🧪 Kiểm tra</button>
                    </div>
                    <input 
                      type="password"
                      value={geminiKey}
                      onChange={(e) => setSettings({ geminiKey: e.target.value, isFreeApiExhausted: false })}
                      className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-emerald-500 font-mono text-sm"
                      placeholder="AIzaSy... (Free Tier - Gmail 1)"
                    />
                    {testResults['key1'] && <p className={`text-xs mt-2 font-bold ${testResults['key1'].includes('✅') ? 'text-emerald-400' : testResults['key1'].includes('⏳') ? 'text-amber-400' : 'text-red-400'}`}>{testResults['key1']}</p>}
                    <p className="text-xs text-slate-500 mt-1">Key ưu tiên dùng trước. Khi 429 → tự động nhảy sang Key 2.</p>
                  </div>

                  <div className={`p-4 rounded-xl border transition-colors ${!usePaidAPI ? 'bg-emerald-900/10 border-emerald-500/20' : 'bg-slate-950 border-slate-800 opacity-50 grayscale'}`}>
                    <div className="flex justify-between items-center mb-2">
                      <label className="text-sm font-bold text-emerald-300">
                        API Key 2 - Miễn Phí (Gmail dự phòng)
                      </label>
                      <button onClick={() => testKey(geminiKey2, 'key2')} className="text-xs bg-slate-700 hover:bg-slate-600 px-3 py-1 rounded-lg text-slate-300 transition-all">🧪 Kiểm tra</button>
                    </div>
                    <input 
                      type="password"
                      value={geminiKey2}
                      onChange={(e) => setSettings({ geminiKey2: e.target.value })}
                      className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-emerald-400 font-mono text-sm"
                      placeholder="AIzaSy... (Free Tier - Gmail 2 khác)"
                    />
                    {testResults['key2'] && <p className={`text-xs mt-2 font-bold ${testResults['key2'].includes('✅') ? 'text-emerald-400' : testResults['key2'].includes('⏳') ? 'text-amber-400' : 'text-red-400'}`}>{testResults['key2']}</p>}
                  </div>

                  <div className={`p-4 rounded-xl border transition-colors ${usePaidAPI ? 'bg-amber-900/10 border-amber-500/30' : 'bg-slate-950 border-slate-800 opacity-50 grayscale'}`}>
                    <label className="block text-sm font-bold text-amber-400 mb-2">API Key - Trả Phí (Tốc biến)</label>
                    <input 
                      type="password"
                      value={geminiPaidKey}
                      onChange={(e) => setSettings({ geminiPaidKey: e.target.value })}
                      className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-amber-500 font-mono text-sm"
                      placeholder="AIzaSy... (Paid Tier)"
                    />
                  </div>
                </div>
              </div>

              {/* OPENAI ENGINE CARD */}
              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl relative overflow-hidden">
                <div className="absolute -top-24 -right-24 w-48 h-48 bg-teal-500/10 blur-[60px] rounded-full pointer-events-none"></div>

                <div className="flex justify-between items-center mb-6 border-b border-slate-800 pb-4 relative z-10">
                  <h3 className="text-lg font-semibold text-white flex items-center gap-2">
                    <span className="text-teal-400">❖</span>
                    AI Đạo Diễn (OpenAI / Micro Drama)
                  </h3>
                  <div className="bg-slate-950 px-3 py-1 rounded-lg border border-slate-800 text-xs font-bold text-teal-500">PAY-AS-YOU-GO</div>
                </div>

                <div className="p-4 rounded-xl border bg-teal-900/10 border-teal-500/30 relative z-10 transition-all focus-within:border-teal-500/50">
                  <div className="flex justify-between items-center mb-2">
                    <label className="text-sm font-bold text-teal-400">OpenAI API Key</label>
                    <button onClick={testOpenAI} className="text-xs bg-slate-700 hover:bg-slate-600 px-3 py-1 rounded-lg text-slate-300 transition-all">🧪 Kiểm tra</button>
                  </div>
                  <input 
                    type="password"
                    value={openAIKey}
                    onChange={(e) => setSettings({ openAIKey: e.target.value })}
                    className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-teal-500 font-mono text-sm shadow-inner"
                  />
                  {testResults['openai'] && <p className={`text-xs mt-2 font-bold ${testResults['openai'].includes('✅') ? 'text-teal-400' : 'text-red-400'}`}>{testResults['openai']}</p>}
                </div>
              </div>

              {/* QWEN DRAMA BLOCK */}
              <div className="bg-gradient-to-br from-slate-800 to-slate-900 border border-slate-700/50 rounded-2xl p-6 shadow-xl relative overflow-hidden">
                <div className="absolute top-0 right-0 w-32 h-32 bg-cyan-500/10 rounded-bl-full blur-2xl pointer-events-none"></div>
                
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <h3 className="text-lg font-bold text-white flex items-center gap-2">
                      Sáng Tác 7 API Key
                      <span className="px-2 py-0.5 bg-cyan-500/20 text-cyan-400 text-[10px] font-black uppercase rounded-full">Qwen Alibaba</span>
                    </h3>
                  </div>
                  <button onClick={testQwen} className="bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-600 px-3 py-1.5 rounded-lg text-xs font-bold transition-all hover:text-white">🧪 Kiểm tra</button>
                </div>
                <input 
                  type="password"
                  value={qwenKey}
                  onChange={(e) => setSettings({ qwenKey: e.target.value })}
                  className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-cyan-500 font-mono text-sm shadow-inner"
                />
                {testResults['qwen'] && <p className={`text-xs mt-2 font-bold ${testResults['qwen'].includes('✅') ? 'text-cyan-400' : 'text-red-400'}`}>{testResults['qwen']}</p>}
              </div>

              {/* GROK ENGINE CARD */}
              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl relative overflow-hidden">
                <div className="absolute -top-24 -right-24 w-48 h-48 bg-fuchsia-500/10 blur-[60px] rounded-full pointer-events-none"></div>

                <div className="flex justify-between items-center mb-6 border-b border-slate-800 pb-4 relative z-10">
                  <h3 className="text-lg font-semibold text-white flex items-center gap-2">
                    <span className="text-fuchsia-400">☢️</span>
                    The Rebel (Grok xAI)
                  </h3>
                  <div className="bg-slate-950 px-3 py-1 rounded-lg border border-slate-800 text-xs font-bold text-fuchsia-500">PAY-AS-YOU-GO</div>
                </div>

                <div className="p-4 rounded-xl border bg-fuchsia-900/10 border-fuchsia-500/30 relative z-10 transition-all focus-within:border-fuchsia-500/50">
                  <div className="flex justify-between items-center mb-2">
                    <label className="text-sm font-bold text-fuchsia-400">Grok API Key</label>
                    <button onClick={testGrok} className="text-xs bg-slate-700 hover:bg-slate-600 px-3 py-1 rounded-lg text-slate-300 transition-all">🧪 Kiểm tra</button>
                  </div>
                  <input 
                    type="password"
                    value={grokKey}
                    onChange={(e) => setSettings({ grokKey: e.target.value })}
                    className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-fuchsia-500 font-mono text-sm shadow-inner"
                  />
                  {testResults['grok'] && <p className={`text-xs mt-2 font-bold ${testResults['grok'].includes('✅') ? 'text-fuchsia-400' : 'text-red-400'}`}>{testResults['grok']}</p>}
                </div>
              </div>

              {/* CLAUDE ENGINE CARD */}
              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl relative overflow-hidden">
                <div className="absolute -top-24 -right-24 w-48 h-48 bg-orange-500/10 blur-[60px] rounded-full pointer-events-none"></div>

                <div className="flex justify-between items-center mb-6 border-b border-slate-800 pb-4 relative z-10">
                  <h3 className="text-lg font-semibold text-white flex items-center gap-2">
                    <span className="text-orange-400">🎭</span>
                    The Wordsmith (Anthropic Claude)
                  </h3>
                  <div className="bg-slate-950 px-3 py-1 rounded-lg border border-slate-800 text-xs font-bold text-orange-500">PAY-AS-YOU-GO</div>
                </div>

                <div className="p-4 rounded-xl border bg-orange-900/10 border-orange-500/30 relative z-10 transition-all focus-within:border-orange-500/50">
                  <div className="flex justify-between items-center mb-2">
                    <label className="text-sm font-bold text-orange-400">Claude API Key</label>
                    <button onClick={testClaude} className="text-xs bg-slate-700 hover:bg-slate-600 px-3 py-1 rounded-lg text-slate-300 transition-all">🧪 Kiểm tra</button>
                  </div>
                  <input 
                    type="password"
                    value={claudeKey}
                    onChange={(e) => setSettings({ claudeKey: e.target.value })}
                    className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-orange-500 font-mono text-sm shadow-inner"
                  />
                  {testResults['claude'] && <p className={`text-xs mt-2 font-bold ${testResults['claude'].includes('✅') ? 'text-orange-400' : 'text-red-400'}`}>{testResults['claude']}</p>}
                </div>
              </div>

              {/* DEEPSEEK ENGINE CARD */}
              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl relative overflow-hidden">
                <div className="absolute -top-24 -right-24 w-48 h-48 bg-indigo-500/10 blur-[60px] rounded-full pointer-events-none"></div>

                <div className="flex justify-between items-center mb-6 border-b border-slate-800 pb-4 relative z-10">
                  <h3 className="text-lg font-semibold text-white flex items-center gap-2">
                    <span className="text-indigo-400">🐋</span>
                    Kẻ Hủy Diệt Cấu Trúc (DeepSeek)
                  </h3>
                  <div className="bg-slate-950 px-3 py-1 rounded-lg border border-slate-800 text-xs font-bold text-indigo-500">PAY-AS-YOU-GO</div>
                </div>

                <div className="p-4 rounded-xl border bg-indigo-900/10 border-indigo-500/30 relative z-10 transition-all focus-within:border-indigo-500/50">
                  <div className="flex justify-between items-center mb-2">
                    <label className="text-sm font-bold text-indigo-400">DeepSeek API Key</label>
                    <button onClick={testDeepSeek} className="text-xs bg-slate-700 hover:bg-slate-600 px-3 py-1 rounded-lg text-slate-300 transition-all">🧪 Kiểm tra</button>
                  </div>
                  <input 
                    type="password"
                    value={deepseekKey}
                    onChange={(e) => setSettings({ deepseekKey: e.target.value })}
                    className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-indigo-500 font-mono text-sm shadow-inner"
                  />
                  {testResults['deepseek'] && <p className={`text-xs mt-2 font-bold ${testResults['deepseek'].includes('✅') ? 'text-indigo-400' : 'text-red-400'}`}>{testResults['deepseek']}</p>}
                </div>
              </div>

              {/* OPENROUTER ENGINE CARD */}
              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl relative overflow-hidden">
                <div className="absolute -top-24 -right-24 w-48 h-48 bg-lime-500/10 blur-[60px] rounded-full pointer-events-none"></div>

                <div className="flex justify-between items-center mb-6 border-b border-slate-800 pb-4 relative z-10">
                  <h3 className="text-lg font-semibold text-white flex items-center gap-2">
                    <span className="text-lime-400">🪐</span>
                    Đa Vũ Trụ LLM (OpenRouter)
                  </h3>
                  <div className="bg-slate-950 px-3 py-1 rounded-lg border border-slate-800 text-xs font-bold text-lime-500">PAY-AS-YOU-GO</div>
                </div>

                <div className="p-4 rounded-xl border bg-lime-900/10 border-lime-500/30 relative z-10 transition-all focus-within:border-lime-500/50">
                  <div className="flex justify-between items-center mb-2">
                    <label className="text-sm font-bold text-lime-400">OpenRouter API Key</label>
                    <button onClick={testOpenRouter} className="text-xs bg-slate-700 hover:bg-slate-600 px-3 py-1 rounded-lg text-slate-300 transition-all">🧪 Kiểm tra</button>
                  </div>
                  <input 
                    type="password"
                    value={openRouterKey}
                    onChange={(e) => setSettings({ openRouterKey: e.target.value })}
                    className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-lime-500 font-mono text-sm shadow-inner"
                  />
                  {testResults['openrouter'] && <p className={`text-xs mt-2 font-bold ${testResults['openrouter'].includes('✅') ? 'text-lime-400' : 'text-red-400'}`}>{testResults['openrouter']}</p>}
                </div>
              </div>

              {/* ── EXPORT / IMPORT KEYS ── */}
              <div className="bg-slate-900 border border-slate-700 rounded-2xl p-6 shadow-xl">
                <h3 className="text-lg font-semibold text-white mb-1 flex items-center gap-2">
                  <span className="text-yellow-400">💾</span> Backup &amp; Restore API Keys
                </h3>
                <p className="text-slate-400 text-xs mb-5">Export tất cả keys ra file để backup. Import lại khi bị mất do xóa cache trình duyệt.</p>
                <div className="flex gap-3 flex-wrap">
                  {/* Export */}
                  <button
                    onClick={() => {
                      const payload = { geminiKey, geminiKey2, geminiPaidKey, openAIKey, grokKey, claudeKey, qwenKey, deepseekKey, openRouterKey, exportedAt: new Date().toISOString() };
                      const encoded = btoa(unescape(encodeURIComponent(JSON.stringify(payload))));
                      const blob = new Blob([encoded], { type: 'text/plain' });
                      const url = URL.createObjectURL(blob);
                      const a = document.createElement('a');
                      a.href = url;
                      a.download = `mcore-keys-backup-${new Date().toLocaleDateString('vi-VN').replace(/\//g,'-')}.mkey`;
                      a.click();
                      URL.revokeObjectURL(url);
                    }}
                    className="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm bg-yellow-500/10 border border-yellow-500/30 text-yellow-400 hover:bg-yellow-500/20 transition-all"
                  >
                    ⬇ Export Keys (.mkey)
                  </button>

                  {/* Import */}
                  <label className="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 hover:bg-emerald-500/20 transition-all cursor-pointer">
                    ⬆ Import Keys (.mkey)
                    <input
                      type="file"
                      accept=".mkey,.txt"
                      className="hidden"
                      onChange={(e) => {
                        const file = e.target.files?.[0];
                        if (!file) return;
                        const reader = new FileReader();
                        reader.onload = (ev) => {
                          try {
                            const decoded = decodeURIComponent(escape(atob(ev.target?.result as string)));
                            const keys = JSON.parse(decoded);
                            const toSet: Record<string, string> = {};
                            if (keys.geminiKey)     toSet.geminiKey     = keys.geminiKey;
                            if (keys.geminiKey2)    toSet.geminiKey2    = keys.geminiKey2;
                            if (keys.geminiPaidKey) toSet.geminiPaidKey = keys.geminiPaidKey;
                            if (keys.openAIKey)     toSet.openAIKey     = keys.openAIKey;
                            if (keys.grokKey)       toSet.grokKey       = keys.grokKey;
                            if (keys.claudeKey)     toSet.claudeKey     = keys.claudeKey;
                            if (keys.qwenKey)       toSet.qwenKey       = keys.qwenKey;
                            if (keys.deepseekKey)   toSet.deepseekKey   = keys.deepseekKey;
                            if (keys.openRouterKey) toSet.openRouterKey = keys.openRouterKey;
                            setSettings(toSet);
                            alert(`✅ Import thành công! Đã khôi phục ${Object.keys(toSet).length} keys.\nBackup từ: ${keys.exportedAt || 'không rõ'}`);
                          } catch {
                            alert('❌ File không hợp lệ hoặc bị hỏng. Vui lòng dùng file .mkey đúng định dạng.');
                          }
                        };
                        reader.readAsText(file);
                        e.target.value = '';
                      }}
                    />
                  </label>
                </div>
                <p className="text-slate-600 text-[10px] mt-3 font-mono">File .mkey là base64-encoded JSON, không phải plaintext. Lưu ở nơi an toàn.</p>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
