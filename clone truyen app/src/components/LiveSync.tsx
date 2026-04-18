"use client";

import { useEffect } from 'react';
import { useStore } from '../store/useStore';

export function LiveSync() {
  useEffect(() => {
    // Polling interval 3 giây
    const interval = setInterval(async () => {
      try {
        const res = await fetch('/api/db');
        if (!res.ok) return;
        const json = await res.json();
        
        if (json.success && json.data) {
          // Lấy dữ liệu Local hiện tại
          const localState = useStore.getState();
          const serverState = json.data;

          // Ngắt mạch đồng bộ draftSpaces nếu người dùng ĐANG GÕ phím trên TextBox/Input
          const activeEl = document.activeElement;
          const isTyping = activeEl && (activeEl.tagName === 'INPUT' || activeEl.tagName === 'TEXTAREA');

          // Merge server vào local
          if (JSON.stringify(localState.queue) !== JSON.stringify(serverState.queue) ||
              localState.isAutoPilotRunning !== serverState.isAutoPilotRunning ||
              (!isTyping && JSON.stringify(localState.draftSpaces) !== JSON.stringify(serverState.draftSpaces))) {
            
            // Chỉ merge queue/draftSpaces từ server, KHÔNG đụng đến API keys
            useStore.setState({
              queue: serverState.queue || [],
              isAutoPilotRunning: serverState.isAutoPilotRunning || false,
              apiLogs: serverState.apiLogs || localState.apiLogs || [],
              draftSpaces: isTyping ? localState.draftSpaces : (serverState.draftSpaces || localState.draftSpaces || {}),
              // Keys luôn lấy từ local (không sync từ server)
              geminiKey: localState.geminiKey,
              geminiKey2: localState.geminiKey2,
              geminiKey3: localState.geminiKey3,
              geminiPaidKey: localState.geminiPaidKey,
              openAIKey: localState.openAIKey,
              grokKey: localState.grokKey,
              claudeKey: localState.claudeKey,
              wpUrl: localState.wpUrl,
              wpUser: localState.wpUser,
              wpAppPassword: localState.wpAppPassword,
            });
          }
        }
      } catch (error) {
        // Đứt mạng thì bỏ qua, đợi nhịp sau
      }
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  return null;
}
