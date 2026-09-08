#!/usr/bin/env python3
"""Build a safe Search Console inspection queue for recent DTT articles.

This tool deliberately does NOT call Google's Indexing API. Normal articles are
prioritized from crawl/indexing signals and surfaced for authorized GSC inspection.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
from urllib.parse import urlsplit, urlunsplit

import requests

DEFAULT_SITE = "https://doctieuthuyet.com"
USER_AGENT = "DTT-Indexing-Queue/1.0 (+https://doctieuthuyet.com/)"


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_z(value: datetime) -> str:
    return value.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_wp_datetime(value: str) -> datetime:
    value = (value or "").strip()
    if not value:
        raise ValueError("empty datetime")
    if value.endswith("Z") or "+" in value[10:]:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    return datetime.fromisoformat(value).replace(tzinfo=timezone.utc)


def parse_iso_datetime(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


def normalize_url(url: str) -> str:
    parts = urlsplit((url or "").strip())
    scheme = parts.scheme.lower() or "https"
    host = (parts.hostname or "").lower()
    port = parts.port
    netloc = host
    if port and not ((scheme == "https" and port == 443) or (scheme == "http" and port == 80)):
        netloc = f"{host}:{port}"
    path = re.sub(r"/{2,}", "/", parts.path or "/")
    if path != "/":
        path = path.rstrip("/") + "/"
    return urlunsplit((scheme, netloc, path, "", ""))


class HeadParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.robots: List[str] = []
        self.canonicals: List[str] = []

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        data = {str(k).lower(): (v or "") for k, v in attrs}
        if tag.lower() == "meta" and data.get("name", "").lower() in {"robots", "googlebot"}:
            if data.get("content"):
                self.robots.append(data["content"].strip())
        elif tag.lower() == "link":
            rel = {part.lower() for part in re.split(r"\s+", data.get("rel", "").strip()) if part}
            if "canonical" in rel and data.get("href"):
                self.canonicals.append(data["href"].strip())


def robots_directives(meta_values: Iterable[str], x_robots: Optional[str]) -> List[str]:
    values = list(meta_values)
    if x_robots:
        values.append(x_robots)
    result: List[str] = []
    for value in values:
        for part in value.split(","):
            token = part.strip().lower()
            if token:
                result.append(token)
    return sorted(set(result))


def is_noindex(directives: Iterable[str]) -> bool:
    return any(token == "noindex" or token.startswith("noindex:") for token in directives)


@dataclass
class AuditRow:
    post_id: int
    title: str
    url: str
    published_gmt: str
    modified_gmt: str
    kind: str
    age_hours: float
    http_status: Optional[int]
    final_url: Optional[str]
    robots: List[str]
    indexable: bool
    canonical: Optional[str]
    canonical_ok: bool
    sitemap: Optional[str]
    sitemap_lastmod: Optional[str]
    sitemap_member: bool
    lastmod_fresh: bool
    lastmod_delta_seconds: Optional[int]
    priority: str
    action: str
    reasons: List[str]


def fetch_sitemap_map(session: requests.Session, site: str, timeout: float) -> Tuple[Dict[str, Tuple[Optional[str], str]], List[str]]:
    response = session.get(f"{site.rstrip('/')}/sitemap_index.xml", timeout=timeout)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    sitemap_urls = [
        node.text.strip()
        for node in root.findall("{*}sitemap/{*}loc")
        if node.text and "post-sitemap" in node.text
    ]
    mapping: Dict[str, Tuple[Optional[str], str]] = {}

    def load_child(sitemap_url: str) -> Tuple[str, bytes]:
        child = session.get(sitemap_url, timeout=timeout)
        child.raise_for_status()
        return sitemap_url, child.content

    with ThreadPoolExecutor(max_workers=min(6, max(1, len(sitemap_urls)))) as pool:
        futures = [pool.submit(load_child, sitemap_url) for sitemap_url in sitemap_urls]
        for future in as_completed(futures):
            sitemap_url, content = future.result()
            child_root = ET.fromstring(content)
            for node in child_root.findall("{*}url"):
                loc = node.find("{*}loc")
                lastmod = node.find("{*}lastmod")
                if loc is None or not loc.text:
                    continue
                mapping[normalize_url(loc.text)] = (
                    lastmod.text.strip() if lastmod is not None and lastmod.text else None,
                    sitemap_url,
                )
    return mapping, sitemap_urls


def fetch_recent_posts(session: requests.Session, site: str, cutoff: datetime, max_posts: int, timeout: float) -> List[dict]:
    """Scan public posts in deterministic ID order, then select recent modifications.

    WordPress REST pagination ordered only by modified time can repeat rows when many
    posts share the same second. ID ordering avoids boundary duplication/gaps while
    still letting us detect recent posts that are accidentally missing from sitemaps.
    """
    endpoint = f"{site.rstrip('/')}/wp-json/wp/v2/posts"
    common = {
        "per_page": 100,
        "orderby": "id",
        "order": "asc",
        "status": "publish",
        "_fields": "id,link,date_gmt,modified_gmt,slug,title,status",
    }
    first = session.get(endpoint, params={**common, "page": 1}, timeout=timeout)
    first.raise_for_status()
    all_posts = list(first.json())
    total_pages = int(first.headers.get("X-WP-TotalPages", "1"))
    for page in range(2, total_pages + 1):
        response = session.get(endpoint, params={**common, "page": page}, timeout=timeout)
        response.raise_for_status()
        all_posts.extend(response.json())

    by_id = {int(post["id"]): post for post in all_posts}
    recent: List[dict] = []
    for post in by_id.values():
        try:
            modified = parse_wp_datetime(post.get("modified_gmt", ""))
        except ValueError:
            continue
        if modified >= cutoff:
            recent.append(post)
    recent.sort(key=lambda post: (parse_wp_datetime(post["modified_gmt"]), int(post["id"])), reverse=True)
    return recent[:max_posts]


def audit_post(session: requests.Session, post: dict, sitemap_map: Dict[str, Tuple[Optional[str], str]], now: datetime, timeout: float, tolerance_seconds: int) -> AuditRow:
    url = normalize_url(post["link"])
    published = parse_wp_datetime(post["date_gmt"])
    modified = parse_wp_datetime(post["modified_gmt"])
    kind = "new" if abs((modified - published).total_seconds()) <= 300 else "updated"
    age_hours = max(0.0, (now - modified).total_seconds() / 3600)

    http_status: Optional[int] = None
    final_url: Optional[str] = None
    directives: List[str] = []
    canonical: Optional[str] = None
    canonical_ok = False
    request_error: Optional[str] = None
    try:
        response = session.get(url, timeout=timeout, allow_redirects=True)
        http_status = response.status_code
        final_url = normalize_url(response.url)
        parser = HeadParser()
        parser.feed(response.text[:2_000_000])
        directives = robots_directives(parser.robots, response.headers.get("X-Robots-Tag"))
        canonical = normalize_url(parser.canonicals[0]) if parser.canonicals else None
        canonical_ok = canonical == url
    except requests.RequestException as exc:
        request_error = f"request_error:{exc.__class__.__name__}"

    sitemap_lastmod, sitemap_url = sitemap_map.get(url, (None, None))
    sitemap_member = sitemap_url is not None
    lastmod_dt = parse_iso_datetime(sitemap_lastmod)
    lastmod_delta: Optional[int] = None
    lastmod_fresh = False
    if lastmod_dt is not None:
        lastmod_delta = int((modified - lastmod_dt).total_seconds())
        lastmod_fresh = lastmod_delta <= tolerance_seconds

    reasons: List[str] = []
    if request_error:
        reasons.append(request_error)
    if http_status != 200:
        reasons.append(f"http_{http_status if http_status is not None else 'error'}")
    if final_url and final_url != url:
        reasons.append("redirected")
    if is_noindex(directives):
        reasons.append("intentional_noindex")
    if not canonical:
        reasons.append("canonical_missing")
    elif not canonical_ok:
        reasons.append("canonical_mismatch")
    if not sitemap_member:
        reasons.append("sitemap_missing")
    elif not lastmod_fresh:
        reasons.append("sitemap_lastmod_stale")

    if "intentional_noindex" in reasons:
        priority, action = "EXCLUDED", "exclude_noindex"
    elif any(
        reason.startswith("request_error")
        or reason.startswith("http_")
        or reason in {"canonical_missing", "canonical_mismatch", "sitemap_missing", "sitemap_lastmod_stale"}
        for reason in reasons
    ):
        priority, action = "P0", "fix_before_gsc"
    elif kind == "new" and age_hours <= 24:
        priority, action = "P1", "gsc_inspect_new"
        reasons.append("new_post_ready_for_gsc")
    elif kind == "updated" and age_hours <= 24:
        priority, action = "P2", "gsc_inspect_updated"
        reasons.append("recent_update_ready_for_gsc")
    elif kind == "new":
        priority, action = "P2", "gsc_inspect_new"
        reasons.append("new_post_ready_for_gsc")
    else:
        priority, action = "P3", "gsc_inspect_updated"
        reasons.append("recent_update_ready_for_gsc")

    return AuditRow(
        post_id=int(post["id"]),
        title=re.sub(r"\s+", " ", (post.get("title") or {}).get("rendered", "")).strip(),
        url=url,
        published_gmt=iso_z(published),
        modified_gmt=iso_z(modified),
        kind=kind,
        age_hours=round(age_hours, 2),
        http_status=http_status,
        final_url=final_url,
        robots=directives,
        indexable=http_status == 200 and not is_noindex(directives),
        canonical=canonical,
        canonical_ok=canonical_ok,
        sitemap=sitemap_url,
        sitemap_lastmod=sitemap_lastmod,
        sitemap_member=sitemap_member,
        lastmod_fresh=lastmod_fresh,
        lastmod_delta_seconds=lastmod_delta,
        priority=priority,
        action=action,
        reasons=reasons,
    )


def report_text(payload: dict) -> str:
    s = payload["summary"]
    lines = [
        "DTT Indexing Queue V1",
        f"Generated: {payload['generated_at']}",
        f"Window: {payload['lookback_hours']}h | selected={s['selected']} | queued={s['queued']} | excluded_noindex={s['excluded_noindex']}",
        f"P0={s['P0']} P1={s['P1']} P2={s['P2']} P3={s['P3']}",
        "",
    ]
    if not payload["queue"]:
        lines.append("Queue is empty.")
    else:
        for row in payload["queue"]:
            lines.append(f"[{row['priority']}] {row['action']} | {row['url']} | {','.join(row['reasons'])}")
    if payload["excluded"]:
        lines += ["", f"Excluded intentional noindex: {len(payload['excluded'])}"]
        lines += [f"[EXCLUDED] {row['url']}" for row in payload["excluded"][:20]]
    return "\n".join(lines) + "\n"


def write_outputs(out_dir: Path, payload: dict, retention_days: int) -> Tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    json_path = out_dir / f"indexing-queue-{stamp}.json"
    text_path = out_dir / f"indexing-queue-{stamp}.txt"
    serialized = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    text = report_text(payload)
    json_path.write_text(serialized, encoding="utf-8")
    text_path.write_text(text, encoding="utf-8")
    (out_dir / "latest.json").write_text(serialized, encoding="utf-8")
    (out_dir / "latest.txt").write_text(text, encoding="utf-8")
    if retention_days > 0:
        cutoff = time.time() - retention_days * 86400
        for pattern in ("indexing-queue-*.json", "indexing-queue-*.txt"):
            for old in out_dir.glob(pattern):
                try:
                    if old.stat().st_mtime < cutoff:
                        old.unlink()
                except OSError:
                    pass
    return json_path, text_path


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Audit recent DTT posts and build a GSC inspection queue.")
    p.add_argument("--site", default=DEFAULT_SITE)
    p.add_argument("--lookback-hours", type=int, default=72)
    p.add_argument("--max-posts", type=int, default=120)
    p.add_argument("--timeout", type=float, default=12.0)
    p.add_argument("--workers", type=int, default=8, help="Concurrent article audits (default: %(default)s)")
    p.add_argument("--lastmod-tolerance-minutes", type=int, default=5)
    p.add_argument("--out-dir", default="output/indexing-queue")
    p.add_argument("--retention-days", type=int, default=45)
    p.add_argument("--print-report", action="store_true")
    return p


def main() -> int:
    args = parser().parse_args()
    if args.lookback_hours <= 0 or args.max_posts <= 0 or args.timeout <= 0 or args.workers <= 0:
        print("lookback-hours, max-posts, timeout and workers must be positive", file=sys.stderr)
        return 2

    site = args.site.rstrip("/")
    generated = now_utc()
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "*/*"})
    try:
        sitemap_map, sitemap_sources = fetch_sitemap_map(session, site, args.timeout)
        posts = fetch_recent_posts(session, site, generated - timedelta(hours=args.lookback_hours), args.max_posts, args.timeout)
    except (requests.RequestException, ET.ParseError, ValueError) as exc:
        print(f"fatal: {exc}", file=sys.stderr)
        return 1

    rows: List[AuditRow] = []
    with ThreadPoolExecutor(max_workers=min(args.workers, max(1, len(posts)))) as pool:
        futures = [
            pool.submit(audit_post, session, post, sitemap_map, generated, args.timeout, args.lastmod_tolerance_minutes * 60)
            for post in posts
        ]
        for future in as_completed(futures):
            rows.append(future.result())
    excluded = [row for row in rows if row.priority == "EXCLUDED"]
    queue = [row for row in rows if row.priority != "EXCLUDED"]
    rank = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    queue.sort(key=lambda row: (rank.get(row.priority, 9), row.age_hours, row.url))

    payload = {
        "schema_version": 1,
        "generated_at": iso_z(generated),
        "site": site,
        "lookback_hours": args.lookback_hours,
        "max_posts": args.max_posts,
        "lastmod_tolerance_minutes": args.lastmod_tolerance_minutes,
        "policy": {
            "google_indexing_api_used": False,
            "purpose": "Prioritize normal articles for crawl-signal fixes and authorized Google Search Console URL Inspection.",
        },
        "sitemap_sources": sitemap_sources,
        "summary": {
            "selected": len(rows),
            "queued": len(queue),
            "excluded_noindex": len(excluded),
            "P0": sum(row.priority == "P0" for row in queue),
            "P1": sum(row.priority == "P1" for row in queue),
            "P2": sum(row.priority == "P2" for row in queue),
            "P3": sum(row.priority == "P3" for row in queue),
        },
        "queue": [asdict(row) for row in queue],
        "excluded": [asdict(row) for row in excluded],
    }
    json_path, text_path = write_outputs(Path(args.out_dir), payload, args.retention_days)
    if args.print_report:
        sys.stdout.write(report_text(payload))
    else:
        print(json.dumps({"ok": True, "json": str(json_path), "report": str(text_path), "summary": payload["summary"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
