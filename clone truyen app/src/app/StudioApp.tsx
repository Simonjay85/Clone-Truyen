"use client";

import React, { useState } from 'react';
import { Sidebar } from '../components/Sidebar';
import { GeminiDramaView } from '../components/GeminiDramaView';
import { MicroDramaView } from '../components/MicroDramaView';
import { GrokDramaView } from '../components/GrokDramaView';
import { ClaudeDramaView } from '../components/ClaudeDramaView';
import { QwenDramaView } from '../components/QwenDramaView';
import { ComboEconomicView } from '../components/ComboEconomicView';
import { ComboRoyalView } from '../components/ComboRoyalView';
import { ChapterSplitterView } from '../components/ChapterSplitterView';
import { AutoPilotView } from '../components/AutoPilotView';
import { SettingsView } from '../components/SettingsView';
import { ApiKeysView } from '../components/ApiKeysView';
import { FinalReviewView } from '../components/FinalReviewView';
import { SocialStudioView } from '../components/SocialStudioView';

export default function StudioApp() {
  const [activeTab, setActiveTab] = useState('gemini_drama');

  return (
    <div className="flex flex-col md:flex-row h-screen bg-[#0f0f17] text-slate-200 overflow-hidden font-sans selection:bg-indigo-500/30">
      <Sidebar currentTab={activeTab} setTab={setActiveTab} />
      
      <main className="flex-1 overflow-y-auto relative custom-scrollbar bg-[#0f0f17]">
        <div className="relative z-10 w-full h-full">
          <div className={activeTab === 'gemini_drama' ? 'block w-full h-full' : 'hidden'}><GeminiDramaView onNavigate={setActiveTab} /></div>
          <div className={activeTab === 'micro_drama' ? 'block w-full h-full' : 'hidden'}><MicroDramaView onNavigate={setActiveTab} /></div>
          <div className={activeTab === 'grok_drama' ? 'block w-full h-full' : 'hidden'}><GrokDramaView onNavigate={setActiveTab} /></div>
          <div className={activeTab === 'claude_drama' ? 'block w-full h-full' : 'hidden'}><ClaudeDramaView onNavigate={setActiveTab} /></div>
          <div className={activeTab === 'qwen_drama' ? 'block w-full h-full' : 'hidden'}><QwenDramaView onNavigate={setActiveTab} /></div>
          <div className={activeTab === 'combo_eco' ? 'block w-full h-full' : 'hidden'}><ComboEconomicView onNavigate={setActiveTab} /></div>
          <div className={activeTab === 'combo_royal' ? 'block w-full h-full' : 'hidden'}><ComboRoyalView onNavigate={setActiveTab} /></div>
          <div className={activeTab === 'chapter_splitter' ? 'block w-full h-full px-8' : 'hidden'}><ChapterSplitterView /></div>
          <div className={activeTab === 'autopilot' ? 'block w-full h-full px-8' : 'hidden'}><AutoPilotView /></div>
          <div className={activeTab === 'final_review' ? 'block w-full h-full px-8' : 'hidden'}><FinalReviewView /></div>
          <div className={activeTab === 'social_studio' ? 'block w-full h-full px-8' : 'hidden'}><SocialStudioView /></div>
          <div className={activeTab === 'logs' ? 'block w-full h-full px-8' : 'hidden'}>
            <div className="py-20 flex flex-col items-center text-slate-500">
               <span className="text-4xl mb-4">🖥️</span>
               <p>Terminal Logs Area (Trống - Server chưa chạy thật)</p>
            </div>
          </div>
          <div className={activeTab === 'settings' ? 'block w-full h-full px-8' : 'hidden'}><SettingsView /></div>
          <div className={activeTab === 'apikeys' ? 'block w-full h-full px-8' : 'hidden'}><ApiKeysView /></div>
        </div>
      </main>
    </div>
  );
}
