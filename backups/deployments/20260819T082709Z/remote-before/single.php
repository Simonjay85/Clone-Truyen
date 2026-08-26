<?php
/**
 * Template for standard WordPress posts.
 *
 * This file intentionally handles only regular posts. Custom post types
 * continue to use their more specific templates, such as single-truyen.php
 * and single-chuong.php.
 *
 * @package Tehi_Theme
 */

$dtt_is_kiem_lai_wiki = is_single('kiem-lai-wiki');
$dtt_wiki_hero_image = get_template_directory_uri() . '/assets/images/kiem-lai-wiki-hero.webp';
get_header();
?>

<style id="dtt-single-post-inline-css">
.dtt-single-post {
    padding: 28px 15px 64px;
}
.dtt-single-post__inner {
    width: min(100%, 1120px);
    margin: 0 auto;
}
.dtt-post-card {
    overflow: hidden;
    background: #fff;
    border: 1px solid rgba(15, 23, 42, .08);
    border-radius: 16px;
    box-shadow: 0 8px 30px rgba(15, 23, 42, .06);
}
.dtt-post-header {
    padding: clamp(24px, 4vw, 48px) clamp(20px, 5vw, 64px) 28px;
    border-bottom: 1px solid #eef0f4;
}
.dtt-post-kicker {
    margin-bottom: 10px;
    color: #6366f1;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: .08em;
    text-transform: uppercase;
}
.dtt-post-title {
    margin: 0;
    color: #111827;
    font-size: clamp(30px, 4vw, 48px);
    font-weight: 800;
    line-height: 1.15;
}
.dtt-post-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 8px 18px;
    margin-top: 16px;
    color: #6b7280;
    font-size: 14px;
}
.dtt-post-meta a {
    color: inherit;
    text-decoration: none;
}
.dtt-post-meta a:hover {
    color: #4f46e5;
}
.dtt-post-featured {
    margin: 0;
    background: #f8fafc;
}
.dtt-post-featured img {
    display: block;
    width: 100%;
    max-height: 560px;
    margin: 0 auto;
    object-fit: cover;
}
.dtt-post-content {
    padding: clamp(24px, 5vw, 64px);
    color: #263244;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 18px;
    line-height: 1.85;
    overflow-wrap: anywhere;
}
.dtt-post-content > *:first-child {
    margin-top: 0;
}
.dtt-post-content > *:last-child {
    margin-bottom: 0;
}
.dtt-post-content h2,
.dtt-post-content h3,
.dtt-post-content h4 {
    margin: 1.6em 0 .55em;
    color: #111827;
    font-family: inherit;
    line-height: 1.3;
}
.dtt-post-content h2 { font-size: 1.55em; }
.dtt-post-content h3 { font-size: 1.3em; }
.dtt-post-content h4 { font-size: 1.12em; }
.dtt-post-content p { margin: 0 0 1.25em; }
.dtt-post-content a {
    color: #4f46e5;
    text-decoration: underline;
    text-underline-offset: 2px;
}
.dtt-post-content img,
.dtt-post-content iframe,
.dtt-post-content video {
    display: block;
    max-width: 100%;
    height: auto;
    margin: 1.5em auto;
}
.dtt-post-content img {
    border-radius: 10px;
    box-shadow: 0 4px 16px rgba(15, 23, 42, .1);
}
.dtt-post-content blockquote {
    margin: 1.5em 0;
    padding: 12px 20px;
    border-left: 4px solid #818cf8;
    background: #f5f7ff;
    color: #4b5563;
}
.dtt-post-content ul,
.dtt-post-content ol {
    margin: 0 0 1.25em;
    padding-left: 1.5em;
}
.dtt-post-content table {
    display: block;
    max-width: 100%;
    overflow-x: auto;
    border-collapse: collapse;
}
.dtt-post-content th,
.dtt-post-content td {
    padding: 8px 12px;
    border: 1px solid #e5e7eb;
}
.dtt-post-footer {
    display: flex;
    flex-wrap: wrap;
    gap: 10px 18px;
    align-items: center;
    padding: 20px clamp(24px, 5vw, 64px) 28px;
    border-top: 1px solid #eef0f4;
    color: #6b7280;
    font-size: 14px;
}
.dtt-post-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
}
.dtt-post-tags a {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 999px;
    background: #eef2ff;
    color: #4f46e5;
    text-decoration: none;
}
.dtt-post-pagination {
    display: flex;
    justify-content: space-between;
    gap: 16px;
    margin-top: 24px;
}
.dtt-post-pagination a {
    display: inline-block;
    padding: 10px 16px;
    border-radius: 10px;
    background: #fff;
    color: #4f46e5;
    box-shadow: 0 4px 16px rgba(15, 23, 42, .06);
    text-decoration: none;
}
:root {
    --dtt-ink: #172033;
    --dtt-muted: #697386;
    --dtt-primary: #5b5bd6;
    --dtt-primary-dark: #4545b8;
    --dtt-surface: #ffffff;
    --dtt-border: rgba(30, 41, 59, .10);
    --dtt-soft: #f5f7ff;
}
.dtt-single-post {
    position: relative;
    isolation: isolate;
    padding: clamp(28px, 5vw, 72px) 16px 88px;
    background: linear-gradient(180deg, #f6f8fc 0%, #eef2f8 100%);
}
.dtt-single-post::before {
    position: absolute;
    z-index: -1;
    top: 0;
    right: 0;
    left: 0;
    height: 240px;
    background: radial-gradient(circle at 15% 0%, rgba(99, 102, 241, .18), transparent 42%),
                radial-gradient(circle at 88% 8%, rgba(14, 165, 233, .13), transparent 34%);
    content: '';
    pointer-events: none;
}
.dtt-single-post__inner {
    width: min(100%, 900px);
}
.dtt-post-card {
    position: relative;
    background: var(--dtt-surface);
    border: 1px solid var(--dtt-border);
    border-radius: 22px;
    box-shadow: 0 18px 55px rgba(30, 41, 59, .10);
}
.dtt-post-card::before {
    position: absolute;
    top: 0;
    right: 12%;
    left: 12%;
    height: 4px;
    border-radius: 0 0 99px 99px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #06b6d4);
    content: '';
}
.dtt-post-header {
    padding: clamp(32px, 6vw, 64px) clamp(22px, 7vw, 78px) 30px;
    border-bottom: 1px solid #edf0f5;
}
.dtt-post-kicker {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-bottom: 16px;
    padding: 6px 12px;
    border: 1px solid rgba(91, 91, 214, .16);
    border-radius: 999px;
    background: #f0f1ff;
    color: var(--dtt-primary-dark);
    font-size: 11px;
    font-weight: 800;
    letter-spacing: .08em;
    line-height: 1;
    text-transform: uppercase;
}
.dtt-post-kicker::before {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #6366f1;
    content: '';
}
.dtt-post-kicker a { color: inherit; text-decoration: none; }
.dtt-post-title {
    max-width: 780px;
    color: var(--dtt-ink);
    font-family: 'Be Vietnam Pro', ui-sans-serif, system-ui, sans-serif;
    font-size: clamp(30px, 5vw, 52px);
    font-weight: 800;
    letter-spacing: -.035em;
    line-height: 1.14;
    text-wrap: balance;
}
.dtt-post-meta {
    align-items: center;
    gap: 8px 16px;
    margin-top: 20px;
    color: var(--dtt-muted);
    font-family: 'Be Vietnam Pro', ui-sans-serif, system-ui, sans-serif;
    font-size: 13px;
}
.dtt-post-meta span {
    display: inline-flex;
    align-items: center;
    gap: 6px;
}
.dtt-post-meta span + span::before {
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: #c8ceda;
    content: '';
}
.dtt-post-meta a { color: var(--dtt-primary); font-weight: 700; }
.dtt-post-featured {
    padding: 20px 22px 0;
    background: linear-gradient(180deg, #fafbff 0%, #fff 100%);
}
.dtt-post-featured img {
    width: min(100%, 820px);
    max-height: 480px;
    border-radius: 16px;
    box-shadow: 0 12px 30px rgba(30, 41, 59, .14);
    object-fit: cover;
}
.dtt-post-content {
    padding: clamp(28px, 7vw, 72px) clamp(22px, 7vw, 78px);
    color: #334155;
    font-family: 'Be Vietnam Pro', ui-sans-serif, system-ui, sans-serif;
    font-size: clamp(17px, 1.6vw, 19px);
    letter-spacing: -.005em;
    line-height: 1.9;
}
.dtt-post-content p { margin: 0 0 1.35em; }
.dtt-post-content h2,
.dtt-post-content h3,
.dtt-post-content h4 {
    position: relative;
    margin: 2em 0 .7em;
    padding-left: 14px;
    color: var(--dtt-ink);
    font-family: 'Be Vietnam Pro', ui-sans-serif, system-ui, sans-serif;
    font-weight: 800;
    letter-spacing: -.02em;
    line-height: 1.35;
}
.dtt-post-content h2::before,
.dtt-post-content h3::before,
.dtt-post-content h4::before {
    position: absolute;
    top: .18em;
    bottom: .18em;
    left: 0;
    width: 4px;
    border-radius: 4px;
    background: linear-gradient(180deg, #6366f1, #06b6d4);
    content: '';
}
.dtt-post-content h2 { font-size: clamp(24px, 3vw, 32px); }
.dtt-post-content h3 { font-size: clamp(21px, 2.5vw, 27px); }
.dtt-post-content h4 { font-size: 1.08em; }
.dtt-post-content a {
    color: var(--dtt-primary-dark);
    font-weight: 600;
    text-decoration-thickness: 1px;
    text-underline-offset: 3px;
}
.dtt-post-content a:hover { color: #3730a3; }
.dtt-post-content img,
.dtt-post-content iframe,
.dtt-post-content video {
    width: auto;
    max-width: 100%;
    border-radius: 14px;
}
.dtt-post-content img { box-shadow: 0 8px 24px rgba(30, 41, 59, .12); }
.dtt-post-content figcaption {
    margin-top: -1em;
    color: var(--dtt-muted);
    font-size: .78em;
    font-style: italic;
    line-height: 1.5;
    text-align: center;
}
.dtt-post-content blockquote {
    position: relative;
    margin: 1.8em 0;
    padding: 18px 22px 18px 28px;
    border: 1px solid #dfe3ff;
    border-left: 4px solid #6366f1;
    border-radius: 0 14px 14px 0;
    background: linear-gradient(135deg, #f7f7ff, #f1faff);
    color: #475569;
}
.dtt-post-content code {
    padding: 2px 6px;
    border-radius: 5px;
    background: #f1f5f9;
    color: #be185d;
    font-size: .88em;
}
.dtt-post-content pre {
    max-width: 100%;
    overflow-x: auto;
    padding: 18px;
    border-radius: 12px;
    background: #111827;
    color: #e5e7eb;
    font-size: .82em;
    line-height: 1.6;
}
.dtt-post-content pre code { padding: 0; background: transparent; color: inherit; }
.dtt-post-content table { width: 100%; margin: 1.5em 0; }
.dtt-post-content th { background: #f5f7ff; color: var(--dtt-ink); font-weight: 800; }
.dtt-post-footer {
    padding: 22px clamp(22px, 7vw, 78px) 30px;
    border-top: 1px solid #edf0f5;
    color: var(--dtt-muted);
    font-family: 'Be Vietnam Pro', ui-sans-serif, system-ui, sans-serif;
}
.dtt-post-tags a {
    padding: 6px 11px;
    border: 1px solid #dde2ff;
    background: #f5f6ff;
    color: var(--dtt-primary-dark);
    font-size: 12px;
    font-weight: 700;
    transition: .2s ease;
}
.dtt-post-tags a:hover {
    background: var(--dtt-primary);
    color: #fff;
    transform: translateY(-1px);
}
.dtt-post-pagination {
    margin-top: 34px;
    padding-top: 22px;
    border-top: 1px dashed #d9dfeb;
}
.dtt-post-pagination a {
    border: 1px solid #e2e6f2;
    background: #fff;
    color: var(--dtt-primary-dark);
    font-weight: 700;
    transition: .2s ease;
}
.dtt-post-pagination a:hover {
    border-color: #b9bdf7;
    background: #f6f7ff;
    transform: translateY(-2px);
}
/* TOC outside article card: desktop sidebar on the far left, inline on mobile. */
@media   (min-width: 1200px) {
    .dtt-single-post__inner {
        width: min(100%, 1190px);
        margin: 0 auto;
    }
    .dtt-article-layout {
        display: grid;
        grid-template-columns: 260px minmax(0, 900px);
        gap: 30px;
        align-items: start;
    }
    .dtt-toc-rail {
        position: sticky;
        top: 96px;
        align-self: start;
        min-width: 0;
    }
}
.dtt-toc-rail nav[aria-label^="Mục lục"] {
    width: 100%;
    max-height: calc(100vh - 124px);
    box-sizing: border-box;
    overflow-y: auto;
    margin: 0;
    padding: 18px 16px 20px;
    border: 1px solid #e2e6f2;
    border-radius: 16px;
    background: linear-gradient(180deg, #fbfcff 0%, #f6f7ff 100%);
    box-shadow: 0 10px 26px rgba(30, 41, 59, .08);
    scrollbar-color: #a8acef transparent;
    scrollbar-width: thin;
}
.dtt-toc-rail nav[aria-label^="Mục lục"]::-webkit-scrollbar { width: 6px; }
.dtt-toc-rail nav[aria-label^="Mục lục"]::-webkit-scrollbar-thumb {
    border-radius: 99px;
    background: #a8acef;
}
.dtt-toc-rail nav[aria-label^="Mục lục"] .dtt-auto-toc__head {
    margin-bottom: 12px;
}
.dtt-toc-rail nav[aria-label^="Mục lục"] .dtt-auto-toc__hint {
    display: block;
    margin-top: 3px;
    color: #8a94a6;
    font-size: 10px;
    line-height: 1.4;
}
.dtt-toc-rail nav[aria-label^="Mục lục"] h2 {
    margin: 0 0 12px;
    color: var(--dtt-ink);
    font-family: 'Be Vietnam Pro', ui-sans-serif, system-ui, sans-serif;
    font-size: 18px;
    font-weight: 800;
    line-height: 1.3;
}
.dtt-toc-rail nav[aria-label^="Mục lục"] ol {
    margin: 0;
    padding-left: 22px;
}
.dtt-toc-rail nav[aria-label^="Mục lục"] li {
    margin: 0;
    color: #8a94a6;
    font-size: 12px;
    line-height: 1.45;
}
.dtt-toc-rail nav[aria-label^="Mục lục"] li + li { margin-top: 7px; }
.dtt-toc-rail nav[aria-label^="Mục lục"] a {
    color: #596174;
    text-decoration: none;
    transition: color .2s ease;
}
.dtt-toc-rail nav[aria-label^="Mục lục"] a:hover,
.dtt-toc-rail nav[aria-label^="Mục lục"] a:focus-visible {
    color: var(--dtt-primary-dark);
    text-decoration: underline;
    text-underline-offset: 3px;
}
.dtt-post-content::after { display: block; clear: both; content: ''; }
.dtt-post-content h2[id],
.dtt-post-content h3[id] { scroll-margin-top: 104px; }
.dtt-toc-rail nav[aria-label^="Mục lục"] li {
    position: relative;
}
.dtt-toc-rail nav[aria-label^="Mục lục"] li > ol {
    margin-top: 7px;
}
.dtt-toc-rail nav[aria-label^="Mục lục"] li.dtt-toc-collapsed > ol {
    display: none;
}
.dtt-toc-toggle {
    display: inline-grid;
    width: 18px;
    height: 18px;
    margin: 0 5px 0 -23px;
    padding: 0;
    place-items: center;
    border: 1px solid #c9cdf5;
    border-radius: 5px;
    background: #fff;
    color: var(--dtt-primary-dark);
    cursor: pointer;
    font: 800 14px/1 system-ui, sans-serif;
    vertical-align: -3px;
    transition: background .2s ease, border-color .2s ease, transform .2s ease;
}
.dtt-toc-toggle:hover,
.dtt-toc-toggle:focus-visible {
    border-color: #8589e8;
    background: #eef0ff;
    outline: none;
}
.dtt-toc-toggle[aria-expanded="false"] { transform: rotate(0deg); }
.dtt-toc-toggle[aria-expanded="true"] { transform: rotate(0deg); }
@media (max-width: 1199px) {
    .dtt-toc-toggle { display: none; }
}

@media (max-width: 1199px) {
    .dtt-toc-rail nav[aria-label^="Mục lục"] {
        float: none;
        position: static;
        width: auto;
        max-height: none;
        margin: 28px 0;
    }
}
#respond {
    position: relative;
    width: min(100%, 900px);
    box-sizing: border-box;
    margin: 30px auto 0;
    padding: clamp(24px, 5vw, 42px) clamp(20px, 5vw, 54px);
    border: 1px solid var(--dtt-border);
    border-radius: 20px;
    background: rgba(255, 255, 255, .96);
    box-shadow: 0 14px 40px rgba(30, 41, 59, .08);
}
#respond::before {
    position: absolute;
    top: 0;
    right: 12%;
    left: 12%;
    height: 3px;
    border-radius: 0 0 99px 99px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #06b6d4);
    content: '';
}
#respond .comment-reply-title {
    margin: 0 0 8px;
    color: var(--dtt-ink);
    font-family: 'Be Vietnam Pro', ui-sans-serif, system-ui, sans-serif;
    font-size: clamp(22px, 3vw, 30px);
    font-weight: 800;
    letter-spacing: -.025em;
    line-height: 1.25;
}
#respond .comment-reply-title small {
    font-size: 12px;
    font-weight: 600;
}
#respond .comment-reply-title small a { color: var(--dtt-primary); }
#respond .comment-notes {
    margin: 0 0 20px;
    color: var(--dtt-muted);
    font-family: 'Be Vietnam Pro', ui-sans-serif, system-ui, sans-serif;
    font-size: 13px;
    line-height: 1.6;
}
#respond .comment-form {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 16px;
    margin: 0;
}
#respond .comment-form p {
    min-width: 0;
    max-width: 100%;
    margin: 0;
}
#respond .comment-form-comment,
#respond .comment-form-cookies-consent,
#respond .form-submit {
    grid-column: 1 / -1;
}
#respond .comment-form label {
    display: block;
    margin: 0 0 7px;
    color: #344054;
    font-family: 'Be Vietnam Pro', ui-sans-serif, system-ui, sans-serif;
    font-size: 13px;
    font-weight: 700;
}
#respond .comment-form .required { color: #e05252; }
#respond .comment-form textarea,
#respond .comment-form input[type="text"],
#respond .comment-form input[type="email"],
#respond .comment-form input[type="url"] {
    display: block;
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
    padding: 11px 13px;
    border: 1px solid #d9deea;
    border-radius: 10px;
    outline: none;
    background: #fbfcff;
    color: var(--dtt-ink);
    font: inherit;
    font-size: 14px;
    line-height: 1.5;
    transition: border-color .2s ease, box-shadow .2s ease, background .2s ease;
}
#respond .comment-form textarea { min-height: 170px; resize: vertical; }
#respond .comment-form textarea:focus,
#respond .comment-form input:focus {
    border-color: #7c83ed;
    background: #fff;
    box-shadow: 0 0 0 4px rgba(99, 102, 241, .12);
}
#respond .comment-form-cookies-consent {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    color: var(--dtt-muted);
    font-size: 12px;
    line-height: 1.55;
}
#respond .comment-form-cookies-consent input {
    width: 15px;
    height: 15px;
    flex: 0 0 auto;
    margin: 2px 0 0;
    accent-color: var(--dtt-primary);
}
#respond .comment-form-cookies-consent label {
    margin: 0;
    color: var(--dtt-muted);
    font-size: 12px;
    font-weight: 500;
}
#respond .form-submit { margin-top: 2px; }
#respond .form-submit input[type="submit"] {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 42px;
    padding: 10px 20px;
    border: 0;
    border-radius: 10px;
    background: linear-gradient(135deg, #6366f1, #4f46e5);
    color: #fff;
    cursor: pointer;
    font-family: 'Be Vietnam Pro', ui-sans-serif, system-ui, sans-serif;
    font-size: 13px;
    font-weight: 800;
    box-shadow: 0 7px 16px rgba(79, 70, 229, .22);
    transition: transform .2s ease, box-shadow .2s ease, filter .2s ease;
}
#respond .form-submit input[type="submit"]:hover {
    filter: brightness(1.05);
    box-shadow: 0 10px 20px rgba(79, 70, 229, .28);
    transform: translateY(-1px);
}
.dtt-single-post .comment-respond,
.dtt-single-post .comment-form,
.dtt-single-post .comment-form p {
    min-width: 0;
    max-width: 100%;
}
.dtt-single-post .comment-form textarea,
.dtt-single-post .comment-form input[type="text"],
.dtt-single-post .comment-form input[type="email"],
.dtt-single-post .comment-form input[type="url"] {
    box-sizing: border-box;
    width: 100%;
    max-width: 100%;
}
.dtt-post-card + .comments-area,
.dtt-post-card ~ .comments-area {
    margin-top: 24px;
    padding: 26px clamp(22px, 5vw, 48px);
    border: 1px solid var(--dtt-border);
    border-radius: 18px;
    background: #fff;
    box-shadow: 0 10px 30px rgba(30, 41, 59, .06);
}
.dtt-related-posts,
#respond {
    content-visibility: auto;
    contain-intrinsic-size: 0 520px;
}
.dtt-related-posts {
    margin-top: 28px;
    padding: clamp(22px, 5vw, 36px);
    border: 1px solid var(--dtt-border);
    border-radius: 20px;
    background: rgba(255, 255, 255, .92);
    box-shadow: 0 12px 34px rgba(30, 41, 59, .07);
}
.dtt-related-head {
    display: flex;
    align-items: end;
    justify-content: space-between;
    gap: 16px;
    margin-bottom: 20px;
}
.dtt-related-title {
    margin: 0;
    color: var(--dtt-ink);
    font-family: 'Be Vietnam Pro', ui-sans-serif, system-ui, sans-serif;
    font-size: clamp(22px, 3vw, 30px);
    font-weight: 800;
    letter-spacing: -.025em;
}
.dtt-related-subtitle {
    margin: 5px 0 0;
    color: var(--dtt-muted);
    font-size: 13px;
}
.dtt-related-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 16px;
}
.dtt-related-card {
    display: flex;
    min-width: 0;
    flex-direction: column;
    overflow: hidden;
    border: 1px solid #e6e9f2;
    border-radius: 14px;
    background: #fff;
    box-shadow: 0 5px 16px rgba(30, 41, 59, .05);
    transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
}
.dtt-related-card:hover {
    border-color: #c9ccff;
    box-shadow: 0 12px 24px rgba(30, 41, 59, .11);
    transform: translateY(-3px);
}
.dtt-related-thumb {
    display: block;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    background: linear-gradient(135deg, #eef2ff, #ecfeff);
}
.dtt-related-thumb img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform .35s ease;
}
.dtt-related-card:hover .dtt-related-thumb img { transform: scale(1.04); }
.dtt-related-placeholder {
    display: grid;
    width: 100%;
    height: 100%;
    place-items: center;
    color: #6366f1;
    font-size: 24px;
    font-weight: 800;
}
.dtt-related-body {
    display: flex;
    min-width: 0;
    flex: 1;
    flex-direction: column;
    padding: 14px 15px 16px;
}
.dtt-related-meta {
    margin-bottom: 7px;
    color: #8a94a6;
    font-size: 11px;
}
.dtt-related-card-title {
    display: -webkit-box;
    overflow: hidden;
    margin: 0;
    color: var(--dtt-ink);
    font-family: 'Be Vietnam Pro', ui-sans-serif, system-ui, sans-serif;
    font-size: 15px;
    font-weight: 800;
    line-height: 1.4;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
}
.dtt-related-card-title a {
    color: inherit;
    text-decoration: none;
}
.dtt-related-card-title a:hover { color: var(--dtt-primary-dark); }
.dtt-related-excerpt {
    display: -webkit-box;
    overflow: hidden;
    margin: 8px 0 12px;
    color: #697386;
    font-size: 12px;
    line-height: 1.55;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
}
.dtt-related-read {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    margin-top: auto;
    color: var(--dtt-primary-dark);
    font-size: 12px;
    font-weight: 800;
    text-decoration: none;
}
.dtt-related-read span { transition: transform .2s ease; }
.dtt-related-card:hover .dtt-related-read span { transform: translateX(3px); }
.dtt-related-empty { margin: 0; color: var(--dtt-muted); font-size: 14px; }
@media (max-width: 900px) {
    .dtt-related-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 640px) {
    .dtt-single-post { padding: 22px 10px 58px; }
    .dtt-post-card { border-radius: 16px; }
    .dtt-post-header { padding-top: 34px; }
    .dtt-post-title { font-size: clamp(28px, 9vw, 38px); letter-spacing: -.025em; }
    .dtt-post-meta { display: grid; gap: 8px; }
    .dtt-post-meta span + span::before { display: none; }
    .dtt-post-featured { padding: 12px 12px 0; }
    .dtt-post-featured img { max-height: 360px; border-radius: 12px; }
    .dtt-post-content { font-size: 17px; line-height: 1.82; }
    .dtt-post-content h2 { font-size: 25px; }
    .dtt-post-content h3 { font-size: 22px; }
    .dtt-post-pagination { flex-direction: column; }
    .dtt-post-pagination a { text-align: center; }
    .dtt-single-post,
    .dtt-single-post * { min-width: 0; }
    #respond {
        width: 100%;
        margin-top: 20px;
        padding: 28px 16px 22px;
        border-radius: 16px;
    }
    #respond .comment-form {
        grid-template-columns: 1fr;
        gap: 12px;
    }
    #respond .comment-form-comment,
    #respond .comment-form-cookies-consent,
    #respond .form-submit { grid-column: auto; }
    #respond .comment-form textarea { min-height: 150px; }
    #respond .form-submit input[type="submit"] { width: 100%; }

    .dtt-single-post .comment-form textarea,
    .dtt-single-post .comment-form input[type="text"],
    .dtt-single-post .comment-form input[type="email"],
    .dtt-single-post .comment-form input[type="url"] {
        box-sizing: border-box;
        width: 100%;
        max-width: 100%;
    }
    .dtt-related-posts { margin-top: 20px; padding: 20px 14px; border-radius: 16px; }
    .dtt-related-head { display: block; margin-bottom: 15px; }
    .dtt-related-subtitle { margin-top: 4px; }
    .dtt-related-grid { grid-template-columns: 1fr; gap: 12px; }
    .dtt-related-card { display: grid; grid-template-columns: 112px minmax(0, 1fr); }
    .dtt-related-thumb { aspect-ratio: 1 / 1; height: 100%; }
    .dtt-related-body { padding: 12px 13px; }
    .dtt-related-excerpt { display: none; }
    .dtt-related-card-title { font-size: 14px; -webkit-line-clamp: 3; }
    .dtt-related-read { margin-top: 8px; }
}
/* Refined TOC motion, depth, and mobile layout. */
.dtt-toc-rail nav[aria-label^="Mục lục"] {
    transition: box-shadow .28s ease, border-color .28s ease, transform .28s ease;
    box-shadow: 0 12px 30px rgba(30, 41, 59, .10), 0 2px 6px rgba(91, 91, 214, .06);
}
.dtt-toc-rail nav[aria-label^="Mục lục"]:hover,
.dtt-toc-rail nav[aria-label^="Mục lục"]:focus-within {
    border-color: rgba(99, 102, 241, .34);
    box-shadow: 0 18px 38px rgba(30, 41, 59, .14), 0 4px 12px rgba(91, 91, 214, .10);
}
.dtt-toc-rail nav[aria-label^="Mục lục"] li > ol {
    display: block;
    max-height: 2200px;
    overflow: hidden;
    margin-top: 7px;
    opacity: 1;
    transition: max-height .34s ease, opacity .24s ease, margin-top .34s ease;
}
.dtt-toc-rail nav[aria-label^="Mục lục"] li.dtt-toc-collapsed > ol {
    display: block;
    max-height: 0;
    margin-top: 0;
    opacity: 0;
}
.dtt-toc-toggle {
    box-shadow: 0 2px 5px rgba(91, 91, 214, .10);
    transition: background .22s ease, border-color .22s ease, box-shadow .22s ease, transform .22s ease;
    touch-action: manipulation;
}
.dtt-toc-toggle:.dtt-toc-toggle:.dtt-toc-toggle:.dtt-toc-toggle:.dtt-toc-toggle:.dtt-toc-toggle:14, .18);
    transform: translateY(-1px);
}
@media (max-width: 1199px) {
    .dtt-article-layout { display: block; }
    .dtt-toc-rail {
                                                            t-toc-rail nav[aria-label^="Mục lục"] {
        max-height: none;
        margin: 0;
        padding: 14px 14px 16px;
        border-radius: 14px;
        box-shadow: 0 8px 22px rgba(30, 41, 59, .10);
    }
    .dtt-toc-rail nav[aria-label^="Mục lục"] h2 {
        margin-bottom: 9px;
        font-size: 16px;
    }
    .dtt-toc-rail nav[aria-label^="Mục lục"] ol {
        padding-left: 20px;
    }
    .dtt-toc-rail nav[aria-label^="Mục lục"] li {
        font-size: 13px;
        line-height: 1.42;
    }
    .dtt-toc-rail nav[aria-label^="Mục lục"] li + li { margin-top: 4px; }
    .dtt-toc-rail nav[aria-label^="Mục lục"] a {
        display: inline-block;
        padding: 2px 0;
    }
    .dtt-toc-rail .dtt-toc-toggle {
        display: inline-grid;
        width: 19px;
        height: 19px;
        margin-left: -24px;
        font-size: 13px;
    }
}
@media (prefers-reduced-motion: reduce) {
    .dtt-toc-rail nav[aria-label^="Mục lục"],
    .dtt-toc-rail nav[aria-label^="Mục lục"] li > ol,
    .dtt-toc-toggle { transition: none; }
}
</style>

<?php if ($dtt_is_kiem_lai_wiki) : ?>
    <link rel="stylesheet" href="<?php echo esc_url(get_template_directory_uri() . '/assets/css/kiem-lai-wiki.css?ver=1.0.0'); ?>">
<?php endif; ?>

<main id="primary" class="site-main dtt-single-post<?php echo $dtt_is_kiem_lai_wiki ? ' dtt-kiem-lai-wiki' : ''; ?>">
    <div class="dtt-single-post__inner">
        <?php while (have_posts()) : the_post(); ?>
            <?php
            $categories = get_the_category();
            $primary_category = !empty($categories) ? $categories[0] : null;
            $content_html = apply_filters('the_content', get_the_content());
            $toc_html = '';
            if (preg_match('/<nav\b[^>]*aria-label=["\x27]Mục lục[^"\x27]*["\x27][^>]*>.*?<\/nav>/is', $content_html, $toc_match)) {
                $toc_html = $toc_match[0];
                $content_html = str_replace($toc_html, '', $content_html);
            }
            ?>
            <?php if ($dtt_is_kiem_lai_wiki) : ?>
                <header class="dtt-kiem-lai-hero" style="--kl-hero-image: url('<?php echo esc_url($dtt_wiki_hero_image); ?>');">
                    <div class="dtt-kiem-lai-hero__content">
                        <nav class="dtt-kiem-lai-breadcrumb" aria-label="Đường dẫn Kiếm Lai Wiki">
                            <a href="<?php echo esc_url(home_url('/')); ?>">DTT</a>
                            <span class="dtt-kiem-lai-breadcrumb__slash" aria-hidden="true">/</span>
                            <?php if ($primary_category) : ?>
                                <a href="<?php echo esc_url(get_category_link($primary_category->term_id)); ?>">
                                    <?php echo esc_html($primary_category->name); ?>
                                </a>
                                <span class="dtt-kiem-lai-breadcrumb__slash" aria-hidden="true">/</span>
                            <?php endif; ?>
                            <span aria-current="page">Wiki trung tâm</span>
                        </nav>

                        <h1 class="dtt-kiem-lai-hero__title">Kiếm Lai <em>Wiki</em></h1>
                        <p class="dtt-kiem-lai-hero__summary">
                            Bản đồ tra cứu thế giới Kiếm Lai — từ Ly Châu và Lạc Phách Sơn đến Kiếm Khí Trường Thành,
                            gom nhân vật, thế lực, cảnh giới và những chặng đường lớn vào một lộ trình dễ khám phá.
                        </p>

                        <div class="dtt-kiem-lai-hero__actions" aria-label="Điều hướng nhanh">
                            <a href="#kiem-lai-noi-gi">Khởi hành từ Ly Châu <span aria-hidden="true">→</span></a>
                            <a href="#thu-vien">Tra thư viện 108 bài <span aria-hidden="true">↗</span></a>
                        </div>

                        <div class="dtt-kiem-lai-hero__stats" aria-label="Tổng quan thư viện Kiếm Lai">
                            <div class="dtt-kiem-lai-hero__stat"><strong>109</strong><span>Bài Kiếm Lai</span></div>
                            <div class="dtt-kiem-lai-hero__stat"><strong>108</strong><span>Bài chuyên sâu</span></div>
                            <div class="dtt-kiem-lai-hero__stat"><strong>05</strong><span>Thiên hạ</span></div>
                            <div class="dtt-kiem-lai-hero__stat"><strong>10</strong><span>Chặng lớn</span></div>
                        </div>
                    </div>
                </header>
            <?php endif; ?>
            <div class="dtt-article-layout">
                <?php if ($toc_html) : ?>
                    <aside class="dtt-toc-rail">
                        <?php echo $toc_html; ?>
                    </aside>
                <?php endif; ?>
            <article id="post-<?php the_ID(); ?>" <?php post_class('dtt-post-card'); ?>>
                <?php if (!$dtt_is_kiem_lai_wiki) : ?>
                    <header class="dtt-post-header">
                        <?php if ($primary_category) : ?>
                            <div class="dtt-post-kicker">
                                <a href="<?php echo esc_url(get_category_link($primary_category->term_id)); ?>">
                                    <?php echo esc_html($primary_category->name); ?>
                                </a>
                            </div>
                        <?php endif; ?>

                        <h1 class="dtt-post-title"><?php the_title(); ?></h1>

                        <div class="dtt-post-meta" aria-label="Thông tin bài viết">
                            <span>Đăng ngày <?php echo esc_html(get_the_date()); ?></span>
                            <?php if (get_the_modified_time('U') !== get_the_time('U')) : ?>
                                <span>Cập nhật <?php echo esc_html(get_the_modified_date()); ?></span>
                            <?php endif; ?>
                            <span>Tác giả <?php the_author_posts_link(); ?></span>
                        </div>
                    </header>
                <?php endif; ?>

                <?php if (has_post_thumbnail()) : ?>
                    <figure class="dtt-post-featured">
                        <?php the_post_thumbnail('full', array(
                            'loading' => 'eager',
                            'decoding' => 'async',
                        )); ?>
                    </figure>
                <?php endif; ?>

                <div class="dtt-post-content entry-content">
                    <?php
                    echo $content_html;

                    wp_link_pages(array(
                        'before' => '<nav class="dtt-post-pagination" aria-label="Phân trang bài viết">',
                        'after'  => '</nav>',
                        'link_before' => '<span>',
                        'link_after'  => '</span>',
                    ));
                    ?>
                </div>

                <?php if (has_tag()) : ?>
                    <footer class="dtt-post-footer">
                        <strong>Thẻ:</strong>
                        <div class="dtt-post-tags">
                            <?php the_tags('', '', ''); ?>
                        </div>
                    </footer>
                <?php endif; ?>
            </article>
            </div>

            <?php
            // Show recent posts from the current post's primary category.
            // The current post is excluded to avoid self-linking.
            $related_args = array(
                'post_type'           => 'post',
                'post__not_in'        => array(get_the_ID()),
                'posts_per_page'      => 3,
                'ignore_sticky_posts' => true,
                'no_found_rows'       => true,
                'orderby'             => 'date',
                'order'               => 'DESC',
            );
            if ($primary_category) {
                $related_args['category__in'] = array($primary_category->term_id);
            }
            $related_query = new WP_Query($related_args);
            ?>

            <?php if ($related_query->have_posts()) : ?>
                <section class="dtt-related-posts" aria-labelledby="dtt-related-title">
                    <div class="dtt-related-head">
                        <div>
                            <h2 id="dtt-related-title" class="dtt-related-title">Bài viết liên quan</h2>
                            <p class="dtt-related-subtitle">Có thể anh sẽ quan tâm</p>
                        </div>
                    </div>
                    <div class="dtt-related-grid">
                        <?php while ($related_query->have_posts()) : $related_query->the_post(); ?>
                            <article class="dtt-related-card">
                                <a class="dtt-related-thumb" href="<?php the_permalink(); ?>" aria-label="Đọc <?php echo esc_attr(get_the_title()); ?>">
                                    <?php if (has_post_thumbnail()) : ?>
                                        <?php the_post_thumbnail('medium_large', array('loading' => 'lazy', 'decoding' => 'async')); ?>
                                    <?php else : ?>
                                        <span class="dtt-related-placeholder" aria-hidden="true">DTT</span>
                                    <?php endif; ?>
                                </a>
                                <div class="dtt-related-body">
                                    <div class="dtt-related-meta"><?php echo esc_html(get_the_date()); ?></div>
                                    <h3 class="dtt-related-card-title">
                                        <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                                    </h3>
                                    <p class="dtt-related-excerpt"><?php echo esc_html(wp_trim_words(get_the_excerpt(), 18, '…')); ?></p>
                                    <a class="dtt-related-read" href="<?php the_permalink(); ?>">Đọc bài viết <span aria-hidden="true">→</span></a>
                                </div>
                            </article>
                        <?php endwhile; ?>
                    </div>
                </section>
                <?php wp_reset_postdata(); ?>
            <?php endif; ?>

            <?php if (comments_open() || get_comments_number()) : ?>
                <?php comments_template(); ?>
            <?php endif; ?>
        <?php endwhile; ?>
    </div>
<script>
(function () {
    function initDttTocToggles() {

        document.querySelectorAll('.dtt-toc-rail nav[aria-label^="Mục lục"]').forEach(function (toc) {
            var toggleIndex = 0;
            toc.querySelectorAll('li').forEach(function (item) {
                var nestedList = null;
                Array.prototype.forEach.call(item.children, function (child) {
                    if (child.tagName === 'OL') {
                        nestedList = child;
                    }
                });

                if (!nestedList || item.querySelector('.dtt-toc-toggle')) {
                    return;
                }

                toggleIndex += 1;
                var button = document.createElement('button');
                var label = item.querySelector(':scope > a');
                var labelText = label ? label.textContent.trim() : 'mục này';
                var controlId = 'dtt-toc-sublist-' + toggleIndex;

                nestedList.id = nestedList.id || controlId;
                var initiallyCollapsed = item.classList.contains('dtt-toc-collapsed');
                button.type = 'button';
                button.className = 'dtt-toc-toggle';
                button.textContent = initiallyCollapsed ? '+' : '−';
                button.setAttribute('aria-expanded', initiallyCollapsed ? 'false' : 'true');
                button.setAttribute('aria-controls', nestedList.id);
                button.setAttribute('aria-label', (initiallyCollapsed ? 'Mở rộng ' : 'Thu gọn ') + labelText);

                button.addEventListener('click', function () {
                    var expanded = button.getAttribute('aria-expanded') === 'true';
                    button.setAttribute('aria-expanded', expanded ? 'false' : 'true');
                    button.textContent = expanded ? '+' : '−';
                    button.setAttribute('aria-label', (expanded ? 'Mở rộng ' : 'Thu gọn ') + labelText);
                    item.classList.toggle('dtt-toc-collapsed', expanded);
                });

                item.insertBefore(button, item.firstChild);
            });
        });
    }

    function initDttWikiScrollspy() {
        var page = document.querySelector('.dtt-kiem-lai-wiki');
        if (!page || !window.IntersectionObserver) {
            return;
        }

        var links = Array.prototype.slice.call(
            page.querySelectorAll('.dtt-toc-rail nav[aria-label^="Mục lục"] a[href^="#"]')
        );
        var sections = links.map(function (link) {
            return document.getElementById(link.getAttribute('href').slice(1));
        }).filter(Boolean);

        if (!sections.length) {
            return;
        }

        function setActive(id) {
            links.forEach(function (link) {
                link.classList.toggle('is-active', link.getAttribute('href') === '#' + id);
            });
        }

        setActive(sections[0].id);
        var observer = new IntersectionObserver(function (entries) {
            var visible = entries.filter(function (entry) { return entry.isIntersecting; });
            if (!visible.length) {
                return;
            }
            visible.sort(function (a, b) {
                return a.boundingClientRect.top - b.boundingClientRect.top;
            });
            setActive(visible[0].target.id);
        }, { rootMargin: '-18% 0px -68% 0px', threshold: [0, 1] });

        sections.forEach(function (section) { observer.observe(section); });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function () {
            initDttTocToggles();
            initDttWikiScrollspy();
        });
    } else {
        initDttTocToggles();
        initDttWikiScrollspy();
    }
}());
</script>

</main>

<?php get_footer(); ?>
