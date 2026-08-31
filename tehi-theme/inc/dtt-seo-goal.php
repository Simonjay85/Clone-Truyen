<?php
/**
 * DTT SEO Goal Loop runtime layer (Batch 7–8).
 *
 * - stronger discovery/archive metadata;
 * - curated editorial copy for the strongest genre landing pages;
 * - chapter title/description/OG/schema/navigation relation to the parent story.
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

function dtt_goal_trim_title_words( $text, $max_chars = 58 ) {
    $text = trim( preg_replace( '/\s+/u', ' ', wp_strip_all_tags( (string) $text ) ) );
    if ( mb_strlen( $text, 'UTF-8' ) <= $max_chars ) {
        return $text;
    }
    $cut = mb_substr( $text, 0, $max_chars + 1, 'UTF-8' );
    $space = mb_strrpos( $cut, ' ', 0, 'UTF-8' );
    if ( false !== $space && $space > (int) ( $max_chars * .65 ) ) {
        $cut = mb_substr( $cut, 0, $space, 'UTF-8' );
    } else {
        $cut = mb_substr( $cut, 0, $max_chars, 'UTF-8' );
    }
    return rtrim( $cut, " \t\n\r\0\x0B,.;:!?—–-" ) . '…';
}

function dtt_goal_trim_description_chars( $text, $max_chars = 158 ) {
    $text = trim( preg_replace( '/\s+/u', ' ', wp_strip_all_tags( html_entity_decode( (string) $text, ENT_QUOTES | ENT_HTML5, 'UTF-8' ) ) ) );
    if ( mb_strlen( $text, 'UTF-8' ) <= $max_chars ) {
        return $text;
    }
    $cut = mb_substr( $text, 0, $max_chars + 1, 'UTF-8' );
    $space = mb_strrpos( $cut, ' ', 0, 'UTF-8' );
    if ( false !== $space && $space > (int) ( $max_chars * .72 ) ) {
        $cut = mb_substr( $cut, 0, $space, 'UTF-8' );
    } else {
        $cut = mb_substr( $cut, 0, $max_chars, 'UTF-8' );
    }
    return rtrim( $cut, " \t\n\r\0\x0B,.;:!?—–-" ) . '…';
}

/** Keep story SERP titles useful without changing the long editorial H1/slug. */
function dtt_goal_story_serp_title( $title ) {
    if ( ! is_singular( 'truyen' ) ) {
        return $title;
    }
    $clean = trim( preg_replace( '/\s+/u', ' ', wp_strip_all_tags( html_entity_decode( (string) $title, ENT_QUOTES | ENT_HTML5, 'UTF-8' ) ) ) );
    $has_site     = (bool) preg_match( '/\s+-\s+DTT\s*$/u', $clean );
    $site_suffix  = $has_site ? ' - DTT' : '';
    $without_site = preg_replace( '/\s+-\s+DTT\s*$/u', '', $clean );
    $story_id     = get_queried_object_id();
    $status       = function_exists( 'tehi_get_verified_story_status' ) ? tehi_get_verified_story_status( $story_id ) : '';

    // Completed short-title stories get a concise "Full" modifier for stronger
    // SERP intent; long editorial titles stay untouched except safe truncation.
    if ( 'hoan-thanh' === $status && ! preg_match( '/\bFull\b/ui', $without_site ) ) {
        $full_candidate = trim( $without_site ) . ' Full' . $site_suffix;
        if ( mb_strlen( $full_candidate, 'UTF-8' ) <= 65 ) {
            return $full_candidate;
        }
    }
    if ( mb_strlen( $clean, 'UTF-8' ) <= 65 ) {
        return $clean;
    }

    $parts = preg_split( '/\s*[|:—–]\s*/u', $without_site, 2 );
    if ( ! empty( $parts[0] ) ) {
        $first = trim( $parts[0] );
        $candidate = $first . $site_suffix;
        if ( mb_strlen( $first, 'UTF-8' ) >= 28 && mb_strlen( $candidate, 'UTF-8' ) <= 65 ) {
            return $candidate;
        }
    }
    $max_base = $has_site ? 55 : 62;
    return dtt_goal_trim_title_words( $without_site, $max_base ) . $site_suffix;
}
add_filter( 'pre_get_document_title', 'dtt_goal_story_serp_title', 950 );
add_filter( 'rank_math/frontend/title', 'dtt_goal_story_serp_title', 950 );

