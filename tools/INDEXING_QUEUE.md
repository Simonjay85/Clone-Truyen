# DTT Indexing Queue V1

`tools/indexing_queue.py` audits recently published/modified **normal WordPress posts** and builds a prioritized queue for crawl-signal fixes and authorized Google Search Console URL Inspection.

It intentionally **does not use Google Indexing API** for normal articles.

## Checks per URL

- HTTP response is `200` and final URL does not redirect away.
- `robots` / `X-Robots-Tag` does not contain `noindex`.
- canonical exists and matches the article URL.
- URL exists in a Rank Math `post-sitemap*.xml` sitemap.
- sitemap `lastmod` is not materially older than WordPress `modified_gmt`.

Intentional `noindex` posts are reported under `excluded` and never enter the GSC queue.

## Priority

- `P0 fix_before_gsc`: technical/indexing signal needs fixing first.
- `P1 gsc_inspect_new`: healthy new post modified within 24h.
- `P2 gsc_inspect_updated` / `gsc_inspect_new`: healthy recent update/new post.
- `P3 gsc_inspect_updated`: older item still inside the lookback window.
- `EXCLUDED`: intentional `noindex`.

## Local run

```bash
python3 tools/indexing_queue.py \
  --site https://doctieuthuyet.com \
  --lookback-hours 72 \
  --max-posts 120 \
  --workers 8 \
  --out-dir output/indexing-queue \
  --print-report
```

Outputs:

- `latest.json` / `latest.txt`
- timestamped `indexing-queue-YYYYMMDDTHHMMSSZ.json/.txt`
- timestamped files older than 45 days are pruned by default.

## Live schedule

Production copy: `/home/ubuntu/dtt-indexing-queue/indexing_queue.py`

Production outputs: `/home/ubuntu/dtt-indexing-queue/output/`

The server is UTC. The daily cron runs at `23:45 UTC`, equivalent to **06:45 Asia/Ho_Chi_Minh**, before the 07:00 SEO Daily Watch. `flock -n` prevents overlapping runs.
