import Link from "next/link";

export default async function ChapterDetail({ params }: { params: Promise<{ slug: string }> }) {
  const resolvedParams = await params;
  // 1. Fetch chapter data
  const res = await fetch(`${process.env.NEXT_PUBLIC_WP_API_URL}/chuong?slug=${resolvedParams.slug}`);
  if (!res.ok) {
    return <div className="p-8 text-center bg-[#fdfaf6] min-h-screen">Lỗi máy chủ WP API!</div>;
  }
  
  const data = await res.json();
  if (!data || data.length === 0) {
    return <div className="p-8 text-center bg-[#fdfaf6] min-h-screen">Không tìm thấy chương này!</div>;
  }

  const chapter = data[0];

  // Strip Facebook group gate from WP content
  let cleanContent = (chapter.content.rendered || '')
    .replace(/<div[^>]*class="[^"]*facebook[^"]*"[^>]*>[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/gi, '')
    .replace(/<div[^>]*>[\s\S]*?Tham gia nhóm Facebook[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/gi, '')
    .replace(/<div[^>]*>[\s\S]*?Nhóm Facebook chưa được cấu hình[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/gi, '');

  return (
    <main className="min-h-screen bg-[#fdfaf6] p-4 md:p-8 font-serif leading-relaxed">
      {/* CSS fallback to hide any remaining Facebook gate elements */}
      <style dangerouslySetInnerHTML={{ __html: `
        .prose div:has(> p:only-child) { }
        .prose [class*="facebook"], 
        .prose [id*="facebook"],
        .prose [class*="fb-gate"],
        .prose [class*="content-gate"],
        .prose [class*="read-more-gate"] { display: none !important; }
      `}} />
      <div className="max-w-3xl mx-auto">
        <Link href="/" className="inline-flex items-center text-[#8b5a2b] hover:text-[#3e3124] mb-8 font-sans font-medium">
          ← Về Trang chủ
        </Link>
        
        <div className="bg-white p-8 md:p-12 rounded-xl shadow-sm border border-[#eee4d9]">
          <h1 className="text-3xl md:text-4xl font-bold text-[#3e3124] mb-8 text-center leading-tight" dangerouslySetInnerHTML={{ __html: chapter.title.rendered }} />
          
          <div className="flex justify-center gap-4 mb-10 font-sans border-y border-[#eee4d9] py-4">
             <button className="bg-[#fcf9f2] text-[#8b5a2b] px-4 py-2 rounded font-medium border border-[#eee4d9] hover:bg-[#eee4d9] transition opacity-50 cursor-not-allowed">Chương Trước</button>
             <button className="bg-[#8b5a2b] text-white px-4 py-2 rounded font-medium shadow-md hover:bg-[#6e4620] transition">Chương Sau</button>
          </div>

          <div 
             className="prose prose-lg md:prose-xl text-[#3e3124] mx-auto max-w-none text-justify [&>p]:mb-6"
             dangerouslySetInnerHTML={{ __html: cleanContent }} 
          />

          <div className="flex justify-center gap-4 mt-12 font-sans border-t border-[#eee4d9] pt-6">
             <button className="bg-[#fcf9f2] text-[#8b5a2b] px-4 py-2 rounded font-medium border border-[#eee4d9] hover:bg-[#eee4d9] transition opacity-50 cursor-not-allowed">Chương Trước</button>
             <button className="bg-[#8b5a2b] text-white px-4 py-2 rounded font-medium shadow-md hover:bg-[#6e4620] transition">Chương Sau</button>
          </div>
        </div>
      </div>
    </main>
  );
}
