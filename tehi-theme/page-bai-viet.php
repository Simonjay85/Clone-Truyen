<?php
/**
 * Dynamic archive for regular WordPress posts.
 *
 * The route is provided by dtt_article_archive_template() in functions.php,
 * so this template does not require a WordPress Page record.
 */
$archive_url = function_exists('dtt_article_archive_url')
    ? dtt_article_archive_url()
    : trailingslashit(home_url('/bai-viet/'));
$paged = max(1, (int) get_query_var('paged'));
$article_fallback_image = get_template_directory_uri() . '/img_data/images/no-image-cover.png?v=3';

$article_hero_css_path = get_template_directory() . '/assets/css/article-hero.css';
if (is_readable($article_hero_css_path)) {
    wp_enqueue_style(
        'dtt-article-hero',
        get_template_directory_uri() . '/assets/css/article-hero.css',
        [],
        (string) filemtime($article_hero_css_path)
    );
}

$article_hero_js_path = get_template_directory() . '/assets/js/article-hero.js';
if (is_readable($article_hero_js_path)) {
    wp_enqueue_script(
        'dtt-article-hero',
        get_template_directory_uri() . '/assets/js/article-hero.js',
        [],
        (string) filemtime($article_hero_js_path),
        true
    );
}

$featured_articles = [];
if (1 === $paged) {
    $featured_query = new WP_Query([
        'post_type'           => 'post',
        'post_status'         => 'publish',
        'posts_per_page'      => 5,
        'ignore_sticky_posts' => true,
        'no_found_rows'       => true,
        'orderby'             => [
            'date' => 'DESC',
            'ID'   => 'DESC',
        ],
    ]);

    while ($featured_query->have_posts()) {
        $featured_query->the_post();
        $featured_categories = get_the_category();
        $featured_excerpt = wp_trim_words(wp_strip_all_tags(get_the_excerpt()), 28, '…');

        $featured_articles[] = [
            'title'    => get_the_title(),
            'url'      => get_permalink(),
            'image'    => has_post_thumbnail()
                ? get_the_post_thumbnail_url(get_the_ID(), 'large')
                : $article_fallback_image,
            'category' => (!empty($featured_categories) && !is_wp_error($featured_categories))
                ? $featured_categories[0]->name
                : '',
            'date'     => get_the_date('d/m/Y'),
            'date_iso' => get_the_date('c'),
            'excerpt'  => $featured_excerpt,
        ];
    }
    wp_reset_postdata();
}

$article_query = new WP_Query([
    'post_type'           => 'post',
    'post_status'         => 'publish',
    'posts_per_page'      => 12,
    'paged'               => $paged,
    // Keep equal-date posts stable across page requests so pagination cannot overlap.
    'orderby'             => [
        'date' => 'DESC',
        'ID'   => 'DESC',
    ],
    'ignore_sticky_posts' => true,
]);

get_header();
?>

