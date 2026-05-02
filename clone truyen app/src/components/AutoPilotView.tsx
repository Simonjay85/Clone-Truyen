/* eslint-disable @typescript-eslint/no-explicit-any */
'use client';
import React, { useEffect, useState } from 'react';
import { useStore } from '../store/useStore';
import { Play, Pause, Trash2, ShieldAlert, Zap, Send } from 'lucide-react';
import { useAutoPilotEngine } from '../hooks/useAutoPilotEngine';
import { agentGeminiDramaExpand, agentMicroDramaExpand, agentGrokDramaExpand, agentClaudeDramaExpand, agentQwenDramaExpand, callWordPress, agentDeepSeekDramaExpand } from '../lib/engine';

export function AutoPilotView({ onNavigate }: { onNavigate?: (tab: string) => void }) {
  const {
    queue, isAutoPilotRunning, toggleAutoPilot, removeQueueItem, clearQueue, updateQueueItem,
    geminiKey, geminiPaidKey, openAIKey, grokKey, claudeKey, qwenKey, usePaidAPI,
    wpUrl, wpUser, wpAppPassword,
  } = useStore();

  const [pulse, setPulse] = useState(false);
  const [isBatchLoading, setIsBatchLoading] = useState(false);
  const [batchStatus, setBatchStatus] = useState('');
  const [bulkEngine, setBulkEngine] = useState('openai');

  // Kích hoạt Engine
  useAutoPilotEngine();

  useEffect(() => {
    if (isAutoPilotRunning) {
      const interval = setInterval(() => setPulse(p => !p), 1000);
      return () => clearInterval(interval);
    }
  }, [isAutoPilotRunning]);

  const draftItems = queue.filter(q => q.status === 'draft_outline');
  const approvalItems = queue.filter(q => q.status === 'pending_approval');

  // ============================================================
  // LÊN DÀN Ý HÀNG LOẠT: Xử lý song song TẤT CẢ draft_outline
  // ============================================================
  const handleBatchOutline = async () => {
    if (draftItems.length === 0) return;
    setIsBatchLoading(true);
    setBatchStatus('🚀 Bắt đầu lên dàn ý hàng loạt...');
    const activeKey = usePaidAPI ? geminiPaidKey : geminiKey;

    for (const item of draftItems) {
      try {
        setBatchStatus(prev => prev + `\n⏳ Đang lên dàn ý: ${item.title}...`);

        // Tạo WP draft post nếu chưa có
        let wpPostId = item.wpPostId;
        if (!wpPostId) {
          if (wpUrl && wpUser && wpAppPassword) {
            try {
              const genreTerms = item.genres
                ? (Array.isArray(item.genres) ? item.genres : item.genres.split(',').map((g: string) => g.trim()).filter(Boolean))
                : [];
              const wpRes = await callWordPress({
                wpUrl, wpUser, wpAppPassword,
                endpoint: 'truyen', method: 'POST',
                payload: {
                  title: item.title,
                  content: item.prompt || '',
                  status: 'draft',
                  ...(genreTerms.length > 0 ? { the_loai: genreTerms } : {}),
                }
              });
              wpPostId = wpRes.id;
            } catch { wpPostId = Date.now(); }
          } else {
            wpPostId = Date.now();
          }
          updateQueueItem(item.id, { wpPostId });
        }

        // Gọi outline engine tương ứng
        const outlineEngine = item.outlineEngine || 'gemini';
        const bounds = { minChapters: item.targetChapters, maxChapters: item.maxChapters || item.targetChapters };
         
        let timeline: any[] | null = null;

        if (outlineEngine === 'gemini') timeline = await agentGeminiDramaExpand(activeKey, item.bible, bounds);
        else if (outlineEngine === 'openai') timeline = await agentMicroDramaExpand(openAIKey, item.bible, bounds);
        else if (outlineEngine === 'grok') timeline = await agentGrokDramaExpand(grokKey, item.bible, bounds);
        else if (outlineEngine === 'claude') timeline = await agentClaudeDramaExpand(claudeKey, item.bible, bounds);
        else if (outlineEngine === 'qwen') timeline = await agentQwenDramaExpand(qwenKey, item.bible, bounds);
        else if (outlineEngine === 'deepseek') timeline = await agentDeepSeekDramaExpand(useStore.getState().deepseekKey, item.bible, bounds);

        updateQueueItem(item.id, {
          status: 'pending_approval',
          bible: { ...(item.bible as any), timeline },
          targetChapters: (timeline as any[])?.length || item.targetChapters,
          wpPostId,
        });
        setBatchStatus(prev => prev + `\n✅ Hoàn tất: ${item.title}`);
      } catch (err: any) {
        updateQueueItem(item.id, { status: 'error', errorLog: `Lỗi lên dàn ý: ${err.message}` });
        setBatchStatus(prev => prev + `\n❌ Lỗi: ${item.title} — ${err.message}`);
      }
    }

    setIsBatchLoading(false);
    setBatchStatus(prev => prev + '\n\n🎉 Xong! Hãy duyệt tất cả dàn ý để bắt đầu viết.');
  };

  return (
    <div className="max-w-5xl mx-auto py-10 animation-fade-in flex flex-col h-full">
      {/* HEADER */}
      <div className="mb-8 flex justify-between items-end flex-shrink-0">
        <div>
          <h2 className="text-3xl font-bold text-white tracking-tight">Trạm Giám Sát M-Core</h2>
          <p className="text-slate-400 mt-2">Theo dõi tiến độ cày cuốc độc lập trên máy Mac.</p>
        </div>

        <div className="flex gap-3 flex-wrap justify-end">
          <button
            onClick={clearQueue}
            className="px-4 py-2 bg-red-500/10 text-red-400 hover:bg-red-500/20 rounded-lg text-sm font-semibold transition-colors flex items-center gap-2"
          >
            <Trash2 size={16} /> Dọn Sạch Trạm
          </button>

          {/* CẬP NHẬT ENGINE HÀNG LOẠT */}
          {queue.some(q => q.status !== 'completed') && (
            <div className="flex items-center gap-2 bg-indigo-500/10 border border-indigo-500/30 rounded-lg pr-3 pl-1">
              <select
                value={bulkEngine}
                onChange={(e) => setBulkEngine(e.target.value)}
                className="bg-transparent border-none text-indigo-200 text-sm py-2 px-2 outline-none font-medium cursor-pointer"
                title="Chọn trí tuệ nhân tạo (AI Engine) cho các truyện đang chạy"
              >
                <option value="gemini" className="bg-slate-900 text-slate-200">🤖 Đổi tất cả sang Gemini</option>
                <option value="openai" className="bg-slate-900 text-slate-200">🧠 Đổi tất cả sang OpenAI</option>
                <option value="claude" className="bg-slate-900 text-slate-200">🎭 Đổi tất cả sang Claude</option>
                <option value="grok" className="bg-slate-900 text-slate-200">⚡ Đổi tất cả sang Grok</option>
                <option value="qwen" className="bg-slate-900 text-slate-200">⚔️ Đổi tất cả sang Qwen</option>
                <option value="deepseek" className="bg-slate-900 text-slate-200">🐋 Đổi tất cả sang DeepSeek</option>
              </select>
              <div className="w-[1px] h-5 bg-indigo-500/30"></div>
              <button
                onClick={() => {
                  queue.forEach(item => {
                    if (item.status !== 'completed') {
                       const newStatus = item.status === 'error' ? ((item.chaptersDone === 0 && !item.bible) ? 'draft_outline' : 'pending') : item.status;
                       updateQueueItem(item.id, { writeEngine: bulkEngine as any, outlineEngine: bulkEngine as any, status: newStatus as any, errorLog: undefined });
                    }
                  });
                }}
                className="text-indigo-400 font-bold hover:text-indigo-300 text-sm flex items-center gap-1 ml-1 whitespace-nowrap"
              >
                ↻ Đồng Bộ ({queue.filter(q => q.status !== 'completed').length}) Truyện
              </button>
            </div>
          )}

          {/* NÚT LÊN DÀN Ý HÀNG LOẠT */}
          {draftItems.length > 0 && (
            <button
              onClick={handleBatchOutline}
              disabled={isBatchLoading}
              className={`px-4 py-2 rounded-lg text-sm font-bold flex items-center gap-2 transition-all border ${
                isBatchLoading
                  ? 'bg-indigo-500/10 text-indigo-300 border-indigo-500/30 cursor-wait animate-pulse'
                  : 'bg-indigo-500/20 text-indigo-300 hover:bg-indigo-500/40 border-indigo-500/50 shadow-[0_0_10px_rgba(99,102,241,0.2)]'
              }`}
            >
              <Zap size={16} />
              {isBatchLoading
                ? `Đang lên dàn ý ${draftItems.length} truyện...`
                : `🚀 Lên Dàn Ý Hàng Loạt (${draftItems.length})`}
            </button>
          )}

          {/* DUYỆT TẤT CẢ */}
          {approvalItems.length > 0 && (
            <button
              onClick={() => approvalItems.forEach(q => updateQueueItem(q.id, { status: 'pending' }))}
              className="px-4 py-2 bg-yellow-500/20 text-yellow-500 hover:bg-yellow-500/40 border border-yellow-500/50 rounded-lg text-sm font-bold transition-colors flex items-center gap-2 shadow-[0_0_10px_rgba(234,179,8,0.2)]"
            >
              ✅ Duyệt Tất Cả ({approvalItems.length}) Dàn Ý
            </button>
          )}

          <button
            onClick={toggleAutoPilot}
            className={`px-6 py-2 rounded-lg text-sm font-bold flex items-center gap-2 transition-all ${
              isAutoPilotRunning
                ? 'bg-amber-500 border border-amber-400 text-amber-950 shadow-[0_0_15px_rgba(245,158,11,0.5)]'
                : 'bg-emerald-600 hover:bg-emerald-500 text-white shadow-lg'
            }`}
          >
            {isAutoPilotRunning ? <><Pause size={16} /> TẠM DỪNG TIẾN TRÌNH</> : <><Play size={16} /> KÍCH HOẠT AUTO-PILOT</>}
          </button>
        </div>
      </div>

      {/* LOG PANEL */}
      {batchStatus && (
        <div className="mb-4 bg-indigo-950/50 border border-indigo-500/30 rounded-xl p-4 text-xs font-mono text-indigo-300 whitespace-pre-wrap max-h-40 overflow-y-auto custom-scrollbar flex-shrink-0">
          {batchStatus}
          <button onClick={() => setBatchStatus('')} className="block mt-2 text-indigo-500 hover:text-white">✕ Đóng log</button>
        </div>
      )}

      {/* ENGINE STATUS */}
      {isAutoPilotRunning && (
        <div className="bg-slate-900 border border-slate-800 p-4 rounded-xl mb-6 flex justify-between items-center flex-shrink-0">
          <div className="flex items-center gap-3">
            <div className={`w-3 h-3 rounded-full ${pulse ? 'bg-emerald-400 scale-125' : 'bg-emerald-600'} transition-all shadow-[0_0_10px_rgba(52,211,153,0.8)]`}></div>
            <span className="text-emerald-400 font-mono text-sm tracking-widest font-bold">M-CORE ENGINE ONLINE</span>
          </div>
          <div className="text-xs text-slate-500 font-mono">Chạy liên tục không ngủ, vòng lặp 5 giây</div>
        </div>
      )}

      {/* QUEUE LIST */}
      <div className="flex-1 overflow-y-auto pr-2 space-y-4 custom-scrollbar">
        {queue.length === 0 ? (
          <div className="h-full flex flex-col items-center justify-center border-2 border-dashed border-slate-800 rounded-2xl text-slate-500">
            <ShieldAlert size={40} className="mb-4 text-slate-700" />
            <p>Trạm đang trống. Mời bạn sang khu vực Brainstorm ném kịch bản vào đây!</p>
          </div>
        ) : (
          queue.map((item, index) => (
            <div key={item.id} className="bg-slate-900 overflow-hidden border border-slate-800 rounded-xl flex items-stretch group hover:border-slate-700 transition-colors">
              <div className="w-16 bg-slate-950 flex flex-col items-center justify-center border-r border-slate-800 text-slate-500 font-black text-xl">
                #{index + 1}
              </div>
              <div className="p-4 flex-1">
                <div className="flex justify-between items-start mb-2">
                  <h4 className="text-lg font-bold text-white leading-tight">{item.title}</h4>
                  <button onClick={() => removeQueueItem(item.id)} className="text-slate-600 hover:text-red-400 opacity-0 group-hover:opacity-100 transition-opacity">
                    <Trash2 size={16} />
                  </button>
                </div>

                <div className="flex flex-wrap gap-2 mb-4">
                  <span className="inline-block px-2 py-1 bg-blue-900/40 text-blue-400 border border-blue-500/20 rounded text-[10px] uppercase font-black tracking-wider">
                    {item.genres}
                  </span>
                  <span className="inline-block px-2 py-1 bg-purple-900/40 text-purple-400 border border-purple-500/20 rounded text-[10px] uppercase font-black tracking-wider">
                    Nguồn: {item.isAdvancedPipeline ? "Sáng tác 7" : item.comboType === 6 ? "Sáng tác 6" : item.comboType === 5 ? "Sáng tác 5" : "Thủ công"}
                  </span>
                  {item.createdAt && (
                    <span suppressHydrationWarning className="inline-block px-2 py-1 bg-slate-800/80 text-slate-400 border border-slate-700/50 rounded text-[10px] uppercase font-bold tracking-wider">
                      Tạo: {new Date(item.createdAt).toLocaleString('vi-VN', { hour: '2-digit', minute: '2-digit', day: '2-digit', month: '2-digit', year: 'numeric' })}
                    </span>
                  )}
                  {item.completedAt && (
                    <span suppressHydrationWarning className="inline-block px-2 py-1 bg-emerald-900/40 text-emerald-400 border border-emerald-500/20 rounded text-[10px] uppercase font-bold tracking-wider flex items-center gap-1">
                      Xong: {new Date(item.completedAt).toLocaleString('vi-VN', { hour: '2-digit', minute: '2-digit', day: '2-digit', month: '2-digit', year: 'numeric' })}
                    </span>
                  )}
                </div>

                {item.status === 'pending_approval' ? (
                  <div className="mt-4 bg-yellow-500/10 border border-yellow-500/50 rounded-xl p-4 flex flex-col gap-3">
                    <div className="flex items-start gap-3">
                      <ShieldAlert className="text-yellow-400 shrink-0 mt-0.5" size={20} />
                      <div className="w-full">
                        <h5 className="font-bold text-yellow-400 text-sm">Dàn ý đã thiết lập xong! AI chốt: {item.targetChapters} Chương.</h5>
                        <p className="text-yellow-500/80 text-xs mt-1">Dưới đây là sơ lược tuyến thời gian (Timeline) mà AI vừa phác thảo.</p>

                        <div className="bg-black/40 border border-yellow-500/30 rounded-lg p-3 mt-3 max-h-48 overflow-y-auto custom-scrollbar text-[13px] text-yellow-100/90 whitespace-pre-wrap font-medium">
                          {(item.bible as any)?.timeline && Array.isArray((item.bible as any).timeline)
                             
                            ? ((item.bible as any).timeline as any[]).map((t: any, i: number) => `TẬP ${i + 1}: ${t.summary || t.plot || t.outline || t.content || JSON.stringify(t)}`).join('\n\n')
                            : (typeof (item.bible as any)?.timeline === 'string' ? (item.bible as any).timeline : JSON.stringify((item.bible as any)?.timeline || 'Không có dữ liệu dàn ý.', null, 2))}
                        </div>

                        <div className="flex flex-wrap items-center gap-3 mt-4">
                          <label className="text-xs font-bold text-yellow-500/80 uppercase tracking-widest whitespace-nowrap">Số Chương:</label>
                          <input
                            type="number"
                            value={parseInt(String(item.targetChapters)) || 1}
                            onChange={(e) => updateQueueItem(item.id, { targetChapters: parseInt(e.target.value) || 1, maxChapters: parseInt(e.target.value) || 1 })}
                            className="bg-black/50 border border-yellow-500/50 rounded text-yellow-400 font-bold px-3 py-1.5 w-20 outline-none text-center shadow-inner"
                          />
                          <button
                            onClick={() => { const b = { ...(item.bible as object) }; delete (b as any).timeline; updateQueueItem(item.id, { status: 'draft_outline', bible: b, errorLog: undefined }); }}
                            className="bg-yellow-500/20 text-yellow-400 hover:bg-yellow-500/30 border border-yellow-500/30 px-4 py-1.5 rounded-lg font-bold text-xs transition-colors whitespace-nowrap"
                          >
                            🔄 Đập Đi Vẽ Lại Dàn Ý
                          </button>
                        </div>
                      </div>
                    </div>
                    <button
                      onClick={() => updateQueueItem(item.id, { status: 'pending' })}
                      className="bg-yellow-500 text-yellow-950 px-4 py-2 rounded-lg font-bold text-sm w-full hover:bg-yellow-400 transition-colors"
                    >
                      ✅ Cấp Quyền & AutoPilot Viết Ngay
                    </button>
                  </div>
                ) : (
                  <>
                    <div className="w-full bg-slate-950 h-3 rounded-full overflow-hidden border border-slate-800">
                      <div
                        className="h-full bg-gradient-to-r from-blue-500 to-purple-500 transition-all duration-1000 ease-in-out relative"
                        style={{ width: `${(item.chaptersDone / (item.targetChapters || 1)) * 100}%` }}
                      >
                        <div className="absolute inset-0 bg-white/20 w-full animate-pulse-slow"></div>
                      </div>
                    </div>
                    <div className="flex justify-between items-center mt-2 text-xs text-slate-400 font-mono">
                      <div className="flex items-center gap-2">
                        <span>TRẠNG THÁI: {item.status.toUpperCase()}</span>
                          <div className="flex items-center gap-2">
                            <select
                              value={item.writeEngine || 'gemini'}
                              onChange={(e) => updateQueueItem(item.id, { writeEngine: e.target.value as any, outlineEngine: e.target.value as any })}
                              className="bg-slate-900/80 border border-slate-700 text-slate-300 text-xs rounded px-2 py-0.5 outline-none hover:border-slate-500 transition-colors"
                              title="Thay đổi nhanh API Engine cho truyện này"
                            >
                              <option value="gemini">🤖 Gemini</option>
                              <option value="openai">🧠 OpenAI</option>
                              <option value="claude">🎭 Claude</option>
                              <option value="grok">⚡ Grok</option>
                              <option value="qwen">⚔️ Qwen</option>
                              <option value="deepseek">🐋 DeepSeek</option>
                            </select>
                            {item.status === 'error' && (
                            <button
                              onClick={() => {
                                const newStatus = (item.chaptersDone === 0 && !item.bible) ? 'draft_outline' : 'pending';
                                updateQueueItem(item.id, { status: newStatus, errorLog: undefined });
                              }}
                              className="flex items-center gap-1 bg-rose-500/10 text-rose-400 border border-rose-500/30 px-2 py-0.5 rounded font-bold hover:bg-rose-500/20 transition-all"
                            >
                              ↻ Thử Lại
                            </button>
                            )}
                          </div>
                      </div>
                      <span>{item.chaptersDone}/{item.targetChapters} CHƯƠNG</span>
                    </div>
                  </>
                )}

                {item.status === 'error' && item.errorLog && (
                  <div className="mt-3 p-2 bg-red-500/10 border border-red-500/20 rounded-md text-red-400 text-xs font-mono whitespace-pre-wrap break-words max-h-24 overflow-y-auto">
                    Biên bản lỗi: {item.errorLog}
                  </div>
                )}

                {/* NÚT GỬI TỔNG DUYỆT — hiện khi truyện đã xong */}
                {(item.status === 'completed' || item.status === 'final_review') && (
                  <button
                    onClick={() => {
                      updateQueueItem(item.id, { status: 'final_review' });
                      if (onNavigate) onNavigate('final_review');
                    }}
                    className="mt-3 w-full flex items-center justify-center gap-2 px-4 py-2.5 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-sm rounded-lg transition-all shadow-[0_0_12px_rgba(16,185,129,0.3)] hover:shadow-[0_0_20px_rgba(16,185,129,0.5)] border border-emerald-500/40"
                  >
                    <Send size={15} />
                    📋 Gửi Tổng Duyệt (Gatekeeper)
                  </button>
                )}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
