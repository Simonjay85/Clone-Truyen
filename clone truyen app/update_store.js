// eslint-disable-next-line @typescript-eslint/no-require-imports
const fs = require('fs');

const tsFilePath = 'src/store/useStore.ts';
let code = fs.readFileSync(tsFilePath, 'utf8');

// The replacement code for the persist middleware configuration
const storageImplementation = `import { create } from 'zustand';
import { persist, StateStorage } from 'zustand/middleware';

const serverStorage: StateStorage = {
  getItem: async (name: string): Promise<string | null> => {
    try {
      const res = await fetch('/api/db');
      if (!res.ok) return null;
      const json = await res.json();
      if (!json.success || !json.data) return null;
      return JSON.stringify(json.data);
    } catch {
      return null;
    }
  },
  setItem: async (name: string, value: string): Promise<void> => {
    try {
      // Bắn thẳng trạng thái mới nhất lên M-Core DB
      await fetch('/api/db', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(JSON.parse(value))
      });
    } catch {}
  },
  removeItem: async (name: string): Promise<void> => {
    // optional
  },
};`;

code = code.replace(/import { create } from 'zustand';\nimport { persist } from 'zustand\/middleware';/, storageImplementation);

const oldPersistConfig = `    {
      name: 'mac-story-studio-storage',
    }`;

const newPersistConfig = `    {
      name: 'mac-story-studio-storage',
      storage: serverStorage,
    }`;

code = code.replace(oldPersistConfig, newPersistConfig);

fs.writeFileSync(tsFilePath, code);
console.log('Update success');