/** Improve a small set of thin static-route snippets found by the final crawl. */
function dtt_goal_static_route_meta() {
    $path = function_exists( 'dtt_seo_request_path' ) ? dtt_seo_request_path() : trim( (string) parse_url( $_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH ), '/' );
    $map = array(
        'gioi-thieu' => array(
            'title'       => 'Giới Thiệu DTT - Thư Viện Truyện & Wiki',
            'description' => 'Tìm hiểu DTT, thư viện đọc truyện và Wiki tiểu thuyết với nội dung được tổ chức theo truyện, chương, thể loại, nhân vật và chủ đề để tra cứu thuận tiện.',
        ),
        'nhom-dich' => array(
            'title'       => 'Nhóm Dịch & Cộng Tác Nội Dung - DTT',
            'description' => 'Khám phá thông tin nhóm dịch và cộng tác nội dung trên DTT, cùng các đầu truyện và chương được liên kết để người đọc theo dõi nguồn nội dung rõ ràng hơn.',
        ),
        'dieu-khoan-su-dung' => array(
            'description' => 'Đọc điều khoản sử dụng DTT để hiểu quyền, trách nhiệm, nguyên tắc sử dụng nội dung và các quy định áp dụng khi truy cập hoặc tương tác với website.',
        ),
        'lien-he-quang-cao' => array(
            'description' => 'Liên hệ DTT về quảng cáo, hợp tác nội dung và các đề xuất thương mại phù hợp với trải nghiệm đọc truyện, Wiki tiểu thuyết và cộng đồng độc giả.',
        ),
        'chinh-sach-bao-mat' => array(
            'description' => 'Xem chính sách bảo mật DTT để biết cách website xử lý dữ liệu, cookie, thông tin kỹ thuật và các lựa chọn liên quan đến quyền riêng tư của người dùng.',
        ),
        'khieu-nai-ban-quyen' => array(
            'description' => 'Gửi khiếu nại bản quyền tới DTT với thông tin nhận diện nội dung, căn cứ quyền sở hữu và chi tiết liên hệ để website có thể kiểm tra và xử lý phù hợp.',
        ),
    );
    return $map[ $path ] ?? array();
}

function dtt_goal_static_route_title( $title ) {
    $meta = dtt_goal_static_route_meta();
    return ! empty( $meta['title'] ) ? $meta['title'] : $title;
}
add_filter( 'pre_get_document_title', 'dtt_goal_static_route_title', 960 );
add_filter( 'rank_math/frontend/title', 'dtt_goal_static_route_title', 960 );

/** Normalize story descriptions and fill the static-route descriptions audited as thin/missing. */
function dtt_goal_final_description_polish( $description ) {
    $meta = dtt_goal_static_route_meta();
    if ( ! empty( $meta['description'] ) ) {
        return $meta['description'];
    }
    if ( ! is_singular( 'truyen' ) ) {
        return $description;
    }

    $story_id  = get_queried_object_id();
    // Preserve the two legacy Rank Math descriptions exactly as stored. They
    // rendered correctly before the CTR prefix pass, while rewriting them can
    // make Rank Math suppress the tag for these old rows.
    if ( in_array( (int) $story_id, array( 2067, 3743 ), true ) && '' !== trim( (string) $description ) ) {
        return $description;
    }
    $candidate = trim( preg_replace( '/\s+/u', ' ', wp_strip_all_tags( html_entity_decode( (string) $description, ENT_QUOTES | ENT_HTML5, 'UTF-8' ) ) ) );
    if ( '' === $candidate ) {
        $candidate = has_excerpt( $story_id ) ? get_the_excerpt( $story_id ) : get_post_field( 'post_content', $story_id );
        $candidate = trim( preg_replace( '/\s+/u', ' ', wp_strip_all_tags( html_entity_decode( (string) $candidate, ENT_QUOTES | ENT_HTML5, 'UTF-8' ) ) ) );
    }

    $status = function_exists( 'tehi_get_verified_story_status' ) ? tehi_get_verified_story_status( $story_id ) : '';
    $count  = function_exists( 'tehi_get_chapter_count' ) ? tehi_get_chapter_count( $story_id ) : 0;
    $prefix = '';
    if ( 'hoan-thanh' === $status && $count > 0 && ! preg_match( '/^Trọn bộ\b/ui', $candidate ) ) {
        $prefix = 'Trọn bộ ' . number_format_i18n( $count ) . ' chương. ';
    }
    $candidate = trim( $prefix . $candidate );
    $candidate = dtt_goal_trim_description_chars( $candidate, 158 );
    if ( mb_strlen( $candidate, 'UTF-8' ) < 120 && $count > 0 ) {
        $suffix = ' Đọc từ Chương 1 trên DTT.';
        if ( mb_strlen( $candidate . $suffix, 'UTF-8' ) <= 158 ) {
            $candidate .= $suffix;
        }
    }
    return $candidate;
}
add_filter( 'rank_math/frontend/description', 'dtt_goal_final_description_polish', 950 );

