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
GSC_SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
GSC_SITES_URL = "https://www.googleapis.com/webmasters/v3/sites"
GSC_INSPECT_URL = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"


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


class GscError(RuntimeError):
    """A bounded Search Console auth/API failure safe to surface in reports."""


def load_gsc_credentials(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    required = ["client_id", "client_secret", "refresh_token"]
    missing = [key for key in required if not str(data.get(key, "")).strip()]
    if missing:
        raise GscError(f"credential_missing_fields:{','.join(missing)}")
    scopes = data.get("scopes") or []
    if isinstance(scopes, str):
        scopes = [item for item in re.split(r"[ ,]+", scopes.strip()) if item]
    if scopes and GSC_SCOPE not in scopes:
        raise GscError("credential_missing_webmasters_readonly_scope")
    return data


def refresh_gsc_access_token(session: requests.Session, credentials: dict, timeout: float) -> str:
    response = session.post(
        str(credentials.get("token_uri") or GOOGLE_TOKEN_URL),
        data={
            "client_id": credentials["client_id"],
            "client_secret": credentials["client_secret"],
            "refresh_token": credentials["refresh_token"],
            "grant_type": "refresh_token",
        },
        timeout=timeout,
    )
    if not response.ok:
        raise GscError(f"token_refresh_http_{response.status_code}")
    token = str(response.json().get("access_token") or "").strip()
    if not token:
        raise GscError("token_refresh_missing_access_token")
    return token


def load_gsc_adc_access_token() -> Tuple[str, Optional[str]]:
    """Load local ADC lazily so VPS installs do not need google-auth packages."""
    try:
        import google.auth  # type: ignore
        from google.auth.transport.requests import Request as GoogleAuthRequest  # type: ignore
    except ImportError as exc:
        raise GscError("google_auth_package_missing_for_adc") from exc
    try:
        credentials, _ = google.auth.default(scopes=[GSC_SCOPE])
        credentials.refresh(GoogleAuthRequest())
    except Exception as exc:
        raise GscError(f"adc_refresh_failed:{exc.__class__.__name__}") from exc
    token = str(getattr(credentials, "token", "") or "").strip()
    if not token:
        raise GscError("adc_refresh_missing_access_token")
    quota_project = str(getattr(credentials, "quota_project_id", "") or "").strip() or None
    return token, quota_project


def gsc_headers(access_token: str, quota_project: Optional[str] = None) -> dict:
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT,
    }
    if quota_project:
        headers["X-Goog-User-Project"] = quota_project
    return headers


def verify_gsc_property(
    session: requests.Session,
    access_token: str,
    site_url: str,
    timeout: float,
    quota_project: Optional[str] = None,
) -> dict:
    response = session.get(
        GSC_SITES_URL,
        headers=gsc_headers(access_token, quota_project),
        timeout=timeout,
    )
    if not response.ok:
        raise GscError(f"sites_list_http_{response.status_code}")
    sites = response.json().get("siteEntry") or []
    match = next((row for row in sites if row.get("siteUrl") == site_url), None)
    if not match:
        raise GscError("property_not_available_to_oauth_grant")
    return {
        "site_url": site_url,
        "permission_level": match.get("permissionLevel"),
    }


def inspect_gsc_url(
    session: requests.Session,
    access_token: str,
    site_url: str,
    inspection_url: str,
    timeout: float,
    language_code: str,
    quota_project: Optional[str] = None,
) -> dict:
    last_status: Optional[int] = None
    last_error: Optional[str] = None
    for attempt in range(3):
        try:
            response = session.post(
                GSC_INSPECT_URL,
                headers=gsc_headers(access_token, quota_project),
                json={
                    "inspectionUrl": inspection_url,
                    "siteUrl": site_url,
                    "languageCode": language_code,
                },
                timeout=timeout,
            )
        except requests.RequestException as exc:
            last_error = exc.__class__.__name__
            if attempt < 2:
                time.sleep(1.5 * (attempt + 1))
                continue
            raise GscError(f"inspect_request_error:{last_error}") from exc
        last_status = response.status_code
        if response.ok:
            return response.json().get("inspectionResult") or {}
        if response.status_code not in {429, 500, 502, 503, 504}:
            raise GscError(f"inspect_http_{response.status_code}")
        time.sleep(1.5 * (attempt + 1))
    raise GscError(f"inspect_http_{last_status or last_error or 'error'}")


