import os

path = "src/components/SettingsView.tsx"
with open(path, "r") as f: c = f.read()

# I will replace the main render of SettingsView
# Find "return ("
idx = c.find("return (")

ui = """
  const { apiLogs = [], clearApiLogs } = useStore();
  const totalCost = apiLogs.reduce((acc, log) => acc + (log.cost || 0), 0);
  const totalTokens = apiLogs.reduce((acc, log) => acc + (log.totalTokens || 0), 0);
  
  const modelStats = apiLogs.reduce((acc: any, log) => {
      acc[log.model] = (acc[log.model] || 0) + log.cost;
      return acc;
  }, {});
  const topModel = Object.keys(modelStats).sort((a,b) => modelStats[b] - modelStats[a])[0] || "None";
  
  const [activeTab, setActiveTab] = React.useState('dashboard');

  return (
    <div className="max-w-7xl mx-auto py-10 animation-fade-in flex flex-col h-[calc(100vh-80px)] px-4">
      <div className="mb-8 flex justify-between items-end flex-shrink-0">
        <div>
          <h2 className="text-3xl font-bold bg-gradient-to-r from-orange-500 to-rose-500 bg-clip-text text-transparent tracking-tight">Trạm Kế Toán API</h2>
          <p className="text-slate-400 mt-2">Dữ liệu Token và biểu giá (Tương đối theo niêm yết API Mĩ).</p>
        </div>
        <div className="flex gap-2">
            <button onClick={() => setActiveTab('dashboard')} className={`px-4 py-2 rounded-xl text-sm font-bold ${activeTab==='dashboard'? 'bg-rose-500/20 text-rose-400 border-rose-500/40' : 'bg-slate-800 text-slate-400'} border`}>📊 Dashboard Quota</button>
            <button onClick={() => setActiveTab('keys')} className={`px-4 py-2 rounded-xl text-sm font-bold ${activeTab==='keys'? 'bg-blue-500/20 text-blue-400 border-blue-500/40' : 'bg-slate-800 text-slate-400'} border`}>🔑 Cấu Hình Keys</button>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto space-y-8 custom-scrollbar pr-2 pb-20">
        {activeTab === 'dashboard' && (
           <div className="space-y-6">
              {/* TOP METRICS */}
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                 <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl relative overflow-hidden group">
                    <div className="absolute top-0 right-0 w-32 h-32 bg-emerald-500/10 rounded-full blur-3xl group-hover:bg-emerald-500/20 transition-all"></div>
                    <h4 className="text-slate-400 text-sm font-bold uppercase tracking-wider mb-2">Tổng Tổn Thất</h4>
                    <div className="text-4xl font-black text-emerald-400">${totalCost.toFixed(5)}</div>
                 </div>
                 <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl relative overflow-hidden group">
                    <div className="absolute top-0 right-0 w-32 h-32 bg-purple-500/10 rounded-full blur-3xl group-hover:bg-purple-500/20 transition-all"></div>
                    <h4 className="text-slate-400 text-sm font-bold uppercase tracking-wider mb-2">Tổng Tokens Đã Nạp</h4>
                    <div className="text-4xl font-black text-purple-400">{totalTokens.toLocaleString()}</div>
                 </div>
                 <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl relative overflow-hidden group">
                    <div className="absolute top-0 right-0 w-32 h-32 bg-amber-500/10 rounded-full blur-3xl group-hover:bg-amber-500/20 transition-all"></div>
                    <h4 className="text-slate-400 text-sm font-bold uppercase tracking-wider mb-2">Mô Hình Khát Máu Nhất</h4>
                    <div className="text-4xl font-black text-amber-400 truncate">{topModel}</div>
                 </div>
              </div>

              {/* TABLE */}
              <div className="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden flex flex-col">
                 <div className="p-4 border-b border-slate-800 flex justify-between items-center bg-slate-950">
                    <h3 className="font-bold tracking-wide text-rose-400">📜 Sổ Sao Kê Chi Tiết (1500 Gọi Gần Nhất)</h3>
                    <button onClick={() => confirm('Xóa sạch sổ?') && clearApiLogs()} className="text-xs bg-red-500/10 text-red-400 px-3 py-1.5 rounded uppercase font-bold hover:bg-red-500/20">Xóa Lịch Sử</button>
                 </div>
                 <div className="overflow-x-auto max-h-[500px]">
                    <table className="w-full text-left text-sm text-slate-300">
                       <thead className="bg-slate-900 text-slate-400 sticky top-0 z-10 shadow-md">
                          <tr>
                             <th className="px-4 py-3 font-medium">Thời Gian</th>
                             <th className="px-4 py-3 font-medium">Model</th>
                             <th className="px-4 py-3 font-medium text-right">Tokens (In/Out)</th>
                             <th className="px-4 py-3 font-medium text-right">Chi Phí</th>
                          </tr>
                       </thead>
                       <tbody className="divide-y divide-slate-800 flex-1">
                          {apiLogs.length === 0 ? (
                            <tr><td colSpan={4} className="px-4 py-8 text-center text-slate-500">Chưa có giao dịch API nào.</td></tr>
                          ) : apiLogs.map((l: any) => (
                             <tr key={l.id} className="hover:bg-slate-800/50 transition-colors">
                                <td className="px-4 py-3 font-mono text-xs">{new Date(l.timestamp).toLocaleTimeString()}</td>
                                <td className="px-4 py-3 font-bold text-rose-300">{l.model}</td>
                                <td className="px-4 py-3 text-right font-mono text-xs text-slate-400">{l.promptTokens} / {l.completionTokens} <span className="text-white bg-slate-800 px-1 rounded">{l.totalTokens}</span></td>
                                <td className="px-4 py-3 text-right font-bold text-emerald-400">${(l.cost || 0).toFixed(6)}</td>
                             </tr>
                          ))}
                       </tbody>
                    </table>
                 </div>
              </div>
           </div>
        )}

        <div className={activeTab === 'keys' ? 'block' : 'hidden'}>
           {/* OLD SETTINGS RESTORED */}
"""
    
ui_footer = """
        </div>
      </div>
    </div>
  );
"""

new_content = c[:idx] + ui + c[idx+8:].replace("</form>\n    </div>\n  );\n}", "</form>\n" + ui_footer)

with open(path, "w") as f: f.write(new_content)

