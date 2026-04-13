<?php get_header(); ?>

<!-- TRUYEN MOI CAP NHAT -->
<div class="test-menu-bottom-13-11-2024 pt-4 position-relative z-1 ">
    <div class="row row-cols-1 row-cols-lg-2 g-2 g-lg-5 ps-4 px-lg-0 m-0">

        <!-- COLUMN 1: Truyện mới -->
        <div class="col-12 col-lg-8 ps-0 ps-lg-5 pe-4 pe-lg-0 ">
            <div class="vanhiep-title-chung position-relative mb-3 " style="z-index: 1;">
                <h2 class="bee-home-title text-uppercase m-0 position-relative ">
                    Truyện Mới Cập Nhật                </h2>
            </div>
            
            <div class="row row-cols-2 row-cols-sm-3 row-cols-xl-4 g-2 g-lg-3  position-relative z-bg ">
                <?php
                    $args = array( 'post_type' => 'truyen', 'posts_per_page' => 12 );
                    $truyens = new WP_Query( $args );
                    if ( $truyens->have_posts() ) :
                        while ( $truyens->have_posts() ) : $truyens->the_post();
                ?>
                <!-- ITEM -->
                <div class="col">
                    <div class="mdv-san-pham-box bg-white overflow-hidden text-center position-relative h-100 p-0 shadow-sm transition-all bee-border position-relative " style="z-index: 1;">
                        <a class="mdv-san-pham-img-box d-block position-relative " href="<?php the_permalink(); ?>">
                            <div class="mdv-san-pham-box-img d-block bg-primary text-white d-flex align-items-center justify-content-center" style="height: 180px;">No Image</div>
                            <div class="mdv-san-pham-box-view d-flex justify-content-between position-absolute px-1 text-white gap-2 ">
                                <div class="san-pham-view fw-bold text-shadow d-inline-flex align-items-start position-relative gap-0 gap-lg-1 ">
                                    <i class="fa-solid fa-eye fs-12 mt-1"></i>0
                                </div>
                                <div class="san-pham-chuong fw-bold text-shadow d-inline-flex align-items-start position-relative  gap-0 gap-lg-1 ">
                                    <i class="fa-solid fa-layer-group fs-12 mt-1 "></i>&nbsp;0
                                </div>
                            </div>
                        </a>
                        <div class="px-2 py-3  py-lg-3 ">
                            <h3 class="mdv-san-pham-title text-capitalize m-0 p-0 overflow-hidden line-clamp-2">
                                <a href="<?php the_permalink(); ?>" class="d-inline-flex"><?php the_title(); ?></a>
                            </h3>
                        </div>
                    </div>
                </div>
                <!-- /ITEM -->
                <?php 
                        endwhile;
                        wp_reset_postdata();
                    endif;
                ?>
            </div>
        </div>

        <!-- COLUMN 2: Sidebar (Giả lập Bảng xếp hạng) -->
        <div class="col-12 col-lg-4 px-0 px-lg-4 pe-lg-5 ps-lg-0 test-menu-bottom-13-11-2024-col2 ">
            <div class="row row-cols-1 me-2 me-lg-0 row-gap-3 ">
                <div class="col px-0  mb-2 mb-lg-0  d-flex flex-column h-100">
                    <div class="bee-home-right-title position-relative mb-3 " style="z-index: 1;">
                        <h2 class="bee-home-title text-uppercase m-0 position-relative ">Bảng Xếp Hạng</h2>
                    </div>
                    <div class="bg-white p-3 shadow-sm test-menu-bottom-13-11-2024-bxh bee-border position-relative " style="z-index: 1;">
                        <p style="color:#666; font-style:italic;">Cột bên này sẽ hiển thị BXH truyện, hoặc top user (Sidebar Template).</p>
                    </div>
                </div>
            </div>
        </div>

    </div>
</div>

<?php get_footer(); ?>
