"use client";

import { useEffect } from 'react';
import { useStore } from '../store/useStore';

export function LiveSync() {
  useEffect(() => {
    const pullData = async () => {
      try {
        const res = await fetch('/api/db', { cache: 'no-store' });
        if (!res.ok) {
           console.error("Lỗi fetch DB: DB timeout hoặc lỗi 500");
           return;
        }
        const json = await res.json();
        
        if (json.success) {
          const localState = useStore.getState();
          const serverState = json.data || {};

          // Ngắt mạch đồng bộ draftSpaces nếu người dùng ĐANG GÕ phím trên TextBox/Input
          const activeEl = document.activeElement;
          const isTyping = activeEl && (activeEl.tagName === 'INPUT' || activeEl.tagName === 'TEXTAREA');

          const isQueueNewer = (localState.queue?.length || 0) > (serverState.queue?.length || 0);
          const isLogsNewer = (localState.apiLogs?.length || 0) > (serverState.apiLogs?.length || 0);

          // Merge server vào local (luôn update hasHydrated = true sau khi pull thành công mẻ đầu)
          useStore.setState({
              queue: isQueueNewer ? localState.queue : (serverState.queue || []),
              isAutoPilotRunning: serverState.isAutoPilotRunning || false,
              apiLogs: isLogsNewer ? localState.apiLogs : (serverState.apiLogs || localState.apiLogs || []),
              draftSpaces: isTyping ? localState.draftSpaces : (serverState.draftSpaces || localState.draftSpaces || {}),
              hasHydrated: true,
          });
        }
      } catch (error) {
        console.error("Lỗi đứt mạng hoặc NextJS compile error:", error);
      }
    };

    // Pull data ngay lập tức khi load app thay vì đợi 3s
    pullData();

    // Polling interval 3 giây
    const interval = setInterval(pullData, 3000);

    return () => clearInterval(interval);
  }, []);

  return null;
}