def normalize_gsc_result(result: dict, expected_url: str) -> dict:
    index = result.get("indexStatusResult") or {}
    google_canonical = index.get("googleCanonical")
    user_canonical = index.get("userCanonical")
    normalized_google = normalize_url(google_canonical) if google_canonical else None
    normalized_user = normalize_url(user_canonical) if user_canonical else None
    expected = normalize_url(expected_url)
    canonical_match = normalized_google in {None, expected, normalized_user}
    coverage = str(index.get("coverageState") or "").strip()
    coverage_lower = coverage.lower()
    verdict = str(index.get("verdict") or "").strip().upper()
    indexing_state = str(index.get("indexingState") or "").strip()
    robots_state = str(index.get("robotsTxtState") or "").strip()
    fetch_state = str(index.get("pageFetchState") or "").strip()

    if indexing_state not in {"", "INDEXING_ALLOWED", "INDEXING_STATE_UNSPECIFIED"}:
        classification = "blocked_from_indexing"
        recommended_action = "fix_gsc_indexing_block"
    elif robots_state and robots_state not in {"ALLOWED", "ROBOTS_TXT_STATE_UNSPECIFIED"}:
        classification = "robots_blocked"
        recommended_action = "fix_gsc_robots_block"
    elif fetch_state and fetch_state not in {"SUCCESSFUL", "PAGE_FETCH_STATE_UNSPECIFIED"}:
        classification = "fetch_problem"
        recommended_action = "fix_gsc_fetch_problem"
    elif normalized_google and not canonical_match:
        classification = "google_canonical_mismatch"
        recommended_action = "review_google_canonical"
    elif verdict == "PASS":
        classification = "indexed"
        recommended_action = "monitor_indexed"
    elif "crawled" in coverage_lower and "not indexed" in coverage_lower:
        classification = "crawled_not_indexed"
        recommended_action = "review_content_quality_and_duplication"
    elif "discovered" in coverage_lower and "not indexed" in coverage_lower:
        classification = "discovered_not_indexed"
        recommended_action = "strengthen_discovery_and_internal_links"
    elif "unknown" in coverage_lower or "not on google" in coverage_lower:
        classification = "unknown_to_google"
        recommended_action = "strengthen_discovery_and_consider_manual_request"
    elif (
        verdict == "NEUTRAL"
        and not index.get("lastCrawlTime")
        and indexing_state in {"", "INDEXING_STATE_UNSPECIFIED"}
        and robots_state in {"", "ROBOTS_TXT_STATE_UNSPECIFIED"}
        and fetch_state in {"", "PAGE_FETCH_STATE_UNSPECIFIED"}
    ):
        classification = "unknown_to_google"
        recommended_action = "strengthen_discovery_and_consider_manual_request"
    elif verdict in {"FAIL", "NEUTRAL"}:
        classification = "not_indexed_other"
        recommended_action = "review_gsc_coverage_state"
    else:
        classification = "gsc_state_unknown"
        recommended_action = "review_gsc_response"

    return {
        "inspected": True,
        "verdict": index.get("verdict"),
        "coverage_state": index.get("coverageState"),
        "robots_txt_state": index.get("robotsTxtState"),
        "indexing_state": index.get("indexingState"),
        "last_crawl_time": index.get("lastCrawlTime"),
        "page_fetch_state": index.get("pageFetchState"),
        "google_canonical": google_canonical,
        "user_canonical": user_canonical,
        "google_canonical_matches": canonical_match,
        "crawled_as": index.get("crawledAs"),
        "sitemaps": index.get("sitemap") or [],
        "referring_urls": index.get("referringUrls") or [],
        "mobile_usability_verdict": (result.get("mobileUsabilityResult") or {}).get("verdict"),
        "rich_results_verdict": (result.get("richResultsResult") or {}).get("verdict"),
        "inspection_result_link": result.get("inspectionResultLink"),
        "classification": classification,
        "recommended_action": recommended_action,
        "manual_request_candidate": classification
        in {"crawled_not_indexed", "discovered_not_indexed", "unknown_to_google", "not_indexed_other"},
    }


