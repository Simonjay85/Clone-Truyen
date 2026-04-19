"use client";

/* eslint-disable @typescript-eslint/no-explicit-any */
import { create } from 'zustand';

const LS_KEY = 'mcore-keys';

function readLocalKeys(): Record<string, any> {
  if (typeof window === 'undefined') return {};
  try {
    const raw = localStorage.getItem(LS_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch { return {}; }
}

function writeLocalKeys(state: Record<string, unknown>) {
  if (typeof window === 'undefined') return;
  const keys = {
    geminiKey: state.geminiKey || '',
    geminiKey2: state.geminiKey2 || '',
    geminiKey3: state.geminiKey3 || '',
    geminiPaidKey: state.geminiPaidKey || '',
    openAIKey: state.openAIKey || '',
    grokKey: state.grokKey || '',
    claudeKey: state.claudeKey || '',
    usePaidAPI: state.usePaidAPI || false,
    wpUrl: state.wpUrl || 'https://doctieuthuyet.com',
    wpUser: state.wpUser || '',
    wpAppPassword: state.wpAppPassword || '',
    webhookUrl: state.webhookUrl || '',
  };
  // Merge: chỉ ghi đè nếu giá trị mới không rỗng
  const existing = readLocalKeys();
  const merged: Record<string, unknown> = {};
  for (const k of Object.keys(keys)) {
    const newVal = (keys as any)[k];
    merged[k] = (newVal !== '' && newVal !== undefined) ? newVal : (existing[k] ?? newVal);
  }
  localStorage.setItem(LS_KEY, JSON.stringify(merged));
}

// Đọc keys ngay lúc module load (đồng bộ, trước khi store tạo)
const savedKeys = readLocalKeys();

// Đồng bộ queue/apiLogs/draftSpaces lên Server DB (fire-and-forget)
function syncToServer(state: { queue: unknown[]; apiLogs: unknown[]; isAutoPilotRunning: boolean; draftSpaces: Record<string, any>; hasHydrated: boolean }) {
  if (!state.hasHydrated) return; // Prevent overwriting DB with initial empty state
  fetch('/api/db', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      queue: state.queue || [],
      apiLogs: (state.apiLogs || []).slice(0, 500),
      isAutoPilotRunning: state.isAutoPilotRunning || false,
      draftSpaces: state.draftSpaces || {},
    })
  }).catch(() => {});
}

export interface ApiLog {
  id: string; // timestamp based
  engineType: string; // gemini, openai, grok, claude
  model: string;
  station: string; 
  project: string; 
  chapter?: number; 
  promptTokens: number;
  completionTokens: number;
  totalTokens: number;
  cost: number;
  timestamp: number;
}

export interface QueueItem {
  id: string;
  title: string;
  genres: string;
  prompt: string;
   
  bible?: any; // The Puppet Master output
  wpPostId?: number; // Corresponding WordPress Post ID
  status: 'draft_outline' | 'pending_approval' | 'pending' | 'writing' | 'final_review' | 'completed' | 'error' | 'published';
  targetChapters: number;
  maxChapters?: number;
  chaptersDone: number;
  wordCount: number;
  finalEvaluation?: { score: number; review: string; evaluator: string };
  publishData?: { categories: string[]; tags: string[]; coverUrl: string; seoTitle: string; seoDescription: string; seoFocusKeyword: string; finalTitle: string; coverImagePrompt?: string; blurb?: string; };
  errorLog?: string;
  comboType?: 5 | 6; // Sáng tác 5 hay 6
  isAdvancedPipeline?: boolean; // Nếu = true => Gọi 7-Module Engine Pipeline.
  model?: string;
  outlineEngine: 'gemini' | 'openai' | 'grok' | 'claude'; // Gọi engine nào dựng dàn ý
  writeEngine: 'gemini' | 'openai' | 'grok' | 'claude';   // Gọi engine nào viết nội dung
  progressLogs?: string[];
  chaptersContent?: { episode: number; title: string; content: string }[];
  isSocialShared?: boolean; // Tự động chui vào hàng đợi Social Studio nếu = false và status = 'published'
  [key: string]: any;
}

interface AppState {
  // Settings
  geminiKey: string;
  geminiKey2: string;
  geminiKey3: string;  // API Key Free thứ 3
  geminiPaidKey: string;
  openAIKey: string;   // API Key trả phí cho OpenAI (Micro Drama)
  grokKey: string;     // API Key cho xAI (Grok)
  claudeKey: string;   // API Key cho Anthropic (Claude)
  usePaidAPI: boolean;
  isFreeApiExhausted: boolean;
  wpUrl: string;
  wpUser: string;
  wpAppPassword: string;
  webhookUrl: string; // URL cho Make.com/Zapier
  
