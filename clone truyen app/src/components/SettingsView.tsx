import React from 'react';
import { useStore } from '../store/useStore';
import { Save, Key, Globe, User, Lock } from 'lucide-react';

export function SettingsView() {
  const {
    geminiKey, geminiKey2, geminiKey3, geminiPaidKey, usePaidAPI, isFreeApiExhausted, 
    openAIKey, grokKey, claudeKey,
    wpUrl, wpUser, wpAppPassword, 
    setSettings 
  } = useStore();

  const [testResults, setTestResults] = React.useState<Record<string, string>>({});
  const [wpTargetId, setWpTargetId] = React.useState('');
  const [wpCleanStatus, setWpCleanStatus] = React.useState('');

  const handleCleanMarkdown = async () => {
    if (!wpUrl || !wpUser || !wpAppPassword) return alert("Chưa kết nối WP!");
    if (!wpTargetId) return alert("Vui lòng nhập Truyện ID!");
    
    setWpCleanStatus('⏳ Đang quét server tìm các chương...');
    try {
      // Lấy toàn bộ vòng lặp phân trang vì REST API không cho filter _truyen_id trực tiếp
      let allChapters: any[] = [];
      let page = 1;
      let hasMore = true;

      while (hasMore) {
        setWpCleanStatus(`⏳ Đang quét server tìm các chương... (Trang ${page})`);
        
        const fetchRes = await fetch('/api/wordpress', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            wpUrl, wpUser, wpAppPassword,
            endpoint: `chuong?per_page=100&page=${page}`,
            method: 'GET'
          })
        });
        
        if (!fetchRes.ok) {
           if (fetchRes.status === 400 || fetchRes.status === 404) { hasMore = false; break; } // Vượt quá số trang
           throw new Error('Không thể fetch dữ liệu từ WP: ' + fetchRes.statusText);
        }
        
        const data = await fetchRes.json();
        if (!Array.isArray(data) || data.length === 0) {
           hasMore = false;
        } else {
           allChapters = [...allChapters, ...data];
           const totalPages = fetchRes.headers?.get('x-wp-totalpages') || '20'; // Xấp xỉ do api backend có thể ko trả header
           if (data.length < 100) {
             hasMore = false; // Last page
           } else {
             page++;
           }
        }
      }
      
      // Lọc local: Chỉ lấy các chương có _truyen_id trùng khớp
      const targetChapters = allChapters.filter(c => c.meta && String(c.meta._truyen_id) === String(wpTargetId));

      if (targetChapters.length === 0) {
        return setWpCleanStatus('⚠️ Không tìm thấy chương nào cho ID này!');
      }

      setWpCleanStatus(`⏳ Đã tìm thấy ${targetChapters.length} chương của Truyện ${wpTargetId}. Đang giặt sạch bằng Omo Matic...`);
      let successCount = 0;

      for (let i = 0; i < targetChapters.length; i++) {
        const item = targetChapters[i];
        let originalContent = item.content?.raw || item.content?.rendered || '';
        
        // Xem xét nội dung có chứa ** không
        if (originalContent.includes('**') || originalContent.includes('*') || originalContent.includes('```')) {
          let cleanedContent = originalContent.replace(/```markdown/gi, '').replace(/```/g, '');
          cleanedContent = cleanedContent.replace(/\*\*([\s\S]*?)\*\*/g, '<strong>$1</strong>').replace(/\*([\s\S]*?)\*/g, '<em>$1</em>');
          
          const updateRes = await fetch('/api/wordpress', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              wpUrl, wpUser, wpAppPassword,
              endpoint: `chuong/${item.id}`,
              method: 'POST',
              payload: { content: cleanedContent }
            })
          });
          
          if (!updateRes.ok) {
             const errText = await updateRes.text();
             throw new Error(`Cập nhật chương ${item.id} thất bại (${updateRes.status}): ${errText}`);
          }
          successCount++;
        }
      }

      setWpCleanStatus(`✅ Đã đập đi xây lại giặt sạch bong ${successCount}/${targetChapters.length} chương! Lên web kiểm tra ngay anh nhé!`);
    } catch (e: any) {
      setWpCleanStatus(`❌ Lỗi Máy Giặt: ${e.message}`);
    }
  };

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
    } catch (e: any) {
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
    } catch (e: any) {
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
    } catch (e: any) {
      setTestResults(r => ({ ...r, grok: `❌ Mất kết nối API` }));
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
    } catch (e: any) {
      setTestResults(r => ({ ...r, claude: `❌ Mất kết nối API` }));
    }
  };

  const testWP = async () => {
    if (!wpUrl || !wpUser || !wpAppPassword) return alert('Chưa điền đầy đủ WP URL, Username, Password!');
    setTestResults(r => ({ ...r, wp: '⏳ Đang kiểm tra kết nối WordPress...' }));
    try {
      const res = await fetch('/api/wordpress', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          wpUrl, wpUser, wpAppPassword,
          endpoint: 'users/me',
          method: 'GET'
        })
      });
      const data = await res.json();
      if (res.ok && data.id) {
        setTestResults(r => ({ ...r, wp: `✅ Kết nối thành công! User: ${data.name} (ID: ${data.id})` }));
      } else {
        const msg = data.error || JSON.stringify(data);
        if (msg.includes('401') || msg.includes('rest_cannot_create') || msg.includes('rest_forbidden')) {
          setTestResults(r => ({ ...r, wp: '❌ Lỗi 401: Sai Username hoặc Application Password. Hãy tạo Application Password mới trong WP Admin > Users > Profile' }));
        } else {
          setTestResults(r => ({ ...r, wp: `❌ Lỗi: ${String(msg).substring(0, 100)}` }));
        }
      }
    } catch (e: any) {
      setTestResults(r => ({ ...r, wp: `❌ Không kết nối được tới ${wpUrl}` }));
    }
  };

  const { apiLogs = [], clearApiLogs } = useStore();
  const totalCost = apiLogs.reduce((acc, log) => acc + (log.cost || 0), 0);
  const totalTokens = apiLogs.reduce((acc, log) => acc + (log.totalTokens || 0), 0);
  
  const modelStats = apiLogs.reduce((acc: any, log) => {
      acc[log.model] = (acc[log.model] || 0) + log.cost;
      return acc;
  }, {});
  const topModel = Object.keys(modelStats).sort((a,b) => modelStats[b] - modelStats[a])[0] || "None";
  
  const [activeTab, setActiveTab] = React.useState('dashboard');

  return (
    <div className="max-w-7xl mx-auto py-10 animation-fade-in flex flex-col h-[calc(100vh-80px)] px-4">
      <div className="mb-8 flex justify-between items-end flex-shrink-0">
        <div>
          <h2 className="text-3xl font-bold bg-gradient-to-r from-orange-500 to-rose-500 bg-clip-text text-transparent tracking-tight">Trạm Kế Toán API</h2>
          <p className="text-slate-400 mt-2">Dữ liệu Token và biểu giá (Tương đối theo niêm yết API Mĩ).</p>
        </div>
        <div className="flex gap-2">
            <button onClick={() => setActiveTab('dashboard')} className={`px-4 py-2 rounded-xl text-sm font-bold ${activeTab==='dashboard'? 'bg-rose-500/20 text-rose-400 border-rose-500/40' : 'bg-slate-800 text-slate-400'} border`}>📊 Dashboard Quota</button>
            <button onClick={() => setActiveTab('keys')} className={`px-4 py-2 rounded-xl text-sm font-bold ${activeTab==='keys'? 'bg-blue-500/20 text-blue-400 border-blue-500/40' : 'bg-slate-800 text-slate-400'} border`}>🔑 Cấu Hình Keys</button>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto space-y-8 custom-scrollbar pr-2 pb-20">
        {activeTab === 'dashboard' && (
           <div className="space-y-6">
              {/* TOP METRICS */}
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

              {/* TABLE */}
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
                             <th className="px-4 py-3 font-medium text-right">Chi Phí</th>
                          </tr>
                       </thead>
                       <tbody className="divide-y divide-slate-800 flex-1">
                          {apiLogs.length === 0 ? (
                            <tr><td colSpan={4} className="px-4 py-8 text-center text-slate-500">Chưa có giao dịch API nào.</td></tr>
                          ) : apiLogs.map((l: any) => (
                             <tr key={l.id} className="hover:bg-slate-800/50 transition-colors">
                                <td className="px-4 py-3 font-mono text-xs">{new Date(l.timestamp).toLocaleTimeString()}</td>
                                <td className="px-4 py-3 font-bold text-rose-300">{l.model}</td>
                                <td className="px-4 py-3 text-right font-mono text-xs text-slate-400">{l.promptTokens} / {l.completionTokens} <span className="text-white bg-slate-800 px-1 rounded">{l.totalTokens}</span></td>
                                <td className="px-4 py-3 text-right font-bold text-emerald-400">${(l.cost || 0).toFixed(6)}</td>
                             </tr>
                          ))}
                       </tbody>
                    </table>
                 </div>
              </div>
           </div>
        )}

        <div className={activeTab === 'keys' ? 'block' : 'hidden'}>
           {/* OLD SETTINGS RESTORED */}

    <div className="max-w-2xl mx-auto py-10 animation-fade-in pb-20">
      <div className="mb-8">
        <h2 className="text-3xl font-bold text-white tracking-tight">Cấu Hình Lõi</h2>
        <p className="text-slate-400 mt-2">Cài đặt kết nối M-Core với Google Gemini và máy chủ WordPress.</p>
      </div>

      <div className="space-y-6">
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
                  <span className="ml-2 text-xs bg-emerald-500/20 px-2 py-0.5 rounded-full text-emerald-400 font-medium">Xoay vòng tự động</span>
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
              <p className="text-xs text-slate-500 mt-1">Cần tạo từ tài khoản Gmail khác.</p>
            </div>

            <div className={`p-4 rounded-xl border transition-colors ${!usePaidAPI ? 'bg-emerald-900/10 border-emerald-500/10' : 'bg-slate-950 border-slate-800 opacity-50 grayscale'}`}>
              <div className="flex justify-between items-center mb-2">
                <label className="text-sm font-bold text-emerald-200">
                  API Key 3 - Miễn Phí (Gmail thứ 3)
                  <span className="ml-2 text-xs bg-emerald-500/20 px-2 py-0.5 rounded-full text-emerald-400 font-medium">Xoay vòng tự động</span>
                </label>
                <button onClick={() => testKey(geminiKey3, 'key3')} className="text-xs bg-slate-700 hover:bg-slate-600 px-3 py-1 rounded-lg text-slate-300 transition-all">🧪 Kiểm tra</button>
              </div>
              <input 
                type="password"
                value={geminiKey3}
                onChange={(e) => setSettings({ geminiKey3: e.target.value })}
                className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-emerald-300 font-mono text-sm"
                placeholder="AIzaSy... (Free Tier - Gmail 3 khác)"
              />
              {testResults['key3'] && <p className={`text-xs mt-2 font-bold ${testResults['key3'].includes('✅') ? 'text-emerald-400' : testResults['key3'].includes('⏳') ? 'text-amber-400' : 'text-red-400'}`}>{testResults['key3']}</p>}
              <p className="text-xs text-slate-500 mt-1">Dự phòng cấp 3. Cần tạo từ tài khoản Gmail thứ 3.</p>
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
              <p className="text-xs text-slate-500 mt-2">Dùng khi tài khoản Free hết hạn mức. Tốc độ bào cực nhanh không giới hạn.</p>
            </div>
          </div>
        </div>

        {/* OPENAI ENGINE CARD */}
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl relative overflow-hidden">
          {/* OpenAI Glow Background */}
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
              <button onClick={testOpenAI} className="text-xs bg-slate-700 hover:bg-slate-600 px-3 py-1 rounded-lg text-slate-300 transition-all flex items-center gap-1.5">
                🧪 Kiểm tra 
              </button>
            </div>
            <input 
              type="password"
              value={openAIKey}
              onChange={(e) => setSettings({ openAIKey: e.target.value })}
              className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-teal-500 font-mono text-sm shadow-inner"
              placeholder="sk-proj-..."
            />
            {testResults['openai'] && <p className={`text-xs mt-2 font-bold ${testResults['openai'].includes('✅') ? 'text-teal-400' : testResults['openai'].includes('⏳') ? 'text-amber-400' : 'text-red-400'}`}>{testResults['openai']}</p>}
            <p className="text-xs text-slate-500 mt-2 leading-relaxed">
              Dành riêng cho <strong>Chế độ Sáng Tác Kịch Bản Ngắn</strong>. OpenAI cực kỳ tuân thủ luật lệ, không dài dòng. Em đã cấu hình dùng `gpt-4o-mini` để Brainstorm (rẻ) và `gpt-4o` để viết kịch bản (khôn ngoan thâm độc).
            </p>
          </div>
        </div>

        {/* GROK ENGINE CARD */}
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl relative overflow-hidden">
          {/* Grok Glow Background */}
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
              <button onClick={testGrok} className="text-xs bg-slate-700 hover:bg-slate-600 px-3 py-1 rounded-lg text-slate-300 transition-all flex items-center gap-1.5">
                🧪 Kiểm tra 
              </button>
            </div>
            <input 
              type="password"
              value={grokKey}
              onChange={(e) => setSettings({ grokKey: e.target.value })}
              className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-fuchsia-500 font-mono text-sm shadow-inner"
              placeholder="xai-..."
            />
            {testResults['grok'] && <p className={`text-xs mt-2 font-bold ${testResults['grok'].includes('✅') ? 'text-fuchsia-400' : testResults['grok'].includes('⏳') ? 'text-amber-400' : 'text-red-400'}`}>{testResults['grok']}</p>}
            <p className="text-xs text-slate-500 mt-2 leading-relaxed">
              Dành riêng cho <strong>Sáng Tác 3</strong>. Grok là cỗ máy sinh nội dung Uncensored, viết cảnh bạo lực ngôn từ, trả thù ngập tràn Toxic mà không bị AI kiểm duyệt chặn lại!
            </p>
          </div>
        </div>

        {/* CLAUDE ENGINE CARD */}
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl relative overflow-hidden">
          {/* Claude Glow Background */}
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
              <button onClick={testClaude} className="text-xs bg-slate-700 hover:bg-slate-600 px-3 py-1 rounded-lg text-slate-300 transition-all flex items-center gap-1.5">
                🧪 Kiểm tra 
              </button>
            </div>
            <input 
              type="password"
              value={claudeKey}
              onChange={(e) => setSettings({ claudeKey: e.target.value })}
              className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-orange-500 font-mono text-sm shadow-inner"
              placeholder="sk-ant-..."
            />
            {testResults['claude'] && <p className={`text-xs mt-2 font-bold ${testResults['claude'].includes('✅') ? 'text-orange-400' : testResults['claude'].includes('⏳') ? 'text-amber-400' : 'text-red-400'}`}>{testResults['claude']}</p>}
            <p className="text-xs text-slate-500 mt-2 leading-relaxed">
              Dành riêng cho <strong>Sáng Tác 4</strong>. Claude là thi hào nghệ thuật, văn phong mượt mà tự nhiên, cực kỳ phù hợp viết truyện lãng mạn, ngôn tình, cung đấu chuyên sâu.
            </p>
          </div>
        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-4">
          <h3 className="text-lg font-semibold text-white flex items-center gap-2 mb-4 border-b border-slate-800 pb-4">
            <Globe className="text-emerald-400" size={20} />
            Kết Nối Máy Chủ (WordPress REST API)
          </h3>
          
          <div>
            <label className="block text-sm font-medium text-slate-400 mb-2">WordPress URL</label>
            <input 
              type="url"
              value={wpUrl}
              onChange={(e) => setSettings({ wpUrl: e.target.value })}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-emerald-500 transition-all"
              placeholder="https://doctieuthuyet.com"
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="flex items-center gap-2 text-sm font-medium text-slate-400 mb-2">
                <User size={14} /> Username
              </label>
              <input 
                type="text"
                value={wpUser}
                onChange={(e) => setSettings({ wpUser: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-emerald-500 transition-all"
                placeholder="admin"
              />
            </div>
            <div>
              <label className="flex items-center gap-2 text-sm font-medium text-slate-400 mb-2">
                <Lock size={14} /> Application Password
              </label>
              <input 
                type="password"
                value={wpAppPassword}
                onChange={(e) => setSettings({ wpAppPassword: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-emerald-500 transition-all"
                placeholder="xxxx xxxx xxxx xxxx"
              />
            </div>
          </div>
          <p className="text-xs text-slate-500 mt-2 italic">
            * Mật khẩu ứng dụng (Application Password) được tạo trong mục Users -{'>'} Profile của WordPress. Không lưu mật khẩu đăng nhập chính thức vào đây.
          </p>
          <div className="mt-4 flex items-center gap-3">
            <button onClick={testWP} className="bg-emerald-600 hover:bg-emerald-500 text-white font-bold py-2 px-4 rounded-lg text-sm transition-colors">
              🔌 Kiểm Tra Kết Nối WP
            </button>
            {testResults['wp'] && (
              <p className={`text-xs font-bold ${testResults['wp'].includes('✅') ? 'text-emerald-400' : testResults['wp'].includes('⏳') ? 'text-amber-400' : 'text-red-400'}`}>
                {testResults['wp']}
              </p>
            )}
          </div>
        </div>

        {/* MÁY GIẶT MARKDOWN TOOL */}
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-4">
          <h3 className="text-lg font-semibold text-white flex items-center gap-2 mb-4 border-b border-slate-800 pb-4">
            <span className="text-pink-400">🛠</span>
            Trạm Bảo Trì Chỉnh Hình WordPress (Markdown Washer)
          </h3>
          <p className="text-sm text-slate-400">
            Dành riêng cho những bộ truyện nhỡ đăng bị dính ký tự ngôi sao <strong className="text-pink-400">**In đậm**</strong>. Cỗ máy sẽ chui vào Server gọt dũa lại.
          </p>
          <div className="flex gap-4">
            <input 
              type="text"
              value={wpTargetId}
              onChange={(e) => setWpTargetId(e.target.value)}
              className="flex-1 bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-pink-500 transition-all"
              placeholder="Nhập ID Truyện (VD: 1421)"
            />
            <button 
              onClick={handleCleanMarkdown}
              className="bg-pink-600 hover:bg-pink-500 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition-colors whitespace-nowrap"
            >
              🫧 Tẩy Sạch Lỗi Markdown
            </button>
          </div>
          {wpCleanStatus && (
            <p className={`text-sm font-bold mt-2 ${wpCleanStatus.includes('✅') ? 'text-emerald-400' : wpCleanStatus.includes('❌') ? 'text-red-400' : 'text-amber-400'}`}>
              {wpCleanStatus}
            </p>
          )}
        </div>
      </div>
      </div>
    </div>
  </div>
</div>
  );
}
