/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable @typescript-eslint/ban-ts-comment */
// @ts-nocheck
import React from 'react';
import { useStore } from '../store/useStore';
import { Globe, User, Lock, Settings } from 'lucide-react';

export function SettingsView() {
  const {
    wpUrl, wpUser, wpAppPassword, webhookUrl,
    setSettings 
  } = useStore();

  const [testResults, setTestResults] = React.useState<Record<string, string>>({});
  const [mounted, setMounted] = React.useState(false);

  React.useEffect(() => {
    setTimeout(() => setMounted(true), 0);
  }, []);

  const [wpTargetId, setWpTargetId] = React.useState('');
  const [wpCleanStatus, setWpCleanStatus] = React.useState('');
  
  const [wpOrphanId, setWpOrphanId] = React.useState('');
  const [wpOrphanStatus, setWpOrphanStatus] = React.useState('');

  const handleFixOrphans = async () => {
    if (!wpUrl || !wpUser || !wpAppPassword) return alert("Chưa kết nối WP!");
    if (!wpOrphanId) return alert("Vui lòng nhập ID Truyện Gốc (Parent ID)!");
    
    setWpOrphanStatus('⏳ Đang quét tìm các chương mồ côi gần đây trên server...');
    try {
        const fetchRes = await fetch('/api/wordpress', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            wpUrl, wpUser, wpAppPassword,
            endpoint: `chuong?per_page=100`, // quét 100 chương mới nhất
            method: 'GET'
          })
        });
        
        if (!fetchRes.ok) throw new Error('Fetch thất bại: ' + fetchRes.statusText);
        const data = await fetchRes.json();
        if (!Array.isArray(data)) throw new Error('Data không hợp lệ từ WordPress');

        // Lọc các chương mà _truyen_id đang trống hoặc chưa set
        const orphans = data.filter((c: any) => !c.meta || !c.meta._truyen_id || String(c.meta._truyen_id) === '0' || String(c.meta._truyen_id) === '');

        if (orphans.length === 0) return setWpOrphanStatus('✅ Tuyệt vời! Không tìm thấy chương nào bị mồ côi trong 100 chương mới nhất.');

        if (!confirm(`Phát hiện ${orphans.length} chương chưa có Truyện Gốc (mồ côi).\n\nVí dụ: ${orphans[0].title?.rendered}\n\nBạn có CHẮC CHẮN muốn nối TẤT CẢ bọn nó vào Truyện ID: ${wpOrphanId} không?`)) {
            return setWpOrphanStatus('⛔ Đã hủy lệnh.');
        }

        setWpOrphanStatus(`⏳ Đang hàn gắn ${orphans.length} chương vào Truyện ${wpOrphanId}...`);
        
        let successCount = 0;
        for (let i = 0; i < orphans.length; i++) {
           const updateRes = await fetch('/api/wordpress', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                wpUrl, wpUser, wpAppPassword,
                endpoint: `chuong/${orphans[i].id}`,
                method: 'POST',
                payload: {
                   meta: { _truyen_id: String(wpOrphanId) }
                }
              })
           });
           if (updateRes.ok) successCount++;
        }
        
        setWpOrphanStatus(`✅ Đã triệu hồi thành công ${successCount}/${orphans.length} chương lạc loài về với Truyện ID: ${wpOrphanId}! Ra F5 lại web kiểm tra nhé.`);
    } catch(e: any) {
        setWpOrphanStatus(`❌ Lỗi Nối Xương: ${e.message}`);
    }
  };

  const handleCleanMarkdown = async () => {
    if (!wpUrl || !wpUser || !wpAppPassword) return alert("Chưa kết nối WP!");
    if (!wpTargetId) return alert("Vui lòng nhập Truyện ID!");
    
    setWpCleanStatus('⏳ Đang quét server tìm các chương...');
    try {
      let allChapters: unknown[] = [];
      let page = 1;
      let hasMore = true;

      while (hasMore) {
        setWpCleanStatus(`⏳ Đang quét server tìm các chương... (Trang ${page})`);
        
        const fetchRes = await fetch('/api/wordpress', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            wpUrl, wpUser, wpAppPassword,
            endpoint: `chuong?per_page=100&page=${page}`,
            method: 'GET'
          })
        });
        
        if (!fetchRes.ok) {
           if (fetchRes.status === 400 || fetchRes.status === 404) { hasMore = false; break; } 
           throw new Error('Không thể fetch dữ liệu từ WP: ' + fetchRes.statusText);
        }
        
        const data = await fetchRes.json();
        if (!Array.isArray(data) || data.length === 0) {
           hasMore = false;
        } else {
           allChapters = [...allChapters, ...data];
           if (data.length < 100) {
             hasMore = false;
           } else {
             page++;
           }
        }
      }
      
      const targetChapters = allChapters.filter(c => c.meta && String(c.meta._truyen_id) === String(wpTargetId));

      if (targetChapters.length === 0) {
        return setWpCleanStatus('⚠️ Không tìm thấy chương nào cho ID này!');
      }

      setWpCleanStatus(`⏳ Đã tìm thấy ${targetChapters.length} chương của Truyện ${wpTargetId}. Đang giặt sạch bằng Omo Matic...`);
      let successCount = 0;

      for (let i = 0; i < targetChapters.length; i++) {
        const item = targetChapters[i];
        const originalContent = (item.content as any)?.raw || (item.content as any)?.rendered || '';
        
        if (originalContent.includes('**') || originalContent.includes('*') || originalContent.includes('```')) {
          let cleanedContent = originalContent.replace(/```markdown/gi, '').replace(/```/g, '');
          cleanedContent = cleanedContent.replace(/\*\*([\s\S]*?)\*\*/g, '<strong>$1</strong>').replace(/\*([\s\S]*?)\*/g, '<em>$1</em>');
          
          const updateRes = await fetch('/api/wordpress', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              wpUrl, wpUser, wpAppPassword,
              endpoint: `chuong/${(item as any).id}`,
              method: 'POST',
              payload: { content: cleanedContent }
            })
          });
          
          if (!updateRes.ok) {
             const errText = await updateRes.text();
             throw new Error(`Cập nhật chương ${(item as any).id} thất bại (${updateRes.status}): ${errText}`);
          }
          successCount++;
        }
      }

      setWpCleanStatus(`✅ Đã đập đi xây lại giặt sạch bong ${successCount}/${targetChapters.length} chương! Lên web kiểm tra ngay anh nhé!`);
    } catch (e: any) {
      setWpCleanStatus(`❌ Lỗi Máy Giặt: ${(e as any).message}`);
    }
  };

  const testWP = async () => {
    if (!wpUrl || !wpUser || !wpAppPassword) return alert('Chưa điền đầy đủ WP URL, Username, Password!');
    setTestResults(r => ({ ...r, wp: '⏳ Đang kiểm tra kết nối WordPress...' }));
    try {
      const res = await fetch('/api/wordpress', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          wpUrl, wpUser, wpAppPassword,
          endpoint: 'users/me',
          method: 'GET'
        })
      });
      const data = await res.json();
      if (res.ok && data.id) {
        setTestResults(r => ({ ...r, wp: `✅ Kết nối thành công! User: ${data.name} (ID: ${data.id})` }));
      } else {
        const msg = data.error || JSON.stringify(data);
        if (msg.includes('401') || msg.includes('rest_cannot_create') || msg.includes('rest_forbidden')) {
          setTestResults(r => ({ ...r, wp: '❌ Lỗi 401: Sai Username hoặc Application Password.' }));
        } else {
          setTestResults(r => ({ ...r, wp: `❌ Lỗi: ${String(msg).substring(0, 100)}` }));
        }
      }
    } catch {
      setTestResults(r => ({ ...r, wp: `❌ Không kết nối được tới ${wpUrl}` }));
    }
  };

  if (!mounted) return <div className="p-8 text-slate-500 font-medium h-full flex items-center justify-center">Đang nạp dữ liệu...</div>;

  return (
    <div className="max-w-4xl mx-auto py-10 animation-fade-in flex flex-col h-full px-4 border-none">
      <div className="mb-8 flex justify-between items-end flex-shrink-0">
        <div>
          <h2 className="text-3xl font-bold text-white tracking-tight flex items-center gap-3">
             <Settings className="text-slate-400" size={32} />
             Cài Đặt Hệ Thống
          </h2>
          <p className="text-slate-400 mt-2">Cấu hình kết nối WordPress, nền tảng xuất bản và các trạm vệ tinh.</p>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto space-y-8 custom-scrollbar pr-2 pb-20">
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-4">
          <h3 className="text-lg font-semibold text-white flex items-center gap-2 mb-4 border-b border-slate-800 pb-4">
            <Globe className="text-emerald-400" size={20} />
            Kết Nối Máy Chủ (WordPress REST API)
          </h3>
          
          <div>
            <label className="block text-sm font-medium text-slate-400 mb-2">WordPress URL</label>
            <input 
              type="url"
              value={wpUrl}
              onChange={(e) => setSettings({ wpUrl: e.target.value })}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-emerald-500 transition-all font-mono text-sm"
              placeholder="https://doctieuthuyet.com"
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="flex items-center gap-2 text-sm font-medium text-slate-400 mb-2">
                <User size={14} /> Username
              </label>
              <input 
                type="text"
                value={wpUser}
                onChange={(e) => setSettings({ wpUser: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-emerald-500 transition-all font-mono text-sm"
                placeholder="admin"
              />
            </div>
            <div>
              <label className="flex items-center gap-2 text-sm font-medium text-slate-400 mb-2">
                <Lock size={14} /> Application Password
              </label>
              <input 
                type="password"
                value={wpAppPassword}
                onChange={(e) => setSettings({ wpAppPassword: e.target.value })}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-emerald-500 transition-all font-mono text-sm shadow-inner"
                placeholder="xxxx xxxx xxxx xxxx"
              />
            </div>
          </div>
          <p className="text-xs text-slate-500 mt-2 italic">
            * Mật khẩu ứng dụng (Application Password) được tạo trong mục Users -{'>'} Profile của WordPress. Không lưu mật khẩu đăng nhập chính thức vào đây.
          </p>
          <div className="mt-4 flex items-center gap-3">
            <button onClick={testWP} className="bg-emerald-600 hover:bg-emerald-500 text-white font-bold py-2 px-4 rounded-lg text-sm transition-colors">
              🔌 Kiểm Tra Kết Nối WP
            </button>
            {testResults['wp'] && (
              <p className={`text-xs font-bold ${testResults['wp'].includes('✅') ? 'text-emerald-400' : testResults['wp'].includes('⏳') ? 'text-amber-400' : 'text-red-400'}`}>
                {testResults['wp']}
              </p>
            )}
          </div>
          
          <div className="pt-6 mt-6 border-t border-slate-800">
            <label className="block text-sm font-medium text-slate-400 mb-2 flex items-center gap-2">
              <Globe size={14} className="text-indigo-400" /> Webhook URL (Make.com / Zapier)
            </label>
            <input 
              type="url"
              value={webhookUrl}
              onChange={(e) => setSettings({ webhookUrl: e.target.value })}
              className="w-full bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-indigo-500 transition-all font-mono text-xs shadow-inner"
              placeholder="https://hook.us1.make.com/..."
            />
            <p className="text-xs text-slate-500 mt-2 italic">
              Để trống nếu anh định dùng tính năng Copy thủ công ở trang Social Studio. Dán link Webhook vào đây nếu anh muốn bấm 1 phát tự động bắn dữ liệu sang Make/Zapier để tự động đăng lên Insta/Pinterest.
            </p>
          </div>
        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-4">
          <h3 className="text-lg font-semibold text-white flex items-center gap-2 mb-4 border-b border-slate-800 pb-4">
            <span className="text-pink-400">🛠</span>
            Trạm Bảo Trì Chỉnh Hình WordPress (Markdown Washer)
          </h3>
          <p className="text-sm text-slate-400">
            Dành riêng cho những bộ truyện nhỡ đăng bị dính ký tự ngôi sao <strong className="text-pink-400">**In đậm**</strong>. Cỗ máy sẽ chui vào Server gọt dũa lại.
          </p>
          <div className="flex gap-4">
            <input 
              type="text"
              value={wpTargetId}
              onChange={(e) => setWpTargetId(e.target.value)}
              className="flex-1 bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-pink-500 transition-all font-mono text-sm"
              placeholder="Nhập ID Truyện (VD: 1421)"
            />
            <button 
              onClick={handleCleanMarkdown}
              className="bg-pink-600 hover:bg-pink-500 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition-colors whitespace-nowrap"
            >
              🫧 Tẩy Sạch Lỗi Markdown
            </button>
          </div>
          {wpCleanStatus && (
            <p className={`text-sm font-bold mt-2 ${wpCleanStatus.includes('✅') ? 'text-emerald-400' : wpCleanStatus.includes('❌') ? 'text-red-400' : 'text-amber-400'}`}>
              {wpCleanStatus}
            </p>
          )}

          <div className="pt-6 mt-6 border-t border-slate-800">
            <h3 className="text-lg font-semibold text-white flex items-center gap-2 mb-4">
              <span className="text-indigo-400">🧲</span>
              Trạm Cứu Hộ Chương Mồ Côi (Orphan Linker)
            </h3>
            <p className="text-sm text-slate-400 mb-4">
              Dành để sửa lỗi những chương truyện đăng lên Web bị Trống ở cột <strong className="text-indigo-400">&quot;Thuộc Truyện Gốc&quot;</strong>. Công cụ này sẽ quét các chương vô gia cư và tự động bắn mã Truyện Mẹ vào cho chúng nó nhận lại tổ tông.
            </p>
            <div className="flex gap-4">
              <input 
                type="text"
                value={wpOrphanId}
                onChange={(e) => setWpOrphanId(e.target.value)}
                className="flex-1 bg-slate-950 border border-slate-800 rounded-lg px-4 py-3 text-slate-300 focus:outline-none focus:border-indigo-500 transition-all font-mono text-sm"
                placeholder="Nhập ID Truyện Mẹ cần gắn vào (VD: 1363)"
              />
              <button 
                onClick={handleFixOrphans}
                className="bg-indigo-600 hover:bg-indigo-500 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition-colors whitespace-nowrap flex items-center gap-2"
              >
                🧲 Triệu Hồi Các Chương Lạc Loài
              </button>
            </div>
            {wpOrphanStatus && (
              <p className={`text-sm font-bold mt-2 ${wpOrphanStatus.includes('✅') ? 'text-emerald-400' : wpOrphanStatus.includes('❌') ? 'text-red-400' : 'text-amber-400'}`}>
                {wpOrphanStatus}
              </p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