/** Final guard in case another late filter empties a valid story description. */
function dtt_goal_story_description_final_guard( $description ) {
    if ( ! is_singular( 'truyen' ) ) {
        return $description;
    }
    $clean = trim( (string) $description );
    if ( '' !== $clean ) {
        return $description;
    }
    $story_id = get_queried_object_id();
    $description = trim( (string) get_post_meta( $story_id, 'rank_math_description', true ) );
    if ( '' === $description ) {
        $description = has_excerpt( $story_id ) ? get_the_excerpt( $story_id ) : get_post_field( 'post_content', $story_id );
    }
    return dtt_goal_final_description_polish( $description );
}
add_filter( 'rank_math/frontend/description', 'dtt_goal_story_description_final_guard', 9999 );

/** Curated descriptions only for the strongest live genre inventories. */
function dtt_goal_genre_editorial_copy( $slug, $term_name = '', $count = 0 ) {
    $map = array(
        'sang-van' => array(
            'summary' => 'Sảng văn tập trung vào cảm giác thỏa mãn khi nhân vật vượt nghịch cảnh, đảo chiều tình thế hoặc từng bước giành lại vị thế bằng năng lực và lựa chọn của chính mình. Nhịp truyện thường rõ mục tiêu, xung đột dễ nắm và có những điểm bùng nổ tạo cảm giác “đã” cho người đọc.',
            'fit'     => 'Phù hợp nếu bạn thích nhịp nhanh, cao trào liên tục và muốn thấy kết quả của quá trình phản công tương đối sớm thay vì chờ quá lâu cho một nút thắt được giải quyết.',
        ),
        'do-thi-va-mat-2' => array(
            'summary' => 'Đô thị vả mặt đặt mâu thuẫn trong bối cảnh hiện đại như công sở, kinh doanh, gia đình hoặc các mối quan hệ xã hội. Trọng tâm là những màn đảo ngược nhận định khi nhân vật từng bị coi thường chứng minh năng lực, vị thế hoặc sự thật bằng hành động cụ thể.',
            'fit'     => 'Nhóm này hợp với người thích bối cảnh đời thường, xung đột trực diện và payoff nhanh, đặc biệt khi các nút thắt danh dự, nghề nghiệp hay địa vị được giải quyết dứt khoát.',
        ),
        'va-mat' => array(
            'summary' => 'Vả mặt là mô-típ xoay quanh việc một nhân vật bị đánh giá sai, chèn ép hoặc phủ nhận rồi tạo ra cú đảo chiều khiến bên đối đầu phải nhìn nhận lại. Sức hút nằm ở quá trình gieo mâu thuẫn, tích lũy bằng chứng và thời điểm sự thật hoặc năng lực được phơi bày.',
            'fit'     => 'Phù hợp với độc giả thích xung đột rõ ràng, tiết tấu nhanh và những màn phản chuyển có kết quả cụ thể thay vì kéo dài hiểu lầm quá lâu.',
        ),
        'do-thi-thuong-chien' => array(
            'summary' => 'Đô thị thương chiến khai thác cạnh tranh kinh doanh trong bối cảnh hiện đại: công ty, hợp đồng, thị trường, quyền kiểm soát và lựa chọn chiến lược. Mâu thuẫn thường không chỉ đến từ tiền bạc mà còn từ niềm tin, lợi ích và cách các nhân vật đọc tình thế.',
            'fit'     => 'Nên chọn nhóm này nếu bạn thích đấu trí, quyết định kinh doanh và những cú xoay chuyển vị thế được xây dựng từ thông tin, quan hệ và năng lực xử lý khủng hoảng.',
        ),
        'hien-dai' => array(
            'summary' => 'Truyện hiện đại dùng đời sống đương đại làm nền cho các mối quan hệ, công việc, gia đình và lựa chọn cá nhân. Bối cảnh quen thuộc giúp xung đột gần với trải nghiệm hàng ngày, từ tình cảm và sự nghiệp đến áp lực xã hội và những thay đổi trong cách nhân vật nhìn chính mình.',
            'fit'     => 'Phù hợp khi bạn muốn một không gian dễ nhập truyện, nhân vật có nghề nghiệp và đời sống quen thuộc, đồng thời vẫn có nhiều sắc thái từ nhẹ nhàng đến kịch tính.',
        ),
        'hao-mon' => array(
            'summary' => 'Hào môn xoay quanh những gia đình nhiều tài sản và ảnh hưởng, nơi quan hệ tình cảm thường đan xen với quyền lực, thừa kế, danh tiếng và lợi ích giữa các thế hệ. Điểm hấp dẫn nằm ở khoảng cách giữa vẻ ngoài hào nhoáng và những xung đột kín bên trong gia tộc.',
            'fit'     => 'Hợp với người thích drama gia đình, mối quan hệ nhiều tầng và các lựa chọn phải cân bằng giữa tình cảm, địa vị và trách nhiệm.',
        ),
        'nu-cuong' => array(
            'summary' => 'Nữ cường đặt nữ nhân vật trung tâm vào vị trí chủ động: tự ra quyết định, phát triển năng lực và trực tiếp xử lý xung đột thay vì chỉ phản ứng với hoàn cảnh. “Mạnh” có thể đến từ trí tuệ, nghề nghiệp, bản lĩnh, kỹ năng hoặc khả năng giữ quyền tự quyết.',
            'fit'     => 'Phù hợp nếu bạn ưu tiên nữ chính có mục tiêu rõ, có đường phát triển riêng và giữ vai trò quyết định trong các bước ngoặt quan trọng.',
        ),
        'co-dai' => array(
            'summary' => 'Truyện cổ đại sử dụng bối cảnh cổ phong hoặc xã hội tiền hiện đại để triển khai câu chuyện về gia tộc, hôn nhân, quyền lực, sinh kế và trật tự lễ nghi. Không gian này tạo ra những giới hạn xã hội khác hiện đại, từ đó làm lựa chọn của nhân vật trở nên đặc biệt hơn.',
            'fit'     => 'Nên đọc nếu bạn thích bối cảnh cổ phong, quan hệ gia tộc hoặc cung đình và muốn theo dõi cách nhân vật xoay xở trong những quy tắc xã hội chặt chẽ.',
        ),
        'xuyen-khong' => array(
            'summary' => 'Xuyên không bắt đầu khi nhân vật rời bối cảnh quen thuộc để bước sang một thời đại, thế giới hoặc thân phận khác. Sự chênh lệch về kiến thức, thói quen và quy tắc sống tạo ra cả lợi thế lẫn rủi ro, đồng thời mở đường cho quá trình thích nghi và thay đổi bản thân.',
            'fit'     => 'Phù hợp với độc giả thích cảm giác khám phá thế giới mới, sự khác biệt văn hóa và những tình huống nhân vật phải học lại cách tồn tại từ đầu.',
        ),
        'am-thuc' => array(
            'summary' => 'Truyện ẩm thực lấy món ăn, nghề bếp hoặc việc kinh doanh đồ ăn làm một phần quan trọng của cốt truyện. Món ăn có thể là mục tiêu nghề nghiệp, phương tiện kết nối nhân vật hoặc cách kể về ký ức, gia đình và quá trình xây dựng cuộc sống.',
            'fit'     => 'Hợp với người thích không khí đời thường, mô tả món ăn, quá trình làm nghề và những câu chuyện phát triển từng bước từ kỹ năng thực tế.',
        ),
        'cung-dau' => array(
            'summary' => 'Cung đấu đặt nhân vật trong môi trường quyền lực có thứ bậc, nơi lời nói, liên minh, gia thế và thông tin đều có thể trở thành lợi thế. Xung đột thường phát triển qua nhiều lớp mưu lược thay vì chỉ dựa vào đối đầu trực tiếp.',
            'fit'     => 'Phù hợp nếu bạn thích đấu trí, quan hệ chằng chịt và các quyết định phải tính đến hậu quả chính trị hoặc vị thế trong một hệ thống khép kín.',
        ),
        'ngoi-thu-nhat' => array(
            'summary' => 'Ngôi thứ nhất kể câu chuyện trực tiếp qua điểm nhìn “tôi”, vì vậy người đọc tiếp cận sự kiện qua trải nghiệm, cảm xúc và giới hạn nhận thức của chính người kể. Cách kể này thường tạo cảm giác gần gũi và khiến việc nhận ra sự thật diễn ra cùng nhịp với nhân vật.',
            'fit'     => 'Hợp với người thích giọng kể cá nhân, cảm giác nhập vai mạnh và những câu chuyện mà góc nhìn chủ quan là một phần quan trọng của trải nghiệm đọc.',
        ),
    );

    if ( empty( $map[ $slug ] ) ) {
        return array();
    }

    $copy = $map[ $slug ];
    $copy['name']  = $term_name;
    $copy['count'] = max( 0, (int) $count );
    return $copy;
}

