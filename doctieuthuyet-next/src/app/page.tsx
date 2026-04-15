import Image from "next/image";
import Link from "next/link";

export const revalidate = 60; // Thử nghiệm ISR caching - Tự động tạo lại trang tĩnh mỗi 60 giây

export default async function Home() {
  const wpApiURL = process.env.NEXT_PUBLIC_WP_API_URL;

  // Gọi song song 5 luồng API để hiển thị giao diện đa mục
  const [heroRes, newRes, hotRes, fullRes, bxhRes] = await Promise.all([
    fetch(`${wpApiURL}/truyen?per_page=1&_embed`, { cache: 'no-store' }),
    fetch(`${wpApiURL}/truyen?per_page=8&_embed`, { cache: 'no-store' }),
    fetch(`${wpApiURL}/truyen?per_page=4&page=2&_embed`, { cache: 'no-store' }),
    fetch(`${wpApiURL}/truyen?per_page=4&page=3&_embed`, { cache: 'no-store' }),
    fetch(`${wpApiURL}/truyen?per_page=10&page=4&_embed`, { cache: 'no-store' }),
  ]);

  const [heroStories, newStories, hotStories, fullStories, bxhStories] = await Promise.all([
    heroRes.ok ? heroRes.json() : [],
    newRes.ok ? newRes.json() : [],
    hotRes.ok ? hotRes.json() : [],
    fullRes.ok ? fullRes.json() : [],
    bxhRes.ok ? bxhRes.json() : [],
  ]);

  const heroStory = heroStories.length > 0 ? heroStories[0] : null;

  const getImg = (story: any) => story?._embedded?.['wp:featuredmedia']?.[0]?.source_url || 'https://via.placeholder.com/300x400?text=No+Cover';
  const sanitizeHtml = (html: string) => html ? html.replace(/<[^>]*>?/gm, '').substring(0, 150) + '...' : "";

  return (
    <main className="min-h-screen bg-[#f3f4f6] font-sans pb-10">
      <div className="max-w-[1200px] mx-auto pt-6 px-4">
        
        {/* HERO BANNER */}
        {heroStory && (
          <div className="bg-white rounded-2xl p-5 shadow-[0_2px_12px_rgba(0,0,0,0.06)] mb-8 flex flex-col md:flex-row gap-5 items-start">
            <div className="w-full md:w-[180px] shrink-0 rounded-2xl overflow-hidden aspect-[3/4] relative">
              <Image src={getImg(heroStory)} alt={heroStory.title.rendered} fill className="object-cover" sizes="180px" />
            </div>
            <div className="flex-1 min-w-0">
              <h2 className="text-[22px] font-extrabold text-[#111827] leading-snug mb-2" dangerouslySetInnerHTML={{ __html: heroStory.title.rendered }} />
              <div className="text-[12px] text-[#9ca3af] mb-3 flex items-center gap-2">
                <span className="bg-[#eef2ff] text-[#4f46e5] border border-[#c7d2fe] px-2 py-[2px] rounded-full font-bold">MỚI XUẤT BẢN</span>
                <span>📅 Vài giờ trước</span>
              </div>
              <p className="text-[13px] text-[#6b7280] leading-[1.7] mb-4 line-clamp-3" dangerouslySetInnerHTML={{ __html: sanitizeHtml(heroStory.content?.rendered || '') }} />
              <div className="flex gap-2">
                <Link href={`/chuong/mo-dau`} className="bg-[#4f46e5] hover:bg-[#4338ca] text-white px-5 py-2 rounded-xl text-[13px] font-bold shadow-[0_2px_8px_rgba(79,70,229,0.25)] transition">📖 Đọc ngay</Link>
                <Link href={`/truyen/${heroStory.slug}`} className="bg-[#f4f4f5] hover:bg-[#e4e4e7] text-[#374151] px-5 py-2 rounded-xl text-[13px] font-bold transition">Danh sách chương</Link>
              </div>
            </div>
          </div>
        )}

        {/* MAIN LAYOUT */}
        <div className="flex flex-col lg:flex-row gap-6 items-start">
          
          {/* CỘT TRÁI (MAIN) */}
          <div className="flex-1 min-w-0 w-full">
            
            {/* 1. MỚI CẬP NHẬT */}
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-[17px] font-extrabold text-[#111827] flex items-center gap-2">
                <span className="text-[#4f46e5]">⚡</span> Mới cập nhật
              </h2>
              <Link href="#" className="text-[13px] text-[#4f46e5] font-semibold hover:underline">Xem tất cả →</Link>
            </div>
            <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3 mb-8">
              {newStories.map((story: any) => (
                <Link href={`/truyen/${story.slug}`} key={story.id} className="group bg-white rounded-2xl overflow-hidden shadow-[0_1px_4px_rgba(0,0,0,0.06)] hover:shadow-[0_6px_20px_rgba(0,0,0,0.12)] hover:-translate-y-0.5 transition-all block">
                  <div className="relative aspect-[3/2] overflow-hidden">
                    <span className="absolute top-2 left-2 bg-[#10b981] text-white text-[10px] font-bold px-1.5 py-0.5 rounded-md z-10">MỚI</span>
                    <Image src={getImg(story)} alt={story.title.rendered} fill className="object-cover group-hover:scale-105 transition-transform duration-300" sizes="(max-width: 768px) 50vw, 25vw" />
                    <div className="absolute inset-x-0 bottom-0 pt-5 pb-2 px-2 bg-gradient-to-t from-black/80 to-transparent text-white text-[11px] flex justify-between z-10">
                      <span>✓ Ch.{Math.floor(Math.random() * 150) + 10}</span>
                      <span className="text-[#fbbf24]">{Math.floor(Math.random() * 24) + 1}h trước</span>
                    </div>
                  </div>
                  <div className="p-2.5 pb-3">
                    <p className="text-[13px] font-bold text-[#111827] line-clamp-2 leading-[1.4] mb-1" dangerouslySetInnerHTML={{ __html: story.title.rendered }} />
                    <div className="flex justify-between items-center mt-2">
                      <span className="text-[11px] text-[#9ca3af] font-medium">👁 {Math.floor(Math.random() * 10000)}</span>
                      <span className="text-[10px] text-[#4f46e5] bg-[#4f46e5]/10 border border-[#4f46e5]/20 px-2 py-1 rounded-md font-bold">Chương mới</span>
                    </div>
                  </div>
                </Link>
              ))}
            </div>

            {/* 2. TRUYỆN HOT */}
            <div className="flex justify-between items-center mb-4 mt-8">
              <h2 className="text-[17px] font-extrabold text-[#111827] flex items-center gap-2">
                <span className="text-[#ef4444]">🔥</span> Truyện hot
              </h2>
              <Link href="#" className="text-[13px] text-[#4f46e5] font-semibold hover:underline">Xem tất cả →</Link>
            </div>
            <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3 mb-8">
              {hotStories.map((story: any) => (
                <Link href={`/truyen/${story.slug}`} key={story.id} className="group bg-white rounded-2xl overflow-hidden shadow-[0_1px_4px_rgba(0,0,0,0.06)] hover:shadow-[0_6px_20px_rgba(0,0,0,0.12)] hover:-translate-y-0.5 transition-all block">
                  <div className="relative aspect-[3/2] overflow-hidden">
                    <span className="absolute top-2 right-2 bg-[#ef4444] text-white text-[10px] font-bold px-1.5 py-0.5 rounded-md z-10">HOT 🔥</span>
                    <Image src={getImg(story)} alt={story.title.rendered} fill className="object-cover group-hover:scale-105 transition-transform duration-300" sizes="(max-width: 768px) 50vw, 25vw" />
                    <div className="absolute inset-x-0 bottom-0 pt-5 pb-2 px-2 bg-gradient-to-t from-black/80 to-transparent text-white text-[11px] flex justify-between z-10">
                      <span>✓ Ch.{Math.floor(Math.random() * 150) + 150}</span>
                      <span className="text-[#fbbf24]">{Math.floor(Math.random() * 24) + 1}h trước</span>
                    </div>
                  </div>
                  <div className="p-2.5 pb-3">
                    <p className="text-[13px] font-bold text-[#111827] line-clamp-2 leading-[1.4] mb-1" dangerouslySetInnerHTML={{ __html: story.title.rendered }} />
                    <div className="flex justify-between items-center mt-2">
                      <span className="text-[11px] text-[#9ca3af] font-medium">👁 {Math.floor(Math.random() * 50000)}</span>
                      <span className="text-[10px] text-[#ef4444] bg-[#ef4444]/10 border border-[#ef4444]/20 px-2 py-1 rounded-md font-bold">Đang Hot</span>
                    </div>
                  </div>
                </Link>
              ))}
            </div>

            {/* 3. TRUYỆN FULL */}
            <div className="flex justify-between items-center mb-4 mt-8">
              <h2 className="text-[17px] font-extrabold text-[#111827] flex items-center gap-2">
                <span className="text-[#10b981]">✔</span> Truyện full
              </h2>
              <Link href="#" className="text-[13px] text-[#4f46e5] font-semibold hover:underline">Xem tất cả →</Link>
            </div>
            <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3 mb-8">
              {fullStories.map((story: any) => (
                <Link href={`/truyen/${story.slug}`} key={story.id} className="group bg-white rounded-2xl overflow-hidden shadow-[0_1px_4px_rgba(0,0,0,0.06)] hover:shadow-[0_6px_20px_rgba(0,0,0,0.12)] hover:-translate-y-0.5 transition-all block">
                  <div className="relative aspect-[3/2] overflow-hidden">
                    <span className="absolute top-2 right-2 bg-[#e11d48] text-white text-[10px] font-bold px-1.5 py-0.5 rounded-md z-10">FULL</span>
                    <Image src={getImg(story)} alt={story.title.rendered} fill className="object-cover group-hover:scale-105 transition-transform duration-300" sizes="(max-width: 768px) 50vw, 25vw" />
                    <div className="absolute inset-x-0 bottom-0 pt-5 pb-2 px-2 bg-gradient-to-t from-black/80 to-transparent text-white text-[11px] flex justify-between z-10">
                      <span>✓ Ch.{Math.floor(Math.random() * 500) + 200}</span>
                      <span className="text-[#10b981]">Đã đủ bộ</span>
                    </div>
                  </div>
                  <div className="p-2.5 pb-3">
                    <p className="text-[13px] font-bold text-[#111827] line-clamp-2 leading-[1.4] mb-1" dangerouslySetInnerHTML={{ __html: story.title.rendered }} />
                    <div className="flex justify-between items-center mt-2">
                      <span className="text-[11px] text-[#9ca3af] font-medium">👁 {Math.floor(Math.random() * 99999)}</span>
                      <span className="text-[10px] text-[#10b981] bg-[#10b981]/10 border border-[#10b981]/20 px-2 py-1 rounded-md font-bold">Hoàn thành</span>
                    </div>
                  </div>
                </Link>
              ))}
            </div>

          </div>

          {/* CỘT PHẢI (SIDEBAR) */}
          <div className="w-full lg:w-[280px] shrink-0 sticky top-4 lg:max-h-[calc(100vh-2rem)] flex flex-col gap-6">
            
            {/* BXH */}
            <div className="bg-white rounded-[20px] p-5 border border-[#f3f4f6] shadow-[0_4px_20px_rgba(0,0,0,0.02)]">
              <h3 className="flex justify-between items-center mb-4 pb-3 border-b border-[#f9fafb]">
                <span className="text-[16px] font-extrabold text-[#111827] flex items-center gap-2"><span className="text-[#ea580c]">🏆</span> Bảng xếp hạng</span>
                <span className="text-[11px] text-[#9ca3af] font-medium">Top 10</span>
              </h3>
              
              <div className="flex justify-between bg-[#f4f4f5] p-1 rounded-xl mb-4">
                <div className="bg-white text-[#4f46e5] text-[12px] font-bold px-4 py-1.5 rounded-lg shadow-sm">Ngày</div>
                <div className="text-[#6b7280] text-[12px] font-semibold px-3 py-1.5">Tuần</div>
                <div className="text-[#6b7280] text-[12px] font-semibold px-3 py-1.5">Tháng</div>
              </div>

              <div className="flex flex-col gap-2">
                {bxhStories.slice(0, 10).map((story: any, i: number) => {
                  const rank = i + 1;
                  const isTop1 = rank === 1;
                  const isTop2 = rank === 2;
                  const isTop3 = rank === 3;
                  const views = Math.floor(Math.random() * 50000) + 10000 - (i * 2000);
                  
                  if (rank <= 3) {
                    const badgeColors = isTop1 ? 'from-[#fcd34d] to-[#d97706] border-white shadow-[#d97706]/30' : 
                                        isTop2 ? 'from-[#e5e7eb] to-[#6b7280] border-white shadow-[#6b7280]/30' : 
                                                 'from-[#fdba74] to-[#c2410c] border-white shadow-[#c2410c]/30';
                    const boxColors = isTop1 ? 'bg-white border-[#fde047] shadow-[#fde047]/15' :
                                      isTop2 ? 'bg-white border-[#e5e7eb] shadow-black/5' :
                                               'bg-white border-[#fed7aa] shadow-[#fed7aa]/15';
                    
                    return (
                      <Link href={`/truyen/${story.slug}`} key={story.id} className={`flex items-center gap-3 p-2.5 rounded-xl border transition-transform hover:translate-x-1 ${boxColors}`}>
                        <div className="relative w-7 h-7 flex items-center justify-center shrink-0">
                          <div className={`relative w-[22px] h-[22px] bg-gradient-to-br ${badgeColors} rounded-full flex items-center justify-center text-white text-[11px] font-black border-[1.5px] z-10`}>{rank}</div>
                        </div>
                        <div className="w-9 h-[48px] relative shrink-0 rounded-md overflow-hidden"><Image src={getImg(story)} alt="cover" fill className="object-cover" /></div>
                        <div className="flex-1 min-w-0">
                          <p className={`text-[13px] font-bold ${isTop1 ? 'text-[#c2410c]' : isTop2 ? 'text-[#374151]' : 'text-[#c2410c]'} truncate mb-0.5`} dangerouslySetInnerHTML={{ __html: story.title.rendered }} />
                          <p className="text-[11px] text-[#9ca3af] font-medium flex items-center gap-1">👁 {views.toLocaleString()}</p>
                        </div>
                      </Link>
                    )
                  } else {
                    return (
                      <Link href={`/truyen/${story.slug}`} key={story.id} className="flex items-center gap-3 py-1.5 group">
                        <div className="w-7 text-center text-[15px] font-extrabold text-[#d1d5db] shrink-0 font-mono">{rank}</div>
                        <div className="w-8 h-[42px] relative shrink-0 rounded-md overflow-hidden"><Image src={getImg(story)} alt="cover" fill className="object-cover" /></div>
                        <div className="flex-1 min-w-0 flex flex-col justify-center">
                          <p className="text-[13px] font-semibold text-[#4b5563] truncate mb-2 group-hover:text-[#4f46e5]" dangerouslySetInnerHTML={{ __html: story.title.rendered }} />
                          <div className="flex items-center gap-3">
                            <div className="flex-1 h-1.5 bg-[#f3f4f6] rounded-full overflow-hidden">
                              <div className="h-full bg-[#818cf8]" style={{ width: `${Math.max(10, 100 - (i * 10))}%` }}></div>
                            </div>
                            <span className="text-[11px] text-[#9ca3af] w-8 text-right shrink-0">{views >= 1000 ? (views/1000).toFixed(1) + 'k' : views}</span>
                          </div>
                        </div>
                      </Link>
                    )
                  }
                })}
              </div>
            </div>

            {/* TEAM RANKING (MOCK UI) */}
            <div className="bg-white rounded-[20px] p-5 border border-[#f3f4f6] shadow-[0_4px_20px_rgba(0,0,0,0.02)]">
              <h3 className="flex justify-between items-center mb-4 pb-3 border-b border-[#f9fafb]">
                <span className="text-[16px] font-extrabold text-[#111827] flex items-center gap-2"><span className="text-[#a855f7]">🛡️</span> Bảng xếp hạng team</span>
              </h3>
              <div className="flex flex-col gap-2">
                {["Mèo Kam Mập", "Lạc Giới Tinh Thư", "Ổ Mật Mật"].map((team, idx) => (
                  <div key={idx} className="flex items-center gap-3 p-2 bg-[#f9fafb] rounded-xl border border-[#f3f4f6]">
                     <div className="w-[22px] h-[22px] bg-[#a855f7] rounded-full flex items-center justify-center text-white text-[11px] font-black">{idx + 1}</div>
                     <span className="text-[13px] font-bold text-[#374151] flex-1 truncate">{team}</span>
                     <span className="text-[11px] text-[#9ca3af] font-medium bg-white px-2 py-0.5 rounded shadow-sm">{Math.floor(Math.random() * 3000) + 1000} view</span>
                  </div>
                ))}
              </div>
            </div>

          </div>

        </div>

      </div>
    </main>
  );
}
