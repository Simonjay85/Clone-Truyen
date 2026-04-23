"use client";

import { useEffect } from 'react';
import { useStore } from '../store/useStore';

export function LiveSync() {
  useEffect(() => {
    // Retry helper: thử lại tối đa maxRetries lần với delay ms giữa mỗi lần
    const fetchWithRetry = async (maxRetries = 2, delay = 500): Promise<Response | null> => {
      for (let i = 0; i <= maxRetries; i++) {
        try {
          const res = await fetch('/api/db', { cache: 'no-store' });
          if (res.ok) return res;
          // Nếu 500 và còn lượt retry, đợi rồi thử lại (tránh race condition khi engine đang ghi)
          if (i < maxRetries) await new Promise(r => setTimeout(r, delay * (i + 1)));
        } catch {
          if (i < maxRetries) await new Promise(r => setTimeout(r, delay * (i + 1)));
        }
      }
      return null; // Hết retry mà vẫn lỗi → bỏ qua lần poll này, không spam console
    };

    const pullData = async () => {
      try {
        const res = await fetchWithRetry(2, 400);
        if (!res) return; // Lỗi tạm thời → bỏ qua, không log để tránh spam

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
        // Chỉ log lỗi mạng thật sự (không phải lỗi 500 tạm thời)
        console.error("Lỗi đứt mạng hoặc NextJS compile error:", error);
      }
    };

    // Pull data ngay lập tức khi load app thay vì đợi 3s
    pullData();

    // Polling interval 5 giây (tăng từ 3s để giảm xung đột write/read)
    const interval = setInterval(pullData, 5000);

    return () => clearInterval(interval);
  }, []);

  return null;
}