/**
 * Visible answer-first block for Wiki/SEO posts.
 *
 * Batch 2 already maintains reviewed, unique Rank Math descriptions. Reusing
 * that concise answer as visible copy keeps the SERP promise and on-page
 * answer aligned instead of inventing a second summary at render time.
 */
function dtt_goal_wiki_answer_first( $post_id = 0 ) {
    $post_id = $post_id ?: get_queried_object_id();
    if ( ! $post_id || ! function_exists( 'dtt_seo_b2_is_wiki_post' ) || ! dtt_seo_b2_is_wiki_post( $post_id ) ) {
        return array();
    }

    $description = trim( (string) get_post_meta( $post_id, 'rank_math_description', true ) );
    if ( '' === $description ) {
        $description = trim( (string) get_post_meta( $post_id, '_yoast_wpseo_metadesc', true ) );
    }
    $description = trim( preg_replace( '/\s+/u', ' ', wp_strip_all_tags( html_entity_decode( $description, ENT_QUOTES | ENT_HTML5, 'UTF-8' ) ) ) );
    if ( mb_strlen( $description, 'UTF-8' ) < 60 ) {
        return array();
    }

    $hub_map = array(
        160 => array('label' => 'Kiếm Lai Wiki', 'url' => home_url('/kiem-lai-wiki/')),
        177 => array('label' => 'Già Thiên Wiki', 'url' => home_url('/gia-thien-wiki/')),
        175 => array('label' => 'Quỷ Bí Chi Chủ Wiki', 'url' => home_url('/quy-bi-chi-chu-wiki/')),
        165 => array('label' => 'Phàm Nhân Tu Tiên Wiki', 'url' => home_url('/pham-nhan-tu-tien-wiki/')),
        174 => array('label' => 'Phàm Nhân Tu Tiên Wiki', 'url' => home_url('/pham-nhan-tu-tien-wiki/')),
        164 => array('label' => 'Tiên Nghịch Wiki', 'url' => home_url('/tien-nghich-wiki/')),
        179 => array('label' => 'Hoàn Mỹ Thế Giới Wiki', 'url' => home_url('/hoan-my-the-gioi-wiki/')),
    );
    $hub = array();
    foreach ( $hub_map as $category_id => $item ) {
        if ( has_category( $category_id, $post_id ) ) {
            $hub = $item;
            break;
        }
    }

    return array(
        'answer'    => $description,
        'hub_label' => $hub['label'] ?? '',
        'hub_url'   => $hub['url'] ?? '',
    );
}

