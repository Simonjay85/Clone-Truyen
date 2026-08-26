# Hướng dẫn Cache + CDN — doctieuthuyet.com

> Ngày: 26/08/2026. Vấn đề đo được: TTFB 1–5.7s (có lúc tới 23–30s),
> static file mất tới 15.8s → origin chậm, không CDN.

## ✅ ĐÃ DEPLOY XONG (26/08/2026)

Server = BT Panel (Bảo Tháp), SSH alias `templystudio` (user ubuntu).

- **Page cache**: đã sửa vhost `/www/server/panel/vhost/nginx/doctieuthuyet.com.conf`:
  - Dùng sẵn zone `WORDPRESS` từ `0.fastcgi_cache.conf` (BT tạo sẵn)
  - Thêm `$skip_cache` cho POST/query-string/wp-admin/wp-json/feed/search + user logged-in
  - PHP location có `fastcgi_cache WORDPRESS` + header `X-DTT-Cache`
- **Cache-Control static**: location regex static assets →
  `Cache-Control: public, max-age=31536000, immutable`
- Backup vhost cũ: `/www/server/panel/vhost/nginx/doctieuthuyet.com.conf.bak-cache-20260826`
- Bản config đang chạy lưu tại repo: `deploy/doctieuthuyet.com.conf.deployed`

### Kết quả kiểm chứng

| Hạng mục | Kết quả |
|---|---|
| Trang bài viết | `x-dtt-cache: HIT`, TTFB ~0.85–1.2s (trước 1–5.7s+) |
| Static assets | 1 dòng `cache-control: public, max-age=31536000, immutable` |
| Homepage | HTTP 200 OK |
| MCP bridge (`/wp-json/doctieuthuyet-mcp/v1/*`) | vẫn hoạt động bình thường |

## Còn lại (tuỳ chọn): Cloudflare CDN

Phần này cần account Cloudflare của chủ domain (đổi nameserver ở nhà đăng ký):

1. Add site `doctieuthuyet.com` (Free plan) → đổi nameserver
2. SSL/TLS mode: **Full (strict)**
3. Speed → Brotli ON, Early Hints ON; Caching → Tiered Cache ON
4. Cache Rule: cache `*/wp-content/*`; **Bypass** `/wp-admin*` và `/wp-json/doctieuthuyet-mcp/*`
5. Kiểm chứng: `curl -sI <static url> | grep cf-cache-status` → HIT

## Purge page cache khi có bài mới

Hiện cache TTL = 60m. Muốn purge ngay khi publish: cài plugin **Nginx Helper**
(WordPress.org), cấu hình method "Delete local server cache files",
path `/www/server/fastcgi_cache`.

## Đã hoàn tất tự động trước đó (cùng ngày)

- [x] Gỡ meta description/keywords/canonical/OG/Twitter hardcode trong
      `tehi-theme/header.php` → chỉ Rank Math xuất (hết duplicate meta)
- [x] Hook auto featured image trong `tehi-theme/functions.php`
- [x] Set featured image cho post 10286 (attachment 12194), og:image live OK

