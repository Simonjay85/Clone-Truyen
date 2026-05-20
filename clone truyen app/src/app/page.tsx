'use client';

import dynamic from 'next/dynamic';

const StudioApp = dynamic(() => import('./StudioApp'), {
  ssr: false,
  loading: () => (
    <div className="min-h-screen bg-[#0f0f17] text-slate-300 flex items-center justify-center font-sans">
      <div className="text-sm font-semibold tracking-wide text-slate-500">Loading Story Studio...</div>
    </div>
  ),
});

export default function Home() {
  return <StudioApp />;
}