/** Add one canonical BreadcrumbList for the bounded Hoàn Mỹ Thế Giới post cluster. */
function dtt_goal_b15_breadcrumb_schema( $data, $jsonld = null ) {
    if ( ! is_singular( 'post' ) || ! has_category( 179 ) ) {
        return $data;
    }

    $has_breadcrumb = false;
    $scan = function ( $node ) use ( &$scan, &$has_breadcrumb ) {
        if ( ! is_array( $node ) || $has_breadcrumb ) {
            return;
        }
        $type = $node['@type'] ?? '';
        $types = is_array( $type ) ? $type : array( $type );
        if ( in_array( 'BreadcrumbList', $types, true ) ) {
            $has_breadcrumb = true;
            return;
        }
        foreach ( $node as $child ) {
            $scan( $child );
        }
    };
    $scan( $data );
    if ( $has_breadcrumb ) {
        return $data;
    }

    $post_id    = get_queried_object_id();
    $post_url   = get_permalink( $post_id );
    $post_title = trim( wp_strip_all_tags( get_the_title( $post_id ) ) );
    if ( ! $post_id || ! $post_url || ! $post_title ) {
        return $data;
    }

    $root       = get_page_by_path( 'hoan-my-the-gioi-wiki', OBJECT, 'post' );
    $root_id    = $root instanceof WP_Post ? (int) $root->ID : 0;
    $root_url   = $root_id ? get_permalink( $root_id ) : home_url( '/hoan-my-the-gioi-wiki/' );
    $root_title = $root_id ? trim( wp_strip_all_tags( get_the_title( $root_id ) ) ) : 'Hoàn Mỹ Thế Giới Wiki';
    $items      = array(
        array( '@type' => 'ListItem', 'position' => 1, 'name' => 'Trang chủ', 'item' => home_url( '/' ) ),
    );

    if ( $root_id && $root_id === (int) $post_id ) {
        $items[] = array( '@type' => 'ListItem', 'position' => 2, 'name' => $post_title, 'item' => $post_url );
    } else {
        $items[] = array( '@type' => 'ListItem', 'position' => 2, 'name' => $root_title, 'item' => $root_url );
        $items[] = array( '@type' => 'ListItem', 'position' => 3, 'name' => $post_title, 'item' => $post_url );
    }

    $data['dttB15Breadcrumb'] = array(
        '@type'           => 'BreadcrumbList',
        '@id'             => trailingslashit( $post_url ) . '#breadcrumb',
        'itemListElement' => $items,
    );
    return $data;
}
add_filter( 'rank_math/json_ld', 'dtt_goal_b15_breadcrumb_schema', 710, 2 );

