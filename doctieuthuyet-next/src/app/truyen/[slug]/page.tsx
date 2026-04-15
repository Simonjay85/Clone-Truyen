import Link from "next/link";
import Image from "next/image";

export default async function StoryDetail({ params }: { params: Promise<{ slug: string }> }) {
  const resolvedParams = await params;
  
  // Fetch story detail from WP REST API (slug based)
  const res = await fetch(`${process.env.NEXT_PUBLIC_WP_API_URL}/truyen?slug=${resolvedParams.slug}&_embed`);
  
  if (!res.ok) {
    return <div className="p-8 text-center bg-[#fdfaf6] min-h-screen">Lỗi máy chủ WP API!</div>;
  }
  
  const data = await res.json();
  if (!data || data.length === 0) {
    return <div className="p-8 text-center bg-[#fdfaf6] min-h-screen">Không tìm thấy truyện!</div>;
  }

  const story = data[0];
  const thumbnailSrc = story._embedded?.['wp:featuredmedia']?.[0]?.source_url || 'https://via.placeholder.com/150x200?text=No+Cover';
  
  // Lấy danh sách chương (Giả lập lấy 50 chương mới nhất của truyện này)
  let chapters = [];
  try {
    // Note: Ở môi trường thật sẽ cần 1 API custom lọc theo _truyen_id
    // Tạm thời kéo chap mới về lọc:
    const chapRes = await fetch(`${process.env.NEXT_PUBLIC_WP_API_URL}/chuong?per_page=100`, { cache: 'no-store' });
    const allChaps = await chapRes.json();
    chapters = allChaps.filter((c: any) => c.meta?._truyen_id === story.id);
    
    // Nếu API không filter được _truyen_id, ta hiển thị tạm 10 chương mới nhất bất kỳ để Demo luồng click
    if(chapters.length === 0) {
        chapters = allChaps.slice(0, 10);
    }
  } catch (e) {}

  return (
    <main className="min-h-screen bg-[#fdfaf6] p-4 md:p-8 font-sans">
      <div className="max-w-4xl mx-auto space-y-6">
        <Link href="/" className="inline-flex items-center text-[#8b5a2b] hover:text-[#3e3124] font-medium">
          ← Trở về Kho Truyện
        </Link>
        
        <div className="bg-white p-6 rounded-xl shadow-sm border border-[#eee4d9] flex flex-col md:flex-row gap-8">
          <div className="w-full md:w-1/3">
            <div className="w-full rounded-lg overflow-hidden shadow-md bg-[#eee4d9]">
              <Image src={thumbnailSrc} alt={story.title.rendered} width={600} height={900} className="w-full h-auto aspect-[2/3] object-cover" />
            </div>
          </div>
          <div className="w-full md:w-2/3">
            <h1 className="text-3xl font-bold text-[#3e3124] mb-4" dangerouslySetInnerHTML={{ __html: story.title.rendered }} />
            
            <div className="flex gap-4 mb-6 relative z-10">
               {chapters.length > 0 && (
                 <Link href={`/chuong/${chapters[0].slug}`} className="bg-[#8b5a2b] text-white px-6 py-2 rounded-full font-medium hover:bg-[#6e4620] transition shadow-md shadow-[#8b5a2b]/20 inline-block text-center cursor-pointer">
                   Đọc Từ Đầu
                 </Link>
               )}
               <button className="bg-[#fcf9f2] text-[#8b5a2b] px-6 py-2 rounded-full font-medium border border-[#eee4d9] hover:bg-[#eee4d9] transition">Lưu Đánh Dấu</button>
            </div>
            
            <div className="prose prose-sm text-[#4a3f35]" dangerouslySetInnerHTML={{ __html: story.content.rendered }} />
          </div>
        </div>

        {/* Danh sách chương */}
        <div className="bg-white p-6 rounded-xl shadow-sm border border-[#eee4d9]">
           <h2 className="text-xl font-bold text-[#3e3124] mb-4 border-b border-[#eee4d9] pb-2">Danh sách chương</h2>
           <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
             {chapters.length > 0 ? chapters.map((chap: any, index: number) => (
                <Link 
                  href={`/chuong/${chap.slug}`} 
                  key={chap.id}
                  className="p-3 bg-[#fcf9f2] border border-[#eee4d9] rounded hover:border-[#8b5a2b] hover:text-[#8b5a2b] text-[#4a3f35] transition flex items-center gap-2 cursor-pointer relative z-10"
                >
                  <span className="text-[#8b5a2b] font-mono text-sm">#{chapters.length - index}</span>
                  <span className="truncate" dangerouslySetInnerHTML={{ __html: chap.title.rendered }} />
                </Link>
             )) : (
               <p className="text-[#8b5a2b] italic">Truyện này chưa có chương nào.</p>
             )}
           </div>
        </div>
      </div>
    </main>
  );
}
