# DTT Indexing Queue V2

`tools/indexing_queue.py` audits recently published/modified **normal WordPress posts** and builds a prioritized queue from both live crawl signals and the official, read-only Google Search Console URL Inspection API.

It intentionally **does not use Google Indexing API** for normal articles.

When the private OAuth credential is absent or invalid, the crawl/sitemap queue still runs and reports GSC as `auth_required`/`error` rather than failing the whole daily job.

## Checks per URL

- HTTP response is `200` and final URL does not redirect away.
- `robots` / `X-Robots-Tag` does not contain `noindex`.
- canonical exists and matches the article URL.
- URL exists in a Rank Math `post-sitemap*.xml` sitemap.
- sitemap `lastmod` is not materially older than WordPress `modified_gmt`.
- GSC index verdict and coverage state.
- Google-selected vs user-declared canonical.
- Google crawl time, fetch state, indexing state and robots state.
- GSC sitemap/referring URL signals when returned by the API.

Intentional `noindex` posts are reported under `excluded` and never enter the GSC queue.

## Priority

- `P0 fix_before_gsc`: technical/indexing signal needs fixing first.
- `P1 gsc_inspect_new`: healthy new post modified within 24h.
- `P2 gsc_inspect_updated` / `gsc_inspect_new`: healthy recent update/new post.
- `P3 gsc_inspect_updated`: older item still inside the lookback window.
- `EXCLUDED`: intentional `noindex`.

After URL Inspection enrichment, GSC can promote an item to `P0` for an indexing/fetch/robots/canonical problem or to `P1` for `Crawled - currently not indexed`, `Discovered - currently not indexed`, or similar non-indexed states.

## Local run

```bash
python3 tools/indexing_queue.py \
  --site https://doctieuthuyet.com \
  --lookback-hours 72 \
  --max-posts 120 \
  --workers 8 \
  --out-dir output/indexing-queue \
  --gsc-credentials /private/path/gsc-oauth.json \
  --gsc-site-url sc-domain:doctieuthuyet.com \
  --print-report
```

On a trusted workstation with Google ADC already authorized, use `--gsc-adc`
instead of `--gsc-credentials`. The ADC quota project is forwarded via
`X-Goog-User-Project` when present.

## Trusted Mac ADC setup

The current DTT automation keeps Google credentials on the trusted Mac and uses
Google Cloud SDK Application Default Credentials (ADC). Authorize once with:

```bash
gcloud auth application-default login \
  --scopes=openid,https://www.googleapis.com/auth/userinfo.email,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/webmasters.readonly
```

The Search Console API is enabled on the configured quota project and the ADC
principal has only the `Service Usage Consumer` quota role there. Then set the
quota project and verify:

```bash
gcloud auth application-default set-quota-project higuppy-seo-api
python3 tools/indexing_queue.py --gsc-adc --print-report
```

The local GSC runner never copies ADC credentials to the VPS.

The Mac LaunchAgent is versioned at
`deploy/com.doctieuthuyet.gsc-indexing.plist` and runs at **06:50
Asia/Ho_Chi_Minh**, five minutes after the VPS crawl/sitemap queue. Install it
under `~/Library/LaunchAgents/` with `launchctl bootstrap`.

Outputs:

- `latest.json` / `latest.txt`
- timestamped `indexing-queue-YYYYMMDDTHHMMSSZ.json/.txt`
- timestamped files older than 45 days are pruned by default.

## Live schedule

Production copy: `/home/ubuntu/dtt-indexing-queue/indexing_queue.py`

Production outputs: `/home/ubuntu/dtt-indexing-queue/output/`

Private GSC credential: `/home/ubuntu/dtt-indexing-queue/private/gsc-oauth.json` (`0600`, never committed).

The server is UTC. The daily cron runs at `23:45 UTC`, equivalent to **06:45 Asia/Ho_Chi_Minh**, before the 07:00 SEO Daily Watch. `flock -n` prevents overlapping runs.

Google currently documents URL Inspection API quota at 2,000 queries/day and 600 queries/minute per Search Console property. DTT defaults to a bounded 120 inspections/run with 4 workers.

## Secure split automation

The production VPS can keep running the crawl/sitemap queue without owning a
Google refresh token. A trusted Mac can run
`tools/run_indexing_queue_local_gsc.sh` with `--gsc-adc`, then atomically sync
only `latest.json` and `latest.txt` to:

`/home/ubuntu/dtt-indexing-queue/gsc/`

This keeps the broader Google ADC credential off the VPS while still giving the
server a current machine-readable GSC result. The Mac job uses an atomic mkdir
lock and the server job continues independently if the Mac is offline. When no
private GSC credential exists on the VPS, the base queue reports GSC as
`disabled` rather than treating the missing credential as an error.
