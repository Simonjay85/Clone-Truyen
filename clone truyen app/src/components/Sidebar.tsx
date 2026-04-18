import React, { useState } from 'react';
import {  Settings, Rocket, TerminalSquare, Clapperboard, BookOpen, Skull, Feather, Menu, X, HeartHandshake } from 'lucide-react';

interface SidebarProps {
  currentTab: string;
  setTab: (tab: string) => void;
}

export function Sidebar({ currentTab, setTab }: SidebarProps) {
  const [isOpen, setIsOpen] = useState(false);

  const tabs = [
    { id: 'gemini_drama', label: 'Sáng Tác 1 (Gemini)', icon: <BookOpen size={20} /> },
    { id: 'micro_drama', label: 'Sáng Tác 2 (OpenAI)', icon: <Clapperboard size={20} /> },
    { id: 'grok_drama', label: 'Sáng Tác 3 (Grok Rebel)', icon: <Skull size={20} /> },
    { id: 'claude_drama', label: 'Sáng Tác 4 (Wordsmith)', icon: <Feather size={20} /> },
    { id: 'combo_eco', label: 'Sáng Tác 5 (Liên Quân KT)', icon: <Rocket size={20} /> },
    { id: 'combo_royal', label: 'Sáng Tác 6 (Liên Quân HG)', icon: <Rocket size={20} /> },
    { id: 'autopilot', label: 'Auto-Pilot M-Core', icon: <Rocket size={20} /> },
    { id: 'final_review', label: 'Tổng Duyệt (Review)', icon: <TerminalSquare size={20} /> },
    { id: 'social_studio', label: 'Social Studio', icon: <HeartHandshake size={20} /> },
    { id: 'settings', label: 'Settings', icon: <Settings size={20} /> },
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

      <div className={`fixed md:relative inset-y-0 left-0 transform ${isOpen ? "translate-x-0" : "-translate-x-full"} md:translate-x-0 z-50 w-64 bg-slate-900 border-r border-slate-800 flex flex-col h-full text-slate-300 transition-transform duration-300 ease-in-out`}>
        <div className="p-6 flex justify-between items-start">
          <div>
            <h1 className="text-xl font-bold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent flex items-center gap-2 tracking-tight">
              <Rocket size={24} className="text-blue-500" />
              Story Studio
            </h1>
            <p className="text-xs text-slate-500 mt-1 uppercase font-bold tracking-widest">macOS Native Core</p>
          </div>
          <button className="md:hidden text-slate-400 hover:text-white -mr-2" onClick={() => setIsOpen(false)}><X size={20} /></button>
        </div>

      <nav className="flex-1 px-4 space-y-2 mt-4">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => { setTab(tab.id); setIsOpen(false); }}
            className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200 font-medium ${
              currentTab === tab.id
                ? 'bg-blue-600/10 text-blue-400 border border-blue-500/20'
                : 'hover:bg-slate-800/50 hover:text-white border border-transparent'
            }`}
          >
            {tab.icon}
            {tab.label}
          </button>
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