function dtt_goal_chapter_parent_id( $chapter_id = 0 ) {
    $chapter_id = $chapter_id ?: get_queried_object_id();
    if ( ! $chapter_id || 'chuong' !== get_post_type( $chapter_id ) ) {
        return 0;
    }
    return absint( get_post_meta( $chapter_id, '_truyen_id', true ) );
}

function dtt_goal_chapter_cover_url( $chapter_id = 0 ) {
    $parent_id = dtt_goal_chapter_parent_id( $chapter_id );
    if ( ! $parent_id ) {
        return '';
    }
    $image = get_the_post_thumbnail_url( $parent_id, 'full' );
    if ( ! $image ) {
        $image = get_template_directory_uri() . '/img_data/images/no-image-cover-v5.png?v=5';
    }
    return $image;
}

function dtt_goal_chapter_title( $title ) {
    if ( ! is_singular( 'chuong' ) ) {
        return $title;
    }
    $chapter_id   = get_queried_object_id();
    $chapter      = trim( wp_strip_all_tags( get_the_title( $chapter_id ) ) );
    $parent_id    = dtt_goal_chapter_parent_id( $chapter_id );
    $parent_title = $parent_id ? trim( wp_strip_all_tags( get_the_title( $parent_id ) ) ) : '';
    if ( ! $parent_title ) {
        return $chapter ?: $title;
    }
    $candidate = $chapter . ' | ' . $parent_title;
    if ( mb_strlen( $candidate, 'UTF-8' ) <= 60 ) {
        return $candidate;
    }
    if ( preg_match( '/\bChương\s+([0-9]+)\b/ui', $chapter, $m ) ) {
        return dtt_goal_trim_title_words( 'Chương ' . $m[1] . ' | ' . $parent_title, 60 );
    }
    return dtt_goal_trim_title_words( $candidate, 60 );
}
add_filter( 'pre_get_document_title', 'dtt_goal_chapter_title', 700 );
add_filter( 'rank_math/frontend/title', 'dtt_goal_chapter_title', 700 );

