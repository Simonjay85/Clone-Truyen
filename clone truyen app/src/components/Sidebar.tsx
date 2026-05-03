import React, { useState } from 'react';
import {  Settings, Rocket, TerminalSquare, Clapperboard, BookOpen, Skull, Feather, Menu, X, HeartHandshake, Swords, Key } from 'lucide-react';

interface SidebarProps {
  currentTab: string;
  setTab: (tab: string) => void;
}

export function Sidebar({ currentTab, setTab }: SidebarProps) {
  const [isOpen, setIsOpen] = useState(false);

  const groupedTabs = [
    {
      group: 'Core AI Authors',
      items: [
        { id: 'gemini_drama', label: 'Sáng Tác 1 (Gemini)', icon: <BookOpen size={16} /> },
        { id: 'micro_drama', label: 'Sáng Tác 2 (OpenAI)', icon: <Clapperboard size={16} /> },
        { id: 'grok_drama', label: 'Sáng Tác 3 (Grok)', icon: <Skull size={16} /> },
        { id: 'claude_drama', label: 'Sáng Tác 4 (Wordsmith)', icon: <Feather size={16} /> },
        { id: 'combo_eco', label: 'Sáng Tác 5 (Kinh Tế)', icon: <Rocket size={16} /> },
        { id: 'combo_royal', label: 'Sáng Tác 6 (Hoàng Gia)', icon: <Rocket size={16} /> },
        { id: 'qwen_drama', label: 'Sáng Tác 7 (Qwen)', icon: <Swords size={16} /> },
        { id: 'deepseek_drama', label: 'Sáng Tác 8 (DeepSeek)', icon: <Feather size={16} /> },
        { id: 'openrouter_drama', label: 'Sáng Tác 9 (OpenRouter)', icon: <Rocket size={16} /> },
      ]
    },
    {
      group: 'Workflow & Publish',
      items: [
        { id: 'chapter_splitter', label: 'Nhập Sỉ Truyện (Splitter)', icon: <Feather size={16} /> },
        { id: 'autopilot', label: 'Auto-Pilot M-Core', icon: <Rocket size={16} /> },
        { id: 'final_review', label: 'Tổng Duyệt (Review)', icon: <TerminalSquare size={16} /> },
        { id: 'social_studio', label: 'Social Studio', icon: <HeartHandshake size={16} /> },
      ]
    },
    {
      group: 'Cấu Hình Trạm',
      items: [
        { id: 'apikeys', label: 'Quota & LLM Keys', icon: <Key size={16} /> },
        { id: 'settings', label: 'WP & Database', icon: <Settings size={16} /> },
      ]
    }
  ];

  return (
    <>
      <div className="md:hidden flex items-center justify-between p-4 bg-slate-900 border-b border-slate-800 shrink-0">
        <h1 className="text-xl font-bold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent flex items-center gap-2 tracking-tight">
          <Rocket size={24} className="text-blue-500" />
          Story Studio
        </h1>
        <button onClick={() => setIsOpen(true)} className="text-slate-300 hover:text-white"><Menu size={24} /></button>
      </div>

      {isOpen && <div className="md:hidden fixed inset-0 bg-black/60 z-40 backdrop-blur-sm" onClick={() => setIsOpen(false)} />}

      <div className={`fixed md:relative inset-y-0 left-0 transform ${isOpen ? "translate-x-0" : "-translate-x-full"} md:translate-x-0 z-50 w-[260px] shrink-0 bg-[#0f0f17] border-r border-white/5 flex flex-col h-full text-slate-300 transition-transform duration-300 ease-in-out`}>
        <div className="p-6 pb-4 flex justify-between items-start shrink-0">
          <div>
            <h1 className="text-2xl font-black bg-gradient-to-r from-indigo-400 to-fuchsia-500 bg-clip-text text-transparent flex items-center gap-2 tracking-tight">
              <Rocket size={26} className="text-indigo-500" />
              Story Studio
            </h1>
            <p className="text-[10px] text-slate-500 mt-1 uppercase font-black tracking-widest pl-1">macOS Native Core</p>
          </div>
          <button className="md:hidden text-slate-400 hover:text-white -mr-2 mt-1" onClick={() => setIsOpen(false)}><X size={20} /></button>
        </div>

      <nav className="flex-1 overflow-y-auto custom-scrollbar px-5 space-y-6 pt-2 pb-6">
        {groupedTabs.map((group, gIdx) => (
          <div key={gIdx} className="space-y-2">
             <div className="text-[10px] font-black text-slate-500 uppercase tracking-widest pl-1 mb-2">{group.group}</div>
             {group.items.map((tab) => (
                <button
                  key={tab.id}
                  onClick={() => { setTab(tab.id); setIsOpen(false); }}
                  className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition-all duration-200 font-medium text-sm ${
                    currentTab === tab.id
                      ? 'bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 shadow-sm'
                      : 'text-slate-400 hover:bg-white/5 hover:text-white border border-transparent'
                  }`}
                >
                  <span className={`${currentTab === tab.id ? 'text-indigo-400' : 'text-slate-500'}`}>{tab.icon}</span>
                  {tab.label}
                </button>
              ))}
          </div>
        ))}
      </nav>

      <div className="p-4 border-t border-slate-800">
        <div className="bg-slate-800/50 rounded-lg p-4 text-xs">
          <div className="flex justify-between items-center mb-2">
            <span className="text-slate-400">Server Local</span>
            <span className="w-2 h-2 rounded-full bg-emerald-500 shadow-[0_0_8px_rgba(16,185,129,0.5)]"></span>
          </div>
          <div className="flex justify-between items-center">
            <span className="text-slate-400">REST API</span>
            <span className="w-2 h-2 rounded-full bg-slate-600"></span>
          </div>
        </div>
      </div>
      </div>
    </>
  );
}