def apply_gsc_priority(row: dict) -> None:
    gsc = row.get("gsc") or {}
    classification = gsc.get("classification")
    if not gsc.get("inspected"):
        return
    if classification in {"blocked_from_indexing", "robots_blocked", "fetch_problem", "google_canonical_mismatch"}:
        row["priority"] = "P0"
        row["action"] = gsc.get("recommended_action") or "fix_gsc_issue"
        row["reasons"].append(f"gsc:{classification}")
    elif classification in {"crawled_not_indexed", "discovered_not_indexed", "unknown_to_google", "not_indexed_other"}:
        if row.get("priority") != "P0":
            row["priority"] = "P1"
        row["action"] = gsc.get("recommended_action") or "review_gsc_indexing"
        row["reasons"].append(f"gsc:{classification}")
    elif classification == "indexed":
        row["action"] = "monitor_indexed"
        row["reasons"].append("gsc:indexed")


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
        "DTT Indexing Queue V2",
        f"Generated: {payload['generated_at']}",
        f"Window: {payload['lookback_hours']}h | selected={s['selected']} | queued={s['queued']} | excluded_noindex={s['excluded_noindex']}",
        f"P0={s['P0']} P1={s['P1']} P2={s['P2']} P3={s['P3']}",
        f"GSC: {payload['gsc']['status']} | inspected={s['gsc_inspected']} indexed={s['gsc_indexed']} not_indexed={s['gsc_not_indexed']} errors={s['gsc_errors']}",
        "",
    ]
    if not payload["queue"]:
        lines.append("Queue is empty.")
    else:
        for row in payload["queue"]:
            gsc = row.get("gsc") or {}
            gsc_note = ""
            if gsc.get("inspected"):
                gsc_note = f" | GSC={gsc.get('classification')} / {gsc.get('coverage_state') or gsc.get('verdict') or 'unknown'}"
            elif gsc.get("error"):
                gsc_note = f" | GSC_ERROR={gsc.get('error')}"
            lines.append(f"[{row['priority']}] {row['action']} | {row['url']} | {','.join(row['reasons'])}{gsc_note}")
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
    p.add_argument("--gsc-credentials", default="", help="Path to a private read-only Google OAuth credential JSON.")
    p.add_argument("--gsc-adc", action="store_true", help="Use local Google Application Default Credentials instead of a credential file.")
    p.add_argument("--gsc-site-url", default="sc-domain:doctieuthuyet.com", help="Exact Search Console property identifier.")
    p.add_argument("--gsc-limit", type=int, default=120, help="Max URL Inspection API calls per run (default: %(default)s).")
    p.add_argument("--gsc-workers", type=int, default=4, help="Concurrent URL Inspection calls (default: %(default)s).")
    p.add_argument("--gsc-language", default="en-US")
    p.add_argument("--print-report", action="store_true")
    return p


