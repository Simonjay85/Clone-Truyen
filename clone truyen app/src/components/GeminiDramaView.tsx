"use client";
/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable @typescript-eslint/ban-ts-comment */
// @ts-nocheck
import React, { useState } from 'react';
import { useStore } from '../store/useStore';
import { Bot, Rocket, PenTool, ExternalLink, Settings, CheckCircle2, User as UserIcon, BookOpen } from 'lucide-react';
import { agentPuppetMaster, callGemini } from '../lib/engine';
import { agentConceptScorer, agentPitchRefiner } from '../lib/advanced_engine';
// callGemini } from '../lib/engine';

const GENRES_GROUPS = {
  "🔥 Kịch Tính Cao": ["Vả Mặt", "Sảng Văn", "Gia Đấu", "Cung Đấu", "Trọng Sinh"],
  "🌍 Bối Cảnh": ["Đô Thị", "Hào Môn", "Xuyên Không", "Mạt Thế", "Hệ Thống", "Hợp Đồng Hôn Nhân", "Tổng Tài"],
  "❤️ Cảm Xúc": ["Ngược Tâm", "Sủng Ngọt", "Hài Hước", "Nữ Cường", "Trà Xanh / Tiểu Tam", "Truy Thê"]
};

export function GeminiDramaView({ onNavigate }: { onNavigate?: (tab: string) => void }) {
  const { geminiKey, addQueueItems, draftSpaces, updateDraftSpace } = useStore();
  
  const [refineFeedback, setRefineFeedback] = useState('');
  const [isRefining, setIsRefining] = useState(false);
  const [title, setTitle] = useState('');
  const [prompt, setPrompt] = useState('');
  const [targetChapters, setTargetChapters] = useState(20);
  const [maxChapters, setMaxChapters] = useState(40);
  const [pitchCount, setPitchCount] = useState(5);
  const [isConfigExpanded, setIsConfigExpanded] = useState(true);
  const [selectedGenres, setSelectedGenres] = useState<string[]>([]);
  const [selectedModel, setSelectedModel] = useState('gpt-4o-mini');
  
  const [isGenerating, setIsGenerating] = useState(false);
  const [showBulkImport, setShowBulkImport] = useState(false);
  const [bulkImportData, setBulkImportData] = useState('');
  const [pitchOptions, setPitchOptions] = useState<unknown[]>([]);
  const [gradingStatus, setGradingStatus] = useState<Record<number, { grading: string; score: number }>>({});
  const [isGradingParam, setIsGradingParam] = useState<number | null>(null);

  const draft = draftSpaces['gemini_drama'] || {};

  React.useEffect(() => {
    setTimeout(() => { if (draft.title !== undefined && draft.title !== title) setTitle(draft.title); }, 0);
    setTimeout(() => { if (draft.prompt !== undefined && draft.prompt !== prompt) setPrompt(draft.prompt); }, 0);
    setTimeout(() => { if (draft.targetChapters !== undefined && draft.targetChapters !== targetChapters) setTargetChapters(draft.targetChapters); }, 0);
    setTimeout(() => { if (draft.pitchCount !== undefined && draft.pitchCount !== pitchCount) setPitchCount(draft.pitchCount); }, 0);
    setTimeout(() => { if (draft.pitchOptions !== undefined && JSON.stringify(draft.pitchOptions) !== JSON.stringify(pitchOptions)) setPitchOptions(draft.pitchOptions); }, 0);
    setTimeout(() => { if (draft.gradingStatus !== undefined && JSON.stringify(draft.gradingStatus) !== JSON.stringify(gradingStatus)) setGradingStatus(draft.gradingStatus); }, 0);
  }, [draft]);

  React.useEffect(() => {
    const timer = setTimeout(() => {
      updateDraftSpace('gemini_drama', { title, prompt, targetChapters, pitchCount, pitchOptions, gradingStatus });
    }, 500);
    return () => clearTimeout(timer);
  }, [title, prompt, targetChapters, pitchCount, pitchOptions, gradingStatus]);

  const toggleGenre = (g: string) => {
    if (selectedGenres.includes(g)) {
      setSelectedGenres(selectedGenres.filter(x => x !== g));
    } else {
      setSelectedGenres([...selectedGenres, g]);
    }
  };

  const handleGenerateOutline = async () => {
    if (!geminiKey) return alert("⚠️ Bạn chưa nhập OpenAI API Key trong Settings!");
    if (!prompt && selectedGenres.length === 0) return alert("Vui lòng nhập Ý tưởng cốt truyện hoặc chọn ít nhất 1 Thể loại!");

    setIsGenerating(true);
    setPitchOptions([]);
    setGradingStatus({});
    
    try {
      const genresStr = selectedGenres.length > 0 ? selectedGenres.join(', ') : 'Hỗn hợp';
      
      const res = await fetch('/api/gemini', {
         method: 'POST',
         headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            apiKey: geminiKey,
            systemPrompt: `Bạn là Đạo Diễn Thiết Lập xuất sắc của Google Gemini. TẠO ĐÚNG ${pitchCount} KỊCH BẢN MICRO-DRAMA KHÁC NHAU ĐỂ LỰA CHỌN.
TUYỆT ĐỐI KHÔNG DÙNG TỪ TIẾNG ANH. Viết bằng tiếng Việt hoặc Hán Việt thuần túy. Xây dựng cốt truyện mang màu sắc Châu Á (đặc biệt là Việt Nam hoặc Trung Quốc).
BẮT BUỘC TRẢ VỀ JSON OBJECT CÓ KEY "pitches" LÀ ARRAY CÓ ĐÚNG ${pitchCount} KỊCH BẢN.
{
  "pitches": [
    {
      "super_title": "Một Tên Truyện SIÊU CUỐN HÚT, trend hiện đại (Ví dụ: 'Mẹ Chồng Khinh Bỉ, Tôi Tát Lật Mặt', 'Trùng Sinh Trở Thành Bà Trùm', 'Tổng Tài Bá Đạo Cầu Xin Tha Thứ'). TUYỆT ĐỐI KHÔNG DÙNG TỪ HÁN VIỆT CŨ KỸ, KHÔNG GẮN ĐUÔI VERSION.",
      "summary": "Tóm tắt truyện (Viết thật dài, miêu tả chi tiết sâu sắc nỗi đau/sự kịch tính, nhồi nhét liên tục các HOOK giật gân, đảm bảo người đọc liếc qua là máu dồn lên não lôi cuốn đọc ngay lập tức!)",
      "worldSettings": "Bối cảnh (1-2 câu)",
      "characterArc": "Vết thương lòng/Sự phát triển của nhân vật",
      "plotTwists": "Cú lật bàn không lường trước/Vả mặt",
      "overallSizzle": "Sự bạo não tóm tắt",
      "genres": "Gán TRỰC TIẾP 1-3 Danh mục/Thể loại chính của truyện (Ví dụ: Trọng Sinh, Vả Mặt, Đô Thị). Danh mục này sẽ đi xuyên suốt hệ thống và làm Category khi đăng lên web.",
      "suggestedChapters": "Hãy sinh ra DUY NHẤT 1 CON SỐ (Number) là số chương mục tiêu ước tính. Con số này PHẢI nằm trong khoảng từ ${targetChapters} đến ${maxChapters}."
    }
  ]
}`,
            userPrompt: prompt ? `Thể loại: ${genresStr}\nYêu cầu gốc: ${prompt}` : `Thể loại: ${genresStr}\nYêu cầu: Dựa vào các thể loại tôi đã chọn, hãy tự do sáng tạo và gợi ý ra các kịch bản xuất sắc, khác biệt, đầy bạo não và lôi cuốn nhất. Không cần bám theo mô-típ sáo rỗng.`,
            jsonMode: true,
            temperature: 1.0,
            model: selectedModel || 'gemini-2.5-flash'
         })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error?.message || JSON.stringify(data.error));
      let text = data.text.trim();
      if (text.startsWith('```json')) text = text.replace('```json', '').replace(/```$/, '').trim();
      else if (text.startsWith('```')) text = text.replace('```', '').replace(/```$/, '').trim();
      const rawData = JSON.parse(text);
      
       
      let pitches: unknown[] = [];
      if (Array.isArray(rawData)) {
          pitches = rawData;
      } else if (rawData.pitches && Array.isArray(rawData.pitches)) {
          pitches = rawData.pitches;
      } else if (rawData.options && Array.isArray(rawData.options)) {
          pitches = rawData.options;
      } else {
          const arrVal = Object.values(rawData as any).find(v => Array.isArray(v));
          pitches = Array.isArray(arrVal) ? arrVal : [rawData];
      }
      
      setPitchOptions(pitches.slice(0, pitchCount)); 
      if (!title && ((pitches[0] as any)?.super_title || (pitches[0] as any)?.protagonist)) setTitle((pitches[0] as any)?.super_title || (pitches[0] as any)?.protagonist);
      
      // Auto-minimize config panel so user can read pitches
      if (pitches.length > 0) {
        setIsConfigExpanded(false);
      }
    } catch (e: any) {
      alert("Lỗi AI: " + e.message);
    } finally {
      setIsGenerating(false);
    }
  };

  
  
  const refineSelectedPitches = async () => {
     if (!geminiKey) return alert("Chưa có API Key");
     if (selectedPitches.length === 0) return alert("Vui lòng tick chọn ít nhất 1 kịch bản để sửa chữa!");
     if (!refineFeedback.trim()) return alert("Vui lòng nhập lời khuyên/hướng sửa đổi làm kim chỉ nam cho AI!");
     
     setIsRefining(true);
     try {
         const newPOptions = [...pitchOptions];
         for (let i = 0; i < selectedPitches.length; i++) {
             const idx = selectedPitches[i];
             const result = await agentPitchRefiner('gemini', geminiKey, selectedModel || 'gemini-1.5-flash', newPOptions[idx], refineFeedback);
             if (result && (result.super_title || result.protagonist)) {
                 newPOptions[idx] = result;
             }
         }
         
         setPitchOptions(newPOptions);
         
         setIsGradingParam(-1);
         const res: any = await agentConceptScorer('gemini', geminiKey, selectedModel || 'gemini-1.5-flash', newPOptions);
          
         const newGradingStatus: any = {};
         if (res.scores && Array.isArray(res.scores)) {
              
             res.scores.forEach((s: any) => {
                 newGradingStatus[s.index] = { score: s.score || 0, grading: s.reason || s.grading || '' };
             });
             setGradingStatus(newGradingStatus);
         }
         
         alert("✅ Phẫu thuật thành công " + selectedPitches.length + " kịch bản và đã Chấm điểm lại xong! Lên Top chưa anh zai?");
         
     } catch (e: any) {
         alert("Lỗi Phẫu Thuật: " + e.message);
     } finally {
         setIsRefining(false);
         setIsGradingParam(null);
     }
  };

  const gradeAllPitches = async () => {
     if (!geminiKey) return alert("Chưa có API Key");
     if (pitchOptions.length === 0) return alert("Chưa có kịch bản nào để chấm!");
     setIsGradingParam(-1);
     try {
         const res = await agentConceptScorer('gemini', geminiKey, 'gemini-1.5-flash', pitchOptions);
          
         const newGradingStatus: any = {};
         if (res.scores && Array.isArray(res.scores)) {
              
             res.scores.forEach((s: any) => {
                 newGradingStatus[s.index] = { score: s.score || 0, grading: s.reason || s.grading || '' };
             });
             setGradingStatus(newGradingStatus);
         }
     } catch (e: any) {
         alert("Lỗi chấm điểm chùm: " + e.message);
     } finally {
         setIsGradingParam(null);
     }
  };

  const gradePitch = async (index: number) => {
     setIsGradingParam(index);
     const pitch = pitchOptions[index];
     try {
        if (!geminiKey) return alert("Chưa có API Key");
        const res = await agentConceptScorer('gemini', geminiKey, selectedModel || 'gemini-1.5-flash', [pitch]);
        
        if (res.scores && Array.isArray(res.scores) && res.scores.length > 0) {
            const gradeData = res.scores[0];
            setGradingStatus(prev => ({ ...prev, [index]: { score: gradeData.score || 0, grading: gradeData.reason || gradeData.grading || '' } }));
        }
     } catch (e: any) {
        alert("Lỗi chấm điểm: " + e.message);
     } finally {
        setIsGradingParam(null);
     }
  };

  const [selectedPitches, setSelectedPitches] = useState<number[]>([]);

  const updatePitch = (idx: number, field: string, value: string) => { const newPOptions = [...pitchOptions]; newPOptions[idx] = { ...(newPOptions[idx] as any), [field]: value }; setPitchOptions(newPOptions); }; const togglePitchSelect = (idx: number) => {
      if (selectedPitches.includes(idx)) setSelectedPitches(selectedPitches.filter(i => i !== idx));
      else setSelectedPitches([...selectedPitches, idx]);
  };


  const handleClearBoard = () => {
    if (confirm("Chắc chắn muốn xóa toàn bộ kịch bản hiện tại?")) {
       setPitchOptions([]);
       setGradingStatus({});
       setSelectedPitches([]);
       setRefineFeedback('');
       sessionStorage.removeItem('md_pitchOptions');
    }
  };

  const handlePushAutopilot = () => {
    if (selectedPitches.length === 0) return alert("Vui lòng tick chọn ít nhất 1 kịch bản để xả vào hệ thống Auto-Pilot!");
    const items = selectedPitches.map(idx => ({
        title: (pitchOptions[idx] as any).super_title || `Truyện Chấn Động ${idx+1}`,
        genres: (pitchOptions[idx] as any).genres || selectedGenres.join(', ') || 'Tự do',
        prompt: prompt,
        bible: pitchOptions[idx],
        targetChapters: parseInt((pitchOptions[idx] as any).suggestedChapters) || targetChapters,
        maxChapters: maxChapters,
        model: selectedModel,
        outlineEngine: 'gemini' as const, writeEngine: 'gemini' as const
    }));
    addQueueItems(items);
    setSelectedPitches([]);
    if (confirm(`🚀 Đã đẩy ${items.length} kịch bản vào lò Auto-Pilot!

Bạn có muốn XÓA TRẮNG Bảng kịch bản hiện tại để viết bộ mới không?`)) {
       setPitchOptions([]);
       setGradingStatus({});
    } else {
       // Filter out the pushed ones so they don't get pushed again by mistake
       const newOptions = pitchOptions.filter((_, idx) => !selectedPitches.includes(idx));
       setPitchOptions(newOptions);
       setGradingStatus({}); // Reset grading as indexes shift
    }
    if (onNavigate) onNavigate('autopilot');
  };

  const notImplemented = (featureName: string) => {
     alert(`Tính năng [${featureName}] đang trong lộ trình phát triển. Vui lòng quay lại sau!`);
  };

  return (
    <div className="w-full h-full flex flex-col font-sans bg-[#0f0f17] text-[#e2e8f0] overflow-hidden animation-fade-in">
      
      {/* 1. NATIVE NAVBAR LIKE SCREENSHOT */}
      <nav className="h-auto md:h-[60px] py-4 md:py-0 bg-[rgba(15,15,23,0.9)] border-b border-[rgba(255,255,255,0.07)] px-4 md:px-6 flex flex-col md:flex-row items-center justify-between shrink-0 z-50 backdrop-blur-md gap-4 md:gap-0">
        <div className="flex items-center gap-2 font-extrabold text-[16px] md:text-[18px] text-white tracking-wide text-center">
          🎬 Trạm Đạo Diễn <span className="bg-gradient-to-br from-blue-500 to-indigo-400 text-white px-2.5 py-0.5 rounded-full text-xs uppercase tracking-wider ml-1">Gemini</span>
        </div>
        
        <div className="flex items-center gap-3">
           <button className="px-6 py-2 rounded-lg bg-gradient-to-br from-blue-500 to-indigo-500 text-white font-bold text-sm shadow-lg">🎬 Đạo Diễn</button>
           <button onClick={() => onNavigate && onNavigate('settings')} className="bg-indigo-500/15 border border-indigo-500/50 px-4 py-1.5 rounded-full text-indigo-300 font-bold flex items-center gap-1.5 hover:bg-indigo-500/30 transition-all">
             📊 API Quota
           </button>
        </div>

        <div className="hidden md:flex items-center gap-4 text-sm">
           <div className="bg-white/5 border border-white/10 px-4 py-1.5 rounded-full text-slate-300 flex items-center gap-2 font-medium">
             <UserIcon size={16} /> alotoinghe
           </div>
           <button className="text-slate-500 hover:text-white transition-colors font-medium">← Về trang chủ</button>
        </div>
      </nav>

      {/* 2. MAIN LAYOUT */}
      <div className="flex flex-col md:flex-row flex-1 overflow-y-auto overflow-x-hidden md:overflow-hidden relative">
        
        {/* LEFT PANEL: CONFIG (width: 540px on Desktop, full width on Mobile) */}
        {isConfigExpanded && (
        <aside className="w-full md:w-[540px] bg-[#13131f] border-b md:border-b-0 md:border-r border-white/5 flex flex-col md:overflow-y-auto custom-scrollbar p-6 shrink-0 z-10 transition-all">
          <div className="flex justify-between items-center mb-5">
             <h3 className="text-xs font-bold text-[#6b7a99] uppercase tracking-[1.5px]">⚙️ Cấu Hình Truyện</h3>
             <button onClick={() => setIsConfigExpanded(false)} className="text-slate-500 hover:text-white p-1 rounded-md hover:bg-white/5">
                ✕ Thao tác xong, đóng lại
             </button>
          </div>
          
          <div className="bg-white/5 border border-white/10 rounded-xl p-5 mb-5">
             <div className="flex justify-between items-center mb-3 text-sm font-semibold text-[#94a3b8]">
                <span>Engine AI Định Tuyến</span>
                <button onClick={() => onNavigate && onNavigate('settings')} className="bg-emerald-500/15 border border-emerald-500/50 px-2 py-1 rounded-lg text-emerald-300 flex items-center gap-1.5 text-xs hover:bg-emerald-500/30 transition-all">
                   <Settings size={14}/> Settings
                </button>
             </div>
             
             <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-lg p-3 text-sm text-emerald-300 leading-relaxed font-medium">
                <strong>❖ OpenAI System:</strong> Model mặc định được thiết lập là <code>gpt-4o-mini</code> để tốn cực ít Credits trong quá trình sinh Kịch bản. <br/><br/>Hệ thống Auto-Pilot đằng sau sẽ tự động switch sang sát thủ <code>gpt-4o</code> để viết kịch bản và rải độc.
             </div>
          </div>

          <div className="bg-white/5 border border-white/10 rounded-xl p-5 mb-5">
             <label className="block text-sm font-semibold text-[#94a3b8] mb-3">Tiêu đề / Tên Truyện</label>
             <input type="text" className="w-full bg-black/30 border border-white/10 rounded-lg p-3 text-sm text-slate-200 outline-none focus:border-indigo-500 font-medium" placeholder="Ví dụ: Chiếc Nhẫn Quyền Năng..." value={title} onChange={e => setTitle(e.target.value)} />
          </div>

          <div className="bg-white/5 border border-white/10 rounded-xl p-5 mb-5">
             <div className="flex justify-between items-end mb-3">
                <label className="text-sm font-semibold text-[#94a3b8]">Ý tưởng cốt truyện (Prompt)</label>
                <button onClick={() => onNavigate && onNavigate('autopilot')} className="bg-indigo-500/15 border border-indigo-500/40 text-indigo-400 font-bold text-xs px-3 py-1.5 rounded-lg hover:bg-indigo-500/30 transition-all">🚀 Trạm Auto-Pilot</button>
             </div>
             <textarea rows={5} className="w-full bg-black/30 border border-white/10 rounded-lg p-3.5 text-sm text-slate-200 outline-none focus:border-indigo-500 resize-none leading-relaxed mb-3 font-medium" placeholder="Mô tả ngắn gọn: Nhân vật, bối cảnh, xung đột chính..." value={prompt} onChange={e => setPrompt(e.target.value)}></textarea>
             
             <div className="flex flex-col gap-3">
                <div className="flex gap-2 w-full">
                   <div className="flex items-center bg-emerald-500/5 border border-emerald-500/40 rounded-lg px-3 py-1.5 flex-[1.5]">
                     <span className="text-[11px] text-emerald-600/80 font-bold uppercase tracking-wide mr-2 w-max">Số Chương:</span>
                     <input type="number" className="w-[45%] bg-transparent text-emerald-400 font-bold text-sm outline-none text-center border-b border-emerald-500/20 focus:border-emerald-500/80 transition-colors" title="Số chương tối thiểu" value={targetChapters} onChange={e => setTargetChapters(parseInt(e.target.value) || 1)} />
                     <span className="text-[11px] text-emerald-600/50 font-bold mx-2">TỐI ĐA</span>
                     <input type="number" className="w-[45%] bg-transparent text-emerald-400 font-bold text-sm outline-none text-center border-b border-emerald-500/20 focus:border-emerald-500/80 transition-colors" title="Số chương tối đa" value={maxChapters} onChange={e => setMaxChapters(parseInt(e.target.value) || 1)} />
                   </div>
                   <div className="flex items-center bg-blue-500/5 border border-blue-500/40 rounded-lg px-3 py-1.5 flex-1">
                     <span className="text-[11px] text-blue-600/80 font-bold uppercase tracking-wide mr-2">Đề Xuất:</span>
                     <input type="number" className="w-full bg-transparent text-blue-400 font-bold text-sm outline-none" title="Số kịch bản gợi ý đồng thời ráp vòng 1" value={pitchCount} onChange={e => setPitchCount(parseInt(e.target.value) || 1)} />
                   </div>
                </div>
                
                <button onClick={handleGenerateOutline} disabled={isGenerating} className="w-full bg-emerald-500/10 border border-emerald-500/40 rounded-lg text-emerald-500 font-bold text-xs py-2.5 hover:bg-emerald-500/20 transition-all flex items-center justify-center gap-2 shadow-[0_0_10px_rgba(16,185,129,0.15)] uppercase tracking-wide">
                  {isGenerating ? '⏳ Đang xoay Kịch Bản...' : `💡 Gợi ý ${pitchCount} Kịch Bản Khác Biệt`}
                </button>
             </div>
             
             <div className="flex gap-2 mt-3">
                <button onClick={() => notImplemented("Gợi ý Tiêu đề AI")} className="flex-1 bg-amber-500/10 border border-amber-500/40 rounded-lg text-amber-500 font-bold text-xs py-2 hover:bg-amber-500/20 transition-all flex items-center justify-center gap-1.5">🤖 Auto Đặt Tên</button>
                <button onClick={() => setShowBulkImport(true)} className="flex-1 bg-pink-500/10 border border-pink-500/40 rounded-lg text-pink-500 font-bold text-xs py-2 hover:bg-pink-500/20 transition-all flex items-center justify-center gap-1.5">📝 Nhập Tự Do</button>
             </div>
          </div>

          <div className="bg-white/5 border border-white/10 rounded-xl p-5">
             <label className="block text-sm font-semibold text-[#94a3b8] mb-3 flex items-center gap-1">Thể loại <span className="font-normal text-xs">(Chọn 1 hoặc nhiều)</span></label>
             <div className="flex flex-col gap-4">
                {Object.entries(GENRES_GROUPS).map(([groupName, genres]) => (
                   <div key={groupName}>
                     <div className="text-[11px] font-bold text-slate-500 mb-2 uppercase tracking-wide">{groupName}</div>
                     <div className="flex flex-wrap gap-2">
                        {genres.map(g => (
                           <button key={g} onClick={() => toggleGenre(g)} className={`px-3 py-1.5 rounded-full border text-xs font-semibold transition-all ${selectedGenres.includes(g) ? 'border-emerald-500 text-emerald-300 bg-emerald-500/20 shadow-[0_0_10px_rgba(16,185,129,0.15)]' : 'border-white/10 text-slate-400 hover:border-emerald-500/50 hover:text-emerald-300'}`}>{g}</button>
                        ))}
                     </div>
                   </div>
                ))}
             </div>
          </div>

        </aside>
        )}

        {/* RIGHT PANEL: EDITOR AREA */}
        <main className={`flex-1 bg-[#0a0a10] flex flex-col min-w-0 ${!isConfigExpanded ? 'md:ml-8' : ''}`}>
           {/* Editor Toolbar */}
           <div className="min-h-[48px] py-3 md:py-0 bg-[#17172a] border-b border-white/5 px-6 flex flex-col md:flex-row justify-between items-center shrink-0 gap-3">
              <div className="flex items-center gap-2 text-sm text-[#6b7a99] font-medium">
                 {!isConfigExpanded && (
                    <button onClick={() => setIsConfigExpanded(true)} className="bg-white/10 hover:bg-white/20 text-white px-3 py-1 rounded-md text-xs font-bold mr-2 transition-all">
                       Mở Cấu Hình ☰
                    </button>
                 )}
                 <div className={`w-2.5 h-2.5 rounded-full ${isGenerating ? 'bg-amber-500 animate-pulse' : pitchOptions.length > 0 ? 'bg-blue-500' : 'bg-slate-600'}`}></div>
                 {isGenerating ? 'Hệ thống AI đang gõ kịch bản. Vui lòng chờ...' : pitchOptions.length > 0 ? `Đã tạo ${pitchOptions.length} kịch bản` : 'Chờ lệnh'}
              </div>
                               <div className="flex gap-4 items-center">
                 {pitchOptions.length > 0 && <button disabled={isGradingParam === -1} onClick={gradeAllPitches} className="bg-amber-500/20 text-amber-400 border border-amber-500/30 px-4 py-2 rounded-lg text-sm font-bold flex items-center gap-2 hover:bg-amber-500/40 transition-all">{isGradingParam === -1 ? '⏳ Đang Chấm Điểm Hàng Loạt...' : '⚖️ Chấm Điểm Hàng Loạt'}</button>}

                 <div className="text-sm text-[#4b5563] font-mono font-medium">
                    {pitchOptions.length > 0 && <button onClick={handleClearBoard} className="bg-red-500/10 text-red-400 hover:bg-red-500/20 px-3 py-1.5 rounded-lg text-sm font-bold flex items-center gap-1 transition-all">🗑 Dọn Sạch</button>}
                 {pitchOptions.length > 0 ? `${selectedPitches.length}/${pitchOptions.length} Đã Chọn` : '0 từ'}
                 </div>
                 {pitchOptions.length > 0 && selectedPitches.length > 0 && (
                   <button onClick={handlePushAutopilot} className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white font-bold text-sm px-6 py-2 rounded-lg flex items-center gap-2 hover:opacity-90 transition-all shadow-lg animate-pulse">
                     <Rocket size={16} /> 🔪 Đẩy {selectedPitches.length} Kịch Bản Vào Auto-Pilot
                   </button>
                 )}
              </div>
           </div>

           <div className="flex-1 md:overflow-y-auto custom-scrollbar p-10 relative text-[#e2e8f0]">
              
              {!isGenerating && pitchOptions.length === 0 && (
                 <div className="h-full flex flex-col items-center justify-center text-center opacity-70">
                    <BookOpen size={72} className="text-[#374151] mb-6" />
                    <h2 className="text-[22px] font-bold text-[#4b5563] mb-4">Xưởng Sáng Tác AI</h2>
                    <p className="text-[15px] text-[#374151] max-w-[420px] leading-relaxed font-medium">
                       Nhập ý tưởng câu chuyện của bạn vào bảng điều khiển bên trái, sau đó bấm <strong>&quot;💡 Gợi ý Kịch Bản&quot;</strong>. Cỗ máy AI sẽ thiết lập các kịch bản và bạn có thể Nhờ Giám Khảo Supreme Judge chấm điểm rủi ro!
                    </p>
                 </div>
              )}

              {isGenerating && (
                 <div className="h-full flex flex-col items-center justify-center">
                    <Bot size={56} className="text-indigo-500 animate-bounce mb-5" />
                    <div className="text-indigo-400 font-bold text-[15px] tracking-[2px] animate-pulse uppercase">AI Đang Lên {pitchCount} Kịch Bản Tuyệt Đỉnh...</div>
                 </div>
              )}


              {/* SCRIPT DOCTOR AREA */}
              {selectedPitches.length > 0 && pitchOptions.length > 0 && !isGenerating && (
                 <div className="bg-gradient-to-r from-red-500/10 to-orange-500/10 border border-red-500/20 rounded-xl p-6 mb-8 mx-10 mt-2 animation-fade-in relative overflow-hidden">
                    <div className="absolute top-0 right-0 p-4 opacity-10 pointer-events-none">
                        <PenTool size={100} />
                    </div>
                    <h3 className="text-[17px] font-black text-rose-400 mb-3 flex items-center gap-2">🛠 Khu Vực Kỹ Sư Kịch Bản (Cấp Cứu)</h3>
                    <p className="text-[#cbd5e1] text-[13px] mb-4 font-medium">Gõ hoặc Dán lời khuyên, phê bình vào đây. AI sẽ bứt tóc sửa lại <strong className="text-white">{selectedPitches.length} kịch bản đang chọn</strong> cho đến khi hoàn hảo và cập nhật lại Bảng Xếp Hạng.</p>
                    <textarea 
                        className="w-full bg-black/40 text-rose-100 border border-red-500/30 rounded-lg p-3 text-[14px] leading-relaxed resize-none focus:border-red-400 focus:bg-black/60 outline-none min-h-[90px] mb-4 shadow-inner"
                        placeholder="Ví dụ: Đổi plot twist thành nam phụ đã âm thầm giật dây từ đầu..."
                        value={refineFeedback}
                        onChange={e => setRefineFeedback(e.target.value)}
                    ></textarea>
                    
                    <button 
                        onClick={refineSelectedPitches} disabled={isRefining || isGradingParam !== null}
                        className="bg-gradient-to-r from-red-600 to-orange-600 text-white font-bold text-[13px] uppercase tracking-wide px-6 py-3 rounded-lg flex items-center gap-2 hover:opacity-90 transition-all shadow-[0_4px_20px_rgba(220,38,38,0.3)] disabled:opacity-50">
                        {isRefining ? '🪄 Bác Sĩ Đang Gọt Giũa Kịch Bản... (Vui lòng chờ)' : '🪄 Bơm Máu Phẫu Thuật Kịch Bản Đi! (Auto-Fix)'}
                    </button>
                 </div>
              )}

              {pitchOptions.length > 0 && !isGenerating && (
                 <>
                               {Object.keys(gradingStatus).length > 2 && !isGenerating && (
                 <div className="bg-[#17172a] rounded-xl border border-white/5 p-6 mb-8 animation-fade-in mx-10 mt-6">
                    <h3 className="text-lg font-bold text-amber-400 mb-4 flex items-center gap-2">📊 Bảng Tổng Sắp Kịch Bản</h3>
                    <div className="overflow-x-auto">
                       <table className="w-full text-left text-sm text-[#cbd5e1]">
                          <thead className="bg-[#1e1e32] text-xs uppercase text-[#6b7a99] font-bold border-b border-white/10">
                             <tr>
                                <th className="px-4 py-3">Chọn</th>
                                <th className="px-4 py-3">STT</th>
                                <th className="px-4 py-3">Đề Tài</th>
                                <th className="px-4 py-3 text-center">Điểm</th>
                                <th className="px-4 py-3">Nhận Xét Của Judge</th>
                             </tr>
                          </thead>
                          <tbody className="divide-y divide-white/5">
                             {pitchOptions.map((p, i) => ({ pitch: p, index: i, grade: gradingStatus[i] }))
                                .filter(item => item.grade?.score !== undefined)
                                .sort((a, b) => b.grade.score - a.grade.score)
                                .map((item) => (
                                <tr key={item.index} className={`hover:bg-white/5 transition-colors ${selectedPitches.includes(item.index) ? 'bg-teal-500/10' : ''}`}>
                                   <td className="px-4 py-3 w-[60px]">
                                      <input type="checkbox" checked={selectedPitches.includes(item.index)} onChange={() => togglePitchSelect(item.index)} className="accent-teal-500 w-4 h-4 cursor-pointer" />
                                   </td>
                                   <td className="px-4 py-3 font-mono font-bold text-slate-500 w-[60px]">#{item.index + 1}</td>
                                   <td className="px-4 py-3 font-bold text-white max-w-[200px] truncate" title={typeof ((item.pitch as any) as any)?.super_title || ((item.pitch as any) as any)?.protagonist === 'object' ? JSON.stringify(((item.pitch as any) as any)?.super_title || ((item.pitch as any) as any)?.protagonist) : ((item.pitch as any) as any)?.super_title || ((item.pitch as any) as any)?.protagonist}>{typeof ((item.pitch as any) as any)?.super_title || ((item.pitch as any) as any)?.protagonist === 'object' ? JSON.stringify(((item.pitch as any) as any)?.super_title || ((item.pitch as any) as any)?.protagonist) : ((item.pitch as any) as any)?.super_title || ((item.pitch as any) as any)?.protagonist}</td>
                                   <td className="px-4 py-3 text-center w-[80px]">
                                      <span className={`font-black ${item.grade.score >= 8 ? 'text-emerald-400' : item.grade.score >= 6 ? 'text-amber-400' : 'text-red-400'}`}>{item.grade.score}</span>
                                   </td>
                                   <td className="px-4 py-3 text-[13px] opacity-80 max-w-[400px] truncate" title={item.grade.grading}>{item.grade.grading}</td>
                                </tr>
                             ))}
                          </tbody>
                       </table>
                    </div>
                 </div>
              )}

                 <div className="grid grid-cols-1 xl:grid-cols-2 gap-8 animation-fade-in pb-10">
                    {pitchOptions.map((pitch, idx) => {
                       const isSelected = selectedPitches.includes(idx);
                       const grading = gradingStatus[idx];
                       return (
                           <div key={idx} className={`bg-[#17172a] rounded-xl border ${isSelected ? 'border-emerald-500 shadow-[0_0_20px_rgba(20,184,166,0.2)]' : 'border-white/5'} p-8 relative flex flex-col transition-all overflow-hidden`}>
                             {/* Checkbox Overlay Background */}
                             {isSelected && <div className="absolute inset-0 bg-emerald-500/5 pointer-events-none"></div>}
                             
                             <div className="flex justify-between items-start mb-6">
                                <div className="flex items-center gap-4">
                                   <button onClick={() => togglePitchSelect(idx)} className={`w-8 h-8 rounded-full border-2 flex items-center justify-center transition-all ${isSelected ? 'bg-emerald-500 border-emerald-500 text-white' : 'border-slate-600 text-transparent hover:border-slate-500'}`}>
                                      <CheckCircle2 size={18} />
                                   </button>
                                   <div className="text-xs font-bold uppercase tracking-widest text-slate-500">PHIÊN BẢN {idx + 1}</div>
                                </div>
                                
                                {grading ? (
                                   <div className="bg-black/40 border border-white/10 px-4 py-2 rounded-lg flex items-center gap-3">
                                      <div className="text-xs text-slate-400 font-medium">ĐIỂM SỐ</div>
                                      <div className={`text-2xl font-black ${grading.score >= 8 ? 'text-emerald-400' : grading.score >= 6 ? 'text-amber-400' : 'text-red-400'}`}>{grading.score}</div>
                                   </div>
                                ) : (
                                   <button disabled={isGradingParam === idx} onClick={() => gradePitch(idx)} className="bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 hover:bg-cyan-500/20 px-4 py-2 rounded-lg text-xs font-bold flex items-center gap-2 transition-all">
                                      {isGradingParam === idx ? '⏳ Đang phân tích...' : '⚖️ Nhờ Judge Chấm Điểm'}
                                   </button>
                                )}
                             </div>

                                                          <input className="w-full text-2xl font-extrabold text-white mb-6 leading-snug bg-transparent border-b border-white/10 hover:border-white/30 focus:border-teal-500 outline-none pb-2 transition-colors"
                                value={(pitch as any).super_title || (pitch as any).protagonist || ''}
                                onChange={(e) => updatePitch(idx, (pitch as any).super_title !== undefined ? 'super_title' : 'protagonist', e.target.value)}
                                placeholder="Tên truyện..."
                             />

                             <div className="space-y-4 text-[14px] leading-relaxed text-[#cbd5e1] mb-6 flex-1">
                                {(pitch as any).summary !== undefined && (
                                   <div>
                                     <h4 className="text-cyan-400 font-bold mb-1 text-xs uppercase tracking-wide">📝 Tóm Tắt</h4>
                                     <textarea className="w-full bg-black/20 text-[#cbd5e1] border border-white/5 rounded p-2 text-sm resize-none focus:border-teal-500 outline-none min-h-[60px]"
                                       value={(pitch as any).summary || ''} onChange={(e) => updatePitch(idx, 'summary', e.target.value)} />
                                   </div>
                                )}
                                <div>
                                   <h4 className="text-indigo-400 font-bold mb-1 text-xs uppercase tracking-wide">🌍 Bối Cảnh</h4>
                                   <textarea className="w-full bg-black/20 text-[#cbd5e1] border border-white/5 rounded p-2 text-sm resize-none focus:border-teal-500 outline-none min-h-[60px]"
                                     value={(pitch as any).worldSettings || ''} onChange={(e) => updatePitch(idx, 'worldSettings', e.target.value)} />
                                </div>
                                <div>
                                   <h4 className="text-amber-400 font-bold mb-1 text-xs uppercase tracking-wide">🤕 Vết Thương Lòng</h4>
                                   <textarea className="w-full bg-black/20 text-[#cbd5e1] border border-white/5 rounded p-2 text-sm resize-none focus:border-teal-500 outline-none min-h-[60px]"
                                     value={(pitch as any).characterArc || ''} onChange={(e) => updatePitch(idx, 'characterArc', e.target.value)} />
                                </div>
                                <div>
                                   <h4 className="text-purple-400 font-bold mb-1 text-xs uppercase tracking-wide">🌪️ Plot Twist</h4>
                                   <textarea className="w-full bg-black/20 text-[#cbd5e1] border border-white/5 rounded p-2 text-sm resize-none focus:border-teal-500 outline-none min-h-[60px]"
                                     value={(pitch as any).plotTwists || ''} onChange={(e) => updatePitch(idx, 'plotTwists', e.target.value)} />
                                </div>
                                <div>
                                   <h4 className="text-rose-400 font-bold mb-1 text-xs uppercase tracking-wide">🔥 Độ Bạo Não</h4>
                                   <textarea className="w-full bg-black/20 text-[#cbd5e1] border border-white/5 rounded p-2 text-sm resize-none focus:border-teal-500 outline-none min-h-[60px]"
                                     value={(pitch as any).overallSizzle || ''} onChange={(e) => updatePitch(idx, 'overallSizzle', e.target.value)} />
                                </div>
                             </div>

                             
                             <div className="mt-4 pt-3 border-t border-white/5 flex gap-4 text-xs font-medium">
                                <div className="bg-emerald-500/10 text-emerald-400 px-3 py-1.5 rounded-lg flex items-center gap-1.5">
                                   <span className="text-emerald-500">🔖</span> Danh Mục WP: 
                                   <input className="bg-transparent border-b border-transparent focus:border-emerald-500 focus:bg-black/20 outline-none px-1 max-w-[150px]"
                                        value={(pitch as any).genres || ''}
                                        onChange={(e) => updatePitch(idx, 'genres', e.target.value)}
                                        placeholder="Nhập thể loại..."
                                   />
                                </div>
                                <div className="bg-amber-500/10 text-amber-500 px-3 py-1.5 rounded-lg flex items-center gap-1.5">
                                   📚 Số chương: 
                                   <input type="number" className="bg-transparent border-b border-transparent focus:border-amber-500 focus:bg-black/20 outline-none px-1 w-[60px]"
                                        value={(pitch as any).suggestedChapters || ''}
                                        onChange={(e) => updatePitch(idx, 'suggestedChapters', e.target.value)}
                                        placeholder="VD: 30"
                                        title="Chỉnh sửa số chương mục tiêu cho truyện này trước khi xả vào hệ thống"
                                   />
                                </div>
                             </div>
                             {grading && grading.grading && (
                                <div className={`p-4 rounded-xl text-sm font-medium border border-l-4 ${grading.score >= 8 ? 'bg-emerald-500/10 border-emerald-500/30 border-l-emerald-500 text-emerald-200' : grading.score >= 6 ? 'bg-amber-500/10 border-amber-500/30 border-l-amber-500 text-amber-200' : 'bg-red-500/10 border-red-500/30 border-l-red-500 text-red-200'}`}>
                                   <strong>👨‍⚖️ Supreme Judge Nhận Xét:</strong> {grading.grading}
                                </div>
                             )}
                          </div>
                       );
                    })}
                 </div>
              </>)}
           </div>
        </main>
      </div>

    
      {showBulkImport && (
        <div className="fixed inset-0 z-[100] bg-black/80 flex items-center justify-center p-6 backdrop-blur-sm">
          <div className="bg-[#17172a] border border-white/10 rounded-xl p-6 w-full max-w-2xl shadow-2xl animation-fade-in relative text-left">
            <div className="flex justify-between items-center mb-4">
              <h3 className="text-lg font-bold text-pink-400">📝 Nhập Sỉ Bản Gốc Từ File/Chatbot</h3>
              <button onClick={() => setShowBulkImport(false)} className="text-slate-500 hover:text-white transition-colors">✕</button>
            </div>
            <p className="text-sm text-slate-400 mb-4 font-medium">Bơm thẳng luồng kịch bản (JSON Object Array) từ ChatGPT hoặc Claude bên ngoài vào. Các field bắt buộc của mỗi Object: <code className="text-rose-300">super_title</code>, <code className="text-rose-300">summary</code>, <code className="text-rose-300">worldSettings</code>, vân vân...</p>
            <textarea 
               rows={12} 
               className="w-full bg-black/40 border border-white/10 rounded-lg p-4 text-[13px] font-mono text-slate-300 outline-none focus:border-pink-500 mb-4 whitespace-pre custom-scrollbar"
               placeholder={'[\n  {\n    "super_title": "Siêu phẩm tỷ lệ chọi 1/1000",\n    "summary": "Tóm tắt gây sốc..."\n  }\n]'}
               value={bulkImportData}
               onChange={(e) => setBulkImportData(e.target.value)}
            />
            <div className="flex justify-end gap-3 font-medium">
               <button onClick={() => setShowBulkImport(false)} className="px-5 py-2 rounded-lg bg-white/5 text-slate-300 hover:bg-white/10 transition-all font-bold">Hủy</button>
               <button onClick={() => {
                  try {
                     const parsed = JSON.parse(bulkImportData);
                     if (!Array.isArray(parsed)) throw new Error('Dữ liệu phải là một mảng JSON bắt đầu bằng [ và kết thúc bằng ]');
                     if (parsed.length === 0) throw new Error('Mảng rỗng!');
                     setPitchOptions(parsed.slice(0, 5));
                     if (!title && (parsed[0]?.super_title || parsed[0]?.protagonist)) setTitle(parsed[0]?.super_title || parsed[0]?.protagonist);
                     setIsConfigExpanded(false);
                     setShowBulkImport(false);
                     setBulkImportData('');
                     alert('✨ Đã bơm nạp thành công ' + parsed.slice(0,5).length + ' kịch bản ngoại viện!');
                  } catch (err: any) {
                     alert('❌ Lỗi định dạng JSON: ' + err.message);
                  }
               }} className="px-5 py-2 rounded-lg bg-gradient-to-r from-pink-600 to-rose-600 hover:opacity-90 text-white shadow-[0_0_15px_rgba(236,72,153,0.3)] transition-all font-bold">Nhập Dữ Liệu Ngay!</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