<style id="dtt-article-archive-styles">
    .dtt-article-archive-page {
        width: 100%;
        max-width: 1400px;
        margin: 0 auto;
        padding: 34px 18px 70px;
        color: #111827;
    }
    .dtt-article-archive-page,
    .dtt-article-archive-page * { box-sizing: border-box; }
    .dtt-article-archive__summary {
        margin: 0 0 16px;
        color: #6b7280;
        font-size: 12px;
        font-weight: 700;
    }
    .dtt-article-archive__grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 18px;
    }
    .dtt-article-archive-card {
        display: flex;
        min-width: 0;
        flex-direction: column;
        overflow: hidden;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        background: #fff;
        box-shadow: 0 5px 18px rgba(15, 23, 42, .035);
        transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
    }
    .dtt-article-archive-card:hover {
        border-color: rgba(79, 70, 229, .28);
        box-shadow: 0 12px 30px rgba(79, 70, 229, .11);
        transform: translateY(-2px);
    }
    .dtt-article-archive-card__thumb {
        display: block;
        aspect-ratio: 16 / 9;
        overflow: hidden;
        background: #eef2ff;
    }
    .dtt-article-archive-card__thumb img {
        display: block;
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform .35s ease;
    }
    .dtt-article-archive-card:hover .dtt-article-archive-card__thumb img { transform: scale(1.03); }
    .dtt-article-archive-card__body {
        display: flex;
        min-width: 0;
        flex: 1;
        flex-direction: column;
        padding: 17px;
    }
    .dtt-article-archive-card__meta {
        display: flex;
        flex-wrap: wrap;
        gap: 7px;
        margin-bottom: 9px;
        color: #6b7280;
        font-size: 10px;
        font-weight: 700;
    }
    .dtt-article-archive-card__category {
        color: #4f46e5;
        font-weight: 900;
    }
    .dtt-article-archive-card__title {
        min-width: 0;
        margin: 0;
        font-size: 18px;
        font-weight: 850;
        line-height: 1.35;
    }
    .dtt-article-archive-card__title a {
        display: -webkit-box;
        overflow: hidden;
        color: #111827;
        text-decoration: none;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 3;
    }
    .dtt-article-archive-card__title a:hover { color: #4f46e5; }
    .dtt-article-archive-card__excerpt {
        display: -webkit-box;
        overflow: hidden;
        margin: 9px 0 17px;
        color: #6b7280;
        font-size: 13px;
        line-height: 1.65;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 4;
    }
    .dtt-article-archive-card__read {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        margin-top: auto;
        color: #4f46e5;
        font-size: 12px;
        font-weight: 900;
        text-decoration: none;
    }
    .dtt-article-archive-card__read:hover { color: #3730a3; }
    .dtt-article-archive__empty {
        grid-column: 1 / -1;
        padding: 48px 18px;
        border: 1px dashed #cbd5e1;
        border-radius: 18px;
        color: #6b7280;
        text-align: center;
    }
    .dtt-article-archive__pagination {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 7px;
        margin-top: 32px;
    }
    .dtt-article-archive__pagination a,
    .dtt-article-archive__pagination span {
        display: inline-flex;
        min-width: 38px;
        min-height: 38px;
        align-items: center;
        justify-content: center;
        padding: 0 12px;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        background: #fff;
        color: #4b5563;
        font-size: 12px;
        font-weight: 800;
        text-decoration: none;
    }
    .dtt-article-archive__pagination a:hover,
    .dtt-article-archive__pagination .current {
        border-color: #4f46e5;
        background: #4f46e5;
        color: #fff;
    }
    .dtt-article-archive__pagination .dots {
        border-color: transparent;
        background: transparent;
    }
    @media (max-width: 980px) {
        .dtt-article-archive__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    }
    @media (max-width: 620px) {
        .dtt-article-archive-page { padding: 22px 12px 48px; }
        .dtt-article-archive__grid { grid-template-columns: minmax(0, 1fr); gap: 14px; }
        .dtt-article-archive-card__title { font-size: 17px; }
    }
</style>

<div class="dtt-article-archive-page">
    <header class="dtt-article-archive__hero dtt-article-hero<?php echo empty($featured_articles) ? ' dtt-article-hero--empty' : ''; ?>">
        <nav class="dtt-article-archive__breadcrumb" aria-label="Đường dẫn">
            <a href="<?php echo esc_url(home_url('/')); ?>">Trang chủ</a>
            <span aria-hidden="true">/</span>
            <span>Bài viết</span>
        </nav>
        <div class="dtt-article-hero__layout">
            <div class="dtt-article-hero__intro">
                <h1 class="dtt-article-archive__title">Bài viết</h1>
                <p class="dtt-article-archive__intro">Tổng hợp những nội dung mới nhất, kiến thức và bài viết chuyên sâu trên DTT.</p>
            </div>

            <?php if (!empty($featured_articles)) : ?>
                <div class="dtt-article-hero__slider swiper" data-dtt-article-hero role="region" aria-label="Bài viết nổi bật">
                    <div class="swiper-wrapper">
                        <?php foreach ($featured_articles as $featured_index => $featured_article) : ?>
                            <article class="dtt-article-hero__slide swiper-slide">
                                <a class="dtt-article-hero__media" href="<?php echo esc_url($featured_article['url']); ?>" aria-label="Đọc bài viết <?php echo esc_attr($featured_article['title']); ?>">
                                    <img
                                        src="<?php echo esc_url($featured_article['image']); ?>"
                                        alt="<?php echo esc_attr($featured_article['title']); ?>"
                                        width="960"
                                        height="640"
                                        loading="<?php echo 0 === $featured_index ? 'eager' : 'lazy'; ?>"
                                        decoding="async"
                                        <?php if (0 === $featured_index) : ?>fetchpriority="high"<?php endif; ?>
                                    >
                                </a>
                                <div class="dtt-article-hero__content">
                                    <div class="dtt-article-hero__meta">
                                        <?php if ($featured_article['category']) : ?>
                                            <span class="dtt-article-hero__category"><?php echo esc_html($featured_article['category']); ?></span>
                                            <span aria-hidden="true">•</span>
                                        <?php endif; ?>
                                        <time datetime="<?php echo esc_attr($featured_article['date_iso']); ?>"><?php echo esc_html($featured_article['date']); ?></time>
                                    </div>
                                    <h2 class="dtt-article-hero__title"><a href="<?php echo esc_url($featured_article['url']); ?>"><?php echo esc_html($featured_article['title']); ?></a></h2>
                                    <?php if ($featured_article['excerpt']) : ?>
                                        <p class="dtt-article-hero__excerpt"><?php echo esc_html($featured_article['excerpt']); ?></p>
                                    <?php endif; ?>
                                    <a class="dtt-article-hero__read" href="<?php echo esc_url($featured_article['url']); ?>">Đọc bài viết <span aria-hidden="true">→</span></a>
                                </div>
                            </article>
                        <?php endforeach; ?>
                    </div>
                    <div class="dtt-article-hero__controls">
                        <div class="dtt-article-hero__pagination swiper-pagination" aria-label="Chọn bài viết"></div>
                        <div class="dtt-article-hero__navigation" aria-label="Điều khiển slider">
                            <button type="button" class="dtt-article-hero__nav swiper-button-prev" aria-label="Bài viết trước"><span aria-hidden="true">←</span></button>
                            <button type="button" class="dtt-article-hero__nav swiper-button-next" aria-label="Bài viết tiếp theo"><span aria-hidden="true">→</span></button>
                        </div>
                    </div>
                </div>
            <?php endif; ?>
        </div>
    </header>

    <?php if ($article_query->have_posts()) : ?>
        <p class="dtt-article-archive__summary">
            <?php echo esc_html(number_format_i18n((int) $article_query->found_posts)); ?> bài viết
        </p>
        <section class="dtt-article-archive__grid" aria-label="Danh sách bài viết">
            <?php while ($article_query->have_posts()) : $article_query->the_post(); ?>
                <?php
                $article_image = has_post_thumbnail()
                    ? get_the_post_thumbnail_url(get_the_ID(), 'medium_large')
                    : $article_fallback_image;
                $article_categories = get_the_category();
                $article_excerpt = wp_trim_words(wp_strip_all_tags(get_the_excerpt()), 32, '…');
                ?>
                <article class="dtt-article-archive-card">
                    <a class="dtt-article-archive-card__thumb" href="<?php the_permalink(); ?>">
                        <img src="<?php echo esc_url($article_image); ?>" alt="<?php the_title_attribute(); ?>" loading="lazy" decoding="async">
                    </a>
                    <div class="dtt-article-archive-card__body">
                        <div class="dtt-article-archive-card__meta">
                            <?php if (!empty($article_categories) && !is_wp_error($article_categories)) : ?>
                                <span class="dtt-article-archive-card__category"><?php echo esc_html($article_categories[0]->name); ?></span>
                                <span aria-hidden="true">•</span>
                            <?php endif; ?>
                            <time datetime="<?php echo esc_attr(get_the_date('c')); ?>"><?php echo esc_html(get_the_date('d/m/Y')); ?></time>
                        </div>
                        <h2 class="dtt-article-archive-card__title"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
                        <?php if ($article_excerpt) : ?>
                            <p class="dtt-article-archive-card__excerpt"><?php echo esc_html($article_excerpt); ?></p>
                        <?php endif; ?>
                        <a class="dtt-article-archive-card__read" href="<?php the_permalink(); ?>">Đọc bài viết <span aria-hidden="true">→</span></a>
                    </div>
                </article>
            <?php endwhile; ?>
        </section>

        <?php
        $pagination = paginate_links([
            'base'      => trailingslashit($archive_url) . 'page/%#%/',
            'format'    => '',
            'current'   => $paged,
            'total'     => max(1, (int) $article_query->max_num_pages),
            'prev_text' => '← Trước',
            'next_text' => 'Sau →',
            'type'      => 'array',
        ]);
        if (!empty($pagination)) :
        ?>
            <nav class="dtt-article-archive__pagination" aria-label="Phân trang bài viết">
                <?php foreach ($pagination as $page_link) : ?>
                    <?php echo wp_kses_post($page_link); ?>
                <?php endforeach; ?>
            </nav>
        <?php endif; ?>
    <?php else : ?>
        <div class="dtt-article-archive__empty">Chưa có bài viết nào được xuất bản.</div>
    <?php endif; ?>

    <?php wp_reset_postdata(); ?>
</div>

<?php get_footer(); ?>
