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

<?php if ($dtt_is_kiem_lai_wiki) : ?>
    <link rel="stylesheet" href="<?php echo esc_url(get_template_directory_uri() . '/assets/css/kiem-lai-wiki.css?ver=1.0.2'); ?>">
<?php else : ?>
    <link rel="stylesheet" href="<?php echo esc_url(get_template_directory_uri() . '/assets/css/single-post-sync.css?ver=1.0.3'); ?>">
<?php endif; ?>

<main id="primary" class="site-main dtt-single-post<?php echo $dtt_is_kiem_lai_wiki ? ' dtt-kiem-lai-wiki' : ' dtt-article-sync'; ?>">
    <div class="dtt-single-post__inner">
        <?php while (have_posts()) : the_post(); ?>
            <?php
            $categories = get_the_category();
            $primary_category = !empty($categories) ? $categories[0] : null;
            $content_html = apply_filters('the_content', get_the_content());
            $toc_html = '';

            // 1. Try extracting existing Gutenberg / theme TOC block
            if (preg_match('/<nav\\b[^>]*aria-label=["\']Mục lục[^"\']*["\'][^>]*>.*?<\\/nav>/is', $content_html, $toc_match)) {
                $toc_html = $toc_match[0];
                $toc_source_html = $toc_html;
                // Gutenberg can leave a stray closing paragraph tag immediately
                // before the TOC list. Remove that malformed wrapper.
                $toc_html = preg_replace('/<\\/p>\\s*(?=<ol\\b)/i', '', $toc_html);
                $toc_html = preg_replace('/<p>\\s*<\\/p>/i', '', $toc_html);
                $content_html = str_replace($toc_source_html, '', $content_html);
            }

            // 2. Auto-generate TOC if no pre-built TOC exists and article has 2 or more <h2> headings
            if (empty($toc_html) && !$dtt_is_kiem_lai_wiki) {
                if (preg_match_all('/<h2([^>]*)>(.*?)<\\/h2>/is', $content_html, $h2_matches, PREG_SET_ORDER)) {
                    if (count($h2_matches) >= 2) {
                        $toc_items = array();
                        $heading_index = 1;
                        foreach ($h2_matches as $h2_item) {
                            $original_h2 = $h2_item[0];
                            $attrs = $h2_item[1];
                            $heading_title = trim(strip_tags($h2_item[2]));

                            if (empty($heading_title)) {
                                continue;
                            }

                            if (preg_match('/id=["\']([^"\']+)["\']/i', $attrs, $id_match)) {
                                $anchor_id = $id_match[1];
                            } else {
                                $anchor_id = sanitize_title($heading_title);
                                if (empty($anchor_id)) {
                                    $anchor_id = 'muc-' . $heading_index;
                                }
                                $new_h2 = '<h2 id="' . esc_attr($anchor_id) . '"' . $attrs . '>' . $h2_item[2] . '</h2>';
                                $pos = strpos($content_html, $original_h2);
                                if ($pos !== false) {
                                    $content_html = substr_replace($content_html, $new_h2, $pos, strlen($original_h2));
                                }
                            }

                            $toc_items[] = '<li><a href="#' . esc_attr($anchor_id) . '">' . esc_html($heading_title) . '</a></li>';
                            $heading_index++;
                        }

                        if (!empty($toc_items)) {
                            $toc_html = '<nav aria-label="Mục lục bài viết"><div class="dtt-auto-toc__head"><h2>Mục lục</h2></div><ol>' . implode('', $toc_items) . '</ol></nav>';
                        }
                    }
                }
            }

            $dtt_is_kiem_lai_article = $primary_category && $primary_category->slug === 'kiem-lai';
            $dtt_article_return_url = $dtt_is_kiem_lai_article ? home_url('/kiem-lai-wiki/') : home_url('/bai-viet/');
            $dtt_article_return_label = $dtt_is_kiem_lai_article ? 'Về Kiếm Lai Wiki' : 'Về thư viện bài viết';
            $has_toc = !empty($toc_html);
            $dtt_is_b15_hmtg_post = !$dtt_is_kiem_lai_wiki && has_category(179, get_the_ID());
            $dtt_b15_root_url = home_url('/hoan-my-the-gioi-wiki/');
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

            <?php if (!$dtt_is_kiem_lai_wiki) : ?>
                <header class="dtt-post-header">
                    <div class="dtt-article-sync__topline">
                        <a class="dtt-article-sync__back" href="<?php echo esc_url($dtt_article_return_url); ?>">
                            <span aria-hidden="true">←</span>
                            <?php echo esc_html($dtt_article_return_label); ?>
                        </a>
                        <span class="dtt-article-sync__status">Hồ sơ nội dung</span>
                    </div>

                    <?php if ($dtt_is_b15_hmtg_post) : ?>
                        <nav class="dtt-b15-breadcrumb" aria-label="Đường dẫn Hoàn Mỹ Thế Giới">
                            <a href="<?php echo esc_url(home_url('/')); ?>">DTT</a>
                            <span aria-hidden="true">/</span>
                            <?php if (is_single('hoan-my-the-gioi-wiki')) : ?>
                                <span aria-current="page">Hoàn Mỹ Thế Giới Wiki</span>
                            <?php else : ?>
                                <a href="<?php echo esc_url($dtt_b15_root_url); ?>">Hoàn Mỹ Thế Giới Wiki</a>
                                <span aria-hidden="true">/</span>
                                <span aria-current="page"><?php echo esc_html(wp_strip_all_tags(get_the_title())); ?></span>
                            <?php endif; ?>
                        </nav>
                    <?php endif; ?>

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

            <div class="dtt-article-layout <?php echo $has_toc ? 'dtt-article-layout--has-toc' : 'dtt-article-layout--no-toc'; ?>">
                <?php if ($has_toc) : ?>
                    <aside class="dtt-toc-rail" aria-label="Mục lục bài viết">
                        <?php echo $toc_html; ?>
                    </aside>
                <?php endif; ?>

                <article id="post-<?php the_ID(); ?>" <?php post_class('dtt-post-card'); ?>>
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
                    if (child.tagName === 'OL' || child.tagName === 'UL') {
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
        var page = document.querySelector('.dtt-kiem-lai-wiki, .dtt-article-sync');
        if (!page || !window.IntersectionObserver) {
            return;
        }

        var links = Array.prototype.slice.call(
            page.querySelectorAll('.dtt-toc-rail nav[aria-label^="Mục lục"] a[href^="#"]')
        );
        var sections = links.map(function (link) {
            var targetId = link.getAttribute('href').slice(1);
            try {
                return document.getElementById(targetId);
            } catch (e) {
                return null;
            }
        }).filter(Boolean);

        if (!sections.length) {
            return;
        }

        function setActive(id) {
            links.forEach(function (link) {
                var isActive = link.getAttribute('href') === '#' + id;
                link.classList.toggle('is-active', isActive);
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