function dtt_goal_chapter_description( $description ) {
    if ( ! is_singular( 'chuong' ) ) {
        return $description;
    }
    $chapter_id   = get_queried_object_id();
    $parent_id    = dtt_goal_chapter_parent_id( $chapter_id );
    $parent_title = $parent_id ? trim( wp_strip_all_tags( get_the_title( $parent_id ) ) ) : '';
    $body         = trim( preg_replace( '/\s+/u', ' ', wp_strip_all_tags( get_post_field( 'post_content', $chapter_id ) ) ) );
    $lead         = wp_trim_words( $body, 22, '…' );
    $prefix       = $parent_title ? 'Đọc ' . get_the_title( $chapter_id ) . ' của ' . $parent_title . '. ' : '';
    $candidate    = trim( $prefix . $lead );
    if ( mb_strlen( $candidate, 'UTF-8' ) > 158 ) {
        $candidate = dtt_goal_trim_title_words( $candidate, 157 );
    }
    return $candidate ?: $description;
}
add_filter( 'rank_math/frontend/description', 'dtt_goal_chapter_description', 700 );

/**
 * Rank Math skips the description tag on a small legacy chapter cohort even
 * when a description value exists. Emit one fallback tag only for the exact
 * audited IDs; other chapters keep Rank Math as the single owner of the tag.
 */
function dtt_goal_legacy_chapter_description_head() {
    if ( ! is_singular( 'chuong' ) ) {
        return;
    }
    $chapter_id = get_queried_object_id();
    if ( ! in_array( (int) $chapter_id, array( 5172, 6260, 6539, 6649 ), true ) ) {
        return;
    }
    $description = trim( (string) get_post_meta( $chapter_id, 'rank_math_description', true ) );
    if ( '' === $description ) {
        $description = dtt_goal_chapter_description( '' );
    }
    if ( '' !== $description ) {
        echo '<meta name="description" content="' . esc_attr( $description ) . '">' . "\n";
    }
}
add_action( 'wp_head', 'dtt_goal_legacy_chapter_description_head', 4 );

function dtt_goal_chapter_og_image( $url ) {
    if ( is_singular( 'chuong' ) ) {
        $image = dtt_goal_chapter_cover_url();
        return $image ?: $url;
    }

    // Discovery/genre pages have no media object of their own. Reuse a real
    // story cover from the current inventory instead of emitting no OG image.
    if ( is_tax( 'the_loai' ) || is_post_type_archive( 'truyen' ) || function_exists( 'dtt_current_landing_seo' ) && ! empty( dtt_current_landing_seo() ) ) {
        $args = array(
            'post_type'      => 'truyen',
            'post_status'    => 'publish',
            'posts_per_page' => 8,
            'orderby'        => 'modified',
            'order'          => 'DESC',
            'no_found_rows'  => true,
        );
        if ( is_tax( 'the_loai' ) ) {
            $term = get_queried_object();
            if ( $term instanceof WP_Term ) {
                $args['tax_query'] = array(array(
                    'taxonomy' => 'the_loai',
                    'field'    => 'term_id',
                    'terms'    => array((int) $term->term_id),
                ));
            }
        }
        $stories = get_posts( $args );
        foreach ( $stories as $story ) {
            $image = get_the_post_thumbnail_url( $story->ID, 'full' );
            if ( $image ) {
                return $image;
            }
        }
        return get_template_directory_uri() . '/img_data/images/no-image-cover-v5.png?v=5';
    }

    if ( empty( $url ) && ! is_admin() && ! is_404() ) {
        return get_template_directory_uri() . '/img_data/images/logo-truyen-moi-v1.png';
    }

    return $url;
}
add_filter( 'rank_math/opengraph/facebook/image', 'dtt_goal_chapter_og_image', 700 );
add_filter( 'rank_math/opengraph/twitter/image', 'dtt_goal_chapter_og_image', 700 );

