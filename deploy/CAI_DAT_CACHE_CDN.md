# Hướng dẫn bật Page Cache + Cloudflare CDN — doctieuthuyet.com

> Ngày tạo: 26/08/2026. Vấn đề đo được: TTFB 1–5.7s, tổng tải tới 23s,
> static file (style.css 41KB) mất tới 15.8s → origin chậm, không CDN.

## Phần 1 — Nginx page cache + Cache-Control (bắt buộc làm trước)

File cấu hình sẵn: `nginx-cache-config.conf` (cùng thư mục).

1. SSH vào server: `ssh root@51.79.53.190`
2. Tìm vhost: `nginx -T | grep -E 'server_name|conf'`
3. Dán nội dung theo chú thích trong file conf (block ngoài server{} + location trong server{})
4. Sửa `fastcgi_pass` đúng version PHP đang chạy (`ls /run/php/`)
5. Tạo thư mục cache: `mkdir -p /var/cache/nginx/dtt && chown www-data:www-data /var/cache/nginx/dtt`
6. `nginx -t && systemctl reload nginx`
7. Kiểm tra: `curl -sI https://doctieuthuyet.com/thien-nguu-that-huyet/ | grep X-DTT-Cache`
   - Request 1: `MISS`, request 2: `HIT` → thành công (TTFB < 100ms)

### Purge cache khi có bài/chương mới (khuyến nghị)

Cài plugin **Nginx Helper** (WordPress.org) → chọn phương thức purge
"Delete local server cache files", đường dẫn cache `/var/cache/nginx/dtt`.
Plugin sẽ tự xóa cache khi publish/cập nhật post.

## Phần 2 — Cloudflare CDN (che origin + cache static toàn cầu)

1. Đăng ký tại cloudflare.com → Add site `doctieuthuyet.com` (Free plan là đủ)
2. Cloudflare tự quét DNS → xác nhận → đổi nameserver tại nhà đăng ký tên miền
3. Sau khi Active, bật lần lượt:

| Setting | Giá trị | Lý do |
|---|---|---|
| SSL/TLS mode | **Full (strict)** | HTTPS end-to-end |
| Speed → Optimization | Brotli ON, Early Hints ON | Nén tốt hơn gzip |
| Caching → Tiered Cache | ON | Giảm load origin |
| Rules → Cache Rule | `Cache Eligible` cho `*doctieuthuyet.com/wp-content/*` | Static hit edge |
| Rules → Cache Rule | `Bypass cache` cho `/wp-admin*` và `/wp-json/doctieuthuyet-mcp/*` | Không phá admin/MCP bridge |
| Scrape Shield | Bot Fight Mode: OFF trước | Tránh chặn crawler của chính mình (tehi-crawler) |

4. Lưu ý MCP bridge: sau khi bật Cloudflare, request đến
   `https://doctieuthuyet.com/wp-json/doctieuthuyet-mcp/v1/*` phải đặt
   **Cache Rule Bypass** (mục 3) để không bị cache response POST.

5. Kiểm chứng cuối:
   ```bash
   curl -sI https://doctieuthuyet.com/wp-content/themes/tehi-theme/assets/css/style.css | grep -iE 'cf-cache-status|cache-control'
   # kỳ vọng: cf-cache-status: HIT + cache-control max-age lớn
   curl -o /dev/null -s -w '%{time_starttransfer}\n' https://doctieuthuyet.com/thien-nguu-that-huyet/
   # kỳ vọng: < 0.3s (trước đây 1–5.7s)
   ```

## Những gì đã hoàn tất tự động (26/08/2026)

- [x] Gỡ meta description/keywords/canonical/OG/Twitter hardcode trong
      `tehi-theme/header.php` → chỉ Rank Math xuất (hết duplicate meta)
- [x] Thêm hook auto featured image vào `tehi-theme/functions.php`
      (ưu tiên ảnh đầu bài → fallback cover mặc định)
- [x] Set featured image cho bài 10286 (Thiên Ngưu Thất Huyệt),
      attachment ID 12194, đã kiểm tra og:image live = OK
- [x] Backup file remote cũ tại server + `/tmp/dtt-backups-20260826/`

## Checklist khi áp dụng phần nginx/Cloudflare

- [ ] nginx -t pass, reload OK
- [ ] X-DTT-Cache: HIT trên trang bài viết
- [ ] Cache-Control 365d trên /wp-content/*
- [ ] Cloudflare active, cf-cache-status HIT cho static
- [ ] Đăng bài thử mới → có featured image tự động
- [ ] PageSpeed Insights mobile: LCP mục tiêu < 2.5s
