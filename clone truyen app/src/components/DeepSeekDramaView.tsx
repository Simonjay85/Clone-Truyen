/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable @typescript-eslint/ban-ts-comment */
// @ts-nocheck
/* eslint-disable @typescript-eslint/no-explicit-any */
import React, { useState, useEffect } from 'react';
import { useStore } from '../store/useStore';
import { BookOpen, Map, PenTool, ShieldAlert, Rocket, Settings, CheckCircle2, Download, Zap, Play, Loader2 } from 'lucide-react';
import { agentGenerateBible, agentGenerateChapterMap, agentWriteChapter, agentRewriteChapter, agentIronRulesV2, agentFinalAudit } from '../lib/advanced_engine';

export function DeepSeekDramaView({ onNavigate }: { onNavigate?: (tab: string) => void }) {
  const { deepseekKey, addQueueItems, draftSpaces, updateDraftSpace, addApiLog, hasHydrated } = useStore();

  const [activeTab, setActiveTab] = useState<1 | 2 | 3 | 4>(1);

  // States
  const [prompt, setPrompt] = useState('');
  const [selectedGenres, setSelectedGenres] = useState<string[]>([]);
  const [targetChapters, setTargetChapters] = useState(15);
  const [autoChapters, setAutoChapters] = useState(true); // Let AI decide chapter count
  
  // Pipeline content states
  const [storyBible, setStoryBible] = useState('');
  const [chapterMap, setChapterMap] = useState<any[]>([]);
  const [currentState, setCurrentState] = useState('{}'); // STATE UPDATE JSON from last chapter

  // Writer states
  const [riskLevel, setRiskLevel] = useState<'low' | 'medium' | 'high'>('low');
  const [selectedChapterIdx, setSelectedChapterIdx] = useState(0);
  const [chapters, setChapters] = useState<{chapter: number; title: string; content: string; usedModel: string}[]>([]);
  const [isWritingChapter, setIsWritingChapter] = useState(false);
  const [isPatching, setIsPatching] = useState(false);
  const [lastUsedModel, setLastUsedModel] = useState<string | null>(null);
  const [auditReports, setAuditReports] = useState<Record<number, any>>({});
  const [includeAuditInExport, setIncludeAuditInExport] = useState(false);
  // State Update JSON parser
  const [pendingStateUpdate, setPendingStateUpdate] = useState<any>(null);
  const [stateParseError, setStateParseError] = useState('');

  // Iron Check states
  const [ironCheckText, setIronCheckText] = useState('');
  const [ironCheckResult, setIronCheckResult] = useState<any>(null);
  const [finalAuditReport, setFinalAuditReport] = useState<string | null>(null);
  
  // Custom Iron Rules (only for Checker — never sent to Chapter Writer)
  const [customIronRules, setCustomIronRules] = useState('');
  const [useFullIronRulesInChecker, setUseFullIronRulesInChecker] = useState(true);

  // Full Export states
  const [exportIncludeBible, setExportIncludeBible] = useState(true);
  const [exportIncludeMap, setExportIncludeMap] = useState(true);
  const [exportIncludeState, setExportIncludeState] = useState(true);
  const [exportIncludeAudit, setExportIncludeAudit] = useState(false);
  const [exportIncludeUsageLog, setExportIncludeUsageLog] = useState(false);

  // Loading States
  const [isGeneratingBible, setIsGeneratingBible] = useState(false);
  const [isGeneratingMap, setIsGeneratingMap] = useState(false);
  const [isCheckingRules, setIsCheckingRules] = useState(false);
  const [isFinalAuditing, setIsFinalAuditing] = useState(false);
  const [isAutoFixing, setIsAutoFixing] = useState(false);
  const [autoFixLog, setAutoFixLog] = useState<{msg: string; type: 'success'|'error'|'info'}[]>([]);

  // AutoPilot States
  const [isAutoPilotPanelOpen, setIsAutoPilotPanelOpen] = useState(false);
  const [apStartChapter, setApStartChapter] = useState(1);
  const [apEndChapter, setApEndChapter] = useState(3);
  const [apMode, setApMode] = useState<'draft_only' | 'balanced' | 'safe'>('balanced');
  const [apMaxChapters, setApMaxChapters] = useState(3);
  const [apDelay, setApDelay] = useState(5);
  const [apIsRunning, setApIsRunning] = useState(false);
  const [apLogs, setApLogs] = useState<{msg: string; type?: 'error'|'success'|'info'|'warning'}[]>([]);

  // Global Toast
  const [toast, setToast] = useState<{text: string, type: 'error'|'success'|'info'} | null>(null);
  const showToast = (text: string, type: 'error'|'success'|'info' = 'info') => {
    setToast({ text, type });
    setTimeout(() => setToast(null), 5000);
  };

  // Load from draft space
  useEffect(() => {
    if (!hasHydrated) return;
    const draft = draftSpaces['deepseek_pipeline'] || {};
    if (draft.prompt      !== undefined) setPrompt(draft.prompt || '');
    if (draft.storyBible  !== undefined) setStoryBible(draft.storyBible || '');
    if (draft.chapterMap  !== undefined) setChapterMap(draft.chapterMap || []);
    if (draft.currentState !== undefined) setCurrentState(draft.currentState || '{}');
    if (draft.targetChapters !== undefined) setTargetChapters(draft.targetChapters || 15);
    if (draft.selectedGenres !== undefined) setSelectedGenres(draft.selectedGenres || []);
    if (draft.autoChapters   !== undefined) setAutoChapters(draft.autoChapters);
    if (draft.riskLevel      !== undefined) setRiskLevel(draft.riskLevel || 'low');
    if (draft.chapters       !== undefined) setChapters(draft.chapters || []);
    if (draft.auditReports   !== undefined) setAuditReports(draft.auditReports || {});
    if (draft.customIronRules !== undefined) setCustomIronRules(draft.customIronRules || '');
    if (draft.useFullIronRulesInChecker !== undefined) setUseFullIronRulesInChecker(draft.useFullIronRulesInChecker);
    if (draft.finalAuditReport !== undefined) setFinalAuditReport(draft.finalAuditReport || null);
  }, [hasHydrated]); // Only hydrate once when the store is populated

  useEffect(() => {
    if (!hasHydrated) return; // Do not overwrite draftSpace with initial empty state before hydration!
    const timer = setTimeout(() => {
      updateDraftSpace('deepseek_pipeline', { prompt, storyBible, chapterMap, currentState, targetChapters, selectedGenres, autoChapters, riskLevel, chapters, auditReports, customIronRules, useFullIronRulesInChecker, finalAuditReport });
    }, 500);
    return () => clearTimeout(timer);
  }, [hasHydrated, prompt, storyBible, chapterMap, currentState, targetChapters, selectedGenres, autoChapters, riskLevel, chapters, auditReports, customIronRules, useFullIronRulesInChecker, finalAuditReport]);

  const toggleGenre = (g: string) => {
    if (selectedGenres.includes(g)) {
      setSelectedGenres(selectedGenres.filter(x => x !== g));
    } else {
      setSelectedGenres([...selectedGenres, g]);
    }
  };

  const extractStateUpdateJSON = (text: string): { parsed: any; error: string } => {
    try {
      let jsonStr = '';
      const stateIndex = text.search(/STATE\s+UPDATE\s+JSON/i);
      if (stateIndex !== -1) {
        const afterState = text.substring(stateIndex);
        const firstBrace = afterState.indexOf('{');
        const lastBrace = afterState.lastIndexOf('}');
        if (firstBrace !== -1 && lastBrace !== -1 && lastBrace >= firstBrace) {
          jsonStr = afterState.substring(firstBrace, lastBrace + 1);
        }
      }

      if (!jsonStr) {
        const lastBrace = text.lastIndexOf('}');
        const firstBrace = text.lastIndexOf('{', lastBrace - 20);
        if (firstBrace !== -1 && lastBrace !== -1 && lastBrace >= firstBrace) {
          jsonStr = text.substring(firstBrace, lastBrace + 1);
        }
      }

      if (!jsonStr) {
        return { parsed: null, error: 'Không tìm thấy block JSON (thiếu {}).' };
      }

      // ── Safe sanitize pipeline (no eval / no new Function) ──────────────────
      // Step 1: Strip markdown code fences
      jsonStr = jsonStr.replace(/```json/gi, '').replace(/```/g, '').trim();
      // Step 2: Strip single-line // comments (line-start only)
      jsonStr = jsonStr.replace(/^\s*\/\/[^\n]*/gm, '');
      // Step 3: Strip /* */ block comments
      jsonStr = jsonStr.replace(/\/\*[\s\S]*?\*\//g, '');
      // Step 4: Fix trailing commas before } or ]
      jsonStr = jsonStr.replace(/,\s*([\}\]])/g, '$1');
      // Step 4.5: Insert missing commas (conservative — newline-separated only)
      jsonStr = jsonStr.replace(/\}(\s*\n\s*)\{/g, '},$1{');
      jsonStr = jsonStr.replace(/\](\s*\n\s*)\[/g, '],$1[');
      // Step 5: Normalize smart/curly quotes to straight quotes
      jsonStr = jsonStr.replace(/[\u201C\u201D]/g, '"').replace(/[\u2018\u2019]/g, "'");
      // Step 6: Character-level scanner — only reliable way to escape control chars in AI strings
      {
        let out = '';
        let inStr = false;
        let i = 0;
        while (i < jsonStr.length) {
          const ch = jsonStr[i];
          if (inStr) {
            if (ch === '\\') {
              // Pass through the entire escape sequence unchanged
              out += ch + (jsonStr[i + 1] ?? '');
              i += 2;
              continue;
            }
            if (ch === '"') {
              inStr = false;
              out += ch;
              i++;
              continue;
            }
            // Escape any bare ASCII control char (0x00–0x1F) inside a string
            const code = ch.charCodeAt(0);
            if (code < 0x20) {
              if      (code === 0x0A) out += '\\n';
              else if (code === 0x0D) out += '\\r';
              else if (code === 0x09) out += '\\t';
              else out += `\\u${code.toString(16).padStart(4, '0')}`;
              i++;
              continue;
            }
          } else {
            if (ch === '"') { inStr = true; out += ch; i++; continue; }
          }
          out += ch;
          i++;
        }
        jsonStr = out;
      }
      // Step 7: Final trailing-comma pass (comment stripping can expose new ones)
      jsonStr = jsonStr.replace(/,\s*([\}\]])/g, '$1');

      // Step 8: Iterative auto-repair — if parse fails with "Expected ','",
      // insert comma at the exact error position and retry (max 5 attempts).
      let parseResult: any = null;
      let lastError = '';
      for (let attempt = 0; attempt < 6; attempt++) {
        try {
          parseResult = JSON.parse(jsonStr);
          lastError = '';
          break;
        } catch (err: any) {
          lastError = err.message || '';
          const posMatch = lastError.match(/position\s+(\d+)/);

          // Auto-repair: truncated JSON (AI hit max_tokens) — close all open braces/brackets
          if (/Unexpected end of JSON/i.test(lastError) && attempt < 2) {
            // Strip any trailing incomplete string value
            jsonStr = jsonStr.replace(/,\s*"[^"]*$/, ''); // remove trailing incomplete key
            jsonStr = jsonStr.replace(/"[^"]*$/, '""'); // close any unclosed string
            // Count unclosed braces and brackets
            let openBraces = 0, openBrackets = 0;
            let inString = false;
            for (let ci = 0; ci < jsonStr.length; ci++) {
              const c = jsonStr[ci];
              if (c === '\\' && inString) { ci++; continue; }
              if (c === '"') { inString = !inString; continue; }
              if (inString) continue;
              if (c === '{') openBraces++;
              else if (c === '}') openBraces--;
              else if (c === '[') openBrackets++;
              else if (c === ']') openBrackets--;
            }
            // Remove trailing comma before closing
            jsonStr = jsonStr.replace(/,\s*$/, '');
            // Close all open structures
            for (let b = 0; b < openBrackets; b++) jsonStr += ']';
            for (let b = 0; b < openBraces; b++) jsonStr += '}';
            console.warn(`[extractStateUpdateJSON] auto-repair: closed ${openBraces} braces, ${openBrackets} brackets (truncated JSON, attempt ${attempt + 1})`);
            continue;
          }

          if (posMatch && /Expected\s+'[,\]]/.test(lastError) && attempt < 5) {
            const pos = parseInt(posMatch[1], 10);
            jsonStr = jsonStr.substring(0, pos) + ',' + jsonStr.substring(pos);
            console.warn(`[extractStateUpdateJSON] auto-repair: inserted comma at pos ${pos} (attempt ${attempt + 1})`);
            continue;
          }
          const pos = posMatch ? parseInt(posMatch[1], 10) : 0;
          console.error('[extractStateUpdateJSON] parse failed:', err.message,
            '\nAround pos', pos, ':\n', jsonStr.substring(Math.max(0, pos - 100), pos + 100));
          return { parsed: null, error: `Lỗi parse JSON: ${err.message}` };
        }
      }
      if (parseResult) {
        return { parsed: parseResult, error: '' };
      }
      return { parsed: null, error: `Lỗi parse JSON sau 5 lần sửa: ${lastError}` };
    } catch (e: any) {
      return { parsed: null, error: `Lỗi extract JSON: ${e.message}` };
    }
  };

  const mergeStateStr = (baseStr: string, incoming: any) => {
    try {
      const base = JSON.parse(baseStr || '{}');
      // If incoming is null (JSON parse failed upstream), keep existing state unchanged
      if (!incoming || typeof incoming !== 'object') return baseStr || '{}';
      const merged = { ...base };

      
      const arrayKeys = [
        'mainKnows', 'mainHas', 'mainLost', 'villainKnows',
        'validEvidence', 'lostEvidence', 'activeAllies', 'disabledAllies',
        'openThreads', 'resolvedThreads', 'foreshadowingPlanted'
      ];
      
      for (const key of arrayKeys) {
        const baseArr = Array.isArray(base[key]) ? base[key] : [];
        const incArr = Array.isArray(incoming[key]) ? incoming[key] : [];
        merged[key] = Array.from(new Set([...baseArr, ...incArr]));
      }

      if (merged.resolvedThreads && merged.openThreads) {
        merged.openThreads = merged.openThreads.filter((t: string) => !merged.resolvedThreads.includes(t));
      }
      
      if (merged.lostEvidence && merged.validEvidence) {
        merged.validEvidence = merged.validEvidence.filter((e: string) => !merged.lostEvidence.includes(e));
      }

      for (const key in incoming) {
        if (!arrayKeys.includes(key)) {
          merged[key] = incoming[key];
        }
      }

      return JSON.stringify(merged, null, 2);
    } catch {
      return JSON.stringify(incoming, null, 2);
    }
  };

  const mergeStateUpdate = (incoming: any) => {
    const finalStr = mergeStateStr(currentState, incoming);
    setCurrentState(finalStr);
    setPendingStateUpdate(null);
    setStateParseError('');
    return finalStr;
  };

  // ── Manual save handlers ───────────────────────────────────────────────────
  const handleSaveBible = () => {
    updateDraftSpace('deepseek_pipeline', { storyBible });
    showToast('✅ Story Bible đã lưu!', 'success');
  };

  const handleSaveMap = () => {
    updateDraftSpace('deepseek_pipeline', { chapterMap });
    showToast('✅ Chapter Map đã lưu!', 'success');
  };

  const handleSaveChapter = () => {
    let newStateToSave = currentState;
    if (pendingStateUpdate) {
      newStateToSave = mergeStateUpdate(pendingStateUpdate);
    }
    updateDraftSpace('deepseek_pipeline', { chapters, currentState: newStateToSave });
    showToast(`✅ Chương ${selectedChapterIdx + 1} đã lưu!`, 'success');
  };

  const handleSaveAudit = () => {
    updateDraftSpace('deepseek_pipeline', { auditReports });
    showToast('✅ Audit Reports đã lưu!', 'success');
  };

  // Strip PRE-WRITE DECLARATION, SELF-CHECK và STATE UPDATE JSON blocks ra khỏi nội dung chương
  const stripMetaBlocks = (content: string): string => {
    if (!content) return content;
    const cleaned = content
      // Strip PRE-WRITE DECLARATION block (appears before chapter content)
      .replace(/━+\s*PRE-WRITE DECLARATION[\s\S]*?---\s*SAU KHI ĐIỀN ĐỦ[\s\S]*?---\s*\n?/im, '')
      // Strip "--- BẮT ĐẦU VIẾT CHƯƠNG ---" separator
      .replace(/---\s*BẮT ĐẦU VIẾT CHƯƠNG\s*---\s*\n?/im, '')
      // Strip ⛔ STOP header from user prompt echo
      .replace(/⛔\s*STOP[\s\S]*?---\s*SAU KHI ĐIỀN ĐỦ[\s\S]*?---\s*\n?/im, '')
      // Fallback: strip individual declaration fields ①–⑧ LOCK (case-insensitive)
      .replace(/[①②③④⑤⑥⑦⑧]\s*[\w\s/]+LOCK[:\s][\s\S]*?(?=\n[①②③④⑤⑥⑦⑧]|\nChương|\n━|\n\[TEASER|\n---)/gim, '')
      // Strip stray numbered declaration fields that leak into chapter body
      .replace(/[①②③④⑤⑥⑦⑧]\s*[\w\s/]+LOCK[:\s].*(?:\n\s+-[^\n]+)*/gim, '')
      // Broad catch-all: if declaration output exists before first "Chương N:", strip it
      .replace(/^[\s\S]*?(?=Chương\s+\d+\s*:)/m, '')
      // Xóa từ "---\n\nSELF-CHECK" hoặc "\nSELF-CHECK" đến hết chuỗi
      .replace(/\n?---\s*\n+SELF-CHECK[\s\S]*$/im, '')
      .replace(/\nSELF-CHECK[\s\S]*$/im, '')
      // Also strip numbered SELF-CHECK format (1. Tiêu đề...)
      .replace(/\nSELF-CHECK\s*\([^)]*\)[\s\S]*$/im, '')
      .replace(/\n?STATE\s*UPDATE\s*JSON:\s*\n?\{[\s\S]*?\}\s*$/im, '')
      .trimEnd();
    return cleaned;
  };

  const handleSendToReview = () => {
    // Chỉ lấy số chương theo đúng Chapter Map hiện tại (tránh lỗi cache cũ còn lưu chương dư)
    const validChapters = chapters.slice(0, chapterMap.length);
    const writtenChapters = validChapters.filter(ch => ch.content && ch.content.trim().length > 0);
    
    if (writtenChapters.length === 0) {
      showToast('❌ Chưa có chương nào được viết!', 'error');
      return;
    }
    if (!storyBible?.trim()) {
      showToast('❌ Cần có Story Bible trước khi gửi Tổng Duyệt!', 'error');
      return;
    }

    let bibleObj: any = {};
    try { bibleObj = JSON.parse(storyBible); } catch { bibleObj = { series_premise: storyBible }; }

    // Trích xuất Tên Truyện
    let extractedTitle = '';
    const titleMatch = storyBible.match(/##\s*(?:Title|Tên Truyện|Tên tác phẩm)[:\-\s]*([^\n]+)/i) || 
                       storyBible.match(/#\s*STORY BIBLE\s*\n+([^\n]+)/i);
    if (titleMatch && titleMatch[1].trim()) {
       extractedTitle = titleMatch[1].replace(/[\*#]/g, '').trim();
    }
    const fallbackTitle = prompt ? prompt.split('\n')[0].slice(0, 60) + '...' : 'Truyện DeepSeek';
    const storyTitle = bibleObj?.title || bibleObj?.story_title || extractedTitle || fallbackTitle;

    const chaptersContent = writtenChapters.map((ch, idx) => ({
      episode: idx + 1,
      title: ch.title || `Chương ${idx + 1}`,
      content: stripMetaBlocks(ch.content)   // 🧹 Tự động xóa SELF-CHECK & STATE UPDATE JSON
    }));

    const wordCount = writtenChapters.reduce((acc, ch) => acc + (ch.content?.split(' ')?.length || 0), 0);

    // ── Kiểm tra trùng lặp ──────────────────────────────────────────────────
    // Dùng fingerprint = 50 ký tự đầu của storyBible để nhận diện cùng một truyện
    const bibleFingerprint = storyBible.trim().slice(0, 50);
    const { queue: currentQueue, updateQueueItem } = useStore.getState();
    const existingIdx = currentQueue.findIndex(q =>
      (q.status === 'final_review' || q.status === 'completed') &&
      (q.title === storyTitle || (q.bible && JSON.stringify(q.bible).slice(0, 50) === bibleFingerprint))
    );

    if (existingIdx !== -1) {
      const existing = currentQueue[existingIdx];
      const choice = confirm(
        `⚠️ Truyện "${storyTitle}" đã có trong Tổng Duyệt (${existing.chaptersDone} chương).\n\n` +
        `Bấm OK = Cập nhật (ghi đè, giữ nguyên 1 bản)\n` +
        `Bấm Cancel = Huỷ (không gửi gì thêm)`
      );
      if (!choice) return;

      // Cập nhật bản hiện có thay vì thêm mới
      updateQueueItem(existing.id, {
        title: storyTitle,
        chaptersContent,
        chaptersDone: writtenChapters.length,
        targetChapters: writtenChapters.length,
        wordCount,
        bible: bibleObj,
        chapterMap: chapterMap,
        genres: bibleObj?.genre || bibleObj?.genres || existing.genres || '',
        completedAt: Date.now(),
        status: 'final_review',
      });
      showToast(`✅ Đã cập nhật "${storyTitle}" (${writtenChapters.length} chương) trong Tổng Duyệt!`, 'success');
      return;
    }

    // ── Không có trùng → xác nhận rồi thêm mới ──────────────────────────────
    if (!confirm(`Gửi ${writtenChapters.length} chương vào Tổng Duyệt?\nTruyện sẽ xuất hiện trong tab "Tổng Duyệt (Review)" để anh duyệt và đăng WordPress.`)) return;

    addQueueItems([{
      id: `ds8_${Date.now()}`,
      title: storyTitle,
      prompt: bibleObj?.series_premise || storyBible.slice(0, 300),
      bible: bibleObj,
      chapterMap: chapterMap,
      targetChapters: writtenChapters.length,
      chaptersDone: writtenChapters.length,
      wordCount,
      chaptersContent,
      status: 'final_review',
      writeEngine: 'deepseek',
      createdAt: Date.now(),
      completedAt: Date.now(),
      genres: bibleObj?.genre || bibleObj?.genres || '',
      isAdvancedPipeline: false,
    }]);

    showToast(`🎉 Đã gửi ${writtenChapters.length} chương vào Tổng Duyệt!`, 'success');
  };

  const handleResetCurrentStory = () => {
    if (!confirm('⚠️ Xoá toàn bộ Story Bible, Chapter Map, Chapters, và Audit Reports? Hành động này không thể hoàn tác.')) return;
    setStoryBible('');
    setChapterMap([]);
    setChapters([]);
    setAuditReports({});
    setCurrentState('{}');
    setIronCheckResult(null);
    setIronCheckText('');
    setFinalAuditReport(null);
    updateDraftSpace('deepseek_pipeline', { storyBible: '', chapterMap: [], chapters: [], auditReports: {}, currentState: '{}', finalAuditReport: null });
    showToast('🗑️ Reset thành công! Đã xoá trắng dữ liệu cốt truyện hiện tại.', 'success');
  };

  const handleGenerateBible = async () => {
    if (!deepseekKey) return showToast("Vui lòng nhập DeepSeek API Key trong cài đặt!", 'error');
    if (!prompt?.trim() && selectedGenres.length === 0) return showToast("Vui lòng nhập ý tưởng hoặc chọn thể loại!", 'error');
    
    setIsGeneratingBible(true);
    try {
      const result = await agentGenerateBible('deepseek', deepseekKey, 'deepseek-reasoner', selectedGenres, prompt);
      // Store raw text; if it's valid JSON we pretty-print, otherwise keep as-is
      try {
        const parsed = JSON.parse(result.text);
        setStoryBible(JSON.stringify(parsed, null, 2));
      } catch {
        setStoryBible(result.text || '');
      }
      setLastUsedModel(result.usedModel);
      setActiveTab(2);
    } catch (e: any) {
      showToast("Lỗi tạo Story Bible: " + e.message, 'error');
    } finally {
      setIsGeneratingBible(false);
    }
  };

  const handleGenerateMap = async () => {
    if (!deepseekKey) return showToast("Chưa có API Key!", 'error');
    if (!storyBible?.trim()) return showToast("Chưa có Story Bible. Vui lòng quay lại Mode 1!", 'error');
    
    setIsGeneratingMap(true);
    try {
      const bibleObj = JSON.parse(storyBible);
      const chapCount = autoChapters ? (bibleObj.recommended_chapters || targetChapters) : targetChapters;
      const result = await agentGenerateChapterMap('deepseek', deepseekKey, 'deepseek-reasoner', bibleObj, chapCount);
      const map = Array.isArray(result.data) ? result.data : (result.data?.chapters || []);
      setChapterMap(map);
      setChapters([]); // Xóa các chương đã viết cũ khi tạo Map mới để tránh lỗi trộn truyện
      setAuditReports({});
      setLastUsedModel(result.usedModel);
      if (autoChapters && map.length > 0) setTargetChapters(map.length);
      setActiveTab(3);
    } catch (e: any) {
      showToast("Lỗi tạo Chapter Map: " + (e.message || "Hãy đảm bảo Story Bible là JSON hợp lệ", 'error'));
    } finally {
      setIsGeneratingMap(false);
    }
  };

  const handleWriteChapter = async () => {
    if (!deepseekKey) return showToast("Chưa có API Key!", 'error');
    if (chapterMap.length === 0) return showToast("Chưa có Chapter Map. Vui lòng tạo Map ở Mode 2!", 'error');
    const beat = chapterMap[selectedChapterIdx];
    if (!beat) return;
    const prevChapter = chapters[selectedChapterIdx - 1];
    const prevContext = prevChapter ? prevChapter.content.slice(-500) : '';
    setIsWritingChapter(true);
    try {
      const bibleObj = JSON.parse(storyBible);
      const result = await agentWriteChapter('deepseek', deepseekKey, 'deepseek-chat', bibleObj, beat, prevContext, riskLevel, currentState, chapterMap.length);
      const newChapters = [...chapters];
      newChapters[selectedChapterIdx] = { chapter: beat.chapter, title: beat.title, content: result.text, usedModel: result.usedModel };
      setChapters(newChapters);
      setLastUsedModel(result.usedModel);
      // Auto-extract STATE UPDATE JSON
      const { parsed, error } = extractStateUpdateJSON(result.text || '');
      if (parsed) {
        setPendingStateUpdate(parsed);
        setStateParseError('');
      } else {
        setPendingStateUpdate(null);
        setStateParseError(error);
      }
    } catch (e: any) {
      showToast("Lỗi viết chương: " + e.message, 'error');
    } finally {
      setIsWritingChapter(false);
    }
  };

  const handlePatchChapter = async () => {
    const currentChapter = chapters[selectedChapterIdx];
    const currentAudit = auditReports[selectedChapterIdx];
    if (!currentChapter) return showToast("Chưa có nội dung chương. Viết chương trước!", 'error');
    if (!currentAudit?.patch_notes) return showToast("Chưa có Patch Notes. Chạy Iron Check trước!", 'error');
    setIsPatching(true);
    try {
      const result = await agentRewriteChapter('deepseek', deepseekKey, 'deepseek-chat', currentChapter.content, currentAudit.patch_notes);
      const newChapters = [...chapters];
      newChapters[selectedChapterIdx] = { ...newChapters[selectedChapterIdx], content: result.text, usedModel: result.usedModel };
      setChapters(newChapters);
      setLastUsedModel(result.usedModel);
      showToast("✅ Patch thành công bằng V3!", 'success');
    } catch (e: any) {
      showToast("Lỗi patch: " + e.message, 'error');
    } finally {
      setIsPatching(false);
    }
  };

  // Build export content (shared by both MD and TXT)
  const buildExportContent = (format: 'md' | 'txt') => {
    let bibleTitle = 'Truyen';
    let logline = '';
    try {
      const b = JSON.parse(storyBible);
      bibleTitle = b.title || 'Truyen';
      logline = b.logline || '';
    } catch { /* ignore */ }

    const hr = format === 'md' ? '\n\n---\n\n' : '\n\n' + '='.repeat(60) + '\n\n';
    const h1 = (t: string) => format === 'md' ? `# ${t}` : t.toUpperCase();
    const h2 = (t: string) => format === 'md' ? `## ${t}` : `[ ${t} ]`;

    const lines: string[] = [];

    // Header
    lines.push(h1(bibleTitle));
    if (logline) lines.push(`\n> ${logline}`);
    lines.push(`\n_Exported: ${new Date().toLocaleString('vi-VN')}_`);
    lines.push(`_Total chapters: ${chapters.filter(Boolean).length}_`);

    // Chapters in order
    const sorted = [...chapters]
      .map((ch, idx) => ({ ...ch, _idx: idx }))
      .filter(ch => ch && ch.content)
      .sort((a, b) => (a.chapter || a._idx) - (b.chapter || b._idx));

    sorted.forEach(ch => {
      lines.push(hr);
      lines.push(h2(`Chương ${ch.chapter}: ${ch.title}`));
      if (ch.usedModel) lines.push(format === 'md' ? `\n_Model: ${ch.usedModel}_` : `[Model: ${ch.usedModel}]`);
      lines.push('\n' + ch.content);

      // Optional: append audit report
      if (includeAuditInExport) {
        const audit = auditReports[ch._idx];
        if (audit) {
          lines.push('\n');
          lines.push(h2(`AUDIT — Chương ${ch.chapter}`));
          lines.push(`Verdict: ${audit.verdict || (audit.is_passed ? 'PASS' : 'FAIL')} | Score: ${audit.score}/10`);
          if (audit.errors?.length) lines.push('Errors:\n' + audit.errors.map((e: string) => `  - ${e}`).join('\n'));
          if (audit.patch_notes) lines.push('Patch Notes: ' + audit.patch_notes);
        }
      }
    });

    return { content: lines.join('\n'), title: bibleTitle };
  };

  const handleExportStory = (format: 'md' | 'txt' = 'md') => {
    const written = chapters.filter(ch => ch && ch.content);
    if (written.length === 0) return showToast('Chưa có chương nào được viết!', 'error');
    const { content, title } = buildExportContent(format);
    const mimeType = format === 'md' ? 'text/markdown;charset=utf-8' : 'text/plain;charset=utf-8';
    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${title.replace(/[^\w\s-]/g, '').trim()}.${format}`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleExportProjectSummary = () => {
    const lines: string[] = [];
    let title = 'story-project';
    
    try {
      const bibleObj = JSON.parse(storyBible);
      title = bibleObj.title || title;
    } catch { }

    lines.push(`# ${title}`);
    
    // Add date components individually to fix zero padding issues natively
    const d = new Date();
    const pad = (n: number) => n.toString().padStart(2, '0');
    const dateStr = `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}-${pad(d.getHours())}-${pad(d.getMinutes())}`;
    
    lines.push(`_Exported: ${d.toLocaleString('vi-VN')}_`);
    lines.push(`_Quality Mode: ${riskLevel === 'high' ? 'High (R1 Reasoner)' : 'Normal (V3 Chat)'}_`);
    lines.push('\n---\n');

    if (exportIncludeBible && storyBible) {
      lines.push('## Story Bible');
      lines.push('```json\n' + storyBible + '\n```\n');
    }

    if (exportIncludeMap && chapterMap.length > 0) {
      lines.push('## Chapter Map');
      lines.push('```json\n' + JSON.stringify(chapterMap, null, 2) + '\n```\n');
    }

    if (exportIncludeState && currentState) {
      lines.push('## Final Current State');
      lines.push('```json\n' + currentState + '\n```\n');
    }

    const written = chapters.filter(ch => ch && ch.content);
    if (written.length > 0) {
      lines.push('## Chapters\n');
      const sorted = [...chapters]
        .map((ch, idx) => ({ ...ch, _idx: idx }))
        .filter(ch => ch && ch.content)
        .sort((a, b) => (a.chapter || a._idx) - (b.chapter || b._idx));

      sorted.forEach(ch => {
        lines.push(`### Chương ${ch.chapter}: ${ch.title}`);
        if (ch.usedModel && exportIncludeUsageLog) lines.push(`_Model: ${ch.usedModel}_`);
        lines.push('\n' + ch.content + '\n');

        if (exportIncludeAudit) {
          const audit = auditReports[ch._idx];
          if (audit) {
            lines.push(`#### AUDIT — Chương ${ch.chapter}`);
            lines.push(`**Verdict:** ${audit.verdict || (audit.is_passed ? 'PASS' : 'FAIL')} | **Score:** ${audit.score}/10`);
            if (audit.errors?.length) lines.push('**Errors:**\n' + audit.errors.map((e: string) => `- ${e}`).join('\n'));
            if (audit.patch_notes) lines.push('**Patch Notes:** ' + audit.patch_notes);
            lines.push('\n');
          }
        }
        lines.push('---\n');
      });
    }

    const content = lines.join('\n');
    const blob = new Blob([content], { type: 'text/markdown;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `story-project-${dateStr}.md`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleRunAutoPilot = async () => {
    if (!deepseekKey) return showToast("Chưa có API Key!", 'error');
    if (!storyBible || chapterMap.length === 0) return showToast("Vui lòng tạo Story Bible và Chapter Map trước!", 'error');
    if (apStartChapter > apEndChapter) return showToast("Chương bắt đầu phải nhỏ hơn hoặc bằng chương kết thúc.", 'success');
    
    // Xoá giới hạn apMaxChapters cứng, thay vào đó dùng nó làm mốc nghỉ (batch)
    // if (apEndChapter - apStartChapter + 1 > apMaxChapters) return showToast(`Chỉ được chạy tối đa ${apMaxChapters} chương mỗi lần để an toàn!`, 'success');
    
    // Check if chapters exist to prevent overwriting without confirm
    const existing = chapters.slice(apStartChapter - 1, apEndChapter).filter(c => c && typeof c.content === 'string' && c.content.trim().length > 0);
    if (existing.length > 0) {
      if (!confirm(`Phát hiện ${existing.length} chương đã có nội dung trong khoảng từ ${apStartChapter} đến ${apEndChapter}. Bấm OK để GHI ĐÈ, Cancel để huỷ.`)) return;
    }

    setApIsRunning(true);
    setApLogs([]);
    const addLog = (msg: string, type: 'info'|'success'|'warning'|'error' = 'info') => {
      setApLogs(prev => [...prev, {msg, type}]);
    };

    let localCurrentState = currentState;
    const localChapters = [...chapters];
    const localAuditReports = { ...auditReports };
    const bibleObj = JSON.parse(storyBible);

    // FIX: Seed characterMap from Bible BEFORE Ch.1 to prevent name drift.
    // The CHARACTER NAME MAP must exist from the very first chapter.
    try {
      const st = JSON.parse(localCurrentState || '{}');
      if (!st.characterMap || Object.keys(st.characterMap).length === 0) {
        const charMap: Record<string, string> = {};
        // Extract from bible's characters array (various formats)
        const chars = bibleObj.characters || bibleObj.nhân_vật || bibleObj.cast || [];
        if (Array.isArray(chars)) {
          for (const c of chars) {
            const name = c.name || c.tên || c.ten || '';
            const role = c.role || c.vai || c.vai_trò || c.type || '';
            if (name) {
              const key = role.toLowerCase().includes('main') || role.toLowerCase().includes('chính')
                ? 'main' : role.toLowerCase().includes('villain') || role.toLowerCase().includes('phản diện')
                ? 'villain_main' : name.toLowerCase().replace(/\s+/g, '_');
              charMap[key] = name;
            }
          }
        }
        // Also extract company name from bible
        const company = bibleObj.company || bibleObj.tập_đoàn || bibleObj.tap_doan || bibleObj.corporation || '';
        if (company) charMap['company_name'] = typeof company === 'string' ? company : (company.name || company.tên || '');
        
        if (Object.keys(charMap).length > 0) {
          st.characterMap = charMap;
          localCurrentState = JSON.stringify(st);
          addLog(`📋 Đã seed characterMap từ Bible: ${Object.entries(charMap).map(([k,v]) => `${k}=${v}`).join(', ')}`, 'info');
        }
      }
    } catch { /* bible parse issue, skip */ }

    addLog(`🚀 Bắt đầu AutoPilot: Chương ${apStartChapter} đến ${apEndChapter} (Mode: ${apMode})`, 'info');

    try {
      for (let i = apStartChapter; i <= apEndChapter; i++) {
        // We can't really break from React state synchronously without refs, but we'll loop.
        
        const idx = i - 1;
        const beat = chapterMap[idx];
        if (!beat) {
          addLog(`❌ Không tìm thấy map cho chương ${i}, dừng AutoPilot.`, 'error');
          break;
        }

        addLog(`✍️ Đang viết chương ${i}...`, 'info');
        const prevContext = localChapters[idx - 1] ? localChapters[idx - 1].content.slice(-500) : '';
        
        // 1. Write
        const writeModel = riskLevel === 'high' ? 'deepseek-reasoner' : 'deepseek-chat';
        const writeRes = await agentWriteChapter('deepseek', deepseekKey, writeModel, bibleObj, beat, prevContext, riskLevel, localCurrentState, chapterMap.length);
        
        if (!writeRes.text || writeRes.text.trim().length === 0) {
          addLog(`❌ Model ${writeModel} trả về rỗng ở chương ${i}, dừng AutoPilot.`, 'error');
          break;
        }

        // ========== STEP 1: Detect DECLARATION on RAW output (before stripping) ==========
        const rawText = writeRes.text;
        // Primary: match ① TAG LOCK, ② Evidence Lock, etc.
        let declarationFieldCount = (rawText.match(/[①②③④⑤⑥⑦⑧]\s*[\w\s/]+LOCK/gi) || []).length;
        // Fallback: if V3 used Vietnamese labels (① KHÓA THẺ:, ② BẰNG CHỨNG:), count circled numbers at line start
        if (declarationFieldCount === 0) {
          const circledNumbers = new Set((rawText.match(/^[①②③④⑤⑥⑦⑧]/gm) || []).map(c => c));
          declarationFieldCount = circledNumbers.size;
        }

        // ========== STEP 2: Post-process — strip meta blocks & duplicate titles ==========
        // Handle: "Chương N: Title\n\nChương N: Title" and "Chương N: Title\n---\nChương N: Title"
        writeRes.text = writeRes.text
          .replace(/^(Chương\s+\d+\s*:\s*[^\n]+)(?:\s*\n)+(?:[\s#-]*\n)*\s*(?:#\s*)?Chương\s+\d+\s*:\s*[^\n]+/m, '$1')
          // Strip stray DECLARATION fields that leaked into chapter content
          .replace(/[①②③④⑤⑥⑦⑧⑨]\s*[\w\s/]+LOCK[:\s].*(?:\n\s+-[^\n]+)*/gim, '');

        // ========== HARD VALIDATOR 1: Name Enforcer ==========
        // Regex-replace ANY wrong character names using characterMap. 
        // This does NOT rely on AI — it's a code-level enforcer.
        try {
          const st = JSON.parse(localCurrentState || '{}');
          const charMap = st.characterMap || {};
          // Build a reverse lookup of known names to detect drift
          const knownNames = Object.values(charMap).filter(Boolean) as string[];
          if (knownNames.length > 0) {
            let text = writeRes.text;
            let nameFixCount = 0;
            
            // Common drift patterns: main character name changes
            const mainName = charMap.main || charMap.nhan_vat_chinh || '';
            const villainName = charMap.villain_main || charMap.phan_dien || '';
            const companyName = charMap.company_name || '';
            
            // Fix main character name drift (e.g., "Nguyễn Văn Minh" → "Minh Anh")
            if (mainName) {
              // Detect if AI used a completely different name for main
              // Common AI drift: changing "Minh Anh" to "Nguyễn Văn Minh" or just "Minh"
              const mainFirstName = mainName.split(' ').pop() || mainName;
              const wrongMainPatterns = [
                /Nguyễn Văn Minh/g,  // Common drift pattern
                /Nguyễn Minh/g,
              ];
              for (const pattern of wrongMainPatterns) {
                if (pattern.test(text) && !text.includes(mainName)) {
                  text = text.replace(pattern, mainName);
                  nameFixCount++;
                }
              }
            }
            
            // Fix company name drift (e.g., "Thực Phẩm Xanh" → "ABC")  
            if (companyName) {
              const wrongCompanyPatterns = [
                /Tập đoàn Thực Phẩm Xanh/g,
                /Công ty Thực Phẩm Xanh/g,
                /Thực Phẩm Xanh/g,
              ];
              for (const pattern of wrongCompanyPatterns) {
                if (pattern.test(text) && !knownNames.some(n => text.includes(n) && n === companyName)) {
                  const replacement = companyName.includes('Tập đoàn') ? companyName : `Tập đoàn ${companyName}`;
                  text = text.replace(pattern, replacement);
                  nameFixCount++;
                }
              }
            }

            // Fix villain name drift (e.g., "Ông Quang" → "Trần Đức" or vice versa)
            if (villainName) {
              // Detect the villain's last-name pattern
              const villainParts = villainName.split(' ');
              const villainLastName = villainParts[villainParts.length - 1];
              // If text uses "sếp Đức" but villain is "Ông Quang", replace
              if (villainName.includes('Quang')) {
                text = text.replace(/Trần Đức/g, villainName);
                text = text.replace(/sếp Đức/g, `sếp ${villainLastName}`);
                nameFixCount++;
              } else if (villainName.includes('Đức')) {
                text = text.replace(/Ông Quang/g, villainName);
                text = text.replace(/sếp Quang/g, `sếp ${villainLastName}`);
                nameFixCount++;
              }
            }
            
            if (nameFixCount > 0) {
              writeRes.text = text;
              addLog(`🔧 Ch.${i}: Name Enforcer sửa ${nameFixCount} lỗi tên trôi.`, 'info');
            }
          }
        } catch { /* ignore */ }

        // ========== HARD VALIDATOR 2: Reveal Blocker ==========
        // If reveal detected BEFORE gate chapter → auto-reject + rewrite
        const revealGateChNum = Math.ceil(chapterMap.length * 0.6);
        if (i < revealGateChNum) {
          const lowerText = writeRes.text.toLowerCase();
          // ── Tier 1: Hard violations (always block) ──
          const hardRevealViolations = [
            'tôi là chủ tịch', 'lộ thân phận', 'cởi áo shipper',
            'thưa chủ tịch', 'cô là chủ tịch', 'anh là chủ tịch', 'nó là chủ tịch',
            'chính là chủ tịch', 'thật sự là chủ tịch', 'hóa ra là chủ tịch',
            'tuyên bố thân phận', 'giơ thẻ đen ra',
            'cô chính là', 'anh chính là', 'hắn chính là',
          ];
          // ── Tier 2: Context-sensitive (only block if near main character) ──
          const contextRevealPatterns = [
            { keyword: 'lộ diện', context: ['main', 'thân phận', 'chủ tịch', 'danh tính'] },
            { keyword: 'thẻ đen', context: ['giơ', 'rút', 'đưa ra', 'quẹt', 'chìa'] },
          ];
          let foundViolation = hardRevealViolations.find(v => lowerText.includes(v));
          // Check context-sensitive patterns only if no hard violation found
          if (!foundViolation) {
            for (const pat of contextRevealPatterns) {
              if (!lowerText.includes(pat.keyword)) continue;
              // Find all occurrences and check nearby context (200 chars window)
              let searchFrom = 0;
              while (searchFrom < lowerText.length) {
                const kwIdx = lowerText.indexOf(pat.keyword, searchFrom);
                if (kwIdx === -1) break;
                const windowStart = Math.max(0, kwIdx - 100);
                const windowEnd = Math.min(lowerText.length, kwIdx + pat.keyword.length + 100);
                const window = lowerText.slice(windowStart, windowEnd);
                if (pat.context.some(ctx => window.includes(ctx))) {
                  foundViolation = `${pat.keyword} (context: ${pat.context.find(ctx => window.includes(ctx))})` as string;
                  break;
                }
                searchFrom = kwIdx + 1;
              }
              if (foundViolation) break;
            }
          }
          if (foundViolation) {
            addLog(`🚫 Ch.${i}: REVEAL BLOCKER — phát hiện "${foundViolation}" trước Ch.${revealGateChNum}. Đang rewrite...`, 'warning');
            
            // Force rewrite with MODIFIED beat containing explicit anti-reveal instruction
            const antiRevealBeat = {
              ...beat,
              beats: [...(beat.beats || beat.key_beats || []), 
                'CẢNH BÁO TỪ HỆ THỐNG: Bản viết trước bị loại vì lộ thân phận main quá sớm. ' +
                'TUYỆT ĐỐI KHÔNG viết bất kỳ cảnh nào main lộ thân phận, giơ thẻ đen, tuyên bố "tôi là chủ tịch", ' +
                'hay bất kỳ ai phát hiện danh tính thật của main. Main phải giữ vỏ bọc shipper 100% chương này.'
              ],
              title: beat.title + ' [ANTI-REVEAL REWRITE]',
            };
            const rewriteRes = await agentWriteChapter('deepseek', deepseekKey, writeModel, bibleObj, antiRevealBeat, prevContext, riskLevel, localCurrentState, chapterMap.length);
            if (rewriteRes.text && rewriteRes.text.trim().length > 0) {
              // Check rewrite with the same detection logic
              const rewriteLower = rewriteRes.text.toLowerCase();
              let rewriteViolation = hardRevealViolations.find(v => rewriteLower.includes(v));
              if (!rewriteViolation) {
                for (const pat of contextRevealPatterns) {
                  if (!rewriteLower.includes(pat.keyword)) continue;
                  let sf = 0;
                  while (sf < rewriteLower.length) {
                    const ki = rewriteLower.indexOf(pat.keyword, sf);
                    if (ki === -1) break;
                    const ws = Math.max(0, ki - 100);
                    const we = Math.min(rewriteLower.length, ki + pat.keyword.length + 100);
                    const w = rewriteLower.slice(ws, we);
                    if (pat.context.some(ctx => w.includes(ctx))) { rewriteViolation = pat.keyword; break; }
                    sf = ki + 1;
                  }
                  if (rewriteViolation) break;
                }
              }
              if (!rewriteViolation) {
                writeRes.text = rewriteRes.text
                  .replace(/^(Chương\s+\d+\s*:\s*[^\n]+)(?:\s*\n)+(?:[\s#-]*\n)*\s*(?:#\s*)?Chương\s+\d+\s*:\s*[^\n]+/m, '$1')
                  .replace(/[①②③④⑤⑥⑦⑧⑨]\s*[\w\s/]+LOCK[:\s].*(?:\n\s+-[^\n]+)*/gim, '')
                  .replace(/\[ANTI-REVEAL REWRITE\]/g, '');
                addLog(`✅ Ch.${i}: Rewrite thành công — không còn reveal violation.`, 'success');
              } else {
                // Strip leaked rewrite metadata and use the rewrite anyway
                writeRes.text = rewriteRes.text.replace(/\[ANTI-REVEAL REWRITE\]/g, '');
                addLog(`⚠️ Ch.${i}: Rewrite vẫn vi phạm reveal ("${rewriteViolation}"). Giữ bản rewrite nhưng cảnh báo.`, 'warning');
              }
            }
          }
        }

        // ========== HARD VALIDATOR 3: Arrest Checker ==========
        // If villain is marked arrested but appears freely in the chapter → warn + try to fix
        try {
          const st = JSON.parse(localCurrentState || '{}');
          if (st.villainArrested) {
            const lowerText = writeRes.text.toLowerCase();
            const villainName = (st.characterMap?.villain_main || st.characterMap?.phan_dien || '').toLowerCase();
            const freeViolations = [
              'bước vào phòng họp', 'ngồi ở', 'đứng dậy', 'cười khẩy',
              'gằn giọng', 'đập bàn', 'quay sang',
            ];
            // Only check if villain name appears + free action
            if (villainName && lowerText.includes(villainName)) {
              const hasFreeBehavior = freeViolations.some(v => {
                const idx = lowerText.indexOf(villainName);
                // Check if free behavior appears within 200 chars after villain name
                const nearby = lowerText.slice(idx, idx + 200);
                return nearby.includes(v);
              });
              if (hasFreeBehavior) {
                addLog(`🚨 Ch.${i}: ARREST CHECKER — villain "${villainName}" đã bị bắt nhưng xuất hiện tự do! Cần review.`, 'warning');
              }
            }
          }
        } catch { /* ignore */ }

        localChapters[idx] = { chapter: beat.chapter, title: beat.title, content: writeRes.text, usedModel: writeRes.usedModel };
        setChapters([...localChapters]);
        setLastUsedModel(writeRes.usedModel);

        // ========== STEP 3: Log DECLARATION status ==========
        if (declarationFieldCount >= 6) {
          addLog(`🔒 Ch.${i}: AI đã điền ${declarationFieldCount}/8 ô DECLARATION — constraint hoạt động.`, 'success');
        } else if (declarationFieldCount > 0) {
          addLog(`⚠️ Ch.${i}: AI chỉ điền ${declarationFieldCount}/8 ô DECLARATION — cần kiểm tra raw output.`, 'warning');
        } else {
          addLog(`🟡 Ch.${i}: AI bỏ qua DECLARATION block — constraint chưa có tác dụng, cần điều chỉnh prompt.`, 'warning');
        }

        await new Promise(r => setTimeout(r, 1500)); // Delay for readability

        // Parse state — do NOT stop AutoPilot on parse failure; chapter already saved
        const { parsed, error } = extractStateUpdateJSON(writeRes.text || '');
        const stateToMerge = parsed;
        if (error || !stateToMerge) {
          addLog(`⚠️ Ch.${i}: Không parse được State JSON (${error}). Giữ state cũ, tiếp tục...`, 'warning');
        }

        // ALWAYS scan chapter text for critical state changes — even when JSON parse succeeds.
        // This is the ground truth. AI may parse state but forget to set villainArrested or identityRevealLayer.
        try {
          const st = JSON.parse(localCurrentState || '{}');
          const chText = writeRes.text.toLowerCase();
          let stateChanged = false;
          
          // Detect identity reveal — CONTEXT-AWARE: only trigger on patterns where
          // the MAIN CHARACTER is clearly revealing their identity, not generic mentions
          // of "chủ tịch" by other characters.
          const mainName = (st.characterMap?.main || '').toLowerCase();
          const strongRevealPatterns = [
            'tôi là chủ tịch', 'tôi chính là chủ tịch',
            'lộ thân phận', 'tuyên bố thân phận',
            'cởi áo shipper', 'giơ thẻ đen ra',
            'cô là chủ tịch', 'anh là chủ tịch', 'hóa ra là chủ tịch',
            'thưa chủ tịch', 'chính là chủ tịch', 'thật sự là chủ tịch',
          ];
          // Context-sensitive: 'lộ diện' only counts if near main's name or 'thân phận'
          const hasStrongReveal = strongRevealPatterns.some(kw => chText.includes(kw));
          let hasContextReveal = false;
          if (!hasStrongReveal && chText.includes('lộ diện')) {
            // Only flag if 'lộ diện' appears near main character name or 'thân phận'/'danh tính'
            const ldIdx = chText.indexOf('lộ diện');
            const nearbyWindow = chText.slice(Math.max(0, ldIdx - 80), Math.min(chText.length, ldIdx + 80));
            if ((mainName && nearbyWindow.includes(mainName)) || nearbyWindow.includes('thân phận') || nearbyWindow.includes('danh tính')) {
              hasContextReveal = true;
            }
          }
          const hasReveal = hasStrongReveal || hasContextReveal;
          if (hasReveal && (!st.identityRevealLayer || (!st.identityRevealLayer.includes('4') && !st.identityRevealLayer.includes('công khai')))) {
            st.identityRevealLayer = 'Tầng 4 — đã lộ công khai';
            st.chapterNumber = i;
            st.chapterFunction = st.chapterFunction || 'IDENTITY_REVEAL';
            stateChanged = true;
            addLog(`🔍 Ch.${i}: Phát hiện reveal trong text → force-set identityRevealLayer = "Tầng 4".`, 'info');
          }
          
          // Detect villain arrest — prevents double-arrest bug
          const arrestKeywords = ['còng tay', 'bị bắt', 'lệnh bắt', 'tạm giam', 'dẫn đi', 'bị dẫn ra'];
          const hasArrest = arrestKeywords.some(kw => chText.includes(kw));
          if (hasArrest && !st.villainArrested) {
            st.villainArrested = `Villain chính bị bắt tại Ch.${i}`;
            stateChanged = true;
            addLog(`🔍 Ch.${i}: Phát hiện villain bị bắt trong text → force-set villainArrested.`, 'info');
          }

          // Preserve characterMap through merges — ensure it doesn't get lost
          if (stateToMerge && st.characterMap && !stateToMerge.characterMap) {
            stateToMerge.characterMap = st.characterMap;
          }
          
          if (stateChanged) {
            localCurrentState = JSON.stringify(st);
          }
        } catch { /* state completely unparseable, skip */ }

        if (apMode === 'draft_only') {
          // Merge state and save
          localCurrentState = mergeStateStr(localCurrentState, stateToMerge);
          setCurrentState(localCurrentState);
          updateDraftSpace('deepseek_pipeline', { chapters: localChapters, currentState: localCurrentState });
          addLog(`✅ Đã lưu Draft chương ${i}.`, 'success');
          await new Promise(r => setTimeout(r, 1500));
        } 
        else if (apMode === 'balanced' || apMode === 'safe') {
          // Audit
          addLog(`🛡️ Đang audit chương ${i}...`, 'info');
          await new Promise(r => setTimeout(r, 1000));
          
          const checkerParams = {
            story_bible: JSON.stringify(bibleObj),
            chapter_map: JSON.stringify(chapterMap),
            previous_state: localCurrentState,
            chapter_draft: writeRes.text,
            chapter_number: i,
            extra_rules: (useFullIronRulesInChecker && customIronRules.trim()) ? customIronRules.trim() : '',
          };
          const auditRes = await agentIronRulesV2('deepseek', deepseekKey, 'deepseek-reasoner', checkerParams);
          const auditParsed = (() => { try { return JSON.parse(auditRes.text); } catch { return { verdict: 'UNKNOWN', score: 0 }; } })();
          
          localAuditReports[idx] = auditParsed;
          setAuditReports({ ...localAuditReports });
          setLastUsedModel(auditRes.usedModel);

          if (auditParsed.verdict === 'REWRITE REQUIRED' || (auditParsed.score && Number(auditParsed.score) < 9.2)) {
            addLog(`❌ Chương ${i} không qua kiểm duyệt (Verdict: ${auditParsed.verdict}, Score: ${auditParsed.score || '?'}/10). Điểm phải >= 9.2. Dừng AutoPilot để tự sửa.`, 'error');
            break;
          }

          let finalChapterText = writeRes.text;

          if (auditParsed.verdict === 'PASS_WITH_PATCHES' && apMode === 'balanced') {
            addLog(`🔧 Đang Patch chương ${i} (V3)...`, 'info');
            await new Promise(r => setTimeout(r, 1500));
            const patchRes = await agentRewriteChapter('deepseek', deepseekKey, 'deepseek-chat', finalChapterText, auditParsed.patch_notes || '');
            if (!patchRes.text || patchRes.text.trim().length === 0) {
              addLog(`❌ Lỗi Patch rỗng ở chương ${i}, dừng AutoPilot.`, 'error');
              break;
            }
            finalChapterText = patchRes.text;
            localChapters[idx].content = finalChapterText;
            localChapters[idx].usedModel = `${writeRes.usedModel} + Patch(${patchRes.usedModel})`;
            setChapters([...localChapters]);
            await new Promise(r => setTimeout(r, 1500));
          }

          if (apMode === 'balanced') {
            localCurrentState = mergeStateStr(localCurrentState, stateToMerge);
            setCurrentState(localCurrentState);
            updateDraftSpace('deepseek_pipeline', { chapters: localChapters, currentState: localCurrentState, auditReports: localAuditReports });
            addLog(`✅ Đã lưu chương ${i} sau Audit.`, 'success');
            await new Promise(r => setTimeout(r, 1500));
          }

          if (apMode === 'safe') {
            addLog(`⏸️ Safe Mode: Tạm dừng sau chương ${i}. Vui lòng kiểm tra và lưu tay.`, 'warning');
            break;
          }
        }

        // Delay between calls or batches
        const chaptersWritten = i - apStartChapter + 1;
        if (i < apEndChapter && apMode !== 'safe') {
          if (chaptersWritten % apMaxChapters === 0) {
            addLog(`🛑 Đã đạt mốc ${apMaxChapters} chương (Max Chapters/Run). Tạm nghỉ 60 giây để tránh Rate Limit API...`, 'warning');
            await new Promise(r => setTimeout(r, 60000));
          } else {
            addLog(`⏳ Chờ ${apDelay} giây...`, 'info');
            await new Promise(r => setTimeout(r, apDelay * 1000));
          }
        }
      }
      addLog(`🎉 AutoPilot hoàn tất.`, 'success');
    } catch (e: any) {
      addLog(`❌ Lỗi API: ${e.message}`, 'error');
    } finally {
      setApIsRunning(false);
    }
  };

  const handleIronCheck = async () => {
    if (!deepseekKey) return showToast("Chưa có API Key!", 'error');
    if (!ironCheckText?.trim()) return showToast("Vui lòng dán nội dung chương cần soi!", 'error');
    if (!storyBible?.trim()) return showToast("Hệ thống cần Story Bible gốc để đối chiếu!", 'success');
    setIsCheckingRules(true);
    try {
      const bibleObj = JSON.parse(storyBible);
      // Build params — include custom Iron Rules only for checker, never for writer
      const checkerParams = {
        story_bible: JSON.stringify(bibleObj),
        chapter_map: JSON.stringify(chapterMap),
        previous_state: currentState,
        chapter_draft: ironCheckText,
        chapter_number: selectedChapterIdx + 1,
        // Append custom rules to system prompt if toggle is ON
        extra_rules: (useFullIronRulesInChecker && customIronRules.trim()) ? customIronRules.trim() : '',
      };
      const result = await agentIronRulesV2('deepseek', deepseekKey, 'deepseek-reasoner', checkerParams);
      setIronCheckResult(result.text ? (() => { try { return JSON.parse(result.text); } catch { return { verdict: 'UNKNOWN', score: 0, errors: [result.text], patch_notes: '' }; } })() : result.data);
      setLastUsedModel(result.usedModel);
    } catch (e: any) {
      showToast("Lỗi Soi Sạn: " + e.message, 'error');
    } finally {
      setIsCheckingRules(false);
    }
  };

  const handleFinalAudit = async () => {
    if (!deepseekKey) return showToast("Vui lòng nhập DeepSeek API Key trong cài đặt!", 'error');
    if (!storyBible?.trim() || chapters.filter(ch => ch && ch.content).length === 0) {
      return showToast("Cần có Story Bible và ít nhất 1 chương đã viết để Final Audit!", 'error');
    }
    
    setIsFinalAuditing(true);
    try {
      const allChaptersText = chapters
        .filter(ch => ch && ch.content)
        .map(ch => `[Chương ${ch.chapter}: ${ch.title}]\n${ch.content}`)
        .join('\n\n');
        
      const auditParams = {
        story_bible: storyBible,
        chapter_map: JSON.stringify(chapterMap),
        all_chapters: allChaptersText,
        current_state: currentState,
        audit_reports: JSON.stringify(auditReports),
        extra_rules: (useFullIronRulesInChecker && customIronRules.trim()) ? customIronRules.trim() : '',
      };
      
      const result = await agentFinalAudit('deepseek', deepseekKey, 'deepseek-reasoner', auditParams);
      setFinalAuditReport(result.text);
      setLastUsedModel(result.usedModel);
      
      // Auto save draft
      updateDraftSpace('deepseek_pipeline', { finalAuditReport: result.text });
    } catch (e: any) {
      showToast("Lỗi Final Audit: " + e.message, 'error');
    }
  };

  // ── AUTO FIX FROM FINAL AUDIT ────────────────────────────────────────────
  const handleAutoFixFromAudit = async () => {
    if (!finalAuditReport) return showToast('Chưa có báo cáo Final Audit. Chạy audit trước!', 'error');
    if (chapters.length === 0) return showToast('Chưa có chương nào để sửa!', 'error');
    if (!deepseekKey) return showToast('Thiếu DeepSeek API Key!', 'error');

    // Parse chapter numbers from audit report — extract from "Chương X" or "Chapter X" patterns
    const chapNums = new Set<number>();
    const patterns = [
      /Chương\s+(\d+)/gi,
      /Chapter\s+(\d+)/gi,
      /ch\.\s*(\d+)/gi,
      /\|(\d+)\|/g,
    ];
    // Only look in Required Fixes / Patch Plan sections to avoid false positives
    const fixSection = finalAuditReport
      .split(/##\s*(Required Fix|Patch Plan|Summary of Required|ADD-ON v2)/i)
      .slice(1)
      .join('\n');
    const searchIn = fixSection || finalAuditReport;
    for (const pat of patterns) {
      let m;
      while ((m = pat.exec(searchIn)) !== null) {
        const n = parseInt(m[1]);
        if (n >= 1 && n <= chapters.length) chapNums.add(n);
      }
    }

    if (chapNums.size === 0) {
      showToast('Không tìm thấy chương cụ thể nào cần sửa trong báo cáo. Hãy dùng nút Patch từng chương riêng lẻ.', 'info');
      return;
    }

    const sorted = Array.from(chapNums).sort((a, b) => a - b);
    setIsAutoFixing(true);
    setAutoFixLog([{ msg: `🔧 Auto Fix bắt đầu — sẽ sửa ${sorted.length} chương: ${sorted.map(n => `Ch.${n}`).join(', ')}`, type: 'info' }]);

    const newChapters = [...chapters];
    for (const chapNum of sorted) {
      const idx = chapNum - 1;
      const chap = newChapters[idx];
      if (!chap?.content) {
        setAutoFixLog(prev => [...prev, { msg: `⚠️ Chương ${chapNum}: Chưa có nội dung, bỏ qua.`, type: 'error' }]);
        continue;
      }
      setAutoFixLog(prev => [...prev, { msg: `⏳ Đang patch Chương ${chapNum}...`, type: 'info' }]);
      try {
        // Build patch notes: use per-chapter audit if exists, otherwise extract from final audit
        const perChapAudit = auditReports[idx];
        const patchNotes = perChapAudit?.patch_notes
          || `Dựa trên Final Audit Report — các lỗi liên quan đến Chương ${chapNum}:\n\n${finalAuditReport.slice(0, 3000)}`;

        const result = await agentRewriteChapter('deepseek', deepseekKey, 'deepseek-chat', chap.content, patchNotes);
        if (!result.text || result.text.trim().length < 100) {
          setAutoFixLog(prev => [...prev, { msg: `❌ Chương ${chapNum}: Kết quả rỗng, bỏ qua.`, type: 'error' }]);
          continue;
        }
        newChapters[idx] = { ...chap, content: result.text, usedModel: `Auto-Fix(${result.usedModel})` };
        setChapters([...newChapters]);
        updateDraftSpace('deepseek_pipeline', { chapters: newChapters });
        setAutoFixLog(prev => [...prev, { msg: `✅ Chương ${chapNum}: Patch xong (${result.usedModel})`, type: 'success' }]);
        await new Promise(r => setTimeout(r, 1500));
      } catch (e: any) {
        setAutoFixLog(prev => [...prev, { msg: `❌ Chương ${chapNum}: Lỗi — ${e.message}`, type: 'error' }]);
      }
    }
    setIsAutoFixing(false);
    setAutoFixLog(prev => [...prev, { msg: `🎉 Auto Fix hoàn tất! Hãy chạy lại Final Audit để xác nhận.`, type: 'success' }]);
    showToast(`✅ Đã patch ${sorted.length} chương. Chạy lại Final Audit để kiểm tra!`, 'success');
  };


  return (
    <div className="flex flex-col h-full bg-[#111] overflow-hidden text-sm relative">
      {toast && (
        <div className={`fixed top-6 right-6 z-50 flex items-center gap-3 px-5 py-4 rounded-xl shadow-2xl border backdrop-blur-xl transition-all animate-in fade-in slide-in-from-top-4 ${
          toast.type === 'error' ? 'bg-rose-500/10 border-rose-500/30 text-rose-400' :
          toast.type === 'success' ? 'bg-emerald-500/10 border-emerald-500/30 text-emerald-400' :
          'bg-blue-500/10 border-blue-500/30 text-blue-400'
        }`}>
          {toast.type === 'error' ? <ShieldAlert size={20}/> : toast.type === 'success' ? <CheckCircle2 size={20}/> : <BookOpen size={20}/>}
          <div className="font-bold tracking-wide">{toast.text}</div>
        </div>
      )}
      {/* HEADER: MODE TABS + RISK SELECTOR */}
      <div className="bg-[#1a1a1a] border-b border-white/10 p-4 shrink-0 overflow-x-auto">
         <div className="flex items-center gap-4 min-w-max">
            {/* Mode Selector (tabs) */}
            <button onClick={() => setActiveTab(1)} className={`px-5 py-2.5 rounded-lg flex items-center gap-2 font-bold transition-all ${activeTab === 1 ? 'bg-gradient-to-r from-blue-600 to-indigo-600 text-white shadow-[0_0_15px_rgba(79,70,229,0.5)]' : 'bg-black/50 text-white/50 hover:text-white/80'}`}>
                <BookOpen size={16}/> Story Bible
            </button>
            <button onClick={() => setActiveTab(2)} className={`px-5 py-2.5 rounded-lg flex items-center gap-2 font-bold transition-all ${activeTab === 2 ? 'bg-gradient-to-r from-emerald-600 to-green-600 text-white shadow-[0_0_15px_rgba(16,185,129,0.5)]' : 'bg-black/50 text-white/50 hover:text-white/80'}`}>
                <Map size={16}/> Chapter Map
            </button>
            <button onClick={() => setActiveTab(3)} className={`px-5 py-2.5 rounded-lg flex items-center gap-2 font-bold transition-all ${activeTab === 3 ? 'bg-gradient-to-r from-amber-600 to-orange-600 text-white shadow-[0_0_15px_rgba(245,158,11,0.5)]' : 'bg-black/50 text-white/50 hover:text-white/80'}`}>
                <PenTool size={16}/> Chapter Writer
            </button>
            <button onClick={() => setActiveTab(4)} className={`px-5 py-2.5 rounded-lg flex items-center gap-2 font-bold transition-all ${activeTab === 4 ? 'bg-gradient-to-r from-rose-600 to-red-600 text-white shadow-[0_0_15px_rgba(225,29,72,0.5)]' : 'bg-black/50 text-white/50 hover:text-white/80'}`}>
                <ShieldAlert size={16}/> Iron Rules
            </button>

            {/* Divider */}
            <div className="w-px h-8 bg-white/10 mx-2"/>

            {/* Risk Selector — only relevant for Chapter Writer */}
            <div className="flex items-center gap-2">
              <span className="text-white/40 text-xs font-semibold uppercase tracking-widest">Risk</span>
              {(['low', 'medium', 'high'] as const).map(level => (
                <button
                  key={level}
                  onClick={() => setRiskLevel(level)}
                  className={`px-3 py-1.5 rounded-lg text-xs font-bold border transition-all capitalize ${
                    riskLevel === level
                      ? level === 'high'   ? 'bg-rose-500/20 border-rose-500 text-rose-400'
                      : level === 'medium' ? 'bg-amber-500/20 border-amber-500 text-amber-400'
                      :                     'bg-emerald-500/20 border-emerald-500 text-emerald-400'
                      : 'bg-black/40 border-white/10 text-white/40 hover:text-white/70'
                  }`}
                >
                  {level}
                </button>
              ))}

              {/* Live readout: shows taskType + model that will be used */}
              {(() => {
                const taskMap: Record<number, string> = { 1: 'story_bible', 2: 'chapter_map', 3: 'chapter_writer', 4: 'iron_rules_checker' };
                const task = taskMap[activeTab];
                const reasonerTasks = ['story_bible', 'chapter_map', 'iron_rules_checker'];
                const model = reasonerTasks.includes(task)
                  ? 'R1'
                  : (task === 'chapter_writer' && riskLevel === 'high' ? 'R1' : 'V3');
                return (
                  <span className="ml-2 text-[10px] font-mono text-white/30 bg-black/40 px-2 py-1 rounded border border-white/5">
                    {task} → {model}
                  </span>
                );
              })()}
            </div>
         </div>
      </div>

      <div className="flex-1 overflow-y-auto p-4 md:p-6 custom-scrollbar">
        {/* MODE 1: STORY BIBLE */}
        {activeTab === 1 && (
          <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-6">
             {/* Left: Input */}
             <div className="bg-[#1a1a1a] rounded-xl border border-white/10 p-6 flex flex-col gap-6">
                <div>
                   <h3 className="text-white font-bold text-lg mb-2 flex items-center gap-2"><Settings className="text-blue-400"/> Cấu Hình Gốc</h3>
                   <p className="text-white/60 mb-4">Nhập ý tưởng thô và DeepSeek R1 sẽ tư duy (Reasoning) để lập ra một Story Bible sắc bén, logic chặt chẽ.</p>
                   
                   <label className="text-white/80 font-semibold mb-2 block">1. Thể Loại (Genres)</label>
                   
                   {/* Hot genres group */}
                   <div className="mb-2">
                      <p className="text-rose-400 text-[10px] font-bold uppercase tracking-widest mb-2">🔥 Đang Hot</p>
                      <div className="flex flex-wrap gap-2">
                         {['Đô Thị Vả Mặt', 'Trọng Sinh Báo Thù', 'Ly Hôn Tổng Tài', 'Hào Môn Tân Phụ', 'Cô Vợ Bí Ẩn', 'Bắt Sóng Đại Lão'].map(g => (
                            <button key={g} onClick={() => toggleGenre(g)} className={`px-3 py-1.5 rounded-full text-xs font-medium border transition-all ${selectedGenres.includes(g) ? 'bg-rose-500/20 border-rose-500 text-rose-400' : 'bg-black/40 border-white/10 text-white/60 hover:text-white/90'}`}>
                               🔥 {g}
                            </button>
                         ))}
                      </div>
                   </div>

                   {/* Zhihu group */}
                   <div className="mb-2">
                      <p className="text-blue-400 text-[10px] font-bold uppercase tracking-widest mb-2">📖 Zhihu / Kịch Tính</p>
                      <div className="flex flex-wrap gap-2">
                         {['Gia Đấu', 'Cung Đấu', 'Công Sở Thủ Đoạn', 'Hôn Nhân Rạn Nứt', 'Bí Ẩn Danh Tính', 'Phản Bội Cú Sốc'].map(g => (
                            <button key={g} onClick={() => toggleGenre(g)} className={`px-3 py-1.5 rounded-full text-xs font-medium border transition-all ${selectedGenres.includes(g) ? 'bg-blue-500/20 border-blue-500 text-blue-400' : 'bg-black/40 border-white/10 text-white/60 hover:text-white/90'}`}>
                               📖 {g}
                            </button>
                         ))}
                      </div>
                   </div>

                   {/* Fantasy group */}
                   <div className="mb-6">
                      <p className="text-purple-400 text-[10px] font-bold uppercase tracking-widest mb-2">✨ Huyền Ảo</p>
                      <div className="flex flex-wrap gap-2">
                         {['Xuyên Không', 'Tiên Hiệp', 'Dị Năng Giác Tỉnh', 'Hệ Thống Giả Mạo', 'Mạt Thế Sinh Tồn', 'Ngôn Tình Cổ Đại'].map(g => (
                            <button key={g} onClick={() => toggleGenre(g)} className={`px-3 py-1.5 rounded-full text-xs font-medium border transition-all ${selectedGenres.includes(g) ? 'bg-purple-500/20 border-purple-500 text-purple-400' : 'bg-black/40 border-white/10 text-white/60 hover:text-white/90'}`}>
                               ✨ {g}
                            </button>
                         ))}
                      </div>
                   </div>

                   <label className="text-white/80 font-semibold mb-2 block">2. Ý Tưởng Gốc (Prompt)</label>
                   <textarea 
                     className="w-full bg-black/40 border border-white/10 rounded-lg p-4 text-white placeholder-white/30 focus:border-blue-500 focus:outline-none resize-none custom-scrollbar" 
                     rows={6}
                     placeholder="Ví dụ: Nữ chính bị chồng và bạn thân lừa dối, hãm hại mất công ty. Cô trọng sinh về 1 năm trước và quyết tâm trả thù..."
                     value={prompt}
                     onChange={(e) => setPrompt(e.target.value)}
                   />
                </div>

                <button 
                  onClick={handleGenerateBible} 
                  disabled={isGeneratingBible}
                  className="w-full py-4 rounded-xl font-bold text-white bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed shadow-[0_0_20px_rgba(79,70,229,0.3)] transition-all flex justify-center items-center gap-2"
                >
                  {isGeneratingBible ? ( <><div className="animate-spin h-5 w-5 border-2 border-white/20 border-t-white rounded-full"></div> Đang Suy Nghĩ (Reasoning)...</> ) : ( <><Zap size={18}/> Tự Động Xây Story Bible</> )}
                </button>
             </div>

             {/* Right: Output/Editor */}
              <div className="bg-[#1a1a1a] rounded-xl border border-white/10 p-6 flex flex-col">
                <div className="flex justify-between items-center mb-4">
                    <h3 className="text-white font-bold text-lg flex items-center gap-2"><BookOpen className="text-blue-400"/> Story Bible (JSON)</h3>
                    <div className="flex items-center gap-2">
                       {lastUsedModel && <span className="text-[10px] bg-blue-500/20 text-blue-400 border border-blue-500/30 px-2 py-1 rounded-full font-mono">{lastUsedModel}</span>}
                       <span className="text-xs text-white/50 bg-black/40 px-3 py-1 rounded-full border border-white/10">Bản thô có thể chỉnh sửa</span>
                    </div>
                </div>
                
                <textarea 
                  className="flex-1 w-full bg-black/50 border border-white/10 rounded-lg p-4 text-emerald-400 font-mono text-xs focus:border-blue-500 focus:outline-none resize-none custom-scrollbar"
                  placeholder="Story Bible sẽ xuất hiện tại đây dưới dạng JSON. Bạn có quyền chỉnh sửa trực tiếp trước khi sinh Dàn ý chương..."
                  value={storyBible}
                  onChange={(e) => setStoryBible(e.target.value)}
                />
                <div className="flex gap-2 mt-3">
                   <button onClick={handleSaveBible} className="flex-1 py-2 rounded-lg text-xs font-bold bg-blue-500/10 border border-blue-500/30 text-blue-400 hover:bg-blue-500/20 transition-all">
                     💾 Save Bible
                   </button>
                   <button onClick={handleResetCurrentStory} className="py-2 px-4 rounded-lg text-xs font-bold bg-rose-500/10 border border-rose-500/30 text-rose-400 hover:bg-rose-500/20 transition-all">
                     🗑️ Reset Current Story
                   </button>
                </div>
              </div>
            </div>
        )}

        {/* MODE 2: CHAPTER MAP */}
        {activeTab === 2 && (
          <div className="max-w-6xl mx-auto flex flex-col h-full gap-6">
             <div className="bg-[#1a1a1a] rounded-xl border border-white/10 p-6 shrink-0 flex flex-wrap items-end gap-6">
                <div className="flex-1">
                   <h3 className="text-white font-bold text-lg mb-2 flex items-center gap-2"><Map className="text-emerald-400"/> Lên Dàn Ý (Chapter Map)</h3>
                   <p className="text-white/60">Dựa vào Story Bible đã chốt, R1 sẽ chia mâu thuẫn thành từng chương theo tỷ lệ vàng.</p>
                </div>
                {/* Chapter count controls */}
                <div className="flex flex-col gap-3">
                   <label className="text-white/80 text-xs font-semibold block">Số Chương (5–20)</label>
                   <div className="flex items-center gap-3">
                      {/* Auto toggle */}
                      <button
                        onClick={() => setAutoChapters(!autoChapters)}
                        className={`flex items-center gap-2 px-3 py-2 rounded-lg border text-xs font-bold transition-all ${autoChapters ? 'bg-emerald-500/20 border-emerald-500 text-emerald-400' : 'bg-black/40 border-white/10 text-white/40'}`}
                      >
                        <span className={`w-3 h-3 rounded-full ${autoChapters ? 'bg-emerald-400' : 'bg-white/20'}`}></span>
                        AI Tự Tính
                      </button>
                      {/* Manual slider (disabled when auto) */}
                      <input
                        type="range"
                        min={5} max={20} step={1}
                        disabled={autoChapters}
                        value={targetChapters}
                        onChange={(e) => setTargetChapters(parseInt(e.target.value))}
                        className="w-32 accent-emerald-500 disabled:opacity-30"
                      />
                      <span className={`text-white font-black text-lg w-8 text-center ${autoChapters ? 'text-white/30 line-through' : 'text-emerald-400'}`}>{targetChapters}</span>
                   </div>
                   {autoChapters && <p className="text-white/40 text-[10px] italic">R1 sẽ tự đánh giá độ phức tạp và đề xuất số chương phù hợp nhất.</p>}
                </div>
                 <div className="flex gap-3">
                   <button 
                     onClick={handleGenerateMap} 
                     disabled={isGeneratingMap}
                     className="py-2.5 px-6 rounded-lg font-bold text-white bg-emerald-600 hover:bg-emerald-500 disabled:opacity-50 disabled:cursor-not-allowed shadow-[0_0_15px_rgba(16,185,129,0.3)] transition-all flex items-center gap-2"
                   >
                     {isGeneratingMap ? 'Đang Lập Map...' : <><Map size={18}/> Sinh Chapter Map</>}
                   </button>
                   <button onClick={handleSaveMap} disabled={chapterMap.length === 0} className="py-2.5 px-4 rounded-lg text-sm font-bold bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 hover:bg-emerald-500/20 disabled:opacity-30 transition-all">
                     💾 Save Map
                   </button>
                   <button onClick={handleResetCurrentStory} className="py-2.5 px-4 rounded-lg text-xs font-bold bg-white/5 border border-white/10 text-white/40 hover:bg-rose-500/10 hover:border-rose-500/30 hover:text-rose-400 transition-all">
                     🗑️ Reset Current Story
                   </button>
                 </div>
             </div>

             <div className="flex-1 overflow-y-auto bg-black/30 rounded-xl border border-white/5 p-4 custom-scrollbar">
                {chapterMap.length === 0 ? (
                    <div className="h-full flex flex-col items-center justify-center text-white/30 italic">Chưa có Chapter Map. Vui lòng bấm Sinh Map.</div>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                       {chapterMap.map((ch: any, idx) => (
                           <div key={idx} className="bg-[#1a1a1a] p-4 rounded-xl border border-white/10 hover:border-emerald-500/50 transition-colors flex flex-col gap-3 group relative">
                              <div className="flex justify-between items-start">
                                 <span className="text-emerald-400 font-black text-xl">CH.{ch.chapter || idx+1}</span>
                                 <span className="text-[10px] font-bold px-2 py-1 rounded bg-black/50 text-white/60 uppercase border border-white/5">{ch.chapter_type || 'Cốt Truyện'}</span>
                              </div>
                              <div className="text-white font-bold leading-tight">{ch.title}</div>
                              <div className="text-white/60 text-xs leading-relaxed">{ch.outline}</div>
                              {ch.has_setback && <div className="text-rose-400 text-xs font-bold mt-auto pt-2 border-t border-white/5">⚠️ MAIN THUA THIỆT Ở CHƯƠNG NÀY</div>}
                           </div>
                       ))}
                    </div>
                )}
             </div>
          </div>
        )}

        {/* MODE 3: CHAPTER WRITER */}
        {activeTab === 3 && (
          <div className="max-w-6xl mx-auto flex flex-col gap-6 h-full">
             {/* Controls bar */}
             <div className="bg-[#1a1a1a] rounded-xl border border-white/10 p-5 shrink-0 flex flex-wrap items-end gap-4">
               <div className="flex-1">
                  <h3 className="text-white font-bold text-lg mb-1 flex items-center gap-2"><PenTool className="text-amber-400"/> Viết Chương</h3>
                  <p className="text-white/50 text-xs">Chọn chương cần viết từ Map. V3 viết thường, R1 viết chương rủi ro cao.</p>
               </div>
               {/* Chapter selector */}
               <div>
                 <label className="text-white/70 text-xs font-semibold block mb-1">Chương</label>
                 <select className="bg-black/50 border border-white/10 rounded-lg px-3 py-2 text-white text-sm focus:border-amber-500 focus:outline-none" value={selectedChapterIdx} onChange={(e) => setSelectedChapterIdx(parseInt(e.target.value))}>
                   {(chapterMap.length > 0 ? chapterMap : [{title:'(Chưa có Map)'}]).map((ch: any, i) => (
                     <option key={i} value={i}>CH.{(ch.chapter||i+1)}: {ch.title?.substring(0,30)}</option>
                   ))}
                 </select>
               </div>
               {/* Risk Level */}
               <div>
                 <label className="text-white/70 text-xs font-semibold block mb-1">Risk Level</label>
                 <div className="flex gap-2">
                   <button onClick={() => setRiskLevel('normal')} className={`px-3 py-1.5 rounded-lg border text-xs font-bold transition-all ${riskLevel==='normal' ? 'bg-amber-500/20 border-amber-500 text-amber-400' : 'bg-black/40 border-white/10 text-white/40'}`}>Normal (V3)</button>
                   <button onClick={() => setRiskLevel('high')} className={`px-3 py-1.5 rounded-lg border text-xs font-bold transition-all ${riskLevel==='high' ? 'bg-rose-500/20 border-rose-500 text-rose-400' : 'bg-black/40 border-white/10 text-white/40'}`}>High (R1)</button>
                 </div>
               </div>
               {/* Action buttons */}
               <div className="flex gap-3 flex-wrap">
                 <button onClick={handleWriteChapter} disabled={isWritingChapter} className="py-2 px-5 rounded-lg font-bold text-white bg-amber-600 hover:bg-amber-500 disabled:opacity-50 flex items-center gap-2 transition-all">
                   {isWritingChapter ? 'Đang viết...' : <><PenTool size={16}/> Viết Chương</>}
                 </button>
                 <button onClick={handlePatchChapter} disabled={isPatching} className="py-2 px-5 rounded-lg font-bold text-white bg-blue-600 hover:bg-blue-500 disabled:opacity-50 flex items-center gap-2 transition-all">
                   {isPatching ? 'Patching...' : <><Zap size={16}/> Patch (V3)</>}
                 </button>
                  {/* Export group */}
                  <div className="flex items-center gap-2 bg-black/30 border border-white/10 rounded-lg px-3 py-1.5">
                    <Download size={14} className="text-emerald-400 shrink-0"/>
                    <button
                      onClick={() => handleExportStory('md')}
                      disabled={chapters.filter(Boolean).length === 0}
                      className="text-xs font-bold text-emerald-400 hover:text-emerald-300 disabled:opacity-30 transition-all"
                    >
                      .MD
                    </button>
                    <span className="text-white/20 text-xs">|</span>
                    <button
                      onClick={() => handleExportStory('txt')}
                      disabled={chapters.filter(Boolean).length === 0}
                      className="text-xs font-bold text-emerald-400 hover:text-emerald-300 disabled:opacity-30 transition-all"
                    >
                      .TXT
                    </button>
                    <span className="text-white/20 text-xs">|</span>
                    <label className="flex items-center gap-1.5 cursor-pointer select-none">
                      <input
                        type="checkbox"
                        checked={includeAuditInExport}
                        onChange={e => setIncludeAuditInExport(e.target.checked)}
                        className="accent-rose-500 w-3 h-3"
                      />
                      <span className="text-[10px] text-white/40 font-semibold">+Audit</span>
                    </label>
                  </div>
                 <button onClick={() => setIsAutoPilotPanelOpen(!isAutoPilotPanelOpen)} className={`py-2 px-5 rounded-lg font-bold text-white flex items-center gap-2 transition-all ${isAutoPilotPanelOpen ? 'bg-purple-600' : 'bg-purple-700 hover:bg-purple-600'}`}>
                   <Rocket size={16}/> AutoPilot
                 </button>
                 {/* Save / Clear group */}
                 <div className="w-px h-8 bg-white/10 self-center"/>
                 <button onClick={handleSaveChapter} disabled={!chapters[selectedChapterIdx]?.content} className="py-2 px-4 rounded-lg text-xs font-bold bg-amber-500/10 border border-amber-500/30 text-amber-400 hover:bg-amber-500/20 disabled:opacity-30 transition-all">
                   💾 Save Chapter
                 </button>
                 <button onClick={handleSaveAudit} disabled={Object.keys(auditReports).length === 0} className="py-2 px-4 rounded-lg text-xs font-bold bg-rose-500/10 border border-rose-500/30 text-rose-400 hover:bg-rose-500/20 disabled:opacity-30 transition-all">
                   💾 Save Audit
                 </button>
                 <button
                   onClick={handleSendToReview}
                   disabled={chapters.filter(ch => ch.content?.trim()).length === 0}
                   className="py-2 px-5 rounded-lg text-xs font-black bg-gradient-to-r from-emerald-600 to-teal-600 text-white hover:opacity-90 disabled:opacity-30 transition-all shadow-[0_0_15px_rgba(16,185,129,0.3)] flex items-center gap-2"
                 >
                   📤 Gửi Tổng Duyệt
                 </button>
                 <button onClick={handleResetCurrentStory} className="py-2 px-4 rounded-lg text-xs font-bold bg-white/5 border border-white/10 text-white/40 hover:bg-rose-500/10 hover:border-rose-500/30 hover:text-rose-400 transition-all">
                   🗑️ Reset Current Story
                 </button>

               </div>
             </div>

             {/* AUTOPILOT PANEL */}
             {isAutoPilotPanelOpen && (
               <div className="bg-purple-900/10 border border-purple-500/30 rounded-xl p-5 mb-6 flex flex-col gap-4">
                 <div className="flex items-center gap-2 mb-2">
                   <Rocket className="text-purple-400" size={18}/>
                   <h3 className="text-white font-bold text-lg">AutoPilot Settings</h3>
                 </div>
                 
                 <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                   <div>
                     <label className="text-white/60 text-xs font-semibold block mb-1">Từ Chương</label>
                     <input type="number" min="1" value={apStartChapter} onChange={e => setApStartChapter(parseInt(e.target.value) || 1)} className="w-full bg-black/40 border border-white/10 rounded-lg p-2 text-white/90 text-sm focus:border-purple-500 focus:outline-none"/>
                   </div>
                   <div>
                     <label className="text-white/60 text-xs font-semibold block mb-1">Đến Chương</label>
                     <input type="number" min="1" value={apEndChapter} onChange={e => setApEndChapter(parseInt(e.target.value) || 3)} className="w-full bg-black/40 border border-white/10 rounded-lg p-2 text-white/90 text-sm focus:border-purple-500 focus:outline-none"/>
                   </div>
                   <div>
                     <label className="text-white/60 text-xs font-semibold block mb-1">Max Chapters/Run</label>
                     <input type="number" min="1" max="5" value={apMaxChapters} onChange={e => setApMaxChapters(Math.min(5, Math.max(1, parseInt(e.target.value) || 3)))} className="w-full bg-black/40 border border-white/10 rounded-lg p-2 text-white/90 text-sm focus:border-purple-500 focus:outline-none"/>
                   </div>
                   <div>
                     <label className="text-white/60 text-xs font-semibold block mb-1">Delay (giây)</label>
                     <input type="number" min="0" value={apDelay} onChange={e => setApDelay(Math.max(0, parseInt(e.target.value) || 0))} className="w-full bg-black/40 border border-white/10 rounded-lg p-2 text-white/90 text-sm focus:border-purple-500 focus:outline-none"/>
                   </div>
                 </div>

                 <div>
                   <label className="text-white/60 text-xs font-semibold block mb-1">Chế độ AutoPilot</label>
                   <div className="flex flex-wrap gap-2">
                     <button onClick={() => setApMode('draft_only')} className={`px-4 py-2 rounded-lg text-sm font-bold border transition-all ${apMode === 'draft_only' ? 'bg-purple-600 border-purple-500 text-white' : 'bg-black/40 border-white/10 text-white/40 hover:bg-white/5'}`}>
                       Draft Only <span className="block text-[10px] font-normal mt-0.5 opacity-70">Viết & Lưu Draft, không Audit</span>
                     </button>
                     <button onClick={() => setApMode('balanced')} className={`px-4 py-2 rounded-lg text-sm font-bold border transition-all ${apMode === 'balanced' ? 'bg-emerald-600 border-emerald-500 text-white' : 'bg-black/40 border-white/10 text-white/40 hover:bg-white/5'}`}>
                       Balanced Auto <span className="block text-[10px] font-normal mt-0.5 opacity-70">Viết ➔ Audit ➔ Tự Patch ➔ Đi tiếp</span>
                     </button>
                     <button onClick={() => setApMode('safe')} className={`px-4 py-2 rounded-lg text-sm font-bold border transition-all ${apMode === 'safe' ? 'bg-amber-600 border-amber-500 text-white' : 'bg-black/40 border-white/10 text-white/40 hover:bg-white/5'}`}>
                       Safe Auto <span className="block text-[10px] font-normal mt-0.5 opacity-70">Viết ➔ Audit ➔ Dừng để xem</span>
                     </button>
                   </div>
                 </div>

                 <div className="flex justify-end gap-3 mt-2 border-t border-purple-500/20 pt-4">
                   {apIsRunning && (
                      <div className="flex items-center text-purple-400 text-sm font-bold mr-auto">
                        <Loader2 className="animate-spin mr-2" size={16}/> Đang chạy AutoPilot...
                      </div>
                   )}
                   <button onClick={handleRunAutoPilot} disabled={apIsRunning} className="py-2.5 px-6 rounded-xl font-bold text-white bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 disabled:opacity-50 transition-all flex items-center gap-2 shadow-[0_0_15px_rgba(147,51,234,0.3)]">
                     <Play size={16}/> Start AutoPilot
                   </button>
                 </div>

                 {/* Progress Logs */}
                 {apLogs.length > 0 && (
                   <div className="bg-black/60 rounded-lg p-3 max-h-40 overflow-y-auto custom-scrollbar mt-2 border border-white/5">
                     {apLogs.map((log, i) => (
                       <div key={i} className={`text-xs font-mono mb-1 ${
                         log.type === 'error' ? 'text-rose-400' : 
                         log.type === 'success' ? 'text-emerald-400' :
                         log.type === 'warning' ? 'text-amber-400' : 'text-white/60'
                       }`}>
                         [{new Date().toLocaleTimeString('vi-VN')}] {log.msg}
                       </div>
                     ))}
                   </div>
                 )}
               </div>
             )}
             {/* Chapter content editor + State JSON */}
             <div className="flex-1 grid grid-cols-1 lg:grid-cols-3 gap-6 overflow-hidden">
               {/* Main editor */}
               <div className="lg:col-span-2 bg-[#1a1a1a] rounded-xl border border-white/10 p-5 flex flex-col">
                 <div className="flex justify-between items-center mb-3">
                   <span className="text-white font-bold">{chapterMap[selectedChapterIdx] ? `CH.${chapterMap[selectedChapterIdx].chapter}: ${chapterMap[selectedChapterIdx].title}` : 'Chưa chọn chương'}</span>
                   {chapters[selectedChapterIdx]?.usedModel && <span className="text-[10px] bg-amber-500/20 text-amber-400 border border-amber-500/30 px-2 py-1 rounded-full font-mono">{chapters[selectedChapterIdx].usedModel}</span>}
                 </div>
                 <textarea className="flex-1 w-full bg-black/40 border border-white/10 rounded-lg p-4 text-white/90 text-sm placeholder-white/30 focus:border-amber-500 focus:outline-none resize-none custom-scrollbar"
                   placeholder="Nội dung chương sẽ xuất hiện ở đây sau khi bấm Viết Chương..."
                   value={chapters[selectedChapterIdx]?.content || ''}
                   onChange={(e) => { const nc=[...chapters]; if(!nc[selectedChapterIdx]) nc[selectedChapterIdx]={chapter:selectedChapterIdx+1,title:'',content:'',usedModel:''}; nc[selectedChapterIdx]={...nc[selectedChapterIdx],content:e.target.value}; setChapters(nc); }}
                 />
               </div>
               {/* State JSON panel — smart parser */}
               <div className="bg-[#1a1a1a] rounded-xl border border-white/10 p-5 flex flex-col gap-3 overflow-hidden">
                 <h4 className="text-white/70 font-bold text-sm shrink-0">📊 State Update JSON</h4>

                 {pendingStateUpdate && (
                   <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-lg p-3 flex flex-col gap-2 shrink-0">
                     <div className="text-emerald-400 text-[10px] font-bold uppercase tracking-widest">✨ Phát hiện State Update mới</div>
                     <pre className="text-emerald-300 font-mono text-[10px] leading-relaxed whitespace-pre-wrap overflow-auto max-h-28 custom-scrollbar">{JSON.stringify(pendingStateUpdate, null, 2)}</pre>
                     <div className="flex gap-2">
                       <button onClick={() => mergeStateUpdate(pendingStateUpdate)} className="flex-1 py-1.5 rounded-lg text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition-all">
                         ✅ Merge vào currentState
                       </button>
                       <button onClick={() => setPendingStateUpdate(null)} className="py-1.5 px-3 rounded-lg text-xs font-bold bg-white/5 border border-white/10 text-white/40 hover:text-white/70 transition-all">
                         ✕
                       </button>
                     </div>
                   </div>
                 )}

                 {stateParseError && !pendingStateUpdate && (
                   <div className="bg-amber-500/10 border border-amber-500/30 rounded-lg p-3 shrink-0">
                     <div className="text-amber-400 text-[10px] font-bold mb-1">⚠️ Không parse được State JSON</div>
                     <div className="text-amber-300/70 text-[10px] font-mono">{stateParseError}</div>
                   </div>
                 )}

                 <div className="flex-1 flex flex-col gap-1 min-h-0">
                   <div className="text-white/30 text-[10px] font-mono">currentState (chỉnh sửa trực tiếp nếu cần)</div>
                   <textarea
                     className="flex-1 min-h-[80px] w-full bg-black/40 border border-white/10 rounded-lg p-2 text-emerald-400 font-mono text-[10px] focus:border-emerald-500 focus:outline-none resize-none custom-scrollbar"
                     value={currentState}
                     onChange={e => setCurrentState(e.target.value)}
                     spellCheck={false}
                   />
                   {(() => {
                     try { JSON.parse(currentState); return <div className="text-emerald-500/60 text-[9px] font-mono">✅ Valid JSON</div>; }
                     catch { return <div className="text-rose-400/60 text-[9px] font-mono">❌ Invalid JSON — sửa lại trước khi dùng</div>; }
                   })()}
                 </div>
               </div>
             </div>
          </div>
        )}

        {/* MODE 4: IRON RULES CHECKER V2 */}
        {activeTab === 4 && (
          <div className="max-w-6xl mx-auto flex flex-col gap-5">

            {/* ── Iron Rules Settings Panel ─────────────────────────────── */}
            <div className="bg-[#1a1a1a] rounded-xl border border-white/10 p-5">
              <div className="flex items-center justify-between mb-4">
                <div className="flex flex-col gap-1">
                  <h3 className="font-bold text-white flex items-center gap-2">
                    <ShieldAlert className="text-rose-500" size={18} />
                    Custom Iron Rules <span className="text-[10px] bg-rose-500/20 text-rose-300 px-2 py-0.5 rounded-full border border-rose-500/30">Optional</span>
                  </h3>
                  <span className="text-white/40 text-[11px]">Mặc định app đã có Iron Rules. Ô này chỉ dùng để bổ sung hoặc override luật riêng.</span>
                </div>
                <div className="flex items-center gap-3">
                  {/* Toggle */}
                  <label className="flex items-center gap-2 cursor-pointer select-none">
                    <div
                      onClick={() => setUseFullIronRulesInChecker(!useFullIronRulesInChecker)}
                      className={`relative w-10 h-5 rounded-full transition-colors cursor-pointer ${useFullIronRulesInChecker ? 'bg-rose-500' : 'bg-white/10'}`}
                    >
                      <div className={`absolute top-0.5 w-4 h-4 rounded-full bg-white shadow transition-all ${useFullIronRulesInChecker ? 'left-5' : 'left-0.5'}`}/>
                    </div>
                    <span className={`text-xs font-bold ${useFullIronRulesInChecker ? 'text-rose-400' : 'text-white/30'}`}>
                      {useFullIronRulesInChecker ? 'Use Custom Rules' : 'Tắt'}
                    </span>
                  </label>
                  {/* Save Iron Rules */}
                  <button
                    onClick={() => { updateDraftSpace('deepseek_pipeline', { customIronRules }); showToast('✅ Iron Rules đã lưu!', 'success'); }}
                    disabled={!customIronRules.trim()}
                    className="py-1.5 px-4 rounded-lg text-xs font-bold bg-rose-500/10 border border-rose-500/30 text-rose-400 hover:bg-rose-500/20 disabled:opacity-30 transition-all"
                  >
                    💾 Save Iron Rules
                  </button>
                </div>
              </div>
              <textarea
                className="w-full h-32 bg-black/40 border border-white/10 rounded-lg p-3 text-white/70 font-mono text-xs placeholder-white/20 focus:border-rose-500 focus:outline-none resize-none custom-scrollbar"
                placeholder="Paste toàn bộ Iron Rules của anh vào đây. Ví dụ: Rule 1: Không dùng Deus Ex Machina. Rule 2: Nhân vật phải hành động theo logic nội tâm..."
                value={customIronRules}
                onChange={e => setCustomIronRules(e.target.value)}
              />
              {customIronRules.trim() && (
                <div className="mt-2 text-[10px] text-white/30 font-mono">
                  {customIronRules.trim().split('\n').length} dòng · {customIronRules.length} ký tự
                  {useFullIronRulesInChecker ? ' · ✅ Sẽ được gửi tới Checker' : ' · ⏸ Đang tắt'}
                </div>
              )}
            </div>

            {/* ── Existing 2-col checker ───────────────────────────────── */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <div className="bg-[#1a1a1a] rounded-xl border border-white/10 p-6 flex flex-col gap-4">
                <h3 className="text-white font-bold text-lg flex items-center gap-2"><ShieldAlert className="text-rose-400"/> Dán Nội Dung Chương</h3>
                <p className="text-white/60">R1 sẽ Soi Sạn dựa trên Iron Rules và Story Bible. Phán quyết: PASS / PASS_WITH_PATCHES / REWRITE_REQUIRED.</p>
                <textarea 
                  className="flex-1 w-full bg-black/40 border border-white/10 rounded-lg p-4 text-white/90 placeholder-white/30 focus:border-rose-500 focus:outline-none resize-none custom-scrollbar"
                  placeholder="Paste chương truyện vào đây..."
                  value={ironCheckText}
                  onChange={(e) => setIronCheckText(e.target.value)}
                />
                <button onClick={handleIronCheck} disabled={isCheckingRules}
                  className="w-full py-4 rounded-xl font-bold text-white bg-gradient-to-r from-rose-600 to-red-600 hover:from-rose-500 hover:to-red-500 disabled:opacity-50 shadow-[0_0_20px_rgba(225,29,72,0.3)] transition-all flex justify-center items-center gap-2">
                  {isCheckingRules ? 'Đang Soi Sạn (R1)...' : <><ShieldAlert/> Audit Chương</>}
                </button>
             </div>
             <div className="bg-[#1a1a1a] rounded-xl border border-white/10 p-6 flex flex-col">
                 <div className="flex justify-between items-center mb-4">
                   <h3 className="text-white font-bold text-lg flex items-center gap-2"><CheckCircle2 className="text-rose-400"/> Kết Quả Phán Quyết</h3>
                   {lastUsedModel && <span className="text-[10px] bg-rose-500/20 text-rose-400 border border-rose-500/30 px-2 py-1 rounded-full font-mono">{lastUsedModel}</span>}
                 </div>
                 {ironCheckResult ? (
                    <div className="flex flex-col gap-5">
                       {/* Verdict badge */}
                       <div className={`p-5 rounded-xl border flex items-center gap-4 ${
                         ironCheckResult.verdict==='PASS' ? 'bg-emerald-500/10 border-emerald-500/30' :
                         ironCheckResult.verdict==='PASS_WITH_PATCHES' ? 'bg-amber-500/10 border-amber-500/30' :
                         'bg-rose-500/10 border-rose-500/30'}`}>
                          <div className={`text-5xl font-black ${
                            ironCheckResult.verdict==='PASS' ? 'text-emerald-400' :
                            ironCheckResult.verdict==='PASS_WITH_PATCHES' ? 'text-amber-400' : 'text-rose-500'}`}>
                            {ironCheckResult.score}/10
                          </div>
                          <div>
                            <div className={`font-black text-lg ${
                              ironCheckResult.verdict==='PASS' ? 'text-emerald-400' :
                              ironCheckResult.verdict==='PASS_WITH_PATCHES' ? 'text-amber-400' : 'text-rose-400'}`}>
                              {ironCheckResult.verdict==='PASS' ? '✅ PASS' : ironCheckResult.verdict==='PASS_WITH_PATCHES' ? '⚠️ PASS WITH PATCHES' : '❌ REWRITE REQUIRED'}
                            </div>
                            <div className="text-white/50 text-xs mt-1">Phán quyết của Iron Rules Checker (R1)</div>
                          </div>
                       </div>
                       {ironCheckResult.errors?.length > 0 && (
                          <div>
                             <h4 className="text-rose-400 font-bold mb-2">Sạn Phát Hiện:</h4>
                             <ul className="list-disc pl-5 text-white/80 space-y-1 text-sm">
                                {ironCheckResult.errors.map((err: string, i: number) => <li key={i}>{err}</li>)}
                             </ul>
                          </div>
                       )}
                       {ironCheckResult.patch_notes && (
                          <div className="bg-amber-500/10 border border-amber-500/20 p-4 rounded-lg">
                             <h4 className="text-amber-400 font-bold mb-2 flex items-center gap-2"><Zap size={14}/> Patch Notes (dành cho V3):</h4>
                             <div className="text-white/80 text-sm leading-relaxed">{ironCheckResult.patch_notes}</div>
                          </div>
                       )}
                    </div>
                 ) : (
                    <div className="h-full flex items-center justify-center text-white/30 italic text-center">
                        Phán quyết PASS / PASS_WITH_PATCHES / REWRITE_REQUIRED sẽ hiện ở đây.
                    </div>
                 )}
             </div>
          </div>

            {/* ── FINAL STORY AUDIT ───────────────────────────────────── */}
            <div className="bg-[#1a1a1a] rounded-xl border border-white/10 p-6 flex flex-col gap-4 mt-2">
              <div className="flex justify-between items-center">
                <div>
                  <h3 className="text-white font-bold text-lg flex items-center gap-2"><CheckCircle2 className="text-emerald-400"/> Final Story Audit</h3>
                  <p className="text-white/60 text-xs mt-1">Đánh giá toàn bộ câu chuyện (Story Bible, Chapter Map, Chapters) để tìm lỗi logic, sạn, và chấm điểm cuối cùng.</p>
                </div>
                <button onClick={handleFinalAudit} disabled={isFinalAuditing} className="py-2 px-6 rounded-xl font-bold text-white bg-gradient-to-r from-emerald-600 to-green-600 hover:from-emerald-500 hover:to-green-500 disabled:opacity-50 transition-all flex items-center gap-2">
                  {isFinalAuditing ? 'Đang Audit Toàn Tập (R1)...' : <><CheckCircle2 size={16}/> Final Audit Toàn Bộ Truyện</>}
                </button>
              </div>

              {finalAuditReport && (
                <div className="bg-black/40 border border-white/10 rounded-lg p-5 mt-2">
                  <div className="flex justify-between items-center mb-4 pb-3 border-b border-white/10">
                    <h4 className="text-emerald-400 font-bold text-sm">Báo Cáo Final Audit</h4>
                    {lastUsedModel && <span className="text-[10px] bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 px-2 py-1 rounded-full font-mono">{lastUsedModel}</span>}
                  </div>
                  <pre className="text-white/80 font-mono text-xs whitespace-pre-wrap leading-relaxed custom-scrollbar max-h-[400px] overflow-y-auto">
                    {finalAuditReport}
                  </pre>

                  {/* AUTO FIX BUTTON — chỉ hiện khi không phải READY_TO_EXPORT */}
                  {!finalAuditReport.includes('READY_TO_EXPORT') && (
                    <div className="mt-4 border-t border-white/10 pt-4 flex flex-col gap-3">
                      <button
                        onClick={handleAutoFixFromAudit}
                        disabled={isAutoFixing}
                        className={`w-full flex items-center justify-center gap-2 px-4 py-3 rounded-xl font-bold text-sm transition-all ${
                          isAutoFixing
                            ? 'bg-amber-500/10 text-amber-300 border border-amber-500/30 cursor-wait animate-pulse'
                            : 'bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500 text-white shadow-[0_0_15px_rgba(245,158,11,0.3)] hover:shadow-[0_0_25px_rgba(245,158,11,0.5)] border border-amber-500/40'
                        }`}
                      >
                        {isAutoFixing ? (
                          <><Loader2 size={16} className="animate-spin" /> Đang Auto Fix.....</>
                        ) : (
                          <><Zap size={16} /> 🔧 Auto Fix Toàn Bộ (Dựa Theo Audit Report)</>
                        )}
                      </button>
                      <p className="text-white/40 text-[11px] text-center">
                        AI sẽ tự đọc báo cáo, xác định chương cần sửa, và patch lần lượt. Sau khi xong, chạy lại Final Audit để xác nhận.
                      </p>

                      {/* Auto Fix Live Log */}
                      {autoFixLog.length > 0 && (
                        <div className="bg-black/60 border border-amber-500/20 rounded-lg p-3 max-h-48 overflow-y-auto custom-scrollbar space-y-1">
                          {autoFixLog.map((log, i) => (
                            <div key={i} className={`text-xs font-mono ${
                              log.type === 'success' ? 'text-emerald-400' :
                              log.type === 'error' ? 'text-rose-400' : 'text-amber-300'
                            }`}>
                              {log.msg}
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  )}
                </div>
              )}
            </div>

            {/* ── EXPORT FULL PROJECT ───────────────────────────────────── */}
            <div className="bg-[#1a1a1a] rounded-xl border border-white/10 p-6 flex flex-col gap-4 mt-2">
              <div className="flex justify-between items-start flex-wrap gap-4">
                <div className="flex flex-col gap-2">
                  <h3 className="text-white font-bold text-lg flex items-center gap-2"><Download className="text-blue-400"/> Export Full Project</h3>
                  <p className="text-white/60 text-xs">Xuất toàn bộ Project thành 1 file Markdown hoàn chỉnh để dễ dàng lưu trữ hoặc gửi cho nền tảng.</p>
                  
                  <div className="flex flex-wrap gap-4 mt-2">
                    <label className="flex items-center gap-1.5 cursor-pointer">
                      <input type="checkbox" checked={exportIncludeBible} onChange={e => setExportIncludeBible(e.target.checked)} className="accent-blue-500 w-3.5 h-3.5"/>
                      <span className="text-xs text-white/80">Story Bible</span>
                    </label>
                    <label className="flex items-center gap-1.5 cursor-pointer">
                      <input type="checkbox" checked={exportIncludeMap} onChange={e => setExportIncludeMap(e.target.checked)} className="accent-blue-500 w-3.5 h-3.5"/>
                      <span className="text-xs text-white/80">Chapter Map</span>
                    </label>
                    <label className="flex items-center gap-1.5 cursor-pointer">
                      <input type="checkbox" checked={exportIncludeState} onChange={e => setExportIncludeState(e.target.checked)} className="accent-blue-500 w-3.5 h-3.5"/>
                      <span className="text-xs text-white/80">Current State</span>
                    </label>
                    <label className="flex items-center gap-1.5 cursor-pointer">
                      <input type="checkbox" checked={exportIncludeAudit} onChange={e => setExportIncludeAudit(e.target.checked)} className="accent-blue-500 w-3.5 h-3.5"/>
                      <span className="text-xs text-white/80">Audit Reports</span>
                    </label>
                    <label className="flex items-center gap-1.5 cursor-pointer">
                      <input type="checkbox" checked={exportIncludeUsageLog} onChange={e => setExportIncludeUsageLog(e.target.checked)} className="accent-blue-500 w-3.5 h-3.5"/>
                      <span className="text-xs text-white/80">Model Usage Log</span>
                    </label>
                  </div>
                </div>

                <button onClick={handleExportProjectSummary} className="py-2.5 px-6 rounded-xl font-bold text-white bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 transition-all flex items-center gap-2 shadow-[0_0_15px_rgba(37,99,235,0.3)]">
                  <Download size={16}/> Export Full Project Summary
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
