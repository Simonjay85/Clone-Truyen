"use client";

import { useEffect } from 'react';
import { useStore } from '../store/useStore';

export function LiveSync() {
  useEffect(() => {
    const pullData = async () => {
      try {
        const res = await fetch('/api/db', { cache: 'no-store' });
        if (!res.ok) {
           useStore.setState({ hasHydrated: true });
           return;
        }
        const json = await res.json();
        
        if (json.success) {
          const localState = useStore.getState();
          const serverState = json.data || {};

          // Ngắt mạch đồng bộ draftSpaces nếu người dùng ĐANG GÕ phím trên TextBox/Input
          const activeEl = document.activeElement;
          const isTyping = activeEl && (activeEl.tagName === 'INPUT' || activeEl.tagName === 'TEXTAREA');

          // Merge server vào local (luôn update hasHydrated = true sau khi pull thành công mẻ đầu)
          useStore.setState({
              queue: serverState.queue || [],
              isAutoPilotRunning: serverState.isAutoPilotRunning || false,
              apiLogs: serverState.apiLogs || localState.apiLogs || [],
              draftSpaces: isTyping ? localState.draftSpaces : (serverState.draftSpaces || localState.draftSpaces || {}),
              hasHydrated: true,
          });
        } else {
           useStore.setState({ hasHydrated: true });
        }
      } catch (error) {
        // Đứt mạng thì bỏ qua, đợi nhịp sau, nhưng cũng mở chốt hydrate để Local thay thế nếu cần thiết
        if (!useStore.getState().hasHydrated) useStore.setState({ hasHydrated: true });
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
