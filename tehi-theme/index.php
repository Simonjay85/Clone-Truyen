<?php get_header(); ?>

<!-- MEOKAMMAP CLONE LAYOUT -->
<style>
    body { background-color: #f7f9fa; }
    .mkm-container { max-width: 1200px; margin: 0 auto; padding: 0 15px; }
    
    /* Hero Section */
    .mkm-hero-card { display: flex; background: #fff; border-radius: 12px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 30px; margin-top: 20px;}
    .mkm-hero-img-wrap { width: 250px; flex-shrink: 0; margin-right: 20px; border-radius: 8px; overflow: hidden;}
    .mkm-hero-img-wrap img { width: 100%; height: auto; object-fit: cover; }
    .mkm-hero-info { flex-grow: 1; display: flex; flex-direction: column;}
    .mkm-hero-title { font-size: 24px; font-weight: 700; color: #333; margin-top: 0; margin-bottom: 10px;}
    .mkm-hero-meta { font-size: 13px; color: #888; margin-bottom: 15px; }
    .mkm-badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; margin-right: 5px; }
    .mkm-badge-hot { background: #ff4d4f; color: #fff; }
    .mkm-badge-full { background: #52c41a; color: #fff; }
    .mkm-badge-new { background: #1890ff; color: #fff; }
    .mkm-hero-desc { font-size: 14px; color: #555; line-height: 1.6; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden; margin-bottom: 20px;}
    .mkm-hero-actions .btn { border-radius: 20px; padding: 6px 20px; font-weight: 600; font-size: 14px; margin-right: 10px;}
    .mkm-btn-primary { background-color: #1890ff; color: #fff; border: 1px solid #1890ff;}
    .mkm-btn-outline { background-color: transparent; color: #1890ff; border: 1px solid #1890ff;}
    
    /* Section Title */
    .mkm-section-title { font-size: 20px; font-weight: 700; color: #333; margin-bottom: 15px; display: flex; align-items: center;}
    .mkm-section-title i { color: #1890ff; margin-right: 8px; }
    .mkm-section-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 15px;}
    .mkm-view-all { font-size: 13px; color: #1890ff; text-decoration: none; font-weight: 600;}
    
    /* Grid System */
    .mkm-row { display: flex; flex-wrap: wrap; margin: -10px; }
    .mkm-col-main { width: 75%; padding: 0 10px; }
    .mkm-col-side { width: 25%; padding: 0 10px; }
    
    @media (max-width: 991px) {
        .mkm-col-main, .mkm-col-side { width: 100%; }
        .mkm-hero-card { flex-direction: column; }
        .mkm-hero-img-wrap { width: 100%; margin-right: 0; margin-bottom: 15px;}
    }

    /* Grid Items */
    .mkm-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-bottom: 30px;}
    @media (max-width: 768px) { .mkm-grid { grid-template-columns: repeat(2, 1fr); } }
    
    .mkm-item { background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.04); position: relative;}
    .mkm-item-img-wrap { position: relative; padding-top: 133%; /* 3:4 aspect ratio */ overflow: hidden;}
    .mkm-item-img-wrap img { position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s; }
    .mkm-item:hover .mkm-item-img-wrap img { transform: scale(1.05); }
    
    .mkm-item-badge-top { position: absolute; top: 8px; left: 8px; z-index: 2; }
    .mkm-item-badge-right { position: absolute; top: 8px; right: 8px; z-index: 2; }
    
    .mkm-item-stats { position: absolute; bottom: 0; left: 0; width: 100%; padding: 8px; background: linear-gradient(transparent, rgba(0,0,0,0.7)); color: #fff; font-size: 11px; display: flex; justify-content: space-between; z-index: 2;}
    .mkm-item-info { padding: 10px; }
    .mkm-item-title { font-size: 14px; font-weight: 700; color: #333; margin: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; text-decoration: none;}
    .mkm-item-title:hover { color: #1890ff; }
    .mkm-item-chapter { font-size: 12px; color: #888; margin-top: 4px;}

    /* Sidebar */
    .mkm-widget { background: #fff; border-radius: 12px; padding: 15px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);}
    .mkm-bxh-list { list-style: none; padding: 0; margin: 0; }
    .mkm-bxh-item { display: flex; align-items: center; margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px dashed #eee;}
    .mkm-bxh-item:last-child { margin-bottom: 0; padding-bottom: 0; border-bottom: none;}
    .mkm-bxh-rank { width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-weight: bold; font-size: 12px; margin-right: 10px; flex-shrink: 0;}
    .mkm-rank-1 { background: #ff4d4f; color: #fff; }
    .mkm-rank-2 { background: #ff7a45; color: #fff; }
    .mkm-rank-3 { background: #ffa940; color: #fff; }
    .mkm-rank-other { background: #f0f0f0; color: #888; }
    
    .mkm-bxh-img { width: 40px; height: 50px; border-radius: 4px; object-fit: cover; margin-right: 10px; flex-shrink: 0;}
    .mkm-bxh-info { flex-grow: 1; overflow: hidden; }
    .mkm-bxh-title { font-size: 13px; font-weight: 600; color: #333; margin: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;}
    .mkm-bxh-meta { font-size: 11px; color: #888; margin-top: 3px; }

    /* Tabs */
    .mkm-tabs { display: flex; background: #f0f2f5; border-radius: 20px; padding: 2px; margin-bottom: 15px;}
    .mkm-tab { flex: 1; text-align: center; font-size: 12px; font-weight: 600; padding: 6px 0; border-radius: 18px; cursor: pointer; color: #888;}
    .mkm-tab.active { background: #fff; color: #1890ff; box-shadow: 0 1px 3px rgba(0,0,0,0.1);}

    /* User BXH */
    .mkm-user-item { display: flex; align-items: center; margin-bottom: 12px;}
    .mkm-user-avatar { width: 36px; height: 36px; border-radius: 50%; border: 2px solid #ffd700; margin-right: 10px; object-fit: cover;}
    .mkm-user-meta { font-size: 11px; color: #ff4d4f; font-weight: 600; display: flex; align-items: center;}
</style>

<div class="mkm-container">

    <!-- HERO SECTION -->
    <?php
    // Fetch 1 featured post
    $hero_args = array( 'post_type' => 'truyen', 'posts_per_page' => 1, 'orderby' => 'rand' ); // Replace logic to get 'featured'
    $hero_query = new WP_Query($hero_args);
    if ($hero_query->have_posts()) : while ($hero_query->have_posts()) : $hero_query->the_post();
        $thumb_url = get_the_post_thumbnail_url() ?: get_template_directory_uri().'/img_data/images/no-image-cover.png';
    ?>
    <div class="mkm-hero-card">
        <div class="mkm-hero-img-wrap">
            <img src="<?php echo esc_url($thumb_url); ?>" alt="<?php the_title(); ?>" loading="lazy">
        </div>
        <div class="mkm-hero-info">
            <h1 class="mkm-hero-title"><?php the_title(); ?></h1>
            <div class="mkm-hero-meta">
                <span class="mkm-badge mkm-badge-hot">Đề Cử</span>
                <span class="mkm-badge mkm-badge-full">Hoàn Thành</span>
                <span style="margin-left: 10px;"><i class="fa fa-user"></i> Tác giả: Đang cập nhật</span>
                <span style="margin-left: 10px;"><i class="fa fa-layer-group"></i> Chương: 1230</span>
            </div>
            <div class="mkm-hero-desc">
                <?php echo wp_trim_words(get_the_excerpt(), 40, '...'); ?>
            </div>
            <div class="mkm-hero-actions mt-auto">
                <a href="<?php the_permalink(); ?>" class="btn mkm-btn-primary"><i class="fa fa-book-open"></i> Đọc ngay</a>
                <a href="<?php the_permalink(); ?>#review" class="btn mkm-btn-outline">Xem đánh giá</a>
            </div>
        </div>
    </div>
    <?php endwhile; wp_reset_postdata(); endif; ?>

    <div class="mkm-row">
        <!-- MAIN CONTENT (Trái 75%) -->
        <div class="mkm-col-main">
            
            <!-- MỚI CẬP NHẬT -->
            <div class="mkm-section-header">
                <div class="mkm-section-title"><i class="fa-solid fa-cloud-arrow-up"></i> Mới cập nhật</div>
                <a href="<?php echo get_site_url(); ?>/truyen-moi-cap-nhat.html" class="mkm-view-all">Xem tất cả <i class="fa fa-angle-right"></i></a>
            </div>
            
            <div class="mkm-grid">
                <?php
                $new_args = array( 'post_type' => 'truyen', 'posts_per_page' => 8 );
                $new_query = new WP_Query($new_args);
                if ($new_query->have_posts()) : while ($new_query->have_posts()) : $new_query->the_post();
                    $thumb_url = get_the_post_thumbnail_url() ?: get_template_directory_uri().'/img_data/images/no-image-cover.png';
                ?>
                <div class="mkm-item">
                    <a href="<?php the_permalink(); ?>" rel="bookmark">
                        <div class="mkm-item-img-wrap">
                            <span class="mkm-badge mkm-badge-new mkm-item-badge-top">MỚI</span>
                            <img src="<?php echo esc_url($thumb_url); ?>" alt="<?php the_title(); ?>" loading="lazy">
                            <div class="mkm-item-stats">
                                <span><i class="fa fa-eye"></i> <?php echo rand(1000, 5000); ?></span>
                                <span><i class="fa fa-list"></i> <?php echo rand(100, 500); ?></span>
                            </div>
                        </div>
                    </a>
                    <div class="mkm-item-info">
                        <a href="<?php the_permalink(); ?>" class="mkm-item-title"><?php the_title(); ?></a>
                        <div class="mkm-item-chapter text-muted text-truncate">Chương mới nhất</div>
                    </div>
                </div>
                <?php endwhile; wp_reset_postdata(); endif; ?>
            </div>

            <!-- TRUYỆN HOT -->
            <div class="mkm-section-header" style="margin-top: 40px;">
                <div class="mkm-section-title"><i class="fa-solid fa-fire" style="color: #ff4d4f;"></i> Truyện hot</div>
                <a href="#" class="mkm-view-all">Xem tất cả <i class="fa fa-angle-right"></i></a>
            </div>
            
            <div class="mkm-grid">
                <?php
                $hot_args = array( 'post_type' => 'truyen', 'posts_per_page' => 4, 'orderby' => 'comment_count' );
                $hot_query = new WP_Query($hot_args);
                if ($hot_query->have_posts()) : while ($hot_query->have_posts()) : $hot_query->the_post();
                    $thumb_url = get_the_post_thumbnail_url() ?: get_template_directory_uri().'/img_data/images/no-image-cover.png';
                ?>
                <div class="mkm-item">
                    <a href="<?php the_permalink(); ?>">
                        <div class="mkm-item-img-wrap">
                            <span class="mkm-badge mkm-badge-hot mkm-item-badge-top">HOT</span>
                            <img src="<?php echo esc_url($thumb_url); ?>" alt="<?php the_title(); ?>" loading="lazy">
                            <div class="mkm-item-stats">
                                <span><i class="fa fa-eye"></i> <?php echo rand(5000, 20000); ?></span>
                            </div>
                        </div>
                    </a>
                    <div class="mkm-item-info">
                        <a href="<?php the_permalink(); ?>" class="mkm-item-title"><?php the_title(); ?></a>
                    </div>
                </div>
                <?php endwhile; wp_reset_postdata(); endif; ?>
            </div>

            <!-- TRUYỆN FULL -->
            <div class="mkm-section-header" style="margin-top: 40px;">
                <div class="mkm-section-title"><i class="fa-solid fa-check-circle" style="color: #52c41a;"></i> Truyện full</div>
                <a href="<?php echo get_site_url(); ?>/hoan-thanh.html" class="mkm-view-all">Xem tất cả <i class="fa fa-angle-right"></i></a>
            </div>
            
            <div class="mkm-grid">
                <?php
                $full_args = array( 'post_type' => 'truyen', 'posts_per_page' => 4 );
                $full_query = new WP_Query($full_args);
                if ($full_query->have_posts()) : while ($full_query->have_posts()) : $full_query->the_post();
                    $thumb_url = get_the_post_thumbnail_url() ?: get_template_directory_uri().'/img_data/images/no-image-cover.png';
                ?>
                <div class="mkm-item">
                    <a href="<?php the_permalink(); ?>">
                        <div class="mkm-item-img-wrap">
                            <span class="mkm-badge mkm-badge-full mkm-item-badge-top">FULL</span>
                            <img src="<?php echo esc_url($thumb_url); ?>" alt="<?php the_title(); ?>" loading="lazy">
                        </div>
                    </a>
                    <div class="mkm-item-info">
                        <a href="<?php the_permalink(); ?>" class="mkm-item-title"><?php the_title(); ?></a>
                    </div>
                </div>
                <?php endwhile; wp_reset_postdata(); endif; ?>
            </div>

        </div>

        <!-- SIDEBAR (Phải 25%) -->
        <div class="mkm-col-side">
            
            <!-- Widget BXH -->
            <div class="mkm-widget">
                <div class="mkm-section-title" style="font-size: 16px;"><i class="fa-solid fa-ranking-star" style="color: #ffaa00;"></i> Bảng xếp hạng</div>
                <div class="mkm-tabs">
                    <div class="mkm-tab active">Thứ Ảo</div>
                    <div class="mkm-tab">Lượt Thích</div>
                    <div class="mkm-tab">Đọc Nhiều</div>
                </div>
                
                <ul class="mkm-bxh-list">
                    <?php
                    $bxh_args = array( 'post_type' => 'truyen', 'posts_per_page' => 10 );
                    $bxh_query = new WP_Query($bxh_args);
                    $rank = 1;
                    if ($bxh_query->have_posts()) : while ($bxh_query->have_posts()) : $bxh_query->the_post();
                        $thumb = get_the_post_thumbnail_url() ?: get_template_directory_uri().'/img_data/images/no-image-cover.png';
                        $rank_class = ($rank <= 3) ? "mkm-rank-$rank" : "mkm-rank-other";
                    ?>
                    <li class="mkm-bxh-item">
                        <div class="mkm-bxh-rank <?php echo $rank_class; ?>"><?php echo $rank; ?></div>
                        <img src="<?php echo esc_url($thumb); ?>" class="mkm-bxh-img" alt="" loading="lazy">
                        <div class="mkm-bxh-info">
                            <a href="<?php the_permalink(); ?>" class="mkm-bxh-title" style="text-decoration: none; display: block;"><?php the_title(); ?></a>
                            <div class="mkm-bxh-meta"><i class="fa fa-eye"></i> <?php echo rand(10000, 99999); ?></div>
                        </div>
                    </li>
                    <?php $rank++; endwhile; wp_reset_postdata(); endif; ?>
                </ul>
            </div>

            <!-- Widget User BXH (Mock) -->
            <div class="mkm-widget">
                <div class="mkm-section-title" style="font-size: 16px;"><i class="fa-solid fa-crown" style="color: #ffaa00;"></i> Bảng xếp hạng User</div>
                <div class="mkm-tabs">
                    <div class="mkm-tab active">Cống hiến</div>
                    <div class="mkm-tab">Đề cử</div>
                </div>
                
                <div class="mkm-user-item">
                    <img src="<?php echo get_template_directory_uri(); ?>/templates/images/meo.png" class="mkm-user-avatar" alt="user">
                    <div>
                        <div style="font-size: 13px; font-weight: 600; color: #333;">Lão Nhị Tehi</div>
                        <div class="mkm-user-meta"><i class="fa-solid fa-chess-queen" style="color: #ffd700; margin-right: 4px;"></i> Đại Thánh 8 Đời</div>
                    </div>
                </div>
                <div class="mkm-user-item">
                    <img src="<?php echo get_template_directory_uri(); ?>/templates/images/meo.png" class="mkm-user-avatar" alt="user" style="border-color: #c0c0c0;">
                    <div>
                        <div style="font-size: 13px; font-weight: 600; color: #333;">Thẩm Nguyệt</div>
                        <div class="mkm-user-meta" style="color: #888;"><i class="fa-solid fa-star" style="margin-right: 4px;"></i> Trúc Cơ Kỳ</div>
                    </div>
                </div>
                <div class="mkm-user-item">
                    <img src="<?php echo get_template_directory_uri(); ?>/templates/images/meo.png" class="mkm-user-avatar" alt="user" style="border-color: #cd7f32;">
                    <div>
                        <div style="font-size: 13px; font-weight: 600; color: #333;">Nhiếp Phong</div>
                        <div class="mkm-user-meta" style="color: #888;"><i class="fa-solid fa-star" style="margin-right: 4px;"></i> Luyện Khí Kỳ</div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</div>

<?php get_footer(); ?>