  // Queue
  queue: QueueItem[];
  apiLogs: ApiLog[];
  isAutoPilotRunning: boolean;
  draftSpaces: Record<string, any>;
  hasHydrated: boolean;
  
  // Actions
  setSettings: (settings: Partial<AppState>) => void;
  addQueueItems: (items: Omit<QueueItem, 'id' | 'status' | 'chaptersDone' | 'wordCount'>[]) => void;
  updateQueueItem: (id: string, updates: Partial<QueueItem>) => void;
  addApiLog: (log: Omit<ApiLog, 'id' | 'timestamp'>) => void;
  clearApiLogs: () => void;
  removeQueueItem: (id: string) => void;
  clearQueue: () => void;
  toggleAutoPilot: () => void;
  updateDraftSpace: (spaceId: string, updates: Record<string, any>) => void;
}

export const useStore = create<AppState>()((set, get) => ({
  // Keys được khởi tạo đồng bộ từ localStorage ngay khi module load
  geminiKey:     savedKeys.geminiKey     || '',
  geminiKey2:    savedKeys.geminiKey2    || '',
  geminiKey3:    savedKeys.geminiKey3    || '',
  geminiPaidKey: savedKeys.geminiPaidKey || '',
  openAIKey:     savedKeys.openAIKey     || '',
  grokKey:       savedKeys.grokKey       || '',
  claudeKey:     savedKeys.claudeKey     || '',
  usePaidAPI:    savedKeys.usePaidAPI    || false,
  isFreeApiExhausted: false,
  wpUrl:         savedKeys.wpUrl         || 'https://doctieuthuyet.com',
  wpUser:        savedKeys.wpUser        || '',
  wpAppPassword: savedKeys.wpAppPassword || '',
  webhookUrl:    savedKeys.webhookUrl    || '',
  
  queue: [],
  apiLogs: [],
  isAutoPilotRunning: false,
  draftSpaces: {},
  hasHydrated: false,
  
  // setSettings: cập nhật store VÀ ghi ngay vào localStorage
  setSettings: (settings) => {
    set((state) => ({ ...state, ...settings }));
    writeLocalKeys({ ...get(), ...settings });
  },

  addApiLog: (log) => {
    set((state) => {
      const newLog = { ...log, id: Math.random().toString(36).substring(2,9), timestamp: Date.now() };
      const newLogs = [newLog, ...state.apiLogs].slice(0, 1500);
      const next = { apiLogs: newLogs };
      syncToServer({ ...state, ...next });
      return next;
    });
  },
  clearApiLogs: () => { set((state) => { syncToServer({ ...state, apiLogs: [] }); return { apiLogs: [] }; }); },

  addQueueItems: (items) => {
    set((state) => {
      const newItems = items.map(item => ({
        id: Math.random().toString(36).substring(2, 10),
        status: 'draft_outline' as const,
        chaptersDone: 0,
        wordCount: 0,
        ...item,
      })) as QueueItem[];
      const next = { queue: [...state.queue, ...newItems] };
      syncToServer({ ...state, ...next });
      return next;
    });
  },

  updateQueueItem: (id, updates) => {
    set((state) => {
      const next = { queue: state.queue.map(item => item.id === id ? { ...item, ...updates } : item) };
      syncToServer({ ...state, ...next });
      return next;
    });
  },

  removeQueueItem: (id) => {
    set((state) => {
      const next = { queue: state.queue.filter(item => item.id !== id) };
      syncToServer({ ...state, ...next });
      return next;
    });
  },

  clearQueue: () => {
    set((state) => {
      syncToServer({ ...state, queue: [], apiLogs: [], isAutoPilotRunning: false });
      return { queue: [], apiLogs: [], isAutoPilotRunning: false };
    });
  },

  toggleAutoPilot: () => {
    set((state) => {
      const next = { isAutoPilotRunning: !state.isAutoPilotRunning };
      syncToServer({ ...state, ...next });
      return next;
    });
  },

  updateDraftSpace: (spaceId, updates) => {
    set((state) => {
      const next = {
        draftSpaces: {
          ...state.draftSpaces,
          [spaceId]: { ...(state.draftSpaces[spaceId] || {}), ...updates }
        }
      };
      syncToServer({ ...state, ...next });
      return next;
    });
  },
}));

// trigger update


