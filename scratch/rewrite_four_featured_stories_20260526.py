import json
import re
from pathlib import Path


ROOT = Path("/Users/aaronnguyen/TN/App/doctieuthuyet")
SCRATCH = ROOT / "scratch"
OUT_REPORT = SCRATCH / "featured_four_rewrite_audit_20260526.md"


def p(text):
    return f"<p>{text.strip()}</p>"


def words(text):
    return len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", text)))


def content(blocks):
    return "\n".join(p(block) for block in blocks)


def chapter(title, blocks):
    return {"title": title, "content": content(blocks)}


def audit_payload(payload):
    chapters = payload["chapters"]
    counts = [words(ch["content"]) for ch in chapters]
    paras = []
    for ch in chapters:
        paras.extend(
            re.sub(r"\s+", " ", para).strip()
            for para in re.split(r"</p>\s*<p>|<p>|</p>", ch["content"])
            if len(re.sub(r"<[^>]+>", "", para).strip()) > 80
        )
    duplicates = len(paras) - len(set(paras))
    return {
        "chapters": len(chapters),
        "min_words": min(counts),
        "avg_words": round(sum(counts) / len(counts)),
        "max_words": max(counts),
        "duplicate_paragraphs": duplicates,
    }


def save(story_id, payload):
    path = SCRATCH / f"rewrite_{story_id}_v13.json"
    payload = {
        "story_id": story_id,
        "title": payload["title"],
        "intro": payload["intro"],
        "focus_keyword": payload["focus_keyword"],
        "seo_title": payload["seo_title"],
        "seo_description": payload["seo_description"],
        "chapters": payload["chapters"],
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path, audit_payload(payload)


STORIES = {
    2190: {
        "title": "Thần Tài Chứng Khoán: Đấu Trường Phố Wall Hà Nội",
        "focus_keyword": "thần tài chứng khoán",
        "seo_title": "Thần Tài Chứng Khoán: Đấu Trường Phố Wall Hà Nội",
        "seo_description": "Bị vu thao túng cổ phiếu giữa Hà Nội, Hoàng Đức Minh dùng dữ liệu lệnh, sao kê ký quỹ và log giao dịch để lật ngược một âm mưu tài chính.",
        "intro": content([
            "Hoàng Đức Minh từng là người phân tích trẻ nhất trong quỹ Phương Bắc, cho đến sáng anh bị kéo ra giữa phòng giao dịch Hà Nội và bị gắn tội thao túng cổ phiếu.",
            "Tài khoản khách hàng bốc hơi, báo chí chờ sẵn dưới sảnh, còn người thầy cũ của anh bình thản ký lệnh sa thải như thể mọi thứ đã được chuẩn bị từ lâu.",
            "Nhưng Minh vẫn giữ một bản sao log lệnh, chuỗi tin nhắn nội bộ và lịch sử ký quỹ bị xóa vội trong đêm. Khi thị trường mở cửa, kẻ tưởng đã đẩy anh xuống đáy sẽ phải tự nhìn bảng điện tố cáo mình.",
        ]),
        "chapters": [
            chapter("Chương 1: Lệnh Bán Lúc Chín Giờ Mười Bảy", [
                "Bảng điện trong phòng giao dịch Phương Bắc đỏ rực như một vết thương mở. Cổ phiếu HNC rơi sàn, chuông cảnh báo ký quỹ vang lên từng hồi, còn Hoàng Đức Minh đứng giữa vòng người đang chụp điện thoại vào mặt anh.",
                "Trần Minh Tuấn, giám đốc quỹ, ném tập hồ sơ xuống bàn kính. Ông ta nói Minh đã tự ý dùng tài khoản khách hàng bán khống, thao túng giá rồi rút tiền qua một ví trung gian. Câu nào cũng đủ khiến một chuyên viên phân tích mất nghề vĩnh viễn.",
                "Điều làm Minh lạnh sống lưng không phải lời buộc tội, mà là thời điểm. Lệnh bán được đóng dấu chín giờ mười bảy, đúng lúc anh đang ở tầng hầm lấy ổ cứng lưu trữ theo yêu cầu của phòng pháp chế. Thẻ ra vào của anh đáng lẽ chứng minh được điều đó, nhưng file log đã biến mất khỏi hệ thống.",
                "Các nhà đầu tư chen nhau đòi giải thích. Một bác về hưu run tay hỏi tiền dưỡng già của ông còn không. Minh cúi đầu xin lỗi vì đã để họ hoảng loạn, nhưng anh không nhận tội. Lời xin lỗi ấy khiến Tuấn cười khẩy, vì ông ta chỉ cần đám đông nghe thấy hai chữ 'xin lỗi'.",
                "Bảo vệ kéo Minh khỏi bàn giao dịch. Điện thoại anh liên tục nhận tin nhắn từ số lạ: 'Nhận hết đi, mẹ cậu sẽ được yên.' Dòng chữ ngắn ngủi khiến anh hiểu vụ này không dừng ở thị trường. Nó đã chạm vào nhà anh.",
                "Ở thang máy, Minh gặp Nguyễn An Nhiên, kiểm toán viên độc lập vừa được mời rà soát quỹ trước vòng gọi vốn. Cô không bênh anh. Cô chỉ nhìn vệt mực đỏ trên hồ sơ rồi hỏi một câu lạnh tanh: nếu anh vô tội, vì sao mã xác thực OTP lại gửi từ điện thoại của anh?",
                "Minh đáp rằng OTP đúng là từ máy anh, nhưng không phải từ tay anh. Trước khi bị tước thẻ, anh kịp nhìn một dòng nhỏ trên bảng điều phối: phiên đăng nhập xuất phát từ mạng nội bộ phòng họp số ba, nơi chỉ ban điều hành có quyền vào.",
                "Nhiên đưa cho anh danh thiếp, kèm một điều kiện. Trong hai mươi bốn giờ, anh phải cung cấp được bằng chứng gốc, không ảnh chụp màn hình, không lời kể. Nếu không, cô sẽ ký báo cáo bất lợi như đúng quy trình. Minh bước ra phố Trần Hưng Đạo trong tiếng mưa, biết rằng trận đấu thật sự vừa mới mở cửa.",
            ]),
            chapter("Chương 2: Ổ Cứng Lạnh Trong Két Sắt", [
                "Đêm đó, Minh quay về căn hộ cũ ở Kim Mã, nơi mẹ anh vẫn giữ thói quen gói từng hóa đơn điện nước trong túi nilon. Bà không hỏi anh có phạm tội không. Bà chỉ đặt bát cháo xuống bàn và nói nếu cần bán nhà trả nợ, bà sẽ ký.",
                "Câu nói ấy làm Minh nghẹn hơn mọi tiếng chửi trong phòng giao dịch. Anh mở chiếc két nhỏ sau tủ sách, lấy ra ổ cứng lạnh chứa bản snapshot dữ liệu giao dịch mà anh từng sao lưu để phục vụ kiểm toán rủi ro. Quy định nội bộ cấm sao lưu cá nhân, nhưng Minh làm vì anh không tin hệ thống xóa log quá dễ.",
                "Ổ cứng có đủ chuỗi lệnh HNC trong ba tuần. Lệnh bán lúc chín giờ mười bảy được gắn mã thiết bị của Minh, nhưng chuỗi xác thực lại đi vòng qua máy chủ phụ đặt trong phòng họp số ba. Người thường sẽ bỏ qua dòng routing đó; dân phân tích định lượng nhìn một lần là biết có người giả lập phiên.",
                "Minh gọi cho An Nhiên. Cô đến sau bốn mươi phút, áo khoác còn vương mưa. Cô không nhận ổ cứng ngay mà đặt túi chống tĩnh điện, máy niêm phong và biên bản bàn giao lên bàn. Mỗi bước đều có camera quay lại để bằng chứng không bị đánh rớt vì lỗi thủ tục.",
                "Khi hash dữ liệu hiện lên, Nhiên im lặng lâu hơn thường lệ. Dấu thời gian trên server lệch ba mươi bảy giây so với thiết bị của Minh, trùng với thời điểm hệ thống camera tầng hầm mất tín hiệu. Có người không chỉ dựng giao dịch giả, mà còn dọn đường chứng cứ giả.",
                "Minh khoanh tròn ba tài khoản hưởng lợi từ cú rơi HNC. Một tài khoản đứng tên công ty tư vấn ở Cầu Giấy, một tài khoản đứng tên tài xế của Tuấn, và một tài khoản mới mở ở Singapore. Số tiền không lớn ngay lần đầu, nhưng đủ để thử đường chuyển.",
                "Nhiên cảnh báo Minh rằng ổ cứng chỉ chứng minh có bất thường, chưa đủ kết tội ai. Muốn lật ngược vụ này, họ cần dòng tiền, cần camera gốc, cần người trong quỹ chịu đối chiếu nhật ký phòng họp. Minh gật đầu, vì anh biết ai đang giữ chìa khóa phụ.",
                "Người đó là Hạnh, nhân viên lễ tân từng bị Tuấn ép ký khống giờ họp. Minh không muốn kéo cô vào nguy hiểm, nhưng nếu Hạnh không nói, mẹ anh sẽ mất nhà, khách hàng mất tiền, còn Tuấn sẽ dùng chính nỗi sợ của mọi người làm áo giáp.",
            ]),
            chapter("Chương 3: Cô Lễ Tân Và Camera Bị Tắt", [
                "Hạnh hẹn Minh ở một quán phở gần ga Hà Nội lúc năm giờ sáng. Cô đội mũ kín, hai tay ôm túi xách trước ngực như thể trong đó có vật dễ vỡ. Trước khi ngồi xuống, cô nhìn quanh ba lần.",
                "Cô kể đêm trước khi HNC rơi, Trần Minh Tuấn đưa một nhóm người lạ vào phòng họp số ba. Họ không đăng ký khách, không đi qua quầy lễ tân, và dùng thang hàng. Hạnh bị yêu cầu tắt camera hành lang mười phút với lý do bảo trì đường truyền.",
                "Minh không trách cô. Anh hỏi cô còn giữ gì không. Hạnh mở điện thoại cũ, cho xem một đoạn ghi âm. Giọng Tuấn rõ ràng: 'Ngày mai cứ để thằng Minh ký trên hệ thống. Nó giỏi thì giỏi, nhưng người nghèo sợ nhất là mẹ bệnh.'",
                "An Nhiên nghe đoạn ghi âm qua tai nghe, lập tức yêu cầu Hạnh đọc lại nguồn file, thời gian tạo và lịch sử sao lưu. Cô không để cảm xúc làm hỏng thủ tục. Mỗi chi tiết phải đứng được trước tòa, trước Ủy ban Chứng khoán và trước cả đội luật sư của quỹ.",
                "Đúng lúc đó, hai người đàn ông mặc vest xám bước vào quán. Một người đặt điện thoại lên bàn Hạnh, màn hình hiện ảnh em trai cô đang tan ca ở Bắc Ninh. Lời đe dọa không cần nói thành câu.",
                "Minh đứng dậy che trước Hạnh, nhưng An Nhiên kéo anh lại. Cô mở loa điện thoại, để đầu dây bên kia là luật sư của công ty kiểm toán và một cán bộ công an kinh tế mà cô vừa báo lịch làm việc. Hai người đàn ông lập tức đổi giọng, giả vờ nhận nhầm bàn rồi rời đi.",
                "Hạnh bật khóc. Minh không an ủi bằng lời hứa suông. Anh viết giấy xác nhận cô là người cung cấp chứng cứ, đề nghị bảo vệ nhân chứng trong đơn gửi cơ quan điều tra. Lần đầu tiên sau hai ngày, Hạnh nhìn anh như nhìn một người có thể thắng.",
                "Nhưng chiến thắng còn xa. Cùng buổi sáng, báo mạng đăng bài 'Thiên tài chứng khoán lộ mặt lừa đảo'. Ảnh Minh bị cắt từ camera hầm gửi xe, đặt cạnh dòng chữ đỏ chói. Trần Minh Tuấn đã nổ phát súng truyền thông trước khi chứng cứ kịp đến nơi.",
            ]),
            chapter("Chương 4: Phiên Giải Trình Ở Ủy Ban", [
                "Phòng giải trình của Ủy ban Chứng khoán không ồn ào như sàn giao dịch. Sự im lặng ở đó nặng hơn, vì mỗi câu nói đều có thể thành căn cứ xử phạt hoặc chuyển hồ sơ hình sự.",
                "Trần Minh Tuấn đến cùng ba luật sư. Ông ta đặt trước mặt hội đồng một bản báo cáo dày, trong đó Minh bị mô tả là nhân viên bất mãn, có động cơ trả thù sau khi bị từ chối thưởng cuối năm. Họ còn đưa bảng sao kê nợ viện phí của mẹ Minh để chứng minh anh cần tiền.",
                "Minh nắm chặt tay dưới bàn. Đòn này bẩn, nhưng hiệu quả. Một vài thành viên hội đồng nhìn anh khác đi. Nợ bệnh viện, lệnh bán giả, OTP từ điện thoại cá nhân: ghép lại đủ thành câu chuyện mà Tuấn muốn mọi người tin.",
                "An Nhiên xin trình bày trước. Cô không nói về nhân cách Minh. Cô chiếu bảng đối chiếu hash ổ cứng, log routing server và lịch tắt camera. Ba đường dữ liệu độc lập cùng chỉ về phòng họp số ba. Nếu Minh đang ở tầng hầm, anh không thể đồng thời thao tác từ mạng nội bộ phòng đó.",
                "Luật sư của Tuấn phản bác rằng dữ liệu sao lưu cá nhân không hợp lệ. Nhiên chờ câu ấy. Cô đưa biên bản niêm phong, video bàn giao và mã kiểm tra trùng với bản backup tự động từ nhà cung cấp hạ tầng cloud. Cả phòng lật tài liệu nghe tiếng giấy sắc như dao.",
                "Minh tiếp tục mở sơ đồ dòng tiền. Tài khoản tài xế của Tuấn nhận tiền ngay sau cú bán tháo, rồi chuyển qua công ty tư vấn Cầu Giấy. Giao dịch được chia nhỏ dưới ngưỡng cảnh báo, nhưng phí chuyển khoản và địa chỉ IP đăng nhập lại giống nhau.",
                "Tuấn bắt đầu mất bình tĩnh. Ông ta nói Minh đánh cắp bí mật thương mại. Minh nhìn thẳng vào ông ta, đáp rằng bí mật thương mại không bao gồm việc dùng tài khoản khách hàng làm mồi câu. Một thành viên hội đồng gõ bút xuống bàn, yêu cầu hai bên giữ trật tự.",
                "Phiên giải trình tạm dừng để xác minh thêm. Trước khi ra ngoài, Tuấn ghé sát Minh thì thầm: 'Cậu nghĩ có dữ liệu là đủ à? Ngày mai HNC còn một nhịp rơi nữa. Lần này, khách hàng sẽ tự xé xác cậu.' Minh hiểu ông ta vẫn còn đòn cuối trên thị trường.",
            ]),
            chapter("Chương 5: Cú Short Bị Đặt Ngược", [
                "Sáng hôm sau, Minh không đến quỹ. Anh ngồi trong một phòng máy thuê theo giờ ở phố Duy Tân, trước mặt là ba màn hình hiển thị lệnh mua bán HNC theo từng mili giây. An Nhiên đứng phía sau, còn Hạnh theo dõi kênh tin nội bộ từ điện thoại.",
                "Tuấn tung tin giả rằng HNC bị hủy hợp đồng xuất khẩu. Giá mở cửa lao dốc. Các nhóm chat đầu tư gào lên bán tháo. Nhiều khách hàng cũ của Minh gửi tin nhắn chửi anh, vì họ vẫn nghĩ anh là người mở đầu thảm họa.",
                "Minh không phản công bằng lời. Anh bám vào dữ liệu đặt lệnh. Có một thuật toán đang đẩy lệnh bán ảo vào sổ, rút ngay trước khi khớp để tạo cảm giác cung khổng lồ. Đây là spoofing, và kẻ chạy thuật toán dùng cùng dấu vân tay mạng với lệnh giả hôm trước.",
                "Anh gửi gói bằng chứng thời gian thực cho Ủy ban và Sở giao dịch, đồng thời đặt một lệnh mua nhỏ ở vùng giá thấp nhất để đánh dấu phản ứng. Thuật toán lập tức đuổi theo, để lộ tham số kích hoạt. Minh ghi lại toàn bộ màn hình, từng frame một.",
                "An Nhiên nhắc anh không được tự ý thao túng ngược. Minh hiểu. Anh không kéo giá, chỉ tạo bẫy đo. Khi đủ dữ liệu, anh khóa máy, để cơ quan giám sát gửi lệnh dừng giao dịch tạm thời. Bảng điện đứng im giữa tiếng la hét của hàng trăm nhà đầu tư.",
                "Trần Minh Tuấn xuất hiện trên livestream tài chính, cố đóng vai nạn nhân. Ông ta nói quỹ Phương Bắc cũng bị thiệt hại nặng và sẽ kiện Minh đến cùng. Ngay lúc đó, thông báo từ Sở giao dịch hiện lên: HNC tạm dừng giao dịch để điều tra dấu hiệu đặt lệnh giả có tổ chức.",
                "Không khí đổi chiều trong vài phút. Những người vừa chửi Minh bắt đầu im lặng. Một khách hàng lớn gọi cho anh, giọng khàn đi: nếu cậu có thể chứng minh quỹ đã dùng tiền của chúng tôi làm lá chắn, tôi sẽ đứng ra làm nguyên đơn.",
                "Minh không thấy hả hê. Anh nhìn danh sách tài khoản bị kẹt margin và hiểu mỗi con số là một gia đình. Anh thắng một nhịp dữ liệu, nhưng muốn cứu họ, anh phải kéo được người giật dây sau Tuấn ra ánh sáng.",
            ]),
            chapter("Chương 6: Hợp Đồng Ngầm Ở Cầu Giấy", [
                "Dòng tiền dẫn Minh đến một văn phòng tư vấn ở Cầu Giấy, nơi bảng hiệu chỉ ghi dịch vụ kế toán thuế. Chủ công ty là em vợ của Tuấn, nhưng người nhận lợi ích thật nằm sau hợp đồng mua dữ liệu nhà đầu tư cá nhân.",
                "An Nhiên xin lệnh làm việc với ngân hàng lưu ký. Hồ sơ trả về cho thấy ba tuần trước, quỹ Phương Bắc đã thế chấp danh mục của khách hàng để vay ngắn hạn, rồi dùng khoản vay đó mua cổ phiếu trong nhóm sân sau. Khi thị trường đảo chiều, Tuấn cần một vật tế thần.",
                "Minh đọc từng hợp đồng phụ lục, càng đọc càng lạnh. Chữ ký điện tử của anh xuất hiện ở nơi anh chưa từng mở file. Mã xác nhận được gửi lúc nửa đêm, khi điện thoại anh đang sạc ở nhà. Vậy ai có quyền nhân bản eSIM?",
                "Câu trả lời nằm ở phòng công nghệ của quỹ. Trưởng phòng IT từng nhận cổ phần ưu đãi từ Tuấn. Người này tạo một máy ảo mang tên thiết bị của Minh, nhận OTP qua bản sao eSIM rồi ký hàng loạt xác nhận nội bộ. Dấu chân kỹ thuật nhỏ, nhưng vẫn để lại trong log nhà mạng.",
                "Họ cần bản xác nhận từ nhà mạng trước khi Tuấn kịp xóa dấu vết. Minh và Nhiên chạy qua ba văn phòng trong một buổi chiều, ký đủ đơn đề nghị, cam kết chịu trách nhiệm và giấy ủy quyền của mẹ Minh để chứng minh điện thoại thuộc sở hữu thật.",
                "Bên ngoài, nhóm truyền thông của Tuấn tung clip cắt ghép cảnh Minh bị bảo vệ kéo đi. Mẹ anh bị hàng xóm hỏi thăm bằng giọng thương hại. Bà gọi cho Minh, chỉ nói một câu: 'Con làm đúng thì đi đến cùng, mẹ chịu được.'",
                "Đêm xuống, nhà mạng gửi bản phản hồi đầu tiên. Có yêu cầu cấp lại eSIM thử nghiệm từ một thiết bị nội bộ của quỹ Phương Bắc. Người phê duyệt không phải Minh, mà là tài khoản quản trị của Trần Minh Tuấn.",
                "Minh in bản xác nhận, đặt cạnh ghi âm của Hạnh và log spoofing. Ba mảnh ghép khớp lại thành một đường thẳng. Ngày mai, tại cuộc họp nhà đầu tư, Tuấn định biến anh thành kẻ lừa đảo trước hàng trăm tỷ đồng. Minh sẽ để ông ta tự đọc bản án của mình trên màn hình lớn.",
            ]),
            chapter("Chương 7: Cuộc Họp Nhà Đầu Tư", [
                "Khách sạn ở phố Lý Thường Kiệt kín người trước giờ họp. Nhà đầu tư cá nhân, đại diện ngân hàng, phóng viên tài chính và luật sư chen kín sảnh. Trần Minh Tuấn chọn nơi sang trọng để dựng sân khấu kết tội Minh lần cuối.",
                "Ông ta mở đầu bằng giọng trầm buồn. Ông nói quỹ bị một nhân viên phản bội, rằng ông đau đớn khi phải công khai sự thật, rằng Phương Bắc sẽ bồi thường trong khả năng. Mỗi câu đều được soạn như thông cáo báo chí.",
                "Minh ngồi hàng cuối đến khi tên mình bị gọi. Đám đông quay lại. Có người chửi, có người giơ điện thoại quay. Anh bước lên sân khấu không cầm giấy diễn thuyết, chỉ cầm một USB đã niêm phong và văn bản tiếp nhận chứng cứ của cơ quan điều tra.",
                "Anh không kể khổ. Anh chiếu timeline: tắt camera, giả lập eSIM, tạo máy ảo, đặt lệnh bán, chuyển tiền qua công ty tư vấn, tung tin giả để short vòng hai. Mỗi sự kiện gắn với một nguồn độc lập. Phòng họp dần im đến mức nghe được tiếng máy lạnh.",
                "Tuấn cố ngắt lời, nhưng An Nhiên đứng dậy yêu cầu ban tổ chức lập biên bản vì đây là buổi công bố thông tin cho nhà đầu tư. Cô đọc mã hồ sơ xác minh từ Ủy ban. Luật sư của Tuấn cúi xuống trao đổi gấp, mặt không còn vẻ tự tin.",
                "Đòn quyết định đến từ Hạnh. Cô xuất hiện qua màn hình, giọng run nhưng rõ. Cô xác nhận việc tắt camera và phát đoạn ghi âm gốc. Khi câu 'người nghèo sợ nhất là mẹ bệnh' vang lên, nhiều nhà đầu tư quay sang nhìn Tuấn bằng ánh mắt khác hẳn.",
                "Một bác về hưu đứng dậy. Ông không hỏi Minh có xin lỗi không. Ông hỏi Tuấn tiền của họ đang nằm ở đâu. Câu hỏi ấy làm cả hội trường nổ tung. Những người từng bao vây Minh giờ quay về phía giám đốc quỹ.",
                "Công an kinh tế bước vào trước khi Tuấn kịp rời sân khấu. Minh nhìn ông ta bị yêu cầu bàn giao điện thoại, lòng không nhẹ đi. Anh đã lấy lại sự thật, nhưng tiền của khách hàng vẫn cần được cứu từng đồng.",
            ]),
            chapter("Chương 8: Bảng Điện Xanh Sau Cơn Bão", [
                "Một tuần sau, HNC giao dịch trở lại. Giá không tăng kịch trần như truyện cổ tích, nhưng không còn rơi tự do. Công ty công bố hợp đồng xuất khẩu là thật, tin hủy hợp đồng là giả, và cơ quan quản lý phong tỏa tài khoản liên quan đến quỹ Phương Bắc.",
                "Minh được mời trở lại với tư cách cố vấn phục hồi danh mục cho nhóm nhà đầu tư bị thiệt hại. Anh từ chối ghế giám đốc quỹ mới, chỉ nhận quyền truy cập dữ liệu và một điều kiện: mọi lệnh xử lý tài sản phải được công khai cho người góp vốn theo ngày.",
                "An Nhiên ký báo cáo cuối cùng. Trong phần kết luận, cô không dùng những chữ hoa mỹ. Cô ghi rõ: Hoàng Đức Minh không thực hiện lệnh thao túng; hệ thống kiểm soát nội bộ của quỹ Phương Bắc bị lợi dụng có chủ đích; cần chuyển hồ sơ sang điều tra hình sự.",
                "Mẹ Minh đến phòng giao dịch lần đầu sau biến cố. Bà đặt túi trái cây lên bàn, bối rối trước những màn hình lớn. Bác nhà đầu tư từng hỏi tiền dưỡng già bước tới xin lỗi. Minh đỡ ông dậy, nói người cần xin lỗi không phải ông.",
                "Tin tức gọi Minh là 'thần tài chứng khoán'. Anh không thích danh xưng đó. Thần tài nghe như may mắn, còn những gì anh trải qua là những đêm đọc log đến rát mắt, những lần bị đe dọa, và cả nỗi sợ mẹ mình bị kéo vào trò bẩn.",
                "Trần Minh Tuấn bị khởi tố. Công ty tư vấn Cầu Giấy bị phong tỏa tài khoản. Trưởng phòng IT khai nhận đổi lấy cổ phần ưu đãi và một căn hộ. Chuỗi domino đổ chậm, nhưng đổ thật.",
                "Chiều muộn, Minh đứng trước bảng điện đã bớt đỏ. An Nhiên hỏi anh sau chuyện này sẽ làm gì. Minh nói anh muốn mở một nền tảng cảnh báo lệnh bất thường miễn phí cho nhà đầu tư nhỏ. Cô nhướng mày, nhắc anh miễn phí không có nghĩa là dễ sống.",
                "Minh mỉm cười. Anh đã học đủ về cái giá của sự im lặng. Nếu thị trường là đấu trường, thì người bình thường cũng cần một tấm khiên. Và lần này, anh sẽ tự rèn nó bằng dữ liệu không ai có thể xóa trong bóng tối.",
            ]),
        ],
    },
    2129: {
        "title": "Độc Bản Dược Thần: Kẻ Lật Kèo Thế Kỷ",
        "focus_keyword": "độc bản dược thần",
        "seo_title": "Độc Bản Dược Thần: Kẻ Lật Kèo Thế Kỷ",
        "seo_description": "Bị cướp công trình dược phẩm, Trần Huy Hoàng dùng sổ thí nghiệm, mẫu gốc và hồ sơ thử nghiệm để lật kèo một tập đoàn trước ngày IPO.",
        "intro": content([
            "Trần Huy Hoàng mất năm năm để hoàn thiện hoạt chất cứu người, rồi mất tất cả trong một buổi họp khi Đường Vĩnh Khang cướp công trình và đẩy anh ra khỏi Khang Thị.",
            "Ngày tập đoàn chuẩn bị IPO, thuốc độc quyền của họ xuất hiện lỗi phản ứng phụ bị che giấu. Nếu Hoàng im lặng, hàng nghìn bệnh nhân sẽ thành vật thử nghiệm.",
            "Anh trở lại Đà Lạt với sổ thí nghiệm gốc, mẫu tế bào lưu trữ và một nữ luật sư không tin vào thiên tài, chỉ tin vào chứng cứ. Kẻ từng cướp tên anh sẽ phải trả lại cả sự thật lẫn mạng sống của những người bị đem ra đặt cược.",
        ]),
        "chapters": [
            chapter("Chương 1: Công Thức Bị Ký Cướp", [
                "Phòng họp tầng mười hai của Khang Thị thơm mùi gỗ mới và cà phê rang, nhưng với Trần Huy Hoàng, nó giống buồng lạnh bảo quản xác. Trên màn hình là công thức HT-17, hoạt chất anh nuôi suốt bảy năm trong phòng thí nghiệm.",
                "Đường Vĩnh Khang đứng cạnh màn hình, mỉm cười nhận tràng pháo tay của hội đồng quản trị. Tên tác giả trên slide không có Hoàng. Hồ sơ sáng chế ghi nhóm nghiên cứu do Khang trực tiếp chỉ đạo, còn Hoàng chỉ là nhân viên hỗ trợ kỹ thuật đã vi phạm kỷ luật.",
                "Hoàng đứng dậy phản đối. Anh đưa sổ thí nghiệm, ảnh gel điện di, mã mẫu tế bào. Khang không thèm nhìn. Ông ta ra hiệu cho bảo vệ, rồi đọc quyết định sa thải vì 'tự ý sao chép bí mật dược phẩm'.",
                "Cú nhục không nằm ở việc bị lôi ra hành lang. Nó nằm ở ánh mắt của đồng nghiệp. Có người từng thức trắng cùng anh bên tủ cấy vô trùng, nay cúi đầu giả vờ không quen. Có người biết công thức thuộc về ai, nhưng cổ phần IPO khiến họ im lặng.",
                "Ngoài trời Đà Lạt mưa mỏng như bụi kính. Hoàng ôm thùng giấy đựng áo blouse, một cuốn sổ bìa xanh và lọ mẫu cấp đông cuối cùng mà anh kịp giấu trong hộp đá khô. Điện thoại báo tài khoản nghiên cứu của anh bị khóa vĩnh viễn.",
                "Năm năm trôi qua, Khang Thị chuẩn bị đưa HT-17 ra thị trường với tên thương mại K-Serum. Báo chí gọi Vĩnh Khang là dược thần Việt Nam. Hoàng làm thuê trong một phòng xét nghiệm nhỏ, lặng lẽ đọc tin và chờ ngày hoạt chất kia phản bội chính kẻ đánh cắp nó.",
                "Dấu hiệu đến từ một bệnh nhân thử nghiệm. Men gan tăng bất thường, protein viêm bùng lên ở nhóm có biến thể gene hiếm. Đó là lỗi Hoàng từng cảnh báo trong bản nháp bị xóa khỏi server.",
                "Anh gửi email cho Khang Thị yêu cầu tạm dừng thử nghiệm. Ba phút sau, một tin nhắn lạ hiện lên: 'Muốn sống thì quên HT-17.' Hoàng nhìn lọ mẫu cũ trong tủ lạnh, biết rằng cuộc trở về sẽ không còn đường lùi.",
            ]),
            chapter("Chương 2: Nữ Luật Sư Và Sổ Thí Nghiệm Bìa Xanh", [
                "Lâm Tuệ Nghi gặp Hoàng tại một quán cà phê nhìn xuống hồ Xuân Hương. Cô là luật sư sở hữu trí tuệ từng thắng ba vụ tranh chấp dược phẩm, nổi tiếng vì không nhận hồ sơ thiếu chứng cứ.",
                "Hoàng đặt cuốn sổ bìa xanh lên bàn. Các trang giấy đã ố vàng, mép dính vết ethanol và mực phòng thí nghiệm. Mỗi thí nghiệm ghi ngày, giờ, nhiệt độ, mã mẫu và chữ ký người chứng kiến. Tuệ Nghi lật từng trang bằng găng tay.",
                "Cô nói sổ viết tay chưa đủ. Khang Thị sẽ bảo anh làm giả sau khi bị sa thải. Hoàng lấy ra ổ cứng chứa ảnh chụp kính hiển vi gốc, metadata vẫn giữ tên máy chụp và thời gian trước ngày Khang nộp sáng chế.",
                "Điểm khiến Tuệ Nghi dừng lại là trang cảnh báo biến thể gene CYP2C19. Hoàng từng ghi rõ HT-17 cần thêm bước tinh lọc đồng phân, nếu không sẽ gây phản ứng gan ở nhóm bệnh nhân nhất định. Trong hồ sơ IPO, cảnh báo này biến mất.",
                "Tuệ Nghi không hứa thắng. Cô ra điều kiện: Hoàng phải cho phép kiểm định độc lập toàn bộ mẫu, chấp nhận bị điều tra việc giữ mẫu rời khỏi công ty, và tuyệt đối không tự tung dữ liệu lên mạng. Anh đồng ý ngay, vì mục tiêu của anh không phải nổi tiếng.",
                "Trong lúc họ lập biên bản bàn giao, một người đàn ông ngồi bàn bên đứng dậy làm rơi điện thoại. Màn hình đang mở camera, hướng thẳng vào sổ thí nghiệm. Tuệ Nghi đóng sổ, gọi quản lý quán trích xuất camera và yêu cầu người kia ở lại.",
                "Người đàn ông bỏ chạy. Hoàng đuổi theo qua con dốc ướt, suýt trượt ngã trước chợ đêm. Anh chỉ kịp giật lại chiếc thẻ nhân viên rơi ra từ túi áo: phòng pháp chế Khang Thị.",
                "Tuệ Nghi nhìn tấm thẻ, giọng bình thản nhưng mắt sắc lại. Nếu họ theo dõi từ buổi gặp đầu tiên, nghĩa là Khang biết sổ bìa xanh tồn tại. Và nếu Khang biết, ngày IPO sẽ được đẩy nhanh trước khi bằng chứng kịp đến cơ quan quản lý.",
            ]),
            chapter("Chương 3: Mẫu Máu Ở Bệnh Viện Tuyến Cuối", [
                "Bệnh viện Chợ Rẫy gửi phản hồi không chính thức cho Tuệ Nghi lúc hai giờ sáng. Ba bệnh nhân trong chương trình mở rộng dùng K-Serum có dấu hiệu tổn thương gan giống nhau, nhưng báo cáo nội bộ của Khang Thị ghi là bệnh nền tiến triển.",
                "Hoàng đọc kết quả xét nghiệm, mặt trắng bệch. Anh nhận ra mẫu biểu hiện protein từng xuất hiện trong thí nghiệm chuột năm thứ ba. Khi đó, anh đề nghị dừng để sửa quy trình tinh lọc. Vĩnh Khang đã gọi đó là nỗi sợ của kẻ không dám thương mại hóa.",
                "Tuệ Nghi không cho Hoàng tiếp xúc bệnh nhân trực tiếp để tránh bị cáo buộc dụ dỗ nhân chứng. Cô liên hệ người nhà qua kênh pháp lý, xin bản sao hồ sơ và giấy đồng ý sử dụng dữ liệu ẩn danh. Mọi thứ chậm đến đau ruột, nhưng sạch.",
                "Khang Thị phản công trước. Họ gửi công văn cho bệnh viện, đe dọa kiện nếu rò rỉ dữ liệu thử nghiệm. Đồng thời, báo mạng đăng bài nói Hoàng bị sa thải vì trầm cảm và hoang tưởng công trình bị cướp.",
                "Hoàng gần như mất kiểm soát khi thấy ảnh mình cũ bị cắt cạnh tiêu đề bẩn. Tuệ Nghi kéo anh khỏi màn hình. Cô nói kẻ có chứng cứ không cần tranh cãi với tin bẩn; kẻ cần tranh cãi là kẻ sợ giấy tờ.",
                "Chiều hôm sau, một điều dưỡng gửi qua luật sư bản log cấp phát thuốc. Lô K-Serum gây phản ứng có mã tinh lọc B-9, đúng mã Hoàng từng đánh dấu nguy hiểm trong sổ bìa xanh. Không còn là tranh chấp danh dự; đây là cảnh báo an toàn thuốc.",
                "Họ lập tức gửi đơn khẩn đến Cục Quản lý Dược, kèm yêu cầu niêm phong lô B-9. Nhưng trước khi hồ sơ được tiếp nhận, Khang Thị công bố họp báo IPO diễn ra sớm hơn ba ngày.",
                "Hoàng đứng trong hành lang bệnh viện, nghe tiếng máy thở từ phòng cấp cứu vọng ra. Anh hiểu nếu chậm, thuốc sẽ ra thị trường trước, bệnh nhân sẽ trả giá trước, còn vụ kiện có thắng cũng chỉ là bia mộ đẹp.",
            ]),
            chapter("Chương 4: Đêm Đột Nhập Kho Lạnh", [
                "Kho lưu mẫu của Khang Thị nằm phía sau khu sản xuất, bảo vệ hai lớp, camera quay liên tục. Hoàng từng thiết kế quy trình ra vào nên biết đường nào có cảm biến, nhưng anh cũng biết bất kỳ bước sai nào cũng biến anh thành kẻ đột nhập thật sự.",
                "Tuệ Nghi không cho anh phá khóa. Cô dùng lệnh bảo toàn chứng cứ tạm thời do tòa tiếp nhận trong ngày, đi cùng chấp hành viên và đại diện phòng công chứng. Khi cánh cổng mở ra hợp pháp, mặt trưởng kho tái mét.",
                "Danh sách lô B-9 trên giấy ghi đã tiêu hủy. Nhưng trong tủ âm sâu, Hoàng nhìn thấy hộp nhựa có vết băng keo màu xanh do chính tay anh từng dùng để đánh dấu mẫu nguy cơ. Mã trên hộp bị cạo, nhưng lớp sương lạnh không che nổi vết khắc nhỏ HT-17-B9.",
                "Trưởng kho nói đó là mẫu đối chứng không liên quan. Hoàng yêu cầu cân khối lượng, đo nhiệt độ lõi và kiểm tra lịch mở tủ. Log cho thấy tủ được mở hai lần vào đêm sau khi bệnh nhân đầu tiên nhập viện.",
                "Một kỹ thuật viên trẻ bật khóc. Cô thú nhận được lệnh chuyển một phần mẫu sang nhãn khác để tránh đoàn kiểm tra. Người ra lệnh là phó tổng phụ trách nghiên cứu, nhưng email chỉ viết tắt VK.",
                "Đúng lúc biên bản gần hoàn tất, hệ thống báo cháy hú lên. Đèn đỏ chớp, nhân viên chạy tán loạn. Một người mặc áo bảo trì lao vào khu tủ đông, tay cầm bình dung môi. Nếu mẫu tan rã, bằng chứng hóa học sẽ mất.",
                "Hoàng không nghĩ nhiều. Anh lao tới khóa cửa phụ, dùng áo blouse quấn quanh bình dung môi và kéo người kia ngã xuống. Hơi lạnh cắt vào tay anh, nhưng hộp B-9 vẫn nằm trong thùng vận chuyển niêm phong.",
                "Tuệ Nghi nhìn vết bỏng lạnh trên da anh, giọng hiếm khi mềm đi. Cô nói từ giờ Khang Thị không chỉ đối mặt với kiện sở hữu trí tuệ, mà còn hủy hoại chứng cứ và che giấu nguy cơ thuốc. Hoàng không đáp. Anh chỉ nhìn hộp mẫu như nhìn một mạng người vừa được kéo lại từ mép vực.",
            ]),
            chapter("Chương 5: Họp Báo IPO Bị Cắt Sóng", [
                "Khách sạn tổ chức họp báo IPO sáng choang ánh đèn. Đường Vĩnh Khang mặc vest xanh đậm, đứng trước backdrop in hình phân tử HT-17 khổng lồ. Ông ta nói về y học nhân văn, về giấc mơ đưa thuốc Việt ra thế giới, về lòng tin của nhà đầu tư.",
                "Hoàng ngồi cuối phòng cùng Tuệ Nghi, không xuất hiện trong danh sách khách mời. Họ vào bằng thư mời của một cổ đông nhỏ đã mất em trai trong chương trình thử nghiệm. Người phụ nữ ấy nắm chặt ảnh bệnh án trong tay.",
                "Khang vừa chuẩn bị ký bản cam kết niêm yết thì màn hình sau lưng chuyển sang màu đen. Không phải do Hoàng hack. Đó là lệnh tạm dừng công bố từ Cục Quản lý Dược, được gửi đến ban tổ chức và sàn tư vấn phát hành.",
                "Phòng họp nổ tung. Nhà báo đứng dậy hỏi về lô B-9. Đại diện ngân hàng bảo lãnh quay sang nhìn Khang. Ông ta vẫn cười, nói đây chỉ là hiểu lầm thủ tục và công ty sẽ hợp tác tối đa.",
                "Tuệ Nghi đứng lên, công bố cô đại diện cho nhóm bệnh nhân yêu cầu bảo toàn chứng cứ. Cô không đọc dài. Cô nêu ba thứ: sổ thí nghiệm bìa xanh, mẫu B-9 niêm phong, log kho lạnh bị mở sau ca phản ứng phụ đầu tiên.",
                "Khang nhìn Hoàng lần đầu trong buổi họp. Ánh mắt ông ta không còn khinh miệt, mà có một vệt hoảng. Ông ta nói Hoàng là kẻ ăn cắp mẫu công ty, không có tư cách nói về đạo đức.",
                "Hoàng bước lên. Anh không nhận mình hoàn hảo. Anh thừa nhận đã giữ mẫu trái quy định vì sợ cảnh báo an toàn bị chôn vùi. Sau đó anh đặt câu hỏi trước hàng trăm camera: nếu mẫu ấy vô giá trị, tại sao Khang Thị phải phái người đốt nó trong kho lạnh?",
                "Câu hỏi treo giữa hội trường như một mũi kim. Họp báo bị cắt sóng trực tiếp, nhưng hàng chục điện thoại cá nhân vẫn đang phát. Chỉ trong mười phút, cụm từ B-9 leo lên đầu tìm kiếm, còn cổ phiếu dự kiến IPO của Khang Thị trở thành quả bom chưa kịp niêm yết đã rò lửa.",
            ]),
            chapter("Chương 6: Bản Đồ Gene Của Người Sống Sót", [
                "Sau họp báo, Khang Thị đổi chiến thuật. Họ đề nghị bồi thường riêng cho gia đình bệnh nhân, yêu cầu ký cam kết im lặng. Một vài người lung lay, vì tiền viện phí mỗi ngày như hòn đá đè lên ngực.",
                "Hoàng không trách họ. Anh đến bệnh viện với tư cách chuyên gia độc lập do luật sư đề nghị, chỉ phân tích dữ liệu ẩn danh. Anh phát hiện ba bệnh nhân nặng nhất cùng mang biến thể gene khiến đồng phân phụ của HT-17 tích tụ trong gan.",
                "Điều đó chứng minh cảnh báo của anh năm xưa chính xác, nhưng cũng mở ra cách cứu người. Nếu tách được đồng phân độc và dùng phác đồ thải trừ đúng thời điểm, bệnh nhân có cơ hội hồi phục. Hoàng lao vào phòng lab của trường đại học y, mượn máy chạy sắc ký qua đêm.",
                "Tuệ Nghi nhắc anh ranh giới pháp lý. Anh không được tự kê thuốc, không được biến bệnh nhân thành thí nghiệm mới. Hoàng gật đầu, làm việc cùng bác sĩ điều trị, biến kết quả nghiên cứu thành khuyến nghị khoa học có chữ ký hội đồng.",
                "Trong lúc đó, Khang tung tin Hoàng lợi dụng bệnh nhân để quảng bá bản thân. Một nhóm người lạ đến trước phòng lab chửi bới, livestream nói anh là kẻ phá hoại thuốc Việt. Hoàng nghe hết, nhưng không ra ngoài.",
                "Ba giờ sáng, kết quả sắc ký hiện lên. Mẫu B-9 có tỷ lệ đồng phân phụ cao gấp mười hai lần lô đối chứng. Đây không phải lỗi ngẫu nhiên; đây là việc bỏ qua bước tinh lọc để giảm chi phí sản xuất trước IPO.",
                "Bác sĩ trưởng khoa nhận bản khuyến nghị và lập tức điều chỉnh phác đồ. Người bệnh đầu tiên qua cơn nguy kịch sau mười tám giờ. Gia đình cô gái cúi đầu cảm ơn, còn Hoàng chỉ thấy hai chân mình khuỵu xuống vì kiệt sức.",
                "Tuệ Nghi đặt tay lên vai anh. Cô nói vụ kiện danh dự có thể kéo dài nhiều năm, nhưng mạng người vừa được cứu ngay trong đêm nay. Hoàng nhìn bình minh xanh nhạt ngoài cửa sổ bệnh viện, lần đầu thấy sự trả thù của mình có hình dạng tử tế.",
            ]),
            chapter("Chương 7: Người Ký Lệnh Tinh Lọc", [
                "Cơ quan điều tra mời Đường Vĩnh Khang làm việc ngay khi kết quả kiểm định độc lập được niêm phong. Ông ta vẫn giữ vẻ điềm tĩnh, khẳng định mọi thay đổi quy trình đều do hội đồng khoa học phê duyệt.",
                "Vấn đề là hội đồng khoa học không tìm thấy biên bản nào cho phép bỏ bước tinh lọc. Chỉ có một email nội bộ đã bị xóa, khôi phục từ máy chủ dự phòng, trong đó Vĩnh Khang viết: 'Chi phí tinh lọc quá cao, tỷ lệ biến thể gene thấp, chấp nhận rủi ro thương mại.'",
                "Luật sư của Khang nói email bị diễn giải sai ngữ cảnh. Tuệ Nghi đưa tiếp phụ lục tài chính: nếu bỏ bước tinh lọc, lợi nhuận trước IPO tăng đủ để định giá công ty thêm nghìn tỷ. Rủi ro y khoa bỗng lộ nguyên hình thành rủi ro bị bán lấy tiền.",
                "Hoàng được mời đối chất. Anh mang theo sổ bìa xanh, không phải để kể công, mà để đọc lại dòng cảnh báo viết năm xưa. Ngày tháng, điều kiện thí nghiệm, chữ ký người chứng kiến đều rõ. Người chứng kiến khi ấy chính là phó tổng nghiên cứu hiện còn làm ở Khang Thị.",
                "Người phó tổng ban đầu chối. Nhưng khi nghe đoạn ghi âm kho lạnh và thấy email VK, ông ta sụp xuống. Ông thừa nhận đã sửa hồ sơ theo lệnh, đổi mã lô B-9 và xóa phụ lục cảnh báo khỏi báo cáo nộp cho nhà đầu tư.",
                "Vĩnh Khang cuối cùng mất bình tĩnh. Ông ta chỉ vào Hoàng, hét rằng nếu không có ông ta, công thức của Hoàng cũng chỉ nằm chết trong phòng thí nghiệm. Hoàng đáp rất khẽ: thương mại hóa thuốc không có nghĩa là thương mại hóa mạng người.",
                "Tin khởi tố lan ra vào chiều cùng ngày. Khang Thị bị đình chỉ IPO, lô K-Serum bị thu hồi, tài sản liên quan bị phong tỏa để bồi thường. Cổ đông giận dữ, bệnh nhân khóc, còn báo chí đổi cách gọi Vĩnh Khang từ dược thần thành kẻ đánh cược sinh mạng.",
                "Hoàng rời trụ sở điều tra khi trời Đà Lạt đổ mưa. Năm năm trước anh cũng bị đẩy ra dưới mưa, nhưng lần này anh không ôm thùng giấy. Anh ôm bản sao quyết định thu hồi thuốc, thứ giấy lạnh nhưng cứu được những người chưa kịp biết mình gặp nguy.",
            ]),
            chapter("Chương 8: Phòng Lab Không Có Tên Ai Trên Cửa", [
                "Ba tháng sau, một phòng lab nhỏ bên rìa Đà Lạt mở cửa. Trên biển hiệu không có tên Hoàng, không có chữ dược thần, chỉ ghi Trung tâm An toàn Hoạt chất Độc lập. Anh muốn nơi này kiểm định thuốc trước khi thị trường gọi chúng là kỳ tích.",
                "Tuệ Nghi trở thành cố vấn pháp lý cho trung tâm. Cô vẫn lạnh lùng với giấy tờ, vẫn bắt mọi mẫu vào lab phải có chuỗi bàn giao hoàn chỉnh. Hoàng đôi khi đùa rằng cô còn đáng sợ hơn tủ âm sâu, và cô đáp tủ âm sâu ít nhất không tự ý giữ mẫu trái quy định.",
                "Những bệnh nhân dùng lô B-9 dần hồi phục. Không phải ai cũng khỏe hoàn toàn, nhưng họ có hồ sơ bồi thường, có phác đồ theo dõi và có lời xin lỗi chính thức từ ban quản trị mới của Khang Thị. Lời xin lỗi đến muộn, nhưng không còn bị chôn.",
                "Sổ bìa xanh được đặt trong tủ kính của phòng lab, không phải như chiến lợi phẩm mà như lời nhắc. Mỗi trang là một lần sai số, một lần thử lại, một lần người làm khoa học phải chọn giữa tốc độ và sự thận trọng.",
                "Hoàng nhận được đề nghị mua lại công thức HT-17 phiên bản đã sửa từ một tập đoàn nước ngoài. Anh không từ chối ngay, nhưng đặt điều kiện dữ liệu phản ứng phụ phải công khai cho cộng đồng y khoa và giá thuốc cho bệnh nhân Việt phải được trần hóa trong mười năm.",
                "Có người nói anh ngây thơ. Hoàng đã nghe câu đó đủ nhiều. Anh biết tiền cần để lab sống, nhưng anh cũng biết im lặng vì tiền đã suýt giết người như thế nào.",
                "Một buổi chiều, cô gái từng nguy kịch đến trung tâm tặng anh chậu cẩm tú cầu. Cô nói muốn học dược. Hoàng nhìn đôi tay cô còn gầy, nhớ tới những dòng men gan đỏ chói trên màn hình bệnh viện, rồi gật đầu nhận cô làm thực tập sinh mùa hè.",
                "Kẻ cướp công trình đã ngã, nhưng chiến thắng thật không phải chiếc còng trên tay Vĩnh Khang. Chiến thắng là mỗi mẫu thuốc từ nay phải đi qua ánh sáng trước khi bước vào cơ thể người bệnh.",
            ]),
        ],
    },
}


STORIES[2120] = {
    "title": "Mẹ Vợ Bắt Rửa Bát, Tôi Nấu Tiệc Michelin Chấn Động Phú Quốc",
    "focus_keyword": "mẹ vợ bắt rửa bát",
    "seo_title": "Mẹ Vợ Bắt Rửa Bát, Tôi Nấu Tiệc Michelin Chấn Động Phú Quốc",
    "seo_description": "Bị nhà vợ khinh là thằng rửa bát, Đặng Quốc Bảo dùng kỹ nghệ bếp, hồ sơ nguyên liệu và đại tiệc Michelin để lật mặt kẻ cướp công thức.",
    "intro": content([
        "Đặng Quốc Bảo bị mẹ vợ bắt rửa bát giữa biệt thự Phú Quốc, bị anh rể gọi là đồ ăn bám ngay trước mặt họ hàng.",
        "Không ai biết người đàn ông cúi đầu bên bồn rửa từng là bếp trưởng đứng sau những bữa tiệc ngoại giao kín, và cũng là chủ nhân công thức bị sư phụ cướp trắng.",
        "Khi đại tiệc Michelin của đảo ngọc đứng trước nguy cơ bị phá, Quốc Bảo bước lại vào bếp. Dao, lửa, hồ sơ kiểm nghiệm và vị giác của anh sẽ khiến cả nhà vợ lẫn kẻ phản bội phải nuốt từng lời khinh miệt.",
    ]),
    "chapters": [
        chapter("Chương 1: Đống Bát Trong Biệt Thự Biển", [
            "Bồn rửa nhà họ Nguyễn cao ngang ngực Đặng Quốc Bảo, chất đầy đĩa sứ viền vàng sau bữa tiệc gia đình. Mỡ cua hoàng đế đông lại trên tay anh, còn ngoài phòng khách, mẹ vợ anh đang kể với khách rằng con gái bà lấy nhầm một thằng vô dụng.",
            "Bà Tuyết gọi anh ra giữa phòng, ném chiếc tạp dề ướt xuống chân. Anh rể Minh Hùng cười lớn, bảo người như Bảo chỉ hợp đứng sau bếp, đừng mơ ngồi cùng bàn với giới làm ăn Phú Quốc. Vợ anh, Ngọc Mai, cúi đầu im lặng.",
            "Quốc Bảo không cãi. Anh nhìn bàn tiệc thừa mứa và nhận ra món cá mú hấp bị xử lý sai nhiệt, gan cầu gai bị tanh vì rửa nước ngọt. Một đầu bếp thật sự thấy những lỗi ấy như vết cắt, nhưng anh đã quen nuốt xuống.",
            "Sự nhục nhã bùng lên khi Minh Hùng bắt anh quỳ lau vệt rượu trên sàn. Điện thoại của khách đồng loạt giơ lên. Một người đùa rằng nên livestream 'chàng rể rửa bát'. Bảo nghe tiếng cười vỡ trên đầu như bát sứ rơi.",
            "Đúng lúc đó, Lê Quỳnh Chi, CEO khu nghỉ dưỡng tổ chức đại tiệc Michelin, bước vào tìm Minh Hùng bàn hợp đồng cung ứng. Cô nhìn Bảo, rồi nhìn con dao gọt tỉa anh vừa đặt cạnh bồn. Lưỡi dao được mài theo góc rất lạ, chỉ dân bếp fine dining mới dùng.",
            "Quỳnh Chi cố tình hỏi ai đã chỉnh lại nước sốt tiêu đỏ trên bàn. Cả nhà im. Bảo không muốn trả lời, nhưng một vị khách nước ngoài đã nếm và khẳng định món duy nhất cứu được bữa tiệc là phần sốt ấy.",
            "Minh Hùng lập tức nói đó là bếp phụ của hắn làm. Bảo vẫn im, cho đến khi Quỳnh Chi đặt trước mặt anh một hạt tiêu chín đỏ và hỏi thời điểm rang. Anh đáp chính xác: mười bảy giây sau khi vỏ nứt, nếu quá hai giây sẽ đắng.",
            "Căn phòng lặng đi. Quỳnh Chi đưa danh thiếp, mời anh đến bếp thử nghiệm lúc nửa đêm. Bà Tuyết quát anh không được làm mất mặt nhà vợ. Bảo cúi xuống nhặt tạp dề, nhưng lần này anh không quay lại bồn rửa. Anh bước ra ngoài, mang theo mùi biển và một món nợ danh dự đã quá hạn.",
        ]),
        chapter("Chương 2: Bếp Thử Nghiệm Lúc Nửa Đêm", [
            "Bếp thử nghiệm của khu nghỉ dưỡng lạnh, sạch và sáng đến mức mọi vết bẩn đều thành tội. Quốc Bảo đứng giữa dãy bếp inox, áo sơ mi cũ khác hẳn đồng phục trắng của đội đầu bếp quốc tế đang nhìn anh bằng ánh mắt nghi ngờ.",
            "Quỳnh Chi không cho anh cơ hội kể khổ. Cô đặt lên bàn ba nguyên liệu: tôm hùm xanh, nấm tràm đầu mùa và tiêu đỏ Phú Quốc. Nhiệm vụ rất rõ: trong bốn mươi phút, tạo một món khai vị đủ trình để giữ lại đoàn thẩm định Michelin.",
            "Bếp phó người Pháp bật cười khi thấy Bảo không dùng bơ nhập khẩu. Anh rang vỏ tôm lấy dầu, hơ tiêu trên than gáo dừa, rồi ngâm nấm tràm trong nước biển đã lọc khoáng. Mỗi thao tác đều nhỏ nhưng có lý do.",
            "Khi món ăn hoàn thành, Quỳnh Chi nếm trước. Cô không khen. Cô hỏi vì sao vị ngọt tôm rõ mà không gắt. Bảo giải thích anh dùng nhiệt thấp để giữ glycogen, dùng tiêu đỏ cắt hậu béo, và để nấm tràm làm cầu nối mùi đất với mùi biển.",
            "Một thành viên đội bếp nhận ra kỹ thuật này giống phong cách của nhà hàng An Thế, nơi sư phụ Lê Hữu Đạt từng nổi danh. Minh Hùng lập tức xuất hiện cùng Đạt, tố Bảo ăn cắp bí quyết cũ rồi giả danh thiên tài.",
            "Đạt cười hiền trước mặt mọi người, nói Bảo từng là phụ bếp bị đuổi vì trộm công thức. Ông ta đưa một bản hợp đồng chuyển giao có chữ ký của Bảo. Chữ ký nhìn rất giống, đến mức vài đầu bếp bắt đầu lùi khỏi anh.",
            "Bảo nhìn bản hợp đồng, thấy vết scan nhòe ở góc trái. Anh biết nó được dựng từ giấy tờ ngày anh nằm viện vì bỏng bếp. Nhưng nói miệng không đủ. Anh yêu cầu Quỳnh Chi cho mình ba ngày và quyền truy cập hồ sơ nguyên liệu.",
            "Quỳnh Chi đồng ý, với một điều kiện: nếu anh không chứng minh được công thức thuộc về mình, cô sẽ giao hợp đồng cho Lê Hữu Đạt để cứu đại tiệc. Bảo nhận điều kiện. Bước ra khỏi bếp, anh thấy Minh Hùng nhắn tin cho bà Tuyết: 'Mai ép nó ký giấy ly hôn.'",
        ]),
        chapter("Chương 3: Công Thức Trong Vết Bỏng", [
            "Quốc Bảo trở về căn phòng trọ cũ sau chợ đêm Dương Đông, nơi anh cất những cuốn sổ bếp trong thùng xốp chống ẩm. Mỗi trang ghi nhiệt độ, mùa gió, độ mặn và cả lỗi thất bại. Với anh, công thức không phải vài dòng nguyên liệu; nó là lịch sử của những vết bỏng.",
            "Trang quan trọng nhất bị cháy một góc. Đó là đêm nhà hàng An Thế hỏa hoạn, cũng là đêm Lê Hữu Đạt tuyên bố Bảo trộm tiền rồi đuổi anh đi. Trên mép giấy còn vệt mỡ tiêu đỏ, dấu mực và một mẩu băng y tế dính máu.",
            "Quỳnh Chi đưa sổ cho chuyên gia giám định giấy. Kết quả sơ bộ cho thấy mực ghi chép có tuổi đời trước ngày Đạt nộp bản quyền món ăn hai năm. Nhưng họ vẫn cần bằng chứng liên kết trực tiếp với món Michelin sắp phục vụ.",
            "Bảo nhớ đến bà Sáu Mận, người trồng tiêu ở Gành Dầu từng bán cho anh mẻ tiêu đỏ đầu tiên. Bà giữ một cuốn sổ giao hàng bằng tay, ghi tên người mua, ngày hái, độ chín. Nếu sổ còn, nó sẽ chứng minh Bảo thử nghiệm công thức trước khi Đạt biết tới.",
            "Họ chạy xe lên vườn trong mưa. Bà Sáu ban đầu không muốn dính vào tranh chấp. Lê Hữu Đạt đã mua hết sản lượng tiêu năm nay và dọa hủy hợp đồng nếu bà giúp Bảo. Người nông dân không sợ kiện, nhưng sợ công nhân mất việc.",
            "Bảo không ép bà. Anh chỉ nấu lại một chén nước dùng nhỏ bằng tiêu lỗi bà định bỏ, rồi chỉ ra vì sao năm ấy anh chọn trái chín nứt chứ không chọn loại đẹp mã. Bà Sáu nhìn anh rất lâu, cuối cùng mở tủ lấy cuốn sổ bọc nilon.",
            "Trong sổ có dòng: 'Bảo An Thế, thử tiêu đỏ, yêu cầu giữ cuống.' Ngày tháng nằm trước hồ sơ của Đạt. Quỳnh Chi lập biên bản ngay tại vườn, chụp từng trang, mời trưởng ấp ký xác nhận.",
            "Trên đường về, xe họ bị hai thanh niên chặn lại đập kính. Một người giật túi tài liệu của Quỳnh Chi. Bảo lao theo qua con đường đất trơn, ngã rách cả lòng bàn tay nhưng giữ được cuốn sổ. Mùi máu trộn mùi tiêu đỏ làm anh nhớ lại đêm bị cướp nghề, và lần này anh không để ai cướp thêm nữa.",
        ]),
        chapter("Chương 4: Lô Tôm Bị Đổ Tội", [
            "Sáng hôm sau, khu bếp Marriott bị thanh tra an toàn thực phẩm kiểm tra đột xuất. Lô tôm hùm xanh dùng cho tiệc Michelin bị tố nhiễm hóa chất bảo quản. Lê Hữu Đạt có mặt rất nhanh, như thể ông ta biết trước thời điểm cửa kho mở.",
            "Minh Hùng đứng cạnh đoàn kiểm tra, liên tục nhắc tên Quốc Bảo. Hắn nói một kẻ từng bị đuổi khỏi nhà hàng vì gian dối thì có thể làm mọi chuyện để nổi tiếng. Bà Tuyết cũng đến, mắng Bảo trước mặt nhân viên rằng anh kéo cả nhà xuống bùn.",
            "Bảo yêu cầu được xem thùng niêm phong. Anh không chạm vào tôm trước khi lập biên bản. Chỉ nhìn lớp đá và mùi clo nhạt, anh biết hóa chất được thêm sau khi hàng vào kho, không phải từ tàu cá.",
            "Quỳnh Chi mở camera kho lạnh. Đúng đoạn quan trọng, hình ảnh bị nhiễu mười một phút. Đoàn kiểm tra lập tức nghi ngờ bên bếp che giấu. Lê Hữu Đạt cười nhỏ, đề nghị dùng nguồn nguyên liệu của ông ta thay thế để 'cứu danh tiếng Phú Quốc'.",
            "Bảo xin kiểm tra nước tan từ đá trong thùng. Anh dùng giấy thử nhanh, rồi yêu cầu gửi mẫu tới phòng kiểm nghiệm độc lập. Trong lúc chờ, anh chỉ ra lớp đá trong thùng tôm không cùng kích thước với đá từ nhà cung ứng chính thức. Có người đã thay đá, không thay tôm.",
            "Một phụ kho trẻ tái mặt. Cậu nói đêm qua Minh Hùng mượn thẻ vào kho với lý do lấy rượu cho khách VIP. Bà Tuyết quát cậu im, nhưng Quỳnh Chi đã yêu cầu bảo vệ giữ bản ghi thẻ từ.",
            "Kết quả kiểm nghiệm nhanh trả về: hóa chất nằm trong nước đá, không thấm vào mô tôm. Lô tôm có thể cứu bằng quy trình xả lạnh và thay bể nước biển, nhưng nếu xử lý sai, toàn bộ sẽ hỏng.",
            "Bảo cởi áo khoác, bước vào kho lạnh cùng đội bếp. Ba giờ liên tục, anh kiểm từng con tôm, loại bỏ phần nguy cơ, phục hồi bằng nước biển giàu oxy. Khi thùng cuối cùng được niêm phong lại, thanh tra ghi nhận quy trình hợp lệ. Lê Hữu Đạt mất đòn đầu, nhưng ánh mắt ông ta cho thấy món chính của âm mưu vẫn chưa dọn lên.",
        ]),
        chapter("Chương 5: Dao Bếp Và Giấy Giám Định", [
            "Buổi đối chất diễn ra ngay trong bếp trung tâm. Một bên là Lê Hữu Đạt với đội luật sư và bản quyền món ăn đóng dấu. Một bên là Quốc Bảo với cuốn sổ cháy góc, sổ tiêu của bà Sáu và bàn tay còn băng trắng.",
            "Đạt cố biến chuyện thành tranh chấp cảm xúc. Ông ta kể đã nuôi Bảo từ phụ bếp nghèo, dạy anh cầm dao, cho anh cơ hội. Giọng ông ta ấm đến mức vài nhân viên trẻ nhìn Bảo như kẻ vô ơn.",
            "Bảo không tranh công nuôi dạy. Anh đặt con dao cũ lên bàn. Chuôi dao có ba vết khắc nhỏ tương ứng ba lần anh sửa góc cắt tôm hùm để giữ nước ngọt. Trong sổ thí nghiệm món ăn, ba lần sửa ấy trùng ngày với ba mẻ tiêu của bà Sáu.",
            "Chuyên gia giám định trình bày kết quả: giấy, mực và vết dầu trên sổ của Bảo đều có niên đại trước hồ sơ bản quyền của Đạt. Vết dầu chứa hợp chất bay hơi từ tiêu đỏ Phú Quốc, không phải hương liệu công nghiệp dùng trong bản công thức của Đạt.",
            "Đạt bắt đầu đổ mồ hôi. Ông ta nói công thức không thể thuộc về một người không có nhà hàng, không có bằng quốc tế. Quỳnh Chi hỏi ngược: vậy vì sao bản công thức ông nộp có một lỗi nhiệt độ mà chỉ người sao chép từ bản nháp mới mắc?",
            "Bảo giải thích lỗi ấy là bẫy. Năm xưa anh cố tình ghi 82 độ trong bản thử gửi Đạt, nhưng nhiệt đúng là 78 độ. Nếu nấu ở 82 độ, protein tôm sẽ co, vị ngọt gãy. Bản quyền của Đạt giữ nguyên con số sai.",
            "Để chứng minh, Bảo nấu hai phiên bản trước mặt thanh tra và đội bếp. Một món ở 82 độ khô xác, một món ở 78 độ ngọt trong. Không cần lời kết án, vị giác của cả phòng đã ký vào biên bản.",
            "Minh Hùng cố lẻn ra ngoài nhưng bị bảo vệ giữ lại vì log thẻ kho. Bà Tuyết nhìn con rể, lần đầu không tìm được câu mắng. Bảo không nhìn bà. Anh nhìn Đạt và nói: 'Ông cướp nghề của tôi một lần. Ông không được dùng nó đầu độc danh dự của Phú Quốc lần nữa.'",
        ]),
        chapter("Chương 6: Mất Nguồn Cung Trước Giờ Tiệc", [
            "Khi tưởng mọi thứ đã ổn, Royal Food, tập đoàn đứng sau Lê Hữu Đạt, tung đòn cuối. Họ mua đứt toàn bộ nấm tràm, tiêu đỏ và nước mắm nhĩ cao cấp trên đảo trong vòng một buổi chiều, rồi gửi thông báo hủy cung ứng cho Marriott.",
            "Đại tiệc còn hai mươi bốn giờ. Đoàn ngoại giao đã hạ cánh. Nếu thực đơn đổi đột ngột, Quỳnh Chi mất hợp đồng, Bảo mất cơ hội rửa sạch tên, còn Phú Quốc thành trò cười trong giới ẩm thực.",
            "Đội bếp đề nghị nhập nguyên liệu từ Sài Gòn. Bảo từ chối. Món này sống bằng thổ nhưỡng đảo: nấm sau mưa, tiêu gặp gió biển, nước mắm có hậu ngọt từ cá cơm địa phương. Thay nguyên liệu là tự thua trước khi ra đĩa.",
            "Anh nhớ đến những nguồn nhỏ không nằm trong danh sách thương mại: tổ hợp phụ nữ làm nước mắm ở Hàm Ninh, nhóm thanh niên hái nấm rừng có giấy phép cộng đồng, và vườn tiêu già của bà Sáu còn giữ một kho giống để làm mắm tiêu.",
            "Quỳnh Chi dùng tư cách khu nghỉ dưỡng lập hợp đồng trực tiếp, trả giá công bằng và cam kết ghi nguồn gốc trên thực đơn. Người dân ban đầu sợ Royal Food trả đũa, nhưng khi biết Bảo là người từng cứu lô tôm và không ép giá, họ đồng ý gom từng mẻ nhỏ.",
            "Minh Hùng, được bảo lãnh ra ngoài, kéo người chặn xe nguyên liệu ở đường ven biển. Lần này Bảo đã chuẩn bị. Mỗi xe có camera hành trình, hợp đồng điện tử, và một nhóm phóng viên ẩm thực đi cùng ghi hình hành trình từ vườn đến bếp.",
            "Đêm đó, bếp Marriott sáng suốt. Nấm được làm sạch bằng cọ mềm, tiêu phơi gió trên khay tre, nước mắm lọc qua vải thô. Bảo không còn là chàng rể bị gọi xuống rửa bát; anh là người chỉ huy một dàn nhạc của mùi hương.",
            "Gần sáng, Quỳnh Chi hỏi anh có mệt không. Bảo nhìn vết băng trên tay đã thấm màu tiêu, nói anh đã mệt suốt nhiều năm vì phải im lặng. Nấu một đêm để lấy lại tên mình, với anh, còn nhẹ hơn rửa bát trong nhục nhã.",
        ]),
        chapter("Chương 7: Đại Tiệc Bên Bờ Biển", [
            "Sảnh tiệc mở ra sát mép sóng. Nến đặt trong vỏ ốc, khăn trải bàn trắng, tiếng đàn dây lẫn tiếng biển. Các vị khách quốc tế không biết phía sau mỗi đĩa ăn là một trận chiến giấy tờ, kho lạnh và những con đường bị chặn.",
            "Món khai vị của Bảo là tôm hùm xanh hấp hơi nước mắm nhĩ, điểm tiêu đỏ và nấm tràm non. Anh yêu cầu phục vụ kể nguồn gốc bằng ba câu ngắn: tôm từ làng chài, tiêu từ Gành Dầu, nấm sau cơn mưa đầu mùa. Không hoa mỹ, chỉ thật.",
            "Đĩa đầu tiên được đưa đến bàn trưởng đoàn thẩm định. Người phụ nữ tóc bạc nếm một miếng rồi đặt dao xuống. Cả bếp nín thở. Bà không khen ngay, chỉ hỏi ai nghĩ ra cách dùng hậu mặn của nước mắm để kéo vị ngọt tôm dài như vậy.",
            "Quỳnh Chi mời Quốc Bảo ra sân khấu. Anh vẫn mặc áo bếp, không vest, tay còn dán băng. Dưới hàng ghế, bà Tuyết và Minh Hùng ngồi cứng đờ vì được mời với tư cách gia đình. Họ không ngờ người bị bắt rửa bát lại là tâm điểm của buổi tiệc.",
            "Lê Hữu Đạt xuất hiện cùng đại diện Royal Food, cố tố Marriott vi phạm bản quyền công thức ngay trước khách quốc tế. Ông ta tưởng Bảo sẽ tránh làm xấu tiệc. Nhưng Quỳnh Chi đã chuẩn bị màn hình, giấy giám định và biên bản nguồn nguyên liệu.",
            "Trước hàng trăm người, Bảo không mắng. Anh chỉ trình bày hai đĩa: bản 82 độ của Đạt và bản 78 độ của anh. Trưởng đoàn thẩm định nếm cả hai, rồi nói bản 82 độ giết chết linh hồn nguyên liệu. Một câu tiếng Anh ngắn khiến mặt Đạt trắng bệch.",
            "Bà Sáu Mận được mời lên nhận lời cảm ơn. Người phụ nữ làm vườn run tay cầm micro, nói Bảo chưa từng ép giá nông dân và luôn trả thêm cho mẻ tiêu khó hái. Tiếng vỗ tay nổi lên không vì drama, mà vì mọi người cảm thấy món ăn có người thật phía sau.",
            "Đêm ấy, đại tiệc không chỉ thành công. Nó biến thành phiên tòa vị giác. Lê Hữu Đạt rời sảnh trong tiếng máy ảnh, Royal Food bị yêu cầu giải trình hợp đồng độc quyền, còn Bảo đứng trước biển, nghe lần đầu tiên mẹ vợ gọi anh bằng tên đầy đủ.",
        ]),
        chapter("Chương 8: Căn Bếp Mang Tên Người Trồng Tiêu", [
            "Một tháng sau, Marriott công bố chuỗi thực đơn Phú Quốc theo mùa, đặt tên từng món theo làng chài, vườn tiêu và tổ hợp nước mắm đã cứu đại tiệc. Quốc Bảo là cố vấn ẩm thực, nhưng anh yêu cầu hợp đồng ghi rõ tỷ lệ lợi nhuận trả về cho nguồn nguyên liệu địa phương.",
            "Lê Hữu Đạt bị thu hồi danh hiệu, hồ sơ bản quyền món ăn bị hủy, Royal Food phải bồi thường cho các nhà cung ứng nhỏ vì hành vi ép độc quyền. Minh Hùng bị điều tra vụ phá kho và chặn xe nguyên liệu. Cái giá đến chậm, nhưng đến đủ.",
            "Bà Tuyết mời Bảo về ăn cơm. Bàn ăn lần này không có đống bát chờ sẵn. Bà lúng túng xin lỗi, nói mình không biết anh từng giỏi như vậy. Bảo đáp rằng vấn đề không phải bà không biết anh giỏi, mà là bà nghĩ người rửa bát thì không đáng được tôn trọng.",
            "Ngọc Mai cuối cùng lên tiếng. Cô xin lỗi vì đã im lặng trong những ngày anh bị làm nhục. Bảo không biến lời xin lỗi thành cảnh đoàn viên dễ dãi. Anh nói hai người cần thời gian, cần học cách đứng cạnh nhau khi một bên bị đám đông đạp xuống.",
            "Quỳnh Chi đề nghị anh mở nhà hàng riêng trong khu nghỉ dưỡng. Bảo đồng ý với một điều kiện: căn bếp phải có chương trình đào tạo miễn phí cho con em làng chài và nông dân trên đảo. Anh không muốn thiên tài nào khác bị kẹt sau bồn rửa vì thiếu một cánh cửa.",
            "Ngày khai trương, bảng hiệu không ghi tên Bảo thật lớn. Nó ghi 'Bếp Mùa Gió', bên dưới là danh sách những người cung ứng: bà Sáu Mận, tổ nước mắm Hàm Ninh, đội hái nấm cộng đồng. Bảo đứng sau quầy, tự tay lau từng chiếc đĩa.",
            "Một vị khách trêu rằng giờ anh nổi tiếng rồi vẫn rửa bát sao. Bảo cười. Rửa bát không nhục. Nhục là bắt người khác rửa bát để chứng minh họ thấp hơn mình. Khi công việc được tôn trọng, cả căn bếp sạch lên theo một cách khác.",
            "Ngoài biển, hoàng hôn đổ xuống màu tiêu chín. Bảo nếm thìa nước sốt đầu tiên của mùa mới, nghe tiếng dao thớt nhịp nhàng sau lưng, và biết cuối cùng tên mình đã trở về đúng nơi nó thuộc về: không phải trên scandal, mà trong hương vị còn đọng lại sau khi khách rời bàn.",
        ]),
    ],
}


STORIES[2112] = {
    "title": "Người Thợ Sửa Xe Ở Hầm B2",
    "focus_keyword": "người thợ sửa xe",
    "seo_title": "Người Thợ Sửa Xe Ở Hầm B2",
    "seo_description": "Bị tát giữa hầm B2 vì cảnh báo phanh siêu xe, Đỗ Nhật Nam dùng log ECU, camera và bằng sáng chế cũ để lật mặt nhóm phá xe trục lợi.",
    "intro": content([
        "Đỗ Nhật Nam chỉ là thợ sửa xe thuê ở hầm B2, áo lúc nào cũng dính dầu và bị khách nhà giàu gọi bằng 'thằng'.",
        "Khi anh cảnh báo chiếc Lamborghini đã bị can thiệp hệ thống phanh, chủ xe tát anh trước mặt đám đông và đòi đuổi việc anh ngay lập tức.",
        "Nhưng trong hộp đen ECU có một chữ ký kỹ thuật không ai ngờ tới: chính Nam từng viết thuật toán gốc ở Đức. Từ hầm xe tối, anh kéo cả đường dây phá siêu xe, gian bảo hiểm và kỹ thuật chính hãng giả mạo ra ánh sáng.",
    ]),
    "chapters": [
        chapter("Chương 1: Cú Tát Cạnh Cột B17", [
            "Hầm B2 của Vincom Đồng Khởi nóng hầm hập mùi xăng, bê tông ẩm và nước rửa xe. Đỗ Nhật Nam đang kiểm tra một chiếc sedan cũ thì nghe tiếng Lamborghini Aventador gầm lên bất thường ở dãy B17.",
            "Âm thanh ấy không phải tiếng pô độ. Nó là tiếng phanh điện tử trả lực sai nhịp, rất khẽ, bị tiếng động cơ che gần hết. Nam bỏ giẻ lau xuống, chạy ra chắn trước đầu xe dù biết người cầm lái là Vương Quốc Anh, tay chơi siêu xe nổi tiếng kiêu ngạo.",
            "Quốc Anh hạ kính, chưa nghe hết câu đã tát Nam lệch mặt. Hắn mắng một thằng sửa xe hầm gửi mà dám dạy chủ Lamborghini cách lái. Bạn bè hắn cười ồ, vài người giơ điện thoại quay.",
            "Nam nuốt máu trong miệng. Anh không xin lỗi vì lời cảnh báo. Anh chỉ chỉ vào bánh trước bên trái, nói cảm biến áp suất không khớp với lực phanh ghi trong ECU. Nếu chạy tốc độ cao, xe có thể khóa bánh lệch.",
            "Quản lý hầm xe sợ mất khách VIP nên bắt Nam im. Quốc Anh ném chìa khóa xuống đất, ép anh quỳ nhặt và lau sạch vết tay dầu trên cửa xe. Nam cúi xuống, không vì phục, mà để nhìn gần vệt tháo ốc trên cụm phanh.",
            "Đúng lúc đó, Nguyễn Trần Khánh Vy, CEO chuỗi showroom Vinh Phát Luxury, đến nhận xe khách. Cô nhìn vết đỏ trên mặt Nam và hỏi vì sao anh dám kết luận can thiệp phanh chỉ bằng âm thanh.",
            "Nam đáp bằng ba chi tiết: tiếng servo hụt nửa nhịp, nhiệt đĩa phanh lệch ba mươi độ, và mã lỗi thoáng qua mà màn hình xe đã tự xóa. Khánh Vy không tin ngay, nhưng cô biết người bịa chuyện không thể bịa đúng cả ba.",
            "Quốc Anh phóng xe ra khỏi hầm để chứng minh. Nam nhìn theo, tay vẫn run vì cú tát. Anh biết nếu chiếc xe đó lên cầu Thủ Thiêm tối nay, người chết có thể không chỉ là kẻ vừa làm nhục anh.",
        ]),
        chapter("Chương 2: Điều Kiện Của Nữ CEO", [
            "Khánh Vy đưa Nam vào phòng kỹ thuật sau showroom, nơi máy chẩn đoán chính hãng đặt trong tủ kính như báu vật. Cô không bênh anh bằng cảm tính. Cô yêu cầu anh chứng minh trong một giờ, nếu sai phải ký biên bản bồi thường danh tiếng.",
            "Nam đồng ý, nhưng cần quyền truy cập bản sao ECU của xe Quốc Anh. Khánh Vy gọi đội hỗ trợ lấy dữ liệu từ lần bảo dưỡng gần nhất. Trưởng kỹ thuật Lê Duy lập tức phản đối, nói dữ liệu thuộc bí mật hãng và Nam không có chứng chỉ.",
            "Cách Lê Duy phản ứng khiến Nam chú ý. Một kỹ thuật viên bình thường sẽ tự tin mở log để bác bỏ thợ hầm. Chỉ người sợ log mới che nó bằng quy trình. Khánh Vy cũng nhận ra điều đó và ra lệnh trích xuất bản đọc chỉ xem, có camera giám sát.",
            "Màn hình hiện hàng nghìn dòng mã. Nam lướt rất nhanh đến cụm điều khiển brake-by-wire. Ở địa chỉ 0x7FA có một đoạn patch nhỏ, ngụy trang như bản cập nhật nhiệt độ. Nó làm trễ phản hồi khi xe ôm cua tốc độ cao.",
            "Lê Duy cười nhạt, bảo Nam nói thuật ngữ để hù người ngoài ngành. Nam không tranh cãi. Anh viết lại mô phỏng lực phanh trên bảng, cho thấy nếu xe chạy trên 120 km/h và đánh lái gấp, bánh trước trái sẽ khóa trước bánh phải 0,18 giây.",
            "Khánh Vy im lặng lâu. Cô hỏi vì sao một thợ hầm B2 hiểu sâu hơn trưởng kỹ thuật chính hãng. Nam tránh ánh mắt cô, nói mình từng làm trong nhóm phát triển phần mềm phanh ở Munich-Sài Gòn, trước khi bị ép nhận lỗi cho một vụ tai nạn thử nghiệm.",
            "Câu đó khiến Lê Duy biến sắc. Anh ta vội gọi điện cho ai đó ngoài hành lang. Nam nghe loáng thoáng tên Vương Thế Hùng, bố của Quốc Anh, người sở hữu hãng bảo hiểm đang định tài trợ giải đua biểu diễn tối mai.",
            "Khánh Vy đưa ra điều kiện mới: Nam phải cùng cô ngăn Quốc Anh đưa xe ra đường đua, nhưng mọi bằng chứng phải hợp pháp. Nam nhìn dữ liệu trên màn hình. Anh từng mất nghề vì một chữ ký giả. Lần này, anh sẽ không để bất kỳ ai nói mình phá xe bằng miệng.",
        ]),
        chapter("Chương 3: Hộp Đen Bị Xóa Dấu", [
            "Một giờ sáng, Nam ngồi trong kho phụ tùng của showroom, trước mặt là bản sao ECU và bộ ghi dữ liệu CAN bus. Bên ngoài kính, Sài Gòn mưa lấm tấm, còn trong phòng chỉ còn tiếng quạt máy chủ.",
            "Đoạn patch được viết rất khéo. Nó tự xóa log sau ba chu kỳ khởi động và chỉ kích hoạt khi xe vào chế độ đường đua. Người làm không phải tay nghiệp dư. Hắn hiểu cả giới hạn cơ khí lẫn cách hãng kiểm tra lỗi bảo hành.",
            "Nam tìm thấy chữ ký biên dịch trong mã: một chuỗi ký tự rút gọn từ thư viện phanh do nhóm cũ của anh viết ở Đức. Tim anh khựng lại. Thư viện đó chưa từng bán ra thị trường Việt Nam, trừ khi có người lấy từ dự án tai nạn năm xưa.",
            "Khánh Vy mang cà phê vào, thấy mặt anh khác đi. Nam kể thật: bốn năm trước, một xe thử nghiệm mất phanh ở đường nội bộ. Anh phát hiện phần mềm bị chỉnh, nhưng báo cáo cuối cùng đổ lỗi cho anh cấu hình sai. Anh bị đuổi, còn dữ liệu gốc biến mất.",
            "Khánh Vy hỏi anh có bằng chứng cũ không. Nam lấy từ ví ra một thẻ nhớ mòn cạnh. Trong đó chỉ còn vài file log cứu được trước khi tài khoản bị khóa. Cô không động vào ngay mà gọi công chứng viên kỹ thuật lập biên bản mở file.",
            "File cũ và patch mới có cùng mẫu lỗi: delay được đặt vừa đủ để tai nạn giống sai lầm người lái. Nếu dùng trong đua biểu diễn, xe đâm, bảo hiểm chi trả, hãng sửa xe kiếm tiền, còn người cài mã có thể short cổ phần đối thủ trong ngành siêu xe.",
            "Camera showroom bắt được Lê Duy lén vào phòng kỹ thuật lúc hai giờ mười lăm. Anh ta rút một USB khỏi túi áo, định cắm vào máy chẩn đoán để ghi đè bản sao. Khánh Vy đã đổi quyền truy cập trước đó, nên hệ thống khóa lại và gửi cảnh báo.",
            "Lê Duy bỏ chạy. Nam đuổi theo xuống hầm, nơi tiếng lốp xe vang lên. Anh chỉ kịp nhìn một chiếc Mercedes đen đón Lê Duy rời đi. Biển số xe thuộc công ty của Vương Thế Hùng. Mối liên kết cuối cùng đã hiện ra, nhưng Quốc Anh vẫn chuẩn bị đua vào sáng mai.",
        ]),
        chapter("Chương 4: Đường Đua Thủ Thiêm", [
            "Trường đua tạm ở Thủ Thiêm đông nghẹt người. Những chiếc siêu xe xếp hàng dưới nắng, camera livestream bay trên cao, Quốc Anh đứng cạnh Aventador như một ngôi sao mạng. Hắn còn cố tình chỉ lên má mình, nhắc lại cú tát hôm qua như chiến tích.",
            "Nam và Khánh Vy đến cùng giấy cảnh báo kỹ thuật. Ban tổ chức ban đầu không cho họ vào khu xe vì Vương Thế Hùng đã gọi trước. Một nhân viên an ninh nói thẳng: thợ sửa xe không có quyền làm chậm sự kiện triệu đô.",
            "Khánh Vy đưa văn bản chịu trách nhiệm của showroom và yêu cầu kiểm tra an toàn bắt buộc. Nam không chờ tranh luận xong. Anh đứng ngoài hàng rào, nghe tiếng Quốc Anh nổ máy. Âm servo lệch vẫn còn đó, rõ hơn vì xe đã vào chế độ Corsa.",
            "Khi Quốc Anh chuẩn bị xuất phát, Nam trèo qua rào chắn. Bảo vệ kéo anh lại, nhưng anh hét mã lỗi 0x7FA và thuật toán delay trước toàn bộ livestream. Khán giả tưởng anh gây rối, còn Quốc Anh đạp ga để chứng minh xe bình thường.",
            "Chiếc Lamborghini lao đi vòng đầu. Đến khúc cua thứ ba, bánh trước trái khựng lại đúng như mô phỏng. Xe quăng đuôi, sượt qua rào bê tông, dừng cách nhóm kỹ thuật vài mét. Không ai chết, nhưng sự im lặng sau cú trượt còn đáng sợ hơn tiếng động cơ.",
            "Quốc Anh bò ra khỏi xe, mặt cắt không còn máu. Hắn vẫn cố mắng Nam phá xe từ xa. Nam không đáp, chỉ yêu cầu niêm phong ECU ngay tại hiện trường. Khánh Vy gọi Cục Đăng kiểm và công an giao thông, biến vụ tai nạn hụt thành hồ sơ kỹ thuật chính thức.",
            "Lê Duy xuất hiện muộn, giả vờ sốc. Nam chỉ vào camera hành trình trong mũ bảo hiểm Quốc Anh. Dữ liệu ghi lại cảnh xe tự giảm lực phanh không theo chân lái. Không còn là tranh cãi giữa thợ hầm và khách VIP; đó là bằng chứng an toàn phương tiện.",
            "Trước hàng nghìn người đang xem livestream, Quốc Anh lần đầu không dám tát ai. Nam đứng bên chiếc xe còn bốc khói, mặt vẫn in dấu hôm qua, nhưng ánh mắt của đám đông đã đổi chiều.",
        ]),
        chapter("Chương 5: Trưởng Kỹ Thuật Chính Hãng", [
            "Buổi giám định diễn ra tại trung tâm đăng kiểm, không có ánh đèn sân khấu nhưng căng như dây phanh. Đại diện hãng, bảo hiểm, công an và luật sư của Vương Thế Hùng đều có mặt. Lê Duy mặc áo kỹ thuật chính hãng, cố giữ vẻ bị xúc phạm.",
            "Anh ta nói Nam dựng chuyện để trả thù quá khứ, rằng thẻ nhớ cũ có thể bị chỉnh sửa. Nam không phản bác bằng cảm xúc. Anh yêu cầu trích xuất trực tiếp từ ECU đã niêm phong sau sự cố, đối chiếu với camera mũ bảo hiểm và dữ liệu lực phanh độc lập.",
            "Kết quả hiện lên từng lớp. Patch 0x7FA tồn tại thật. Thời điểm cài đặt trùng với lần xe vào xưởng của Lê Duy. Chứng thư cập nhật mang tài khoản kỹ thuật cấp cao, người duy nhất có quyền ký là anh ta.",
            "Lê Duy chuyển sang đổ lỗi cho USB nhiễm mã độc. Nam hỏi nếu mã độc ngẫu nhiên, vì sao nó chỉ kích hoạt trong chế độ đua và tự xóa log sau ba chu kỳ. Cả phòng im lặng. Một chuyên gia của Cục Đăng kiểm gật đầu rất khẽ.",
            "Khánh Vy tung thêm biên bản: ba siêu xe khác từng gặp lỗi tương tự sau bảo dưỡng ở cùng xưởng, tất cả đều mua bảo hiểm gói cao từ công ty của Vương Thế Hùng. Tai nạn không đủ chết người, nhưng đủ để đòi bồi thường và thay phụ tùng giá khủng.",
            "Nam đặt thẻ nhớ cũ lên bàn. Mã patch trong vụ tai nạn năm xưa có cùng chữ ký biên dịch. Điều đó không chỉ minh oan cho anh, mà còn chứng minh đường dây này hoạt động từ lâu. Lê Duy nhìn thẻ nhớ như nhìn một quả mìn vừa tháo chốt.",
            "Luật sư Vương gia yêu cầu dừng buổi làm việc vì dữ liệu liên quan bí mật thương mại. Đại diện công an đáp rằng an toàn giao thông và gian lận bảo hiểm không nằm dưới bí mật thương mại. Câu trả lời ấy làm Lê Duy ngồi phịch xuống ghế.",
            "Trước khi bị đưa đi lấy lời khai, Lê Duy nhìn Nam, nói anh vẫn chỉ là thợ sửa xe không có chỗ đứng. Nam lau dầu trên tay, đáp rằng chỗ đứng của thợ sửa xe là nơi xe không giết người. Câu ấy được một phóng viên ghi lại, lan nhanh hơn mọi đoạn clip chế giễu hôm trước.",
        ]),
        chapter("Chương 6: Hai Mươi Bốn Giờ Bị Phong Tỏa", [
            "Vương Thế Hùng không để con trai và đường dây bảo hiểm bị kéo xuống dễ dàng. Sáng hôm sau, xưởng nơi Nam làm bị niêm phong vì cáo buộc sửa chữa không phép. Tài khoản cá nhân của anh bị báo giao dịch bất thường, chủ nhà trọ yêu cầu anh dọn đi.",
            "Khánh Vy đề nghị đưa anh về căn hộ an toàn. Nam từ chối ở lại lâu, vì trong xưởng vẫn còn dụng cụ, máy đo và hồ sơ khách hàng nghèo gửi xe sửa góp. Nếu xưởng bị xóa sạch, không chỉ anh mất chỗ làm, nhiều người cũng mất phương tiện mưu sinh.",
            "Họ phát hiện lệnh niêm phong dựa trên đơn tố cáo nặc danh: Nam can thiệp trái phép vào xe khách để tống tiền. Đơn kèm hình ảnh anh mở capo Lamborghini trong hầm B2, cắt đúng khoảnh khắc anh kiểm tra cảnh báo trước cú tát.",
            "Nam cần chứng minh mình từng cảnh báo trước khi chạm vào xe. Camera hầm B2 là chìa khóa, nhưng quản lý trung tâm thương mại nói dữ liệu đã bị ghi đè. Nam không tin. Hệ thống camera thường còn cache trên đầu ghi phụ ở phòng an ninh.",
            "Anh quay lại hầm B2, nơi mọi chuyện bắt đầu. Một bảo vệ lớn tuổi nhận ra anh và lén cho biết đêm xảy ra vụ việc có người của Vương gia đến xin xóa đoạn B17. Ông không dám giữ bản gốc, nhưng đã chụp lại màn hình vì thấy Nam bị tát oan.",
            "Ảnh chụp không đủ làm bằng chứng chính, nhưng đủ chỉ ra thời điểm. Từ đó, Khánh Vy yêu cầu trích xuất đầu ghi phụ theo thủ tục pháp lý. Dữ liệu còn lại ba mươi giây: Nam chưa hề chạm xe trước khi cảnh báo, và Quốc Anh là người đánh trước.",
            "Cùng lúc, một khách hàng cũ của Nam mang đến hóa đơn sửa xe. Anh từng phát hiện lỗi phanh xe gia đình họ và không lấy thêm tiền, chỉ yêu cầu thay phụ tùng đúng chuẩn. Những người nhỏ bé mà Vương gia bỏ qua bắt đầu đứng thành hàng.",
            "Tối đó, lệnh niêm phong xưởng bị tạm dừng. Nam ngồi trên bậc thềm, tay cầm chiếc cờ lê cũ. Anh không có tập đoàn sau lưng, nhưng có camera, hóa đơn, lời khai và những chiếc xe còn chạy an toàn nhờ anh. Chừng đó đủ để đi tiếp.",
        ]),
        chapter("Chương 7: Bằng Sáng Chế Bị Chôn", [
            "Mấu chốt cuối cùng là quyền sở hữu thuật toán phanh. Nếu Vương Thế Hùng chứng minh phần mềm thuộc hãng, Nam sẽ bị biến thành kẻ xâm nhập hệ thống. Nếu Nam chứng minh mình là đồng tác giả bị xóa tên, toàn bộ câu chuyện đảo chiều.",
            "Khánh Vy tìm đến một luật sư sở hữu trí tuệ. Hồ sơ ở Đức cho thấy bản mô tả thuật toán ban đầu có ba tác giả, trong đó có Do Nhat Nam. Khi chuyển giao sang đối tác Việt Nam, tên anh biến mất khỏi phụ lục nội bộ.",
            "Nam nhớ người ký biên bản năm xưa: một kỹ sư Đức tên Karl, đã nghỉ hưu. Anh gửi email không hy vọng nhiều. Sáu giờ sau, Karl trả lời bằng tiếng Việt vụng về: 'Tôi vẫn giữ bản scan vì ngày đó tôi không đồng ý cách họ đối xử với cậu.'",
            "Bản scan có chữ ký của Nam, mã commit đầu tiên và ghi chú cảnh báo không được dùng thuật toán ngoài phạm vi thử nghiệm. Vương Thế Hùng không chỉ dùng phần mềm trộm; ông ta dùng một bản chưa hoàn thiện để tạo tai nạn có kiểm soát.",
            "Buổi công bố chứng cứ được tổ chức tại showroom Vinh Phát. Khánh Vy mời báo chí, Cục Đăng kiểm và đại diện hãng. Vương Thế Hùng đến với đội luật sư, tự tin rằng tiền có thể bẻ cong mọi câu hỏi.",
            "Nam trình bày bản quyền thuật toán, log ECU, dữ liệu bảo hiểm và camera hầm B2. Anh không nói mình là thiên tài bị hại. Anh nói nếu hệ thống này tiếp tục bị dùng, người chết tiếp theo có thể là bất kỳ ai ngồi trên xe đã qua bảo dưỡng.",
            "Karl xuất hiện qua cuộc gọi video, xác nhận Nam là người viết module an toàn lõi và từng cảnh báo rủi ro. Màn hình im vài giây, rồi phóng viên đồng loạt giơ máy. Vương Thế Hùng lần đầu cúi mặt đọc tin nhắn từ luật sư thay vì nhìn thẳng.",
            "Cơ quan điều tra yêu cầu phong tỏa hồ sơ bảo hiểm của nhóm Vương gia. Quốc Anh, người từng tát Nam, đứng ở góc phòng không nói được câu nào. Nam nhìn hắn, không đòi quỳ xin lỗi. Anh chỉ yêu cầu hắn ký biên bản thừa nhận cú tát và lời vu khống trước hầm B2.",
        ]),
        chapter("Chương 8: Xưởng Sáng Đèn Sau Nửa Đêm", [
            "Ba tháng sau, hầm B2 vẫn có mùi xăng và bê tông ẩm, nhưng cột B17 không còn là nơi Nam bị chế giễu. Trên tường gần đó treo biển nhỏ: khu kiểm tra an toàn phanh miễn phí cho xe hiệu suất cao.",
            "Khánh Vy mời Nam làm giám đốc kỹ thuật của trung tâm mới. Anh nhận, với điều kiện tầng trệt dành một xưởng đào tạo thợ trẻ không cần bằng cấp đẹp, chỉ cần chịu học và tôn trọng sinh mạng người ngồi sau vô lăng.",
            "Vụ Vương gia kéo theo điều tra gian lận bảo hiểm. Lê Duy bị truy tố, Vương Thế Hùng mất quyền điều hành công ty bảo hiểm, còn Quốc Anh phải công khai xin lỗi và tham gia khóa an toàn lái xe bắt buộc. Lời xin lỗi của hắn vụng về, nhưng được ghi âm đầy đủ.",
            "Nam không trở thành người thích phát biểu. Anh vẫn thích cúi dưới gầm xe, nghe tiếng bạc đạn, ngửi mùi má phanh, đọc những lỗi mà màn hình đôi khi chưa kịp hiện. Chỉ khác là giờ không ai gọi anh là thằng sửa xe để hạ thấp nữa.",
            "Một buổi tối, người bảo vệ từng giúp giữ ảnh camera mang chiếc xe máy cũ đến xưởng. Nam tự tay chỉnh phanh, không lấy tiền. Ông bảo hồi đó thấy cậu bị đánh mà không dám can, giờ vẫn áy náy. Nam nói nếu ông không giữ tấm ảnh, sự thật đã mất một bánh răng.",
            "Khánh Vy đứng ngoài cửa nhìn anh làm việc. Cô hỏi anh có tiếc những năm bị chôn dưới hầm không. Nam vặn con ốc cuối, đáp rằng tiếc thì có, nhưng dưới hầm anh học được cách nghe âm thanh thật của máy móc, không bị tiếng vỗ tay trên mặt đất làm nhiễu.",
            "Đêm khai trương, hàng siêu xe xếp ngoài trung tâm. Nhưng Nam chú ý hơn đến nhóm thợ trẻ đang học cách ghi log trước khi sửa. Anh bắt họ lặp lại nguyên tắc đầu tiên: không được đoán khi có thể kiểm tra, không được im khi thấy nguy hiểm.",
            "Sau nửa đêm, xưởng vẫn sáng đèn. Nam lau tay bằng chiếc giẻ cũ, đi ngang qua cột B17 và dừng lại một giây. Nơi từng chứng kiến cú tát giờ chứng kiến một nghề được trả lại danh dự. Anh mỉm cười rất nhẹ, rồi quay vào tiếng máy đang chờ mình lắng nghe.",
        ]),
    ],
}


def main():
    report = ["# Audit sau khi viết lại 4 truyện nổi bật", ""]
    for story_id, payload in STORIES.items():
        path, metrics = save(story_id, payload)
        report.append(f"## {story_id} - {payload['title']}")
        report.append(f"- File: `{path}`")
        report.append(f"- Số chương: {metrics['chapters']}")
        report.append(f"- Word/chương: min {metrics['min_words']} / avg {metrics['avg_words']} / max {metrics['max_words']}")
        report.append(f"- Đoạn lặp exact trong truyện: {metrics['duplicate_paragraphs']}")
        report.append("")

    all_paras = []
    for story_id in STORIES:
        data = json.loads((SCRATCH / f"rewrite_{story_id}_v13.json").read_text(encoding="utf-8"))
        for ch in data["chapters"]:
            for para in re.split(r"</p>\s*<p>|<p>|</p>", ch["content"]):
                cleaned = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", para)).strip()
                if len(cleaned) > 80:
                    all_paras.append((cleaned, story_id))
    seen = {}
    cross = []
    for para, sid in all_paras:
        if para in seen and seen[para] != sid:
            cross.append((seen[para], sid, para[:120]))
        else:
            seen[para] = sid
    report.append(f"## Cross-story duplicate exact paragraphs")
    report.append(f"- Tổng số: {len(cross)}")
    if cross:
        for a, b, sample in cross[:10]:
            report.append(f"- {a} / {b}: {sample}")
    OUT_REPORT.write_text("\n".join(report), encoding="utf-8")
    print(OUT_REPORT)


if __name__ == "__main__":
    main()