function dtt_goal_chapter_schema( $data, $jsonld = null ) {
    if ( ! is_singular( 'chuong' ) ) {
        return $data;
    }
    $chapter_id   = get_queried_object_id();
    $parent_id    = dtt_goal_chapter_parent_id( $chapter_id );
    $parent_title = $parent_id ? get_the_title( $parent_id ) : '';
    $parent_url   = $parent_id ? get_permalink( $parent_id ) : '';
    $image        = dtt_goal_chapter_cover_url( $chapter_id );

    if ( $parent_id && $parent_url ) {
        $data['dttChapterBreadcrumb'] = array(
            '@type'           => 'BreadcrumbList',
            '@id'             => get_permalink( $chapter_id ) . '#breadcrumb',
            'itemListElement' => array(
                array('@type' => 'ListItem', 'position' => 1, 'name' => 'Trang chủ', 'item' => home_url('/')),
                array('@type' => 'ListItem', 'position' => 2, 'name' => $parent_title, 'item' => $parent_url),
                array('@type' => 'ListItem', 'position' => 3, 'name' => get_the_title( $chapter_id ), 'item' => get_permalink( $chapter_id )),
            ),
        );
        $data['dttChapterCreativeWork'] = array(
            '@type'      => 'CreativeWork',
            '@id'        => get_permalink( $chapter_id ) . '#chapter',
            'name'       => get_the_title( $chapter_id ),
            'url'        => get_permalink( $chapter_id ),
            'inLanguage' => 'vi',
            'isPartOf'   => array('@type' => 'Book', '@id' => $parent_url . '#book', 'name' => $parent_title, 'url' => $parent_url),
        );
        if ( $image ) {
            $data['dttChapterCreativeWork']['image'] = $image;
        }
    }
    return $data;
}
add_filter( 'rank_math/json_ld', 'dtt_goal_chapter_schema', 700, 2 );

function dtt_goal_chapter_prev_next_head() {
    if ( ! is_singular( 'chuong' ) ) {
        return;
    }
    $chapter_id = get_queried_object_id();
    $parent_id  = dtt_goal_chapter_parent_id( $chapter_id );
    if ( ! $parent_id || ! function_exists( 'tehi_get_ordered_chapters' ) ) {
        return;
    }
    $chapters = tehi_get_ordered_chapters( $parent_id );
    foreach ( $chapters as $i => $chapter ) {
        if ( (int) $chapter->ID !== (int) $chapter_id ) {
            continue;
        }
        if ( $i > 0 ) {
            echo '<link rel="prev" href="' . esc_url( get_permalink( $chapters[ $i - 1 ]->ID ) ) . '">' . "\n";
        }
        if ( $i < count( $chapters ) - 1 ) {
            echo '<link rel="next" href="' . esc_url( get_permalink( $chapters[ $i + 1 ]->ID ) ) . '">' . "\n";
        }
        break;
    }
}
add_action( 'wp_head', 'dtt_goal_chapter_prev_next_head', 12 );

/**
 * Rank Math paginates post-type sitemaps with `ORDER BY post_modified` only.
 * Bulk editorial updates/imports can leave multiple rows with the exact same
 * second-level timestamp at a 200-URL boundary, making MySQL free to return
 * tied rows in a different order for adjacent sitemap requests. That can
 * produce one duplicate URL and one omitted URL even after caches are purged.
 *
 * Keep the fix deliberately narrow: only alter Rank Math's exact sitemap
 * pagination query on child `*-sitemapN.xml` requests and add the post ID as
 * a deterministic tie-breaker. No normal frontend/admin query is touched.
 */
function dtt_goal_rank_math_stable_sitemap_query( $query ) {
    if ( ! is_string( $query ) || '' === $query ) {
        return $query;
    }

    $request_uri = isset( $_SERVER['REQUEST_URI'] ) ? wp_unslash( $_SERVER['REQUEST_URI'] ) : '';
    $path        = (string) parse_url( $request_uri, PHP_URL_PATH );
    if ( ! preg_match( '#/[a-z0-9_-]+-sitemap[0-9]*\.xml$#i', $path ) ) {
        return $query;
    }

    $needle = 'ORDER BY p.post_modified DESC LIMIT';
    if ( false === strpos( $query, $needle ) ) {
        return $query;
    }

    return str_replace(
        $needle,
        'ORDER BY p.post_modified DESC, p.ID DESC LIMIT',
        $query
    );
}
add_filter( 'query', 'dtt_goal_rank_math_stable_sitemap_query', 9999 );
