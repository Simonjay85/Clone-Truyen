import os

path = "src/store/useStore.ts"
with open(path, "r") as f:
    c = f.read()

api_log_interface = """
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
"""

if "export interface ApiLog" not in c:
    c = c.replace("export interface QueueItem", api_log_interface + "\nexport interface QueueItem")

if "apiLogs: ApiLog[];" not in c:
    c = c.replace("queue: QueueItem[];", "queue: QueueItem[];\n  apiLogs: ApiLog[];")
if "addApiLog: (log: Omit<ApiLog, 'id' | 'timestamp'>) => void;" not in c:
    c = c.replace("updateQueueItem: (id: string, updates: Partial<QueueItem>) => void;", "updateQueueItem: (id: string, updates: Partial<QueueItem>) => void;\n  addApiLog: (log: Omit<ApiLog, 'id' | 'timestamp'>) => void;\n  clearApiLogs: () => void;")

if "apiLogs: []," not in c:
    c = c.replace("queue: [],", "queue: [],\n      apiLogs: [],")

if "addApiLog: (log)" not in c:
    funcs = """
      addApiLog: (log) => set((state) => {
        const newLog = { 
          ...log, 
          id: Math.random().toString(36).substring(2, 9), 
          timestamp: Date.now() 
        };
        const newLogs = [newLog, ...state.apiLogs].slice(0, 1500);
        return { apiLogs: newLogs };
      }),
      clearApiLogs: () => set({ apiLogs: [] }),
"""
    c = c.replace("setSettings: (settings) => set((state) => ({ ...state, ...settings })),", "setSettings: (settings) => set((state) => ({ ...state, ...settings })),\n" + funcs)

with open(path, "w") as f:
    f.write(c)