def main() -> int:
    args = parser().parse_args()
    if args.lookback_hours <= 0 or args.max_posts <= 0 or args.timeout <= 0 or args.workers <= 0 or args.gsc_limit < 0 or args.gsc_workers <= 0:
        print("lookback-hours, max-posts, timeout, workers and gsc-workers must be positive; gsc-limit cannot be negative", file=sys.stderr)
        return 2
    if args.gsc_adc and args.gsc_credentials:
        print("choose either --gsc-adc or --gsc-credentials, not both", file=sys.stderr)
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
    queue_rows = [row for row in rows if row.priority != "EXCLUDED"]
    rank = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    queue_rows.sort(key=lambda row: (rank.get(row.priority, 9), row.age_hours, row.url))

    queue = [asdict(row) for row in queue_rows]
    excluded_payload = [asdict(row) for row in excluded]
    gsc_state = {
        "status": "disabled",
        "site_url": args.gsc_site_url,
        "permission_level": None,
        "credential_path_configured": bool(args.gsc_credentials),
        "auth_mode": "adc" if args.gsc_adc else ("credential_file" if args.gsc_credentials else "off"),
        "quota_project_configured": False,
        "error": None,
    }
    if args.gsc_adc or args.gsc_credentials:
        credential_path = Path(args.gsc_credentials).expanduser()
        if args.gsc_credentials and not credential_path.is_file():
            gsc_state["status"] = "auth_required"
            gsc_state["error"] = "credentials_file_missing"
        else:
            try:
                quota_project: Optional[str] = None
                if args.gsc_adc:
                    access_token, quota_project = load_gsc_adc_access_token()
                else:
                    credentials = load_gsc_credentials(credential_path)
                    access_token = refresh_gsc_access_token(session, credentials, args.timeout)
                    quota_project = str(credentials.get("quota_project_id") or "").strip() or None
                property_info = verify_gsc_property(
                    session,
                    access_token,
                    args.gsc_site_url,
                    args.timeout,
                    quota_project,
                )
                gsc_state.update(
                    {
                        "status": "connected",
                        "permission_level": property_info.get("permission_level"),
                        "quota_project_configured": bool(quota_project),
                    }
                )
                targets = [row for row in queue if row["priority"] != "P0"][: args.gsc_limit]

                def inspect_target(row: dict) -> Tuple[str, dict]:
                    try:
                        raw = inspect_gsc_url(
                            session,
                            access_token,
                            args.gsc_site_url,
                            row["url"],
                            args.timeout,
                            args.gsc_language,
                            quota_project,
                        )
                        return row["url"], normalize_gsc_result(raw, row["url"])
                    except (requests.RequestException, GscError, ValueError) as exc:
                        return row["url"], {"inspected": False, "error": str(exc)}

                results: Dict[str, dict] = {}
                if targets:
                    with ThreadPoolExecutor(max_workers=min(args.gsc_workers, len(targets))) as pool:
                        futures = [pool.submit(inspect_target, row) for row in targets]
                        for future in as_completed(futures):
                            url, result = future.result()
                            results[url] = result
                for row in queue:
                    if row["url"] in results:
                        row["gsc"] = results[row["url"]]
                        apply_gsc_priority(row)
                    else:
                        row["gsc"] = {"inspected": False, "skipped": "not_selected_for_gsc"}
            except (OSError, json.JSONDecodeError, requests.RequestException, GscError, ValueError) as exc:
                gsc_state["status"] = "error"
                gsc_state["error"] = str(exc)

    queue.sort(key=lambda row: (rank.get(row["priority"], 9), row["age_hours"], row["url"]))
    gsc_inspected = [row for row in queue if (row.get("gsc") or {}).get("inspected")]
    gsc_errors = [row for row in queue if (row.get("gsc") or {}).get("error")]
    gsc_indexed = [row for row in gsc_inspected if row["gsc"].get("classification") == "indexed"]
    gsc_not_indexed = [
        row
        for row in gsc_inspected
        if row["gsc"].get("classification")
        in {"crawled_not_indexed", "discovered_not_indexed", "unknown_to_google", "not_indexed_other"}
    ]

    payload = {
        "schema_version": 2,
        "generated_at": iso_z(generated),
        "site": site,
        "lookback_hours": args.lookback_hours,
        "max_posts": args.max_posts,
        "lastmod_tolerance_minutes": args.lastmod_tolerance_minutes,
        "policy": {
            "google_indexing_api_used": False,
            "gsc_url_inspection_api_read_only": True,
            "purpose": "Prioritize normal articles using live crawl signals plus authorized read-only Google Search Console URL Inspection.",
        },
        "gsc": gsc_state,
        "sitemap_sources": sitemap_sources,
        "summary": {
            "selected": len(rows),
            "queued": len(queue),
            "excluded_noindex": len(excluded),
            "P0": sum(row["priority"] == "P0" for row in queue),
            "P1": sum(row["priority"] == "P1" for row in queue),
            "P2": sum(row["priority"] == "P2" for row in queue),
            "P3": sum(row["priority"] == "P3" for row in queue),
            "gsc_inspected": len(gsc_inspected),
            "gsc_indexed": len(gsc_indexed),
            "gsc_not_indexed": len(gsc_not_indexed),
            "gsc_errors": len(gsc_errors),
        },
        "queue": queue,
        "excluded": excluded_payload,
    }
    json_path, text_path = write_outputs(Path(args.out_dir), payload, args.retention_days)
    if args.print_report:
        sys.stdout.write(report_text(payload))
    else:
        print(json.dumps({"ok": True, "json": str(json_path), "report": str(text_path), "summary": payload["summary"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
