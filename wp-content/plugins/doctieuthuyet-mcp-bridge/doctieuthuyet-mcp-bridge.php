<?php
/**
 * Plugin Name: DocTieuThuyet MCP Bridge
 * Description: Token-authenticated, allowlisted WordPress bridge for safe truyen/chuong and normal post/media/SEO workflows.
 * Version:     4.2.0
 * Author:      DocTieuThuyet
 * License:     GPL-2.0+
 * Text Domain: doctieuthuyet-mcp-bridge
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

if ( defined( 'DTTMCP_LOADED' ) ) {
    return;
}

define( 'DTTMCP_LOADED', true );
define( 'DTTMCP_NAMESPACE', 'doctieuthuyet-mcp/v1' );
define( 'DTTMCP_RELATION_META_KEY', '_truyen_id' );
define( 'DTTMCP_CONFIRMATION_TTL', 600 );
define( 'DTTMCP_IDEMPOTENCY_TTL', DAY_IN_SECONDS );

/** The bridge never accepts a post type, taxonomy, or meta key from the caller. */
function dttmcp_allowed_post_types() {
    return array( 'truyen', 'chuong', 'post' );
}

function dttmcp_allowed_taxonomies() {
    return array( 'the_loai', 'category', 'post_tag' );
}

function dttmcp_request_id( $request ) {
    $value = method_exists( $request, 'get_header' ) ? (string) $request->get_header( 'x-request-id' ) : '';
    if ( ! preg_match( '/^[A-Za-z0-9._:-]{1,100}$/', $value ) ) {
        $value = function_exists( 'wp_generate_uuid4' ) ? wp_generate_uuid4() : uniqid( 'dtt-', true );
    }
    return $value;
}

function dttmcp_safe_text( $value, $fallback = '' ) {
    if ( ! is_scalar( $value ) ) {
        return $fallback;
    }
    $value = preg_replace( '/[\x00-\x1F\x7F]/', ' ', (string) $value );
    $value = trim( (string) $value );
    return $value === '' ? $fallback : substr( $value, 0, 500 );
}

function dttmcp_safe_code( $value, $fallback = 'DTT_MCP_ERROR' ) {
    $value = preg_replace( '/[^A-Za-z0-9_-]/', '_', (string) $value );
    $value = strtoupper( substr( $value, 0, 100 ) );
    return $value === '' ? $fallback : $value;
}

function dttmcp_response( $request, $ok, $data = array(), $warnings = array(), $error = null, $status = 200 ) {
    $body = array(
        'ok'         => (bool) $ok,
        'request_id' => dttmcp_request_id( $request ),
        'data'       => $data === null ? array() : $data,
        'warnings'   => array_values( array_map( 'strval', (array) $warnings ) ),
        'error'      => $error,
    );
    return new WP_REST_Response( $body, (int) $status );
}

function dttmcp_error_response( $request, $code, $message, $status = 400, $details = array(), $data = array(), $warnings = array() ) {
    $error = array(
        'code'    => dttmcp_safe_code( $code ),
        'message' => dttmcp_safe_text( $message, 'The DTT MCP operation failed.' ),
    );
    if ( ! empty( $details ) ) {
        $error['details'] = $details;
    }
    return dttmcp_response( $request, false, $data, $warnings, $error, $status );
}

function dttmcp_wp_error( $code, $message, $status = 400, $details = array() ) {
    return new WP_Error(
        (string) $code,
        (string) $message,
        array( 'status' => (int) $status, 'dttmcp_details' => $details )
    );
}

function dttmcp_wp_error_details( $error ) {
    if ( ! is_wp_error( $error ) ) {
        return array();
    }
    $data = method_exists( $error, 'get_error_data' ) ? $error->get_error_data() : array();
    return is_array( $data ) && isset( $data['dttmcp_details'] ) && is_array( $data['dttmcp_details'] ) ? $data['dttmcp_details'] : array();
}

function dttmcp_wp_error_status( $error, $fallback = 400 ) {
    if ( ! is_wp_error( $error ) ) {
        return $fallback;
    }
    $data = method_exists( $error, 'get_error_data' ) ? $error->get_error_data() : array();
    return is_array( $data ) && isset( $data['status'] ) ? (int) $data['status'] : $fallback;
}

function dttmcp_wp_error_message( $error ) {
    return is_wp_error( $error ) && method_exists( $error, 'get_error_message' ) ? dttmcp_safe_text( $error->get_error_message(), 'WordPress operation failed.' ) : 'WordPress operation failed.';
}

function dttmcp_body( $request ) {
    $body = method_exists( $request, 'get_json_params' ) ? $request->get_json_params() : array();
    return is_array( $body ) ? $body : array();
}

function dttmcp_id( $value ) {
    $id = function_exists( 'absint' ) ? absint( $value ) : abs( (int) $value );
    return $id > 0 ? $id : 0;
}

function dttmcp_auth( $request ) {
    $expected = defined( 'DOCTIEUTHUYET_MCP_TOKEN' ) ? (string) DOCTIEUTHUYET_MCP_TOKEN : '';
    if ( $expected === '' ) {
        return dttmcp_wp_error( 'AUTH_NOT_CONFIGURED', 'MCP token is not configured.', 503 );
    }
    $header = method_exists( $request, 'get_header' ) ? trim( (string) $request->get_header( 'authorization' ) ) : '';
    if ( $header === '' && isset( $_SERVER['HTTP_AUTHORIZATION'] ) ) {
        $header = trim( (string) $_SERVER['HTTP_AUTHORIZATION'] );
    }
    if ( $header === '' && isset( $_SERVER['REDIRECT_HTTP_AUTHORIZATION'] ) ) {
        $header = trim( (string) $_SERVER['REDIRECT_HTTP_AUTHORIZATION'] );
    }
    if ( ! preg_match( '/^Bearer\s+(.+)$/i', $header, $matches ) ) {
        return dttmcp_wp_error( 'AUTH_MISSING', 'Missing bearer token.', 401 );
    }
    $provided = trim( $matches[1] );
    if ( $provided === '' || ! hash_equals( $expected, $provided ) ) {
        return dttmcp_wp_error( 'AUTH_FAILED', 'Invalid bearer token.', 401 );
    }
    return true;
}

/**
 * Token auth is the service permission boundary. Deployments that bootstrap a
 * WordPress user can opt into capability checks, and tests can override the
 * decision without granting arbitrary REST access.
 */
function dttmcp_can( $capability, $post_id = 0 ) {
    $override = null;
    if ( function_exists( 'apply_filters' ) ) {
        $override = apply_filters( 'dttmcp_permission_check', null, $capability, (int) $post_id );
    }
    if ( null !== $override ) {
        return (bool) $override;
    }
    if ( defined( 'DOCTIEUTHUYET_MCP_REQUIRE_WP_CAPS' ) && DOCTIEUTHUYET_MCP_REQUIRE_WP_CAPS ) {
        return function_exists( 'current_user_can' ) && current_user_can( $capability, $post_id );
    }
    return true;
}

function dttmcp_require_capability( $request, $capability, $post_id = 0 ) {
    if ( dttmcp_can( $capability, $post_id ) ) {
        return true;
    }
    return dttmcp_error_response( $request, 'PERMISSION_DENIED', 'The configured WordPress capability check denied this operation.', 403, array( 'capability' => $capability ) );
}

function dttmcp_audit( $request, $action, $target_ids, $success, $code = null, $details = array() ) {
    $event = array(
        'component'  => 'doctieuthuyet-mcp-bridge',
        'action'     => dttmcp_safe_code( $action, 'WRITE' ),
        'request_id' => dttmcp_request_id( $request ),
        'target_ids' => array_values( array_map( 'intval', (array) $target_ids ) ),
        'success'    => (bool) $success,
    );
    if ( $code ) {
        $event['code'] = dttmcp_safe_code( $code );
    }
    if ( ! empty( $details ) ) {
        $event['details'] = $details;
    }
    if ( function_exists( 'do_action' ) ) {
        do_action( 'dttmcp_audit_log', $event );
    }
    if ( function_exists( 'error_log' ) && ! ( defined( 'DTTMCP_TESTING' ) && DTTMCP_TESTING ) ) {
        error_log( function_exists( 'wp_json_encode' ) ? wp_json_encode( $event ) : json_encode( $event ) );
    }
}

function dttmcp_guarded( $callback ) {
    return function ( $request ) use ( $callback ) {
        $GLOBALS['dttmcp_current_request_id'] = dttmcp_request_id( $request );
        $auth = dttmcp_auth( $request );
        if ( is_wp_error( $auth ) ) {
            return dttmcp_error_response( $request, $auth->get_error_code(), dttmcp_wp_error_message( $auth ), dttmcp_wp_error_status( $auth, 401 ), dttmcp_wp_error_details( $auth ) );
        }
        try {
            $result = call_user_func( $callback, $request );
            if ( is_wp_error( $result ) ) {
                return dttmcp_error_response( $request, $result->get_error_code(), dttmcp_wp_error_message( $result ), dttmcp_wp_error_status( $result ), dttmcp_wp_error_details( $result ) );
            }
            return $result instanceof WP_REST_Response ? $result : dttmcp_response( $request, true, is_array( $result ) ? $result : array( 'result' => $result ) );
        } catch ( Throwable $exception ) {
            dttmcp_audit( $request, 'unhandled_write_or_read', array(), false, 'INTERNAL_ERROR' );
            return dttmcp_error_response( $request, 'INTERNAL_ERROR', 'The bridge operation failed unexpectedly.', 500 );
        }
    };
}

function dttmcp_post( $id, $type = null ) {
    $id = dttmcp_id( $id );
    if ( ! $id || ! function_exists( 'get_post' ) ) {
        return null;
    }
    $post = get_post( $id );
    if ( ! $post || ! in_array( $post->post_type, dttmcp_allowed_post_types(), true ) || ( $type && $post->post_type !== $type ) ) {
        return null;
    }
    return $post;
}

function dttmcp_sanitize_text( $value ) {
    if ( function_exists( 'sanitize_text_field' ) ) {
        return sanitize_text_field( (string) $value );
    }
    return trim( strip_tags( (string) $value ) );
}

function dttmcp_sanitize_html( $value ) {
    return function_exists( 'wp_kses_post' ) ? wp_kses_post( (string) $value ) : strip_tags( (string) $value, '<p><br><strong><em><ul><ol><li><a><blockquote>' );
}

function dttmcp_sanitize_slug( $value ) {
    if ( function_exists( 'sanitize_title' ) ) {
        return sanitize_title( (string) $value );
    }
    $value = strtolower( trim( (string) $value ) );
    $value = preg_replace( '/[^a-z0-9]+/', '-', $value );
    return trim( (string) $value, '-' );
}

function dttmcp_normalize_title( $value ) {
    $value = function_exists( 'wp_strip_all_tags' ) ? wp_strip_all_tags( (string) $value ) : strip_tags( (string) $value );
    if ( function_exists( 'remove_accents' ) ) {
        $value = remove_accents( $value );
    }
    $value = strtolower( trim( preg_replace( '/\s+/', ' ', $value ) ) );
    return $value;
}

function dttmcp_meta_key( $field, $post_type ) {
    $key = '';
    if ( function_exists( 'apply_filters' ) ) {
        $key = apply_filters( 'dttmcp_existing_meta_key', '', $field, $post_type );
    }
    if ( ! is_string( $key ) || ! preg_match( '/^_[A-Za-z0-9_:-]+$/', $key ) ) {
        return '';
    }
    return $key;
}

function dttmcp_meta_get( $post_id, $field, $post_type ) {
    $key = dttmcp_meta_key( $field, $post_type );
    if ( ! $key || ! function_exists( 'get_post_meta' ) ) {
        return '';
    }
    return get_post_meta( $post_id, $key, true );
}

function dttmcp_meta_set( $post_id, $field, $post_type, $value ) {
    $key = dttmcp_meta_key( $field, $post_type );
    if ( ! $key || ! function_exists( 'update_post_meta' ) ) {
        return false;
    }
    return update_post_meta( $post_id, $key, $value );
}

function dttmcp_extract_chapter_number( $title ) {
    if ( preg_match( '/(?:chương|chuong|chapter)\s*[-:#.]?\s*(\d+)/iu', (string) $title, $matches ) ) {
        return dttmcp_id( $matches[1] );
    }
    return 0;
}

function dttmcp_chapter_number( $post ) {
    $value = dttmcp_meta_get( $post->ID, 'chapter_number', 'chuong' );
    if ( is_numeric( $value ) && (int) $value > 0 ) {
        return (int) $value;
    }
    return dttmcp_extract_chapter_number( isset( $post->post_title ) ? $post->post_title : '' );
}

function dttmcp_modified_gmt( $post ) {
    if ( isset( $post->post_modified_gmt ) && $post->post_modified_gmt ) {
        return (string) $post->post_modified_gmt;
    }
    if ( function_exists( 'get_post_modified_time' ) ) {
        return (string) get_post_modified_time( 'Y-m-d H:i:s', true, $post );
    }
    return isset( $post->post_modified ) ? (string) $post->post_modified : '';
}

function dttmcp_terms( $post_id, $taxonomy ) {
    if ( ! in_array( $taxonomy, dttmcp_allowed_taxonomies(), true ) && 'post_tag' !== $taxonomy ) {
        return array();
    }
    if ( ! function_exists( 'wp_get_post_terms' ) ) {
        return array();
    }
    $terms = wp_get_post_terms( $post_id, $taxonomy );
    if ( is_wp_error( $terms ) || ! is_array( $terms ) ) {
        return array();
    }
    $result = array();
    foreach ( $terms as $term ) {
        $result[] = array(
            'id'   => isset( $term->term_id ) ? (int) $term->term_id : 0,
            'name' => isset( $term->name ) ? (string) $term->name : '',
            'slug' => isset( $term->slug ) ? (string) $term->slug : '',
        );
    }
    return $result;
}

function dttmcp_post_payload( $post ) {
    $payload = array(
        'id'                => (int) $post->ID,
        'post_type'         => (string) $post->post_type,
        'title'             => isset( $post->post_title ) ? (string) $post->post_title : '',
        'slug'              => isset( $post->post_name ) ? (string) $post->post_name : '',
        'status'            => isset( $post->post_status ) ? (string) $post->post_status : '',
        'content'           => isset( $post->post_content ) ? (string) $post->post_content : '',
        'excerpt'           => isset( $post->post_excerpt ) ? (string) $post->post_excerpt : '',
        'author'            => isset( $post->post_author ) ? (int) $post->post_author : 0,
        'date'              => isset( $post->post_date ) ? (string) $post->post_date : '',
        'date_gmt'          => isset( $post->post_date_gmt ) ? (string) $post->post_date_gmt : '',
        'modified'          => isset( $post->post_modified ) ? (string) $post->post_modified : '',
        'modified_gmt'      => dttmcp_modified_gmt( $post ),
        'featured_image'    => function_exists( 'get_post_thumbnail_id' ) ? (int) get_post_thumbnail_id( $post->ID ) : 0,
    );
    if ( 'chuong' === $post->post_type ) {
        $payload['truyen_id'] = function_exists( 'get_post_meta' ) ? dttmcp_id( get_post_meta( $post->ID, DTTMCP_RELATION_META_KEY, true ) ) : 0;
        $payload['chapter_number'] = dttmcp_chapter_number( $post );
        $payload['chapter_number_mapping'] = dttmcp_meta_key( 'chapter_number', 'chuong' ) ?: null;
    } else {
        $payload['genres'] = dttmcp_terms( $post->ID, 'the_loai' );
        if ( function_exists( 'taxonomy_exists' ) && taxonomy_exists( 'post_tag' ) && function_exists( 'is_object_in_taxonomy' ) && is_object_in_taxonomy( 'truyen', 'post_tag' ) ) {
            $payload['tags'] = dttmcp_terms( $post->ID, 'post_tag' );
        }
        $story_status = dttmcp_meta_get( $post->ID, 'story_status', 'truyen' );
        if ( '' !== (string) $story_status ) {
            $payload['story_status'] = (string) $story_status;
        }
    }
    if ( function_exists( 'get_permalink' ) ) {
        $payload['link'] = get_permalink( $post->ID );
    }
    return $payload;
}

function dttmcp_posts( $args ) {
    if ( ! function_exists( 'get_posts' ) ) {
        return array();
    }
    $defaults = array(
        'post_status'    => 'any',
        'posts_per_page' => 200,
        'no_found_rows'  => true,
    );
    $posts = get_posts( array_merge( $defaults, $args ) );
    return is_array( $posts ) ? $posts : array();
}

/** Return bounded WordPress query results together with found_posts for pagination. */
function dttmcp_query_posts( $args ) {
    $defaults = array(
        'post_status'    => 'any',
        'posts_per_page' => 200,
        'no_found_rows'  => false,
    );
    $query_args = array_merge( $defaults, $args );
    if ( class_exists( 'WP_Query' ) ) {
        $query = new WP_Query( $query_args );
        return array( 'posts' => is_array( $query->posts ) ? $query->posts : array(), 'total' => (int) $query->found_posts );
    }
    $posts = dttmcp_posts( $query_args );
    $count_args = $query_args;
    unset( $count_args['paged'], $count_args['offset'], $count_args['no_found_rows'] );
    $count_args['posts_per_page'] = 5000;
    $count_args['paged'] = 1;
    $all_posts = dttmcp_posts( $count_args );
    return array( 'posts' => $posts, 'total' => count( $all_posts ) );
}

function dttmcp_pagination( $page, $per_page, $total_items, $returned ) {
    $page = max( 1, (int) $page );
    $per_page = max( 1, (int) $per_page );
    $total_items = max( 0, (int) $total_items );
    return array(
        'page'        => $page,
        'per_page'    => $per_page,
        'returned'    => (int) $returned,
        'total_items' => $total_items,
        'total_pages' => $total_items ? (int) ceil( $total_items / $per_page ) : 0,
    );
}

function dttmcp_related_chapters( $truyen_id, $limit = 200 ) {
    $posts = dttmcp_posts( array(
        'post_type'  => 'chuong',
        'meta_key'   => DTTMCP_RELATION_META_KEY,
        'meta_value' => (string) dttmcp_id( $truyen_id ),
        'posts_per_page' => min( 200, max( 1, (int) $limit ) ),
    ) );
    usort( $posts, function ( $left, $right ) {
        $left_number  = dttmcp_chapter_number( $left );
        $right_number = dttmcp_chapter_number( $right );
        if ( $left_number === $right_number ) {
            return (int) $left->ID <=> (int) $right->ID;
        }
        if ( 0 === $left_number ) return 1;
        if ( 0 === $right_number ) return -1;
        return $left_number <=> $right_number;
    } );
    return $posts;
}

function dttmcp_find_story_duplicate( $body, $exclude_id = 0 ) {
    $slug = dttmcp_sanitize_slug( isset( $body['slug'] ) && $body['slug'] ? $body['slug'] : ( $body['title'] ?? '' ) );
    if ( $slug ) {
        foreach ( dttmcp_posts( array( 'post_type' => 'truyen', 'name' => $slug, 'posts_per_page' => 20 ) ) as $post ) {
            if ( (int) $post->ID !== (int) $exclude_id ) return $post;
        }
    }
    $normalized = dttmcp_normalize_title( $body['title'] ?? '' );
    if ( $normalized ) {
        foreach ( dttmcp_posts( array( 'post_type' => 'truyen', 'posts_per_page' => 200 ) ) as $post ) {
            if ( (int) $post->ID !== (int) $exclude_id && dttmcp_normalize_title( $post->post_title ) === $normalized ) return $post;
        }
    }
    return null;
}

function dttmcp_find_chapter_duplicate( $truyen_id, $chapter_number, $exclude_id = 0 ) {
    if ( $chapter_number <= 0 ) return null;
    foreach ( dttmcp_related_chapters( $truyen_id ) as $post ) {
        if ( (int) $post->ID !== (int) $exclude_id && dttmcp_chapter_number( $post ) === (int) $chapter_number ) return $post;
    }
    return null;
}

function dttmcp_terms_input( $body ) {
    $terms = isset( $body['genres'] ) ? $body['genres'] : ( $body['the_loai'] ?? array() );
    if ( ! is_array( $terms ) ) return array();
    $result = array();
    foreach ( $terms as $term ) {
        if ( is_int( $term ) || ctype_digit( (string) $term ) ) {
            $result[] = dttmcp_id( $term );
        } elseif ( is_string( $term ) && trim( $term ) !== '' ) {
            $result[] = dttmcp_sanitize_text( $term );
        }
    }
    return array_values( array_filter( $result ) );
}

function dttmcp_apply_story_fields( $post_id, $body, &$warnings ) {
    if ( array_key_exists( 'genres', $body ) || array_key_exists( 'the_loai', $body ) ) {
        if ( function_exists( 'wp_set_post_terms' ) ) {
            $result = wp_set_post_terms( $post_id, dttmcp_terms_input( $body ), 'the_loai', false );
            if ( is_wp_error( $result ) ) return $result;
        }
    }
    if ( array_key_exists( 'tags', $body ) ) {
        $can_use_tags = function_exists( 'taxonomy_exists' ) && taxonomy_exists( 'post_tag' ) && function_exists( 'is_object_in_taxonomy' ) && is_object_in_taxonomy( 'truyen', 'post_tag' );
        if ( ! $can_use_tags ) {
            $warnings[] = 'TAGS_SKIPPED_TAXONOMY_NOT_REGISTERED';
        } elseif ( function_exists( 'wp_set_post_terms' ) ) {
            $tags = array_map( 'dttmcp_sanitize_text', is_array( $body['tags'] ) ? $body['tags'] : array() );
            $result = wp_set_post_terms( $post_id, $tags, 'post_tag', false );
            if ( is_wp_error( $result ) ) return $result;
        }
    }
    if ( array_key_exists( 'featured_image', $body ) ) {
        $attachment = dttmcp_id( $body['featured_image'] );
        $attachment_post = function_exists( 'get_post' ) ? get_post( $attachment ) : null;
        if ( ! $attachment_post || 'attachment' !== $attachment_post->post_type || ! function_exists( 'set_post_thumbnail' ) ) {
            return dttmcp_wp_error( 'INVALID_FEATURED_IMAGE', 'featured_image must be an existing attachment ID.', 422 );
        }
        set_post_thumbnail( $post_id, $attachment );
    }
    if ( array_key_exists( 'story_status', $body ) ) {
        if ( ! dttmcp_meta_set( $post_id, 'story_status', 'truyen', dttmcp_sanitize_text( $body['story_status'] ) ) ) {
            return dttmcp_wp_error( 'META_MAPPING_REQUIRED', 'story_status is disabled until the existing website meta key is explicitly mapped.', 422 );
        }
    }
    if ( isset( $body['seo'] ) ) {
        $mapping = function_exists( 'apply_filters' ) ? apply_filters( 'dttmcp_seo_meta_keys', array(), 'truyen' ) : array();
        if ( ! is_array( $mapping ) || empty( $mapping ) ) {
            $warnings[] = 'SEO_MAPPING_NOT_CONFIGURED';
        } else {
            foreach ( array( 'title', 'description', 'focus_keyword', 'canonical_url' ) as $field ) {
                if ( isset( $body['seo'][ $field ], $mapping[ $field ] ) && is_string( $mapping[ $field ] ) && preg_match( '/^_[A-Za-z0-9_:-]+$/', $mapping[ $field ] ) ) {
                    update_post_meta( $post_id, $mapping[ $field ], dttmcp_sanitize_text( $body['seo'][ $field ] ) );
                }
            }
        }
    }
    return true;
}

function dttmcp_story_insert_data( $body ) {
    $title = dttmcp_sanitize_text( $body['title'] ?? '' );
    return array(
        'post_type'    => 'truyen',
        'post_status'  => 'draft',
        'post_title'   => $title,
        'post_name'    => dttmcp_sanitize_slug( $body['slug'] ?? $title ),
        'post_content' => dttmcp_sanitize_html( $body['content'] ?? ( $body['description'] ?? '' ) ),
        'post_excerpt' => dttmcp_sanitize_html( $body['excerpt'] ?? '' ),
        'post_author'  => dttmcp_id( $body['author'] ?? 0 ),
    );
}

function dttmcp_chapter_insert_data( $body ) {
    $title = dttmcp_sanitize_text( $body['title'] ?? '' );
    return array(
        'post_type'    => 'chuong',
        'post_status'  => 'draft',
        'post_title'   => $title,
        'post_name'    => dttmcp_sanitize_slug( $body['slug'] ?? $title ),
        'post_content' => dttmcp_sanitize_html( $body['content'] ?? '' ),
    );
}

function dttmcp_create_status_guard( $body ) {
    if ( array_key_exists( 'status', $body ) && 'draft' !== (string) $body['status'] ) {
        return dttmcp_wp_error( 'CREATE_STATUS_FORBIDDEN', 'Create actions always create draft content; status must be omitted or draft.', 422 );
    }
    return true;
}

function dttmcp_create_story_internal( $body, &$warnings ) {
    $title = dttmcp_sanitize_text( $body['title'] ?? '' );
    if ( '' === $title ) return dttmcp_wp_error( 'MISSING_TITLE', 'Story title is required.', 400 );
    $duplicate = dttmcp_find_story_duplicate( $body );
    if ( $duplicate ) return dttmcp_wp_error( 'DUPLICATE_STORY', 'A story with the same slug or normalized title already exists.', 409, array( 'existing_id' => (int) $duplicate->ID ) );
    $id = wp_insert_post( dttmcp_story_insert_data( $body ), true );
    if ( is_wp_error( $id ) ) return $id;
    $field_result = dttmcp_apply_story_fields( dttmcp_id( $id ), $body, $warnings );
    if ( is_wp_error( $field_result ) ) {
        return dttmcp_wp_error( $field_result->get_error_code(), dttmcp_wp_error_message( $field_result ), 422, array( 'created_id' => dttmcp_id( $id ) ) );
    }
    return array( 'id' => dttmcp_id( $id ), 'action' => 'created', 'post' => dttmcp_post( $id, 'truyen' ) );
}

function dttmcp_create_chapter_internal( $body, $parent_id, &$warnings ) {
    $parent = dttmcp_post( $parent_id, 'truyen' );
    if ( ! $parent ) return dttmcp_wp_error( 'TRUYEN_NOT_FOUND', 'Parent truyen was not found.', 404 );
    $title = dttmcp_sanitize_text( $body['title'] ?? '' );
    if ( '' === $title ) return dttmcp_wp_error( 'MISSING_TITLE', 'Chapter title is required.', 400 );
    $number = dttmcp_id( $body['chapter_number'] ?? 0 );
    if ( ! $number ) $number = dttmcp_extract_chapter_number( $title );
    if ( $number <= 0 ) return dttmcp_wp_error( 'INVALID_CHAPTER_NUMBER', 'A positive chapter_number or a numbered chapter title is required.', 422 );
    $duplicate = dttmcp_find_chapter_duplicate( $parent_id, $number );
    if ( $duplicate ) return dttmcp_wp_error( 'DUPLICATE_CHAPTER', 'A chapter with this truyen_id and chapter_number already exists.', 409, array( 'existing_id' => (int) $duplicate->ID ) );
    $id = wp_insert_post( dttmcp_chapter_insert_data( $body ), true );
    if ( is_wp_error( $id ) ) return $id;
    update_post_meta( dttmcp_id( $id ), DTTMCP_RELATION_META_KEY, $parent_id );
    if ( dttmcp_meta_key( 'chapter_number', 'chuong' ) ) {
        dttmcp_meta_set( dttmcp_id( $id ), 'chapter_number', 'chuong', $number );
    } else {
        $warnings[] = 'CHAPTER_NUMBER_META_MAPPING_NOT_CONFIGURED_TITLE_FALLBACK_USED';
    }
    if ( isset( $body['seo'] ) ) {
        $mapping = function_exists( 'apply_filters' ) ? apply_filters( 'dttmcp_seo_meta_keys', array(), 'chuong' ) : array();
        if ( empty( $mapping ) ) $warnings[] = 'SEO_MAPPING_NOT_CONFIGURED';
    }
    return array( 'id' => dttmcp_id( $id ), 'action' => 'created', 'post' => dttmcp_post( $id, 'chuong' ) );
}

function dttmcp_expected_lock( $request, $post ) {
    $body = dttmcp_body( $request );
    if ( ! array_key_exists( 'expected_modified_gmt', $body ) ) return true;
    $expected = trim( (string) $body['expected_modified_gmt'] );
    if ( $expected !== dttmcp_modified_gmt( $post ) ) {
        return dttmcp_error_response( $request, 'OPTIMISTIC_LOCK_CONFLICT', 'The post was modified after the caller read it.', 409, array( 'expected_modified_gmt' => $expected, 'actual_modified_gmt' => dttmcp_modified_gmt( $post ) ) );
    }
    return true;
}

function dttmcp_update_story_internal( $post, $body, &$warnings ) {
    if ( array_key_exists( 'status', $body ) || array_key_exists( 'schedule_at', $body ) ) return dttmcp_wp_error( 'STATUS_UPDATE_SEPARATE', 'Content updates and status updates are separate actions.', 422 );
    $data = array( 'ID' => (int) $post->ID );
    $changed = false;
    foreach ( array( 'title', 'slug', 'author' ) as $field ) {
        if ( array_key_exists( $field, $body ) ) {
            $data[ 'post_' . ( 'title' === $field ? 'title' : ( 'slug' === $field ? 'name' : 'author' ) ) ] = 'author' === $field ? dttmcp_id( $body[ $field ] ) : ( 'title' === $field ? dttmcp_sanitize_text( $body[ $field ] ) : dttmcp_sanitize_slug( $body[ $field ] ) );
            $changed = true;
        }
    }
    if ( array_key_exists( 'content', $body ) || array_key_exists( 'description', $body ) ) { $data['post_content'] = dttmcp_sanitize_html( $body['content'] ?? $body['description'] ); $changed = true; }
    if ( array_key_exists( 'excerpt', $body ) ) { $data['post_excerpt'] = dttmcp_sanitize_html( $body['excerpt'] ); $changed = true; }
    if ( array_key_exists( 'meta', $body ) ) return dttmcp_wp_error( 'META_NOT_ALLOWED', 'Arbitrary meta writes are not allowed.', 422 );
    if ( ! $changed && ! array_key_exists( 'genres', $body ) && ! array_key_exists( 'the_loai', $body ) && ! array_key_exists( 'tags', $body ) && ! array_key_exists( 'featured_image', $body ) && ! array_key_exists( 'story_status', $body ) && ! array_key_exists( 'seo', $body ) ) return dttmcp_wp_error( 'NO_CONTENT_FIELDS', 'Provide at least one allowlisted content field.', 400 );
    if ( $changed ) {
        $updated = wp_update_post( $data, true );
        if ( is_wp_error( $updated ) ) return $updated;
    }
    $fields = dttmcp_apply_story_fields( $post->ID, $body, $warnings );
    if ( is_wp_error( $fields ) ) return $fields;
    return dttmcp_post( $post->ID, 'truyen' );
}

function dttmcp_update_chapter_internal( $post, $body, &$warnings ) {
    if ( array_key_exists( 'status', $body ) || array_key_exists( 'schedule_at', $body ) ) return dttmcp_wp_error( 'STATUS_UPDATE_SEPARATE', 'Content updates and status updates are separate actions.', 422 );
    $data = array( 'ID' => (int) $post->ID );
    $changed = false;
    foreach ( array( 'title', 'slug' ) as $field ) {
        if ( array_key_exists( $field, $body ) ) { $data[ 'post_' . ( 'title' === $field ? 'title' : 'name' ) ] = 'title' === $field ? dttmcp_sanitize_text( $body[ $field ] ) : dttmcp_sanitize_slug( $body[ $field ] ); $changed = true; }
    }
    if ( array_key_exists( 'content', $body ) ) { $data['post_content'] = dttmcp_sanitize_html( $body['content'] ); $changed = true; }
    if ( array_key_exists( 'truyen_id', $body ) ) {
        $parent = dttmcp_post( $body['truyen_id'], 'truyen' );
        if ( ! $parent ) return dttmcp_wp_error( 'TRUYEN_NOT_FOUND', 'Parent truyen was not found.', 404 );
        update_post_meta( $post->ID, DTTMCP_RELATION_META_KEY, dttmcp_id( $body['truyen_id'] ) );
        $changed = true;
    }
    if ( array_key_exists( 'chapter_number', $body ) ) {
        $number = dttmcp_id( $body['chapter_number'] );
        if ( ! $number ) return dttmcp_wp_error( 'INVALID_CHAPTER_NUMBER', 'chapter_number must be a positive integer.', 422 );
        $parent_id = dttmcp_id( get_post_meta( $post->ID, DTTMCP_RELATION_META_KEY, true ) );
        $duplicate = dttmcp_find_chapter_duplicate( $parent_id, $number, $post->ID );
        if ( $duplicate ) return dttmcp_wp_error( 'DUPLICATE_CHAPTER', 'Another chapter already uses this truyen_id and chapter_number.', 409, array( 'existing_id' => (int) $duplicate->ID ) );
        if ( dttmcp_meta_key( 'chapter_number', 'chuong' ) ) dttmcp_meta_set( $post->ID, 'chapter_number', 'chuong', $number ); else $warnings[] = 'CHAPTER_NUMBER_META_MAPPING_NOT_CONFIGURED_TITLE_FALLBACK_USED';
        $changed = true;
    }
    if ( array_key_exists( 'meta', $body ) ) return dttmcp_wp_error( 'META_NOT_ALLOWED', 'Arbitrary meta writes are not allowed.', 422 );
    if ( ! $changed && ! array_key_exists( 'seo', $body ) ) return dttmcp_wp_error( 'NO_CONTENT_FIELDS', 'Provide at least one allowlisted content field.', 400 );
    if ( $changed && count( $data ) > 1 ) {
        $updated = wp_update_post( $data, true );
        if ( is_wp_error( $updated ) ) return $updated;
    }
    return dttmcp_post( $post->ID, 'chuong' );
}

function dttmcp_story_validation( $post ) {
    $errors = array();
    if ( trim( (string) $post->post_title ) === '' ) $errors[] = 'TITLE_REQUIRED';
    if ( trim( (string) $post->post_name ) === '' ) $errors[] = 'SLUG_REQUIRED';
    $duplicate = dttmcp_find_story_duplicate( array( 'title' => $post->post_title, 'slug' => $post->post_name ), $post->ID );
    if ( $duplicate ) $errors[] = 'DUPLICATE_STORY';
    return $errors;
}

function dttmcp_chapter_validation( $post ) {
    $errors = array();
    $parent_id = dttmcp_id( get_post_meta( $post->ID, DTTMCP_RELATION_META_KEY, true ) );
    if ( ! $parent_id || ! dttmcp_post( $parent_id, 'truyen' ) ) $errors[] = 'PARENT_TRUYEN_REQUIRED';
    $number = dttmcp_chapter_number( $post );
    if ( $number <= 0 ) $errors[] = 'CHAPTER_NUMBER_REQUIRED';
    if ( trim( wp_strip_all_tags( (string) $post->post_content ) ) === '' ) $errors[] = 'CONTENT_REQUIRED';
    $duplicate = dttmcp_find_chapter_duplicate( $parent_id, $number, $post->ID );
    if ( $duplicate ) $errors[] = 'DUPLICATE_CHAPTER';
    return $errors;
}

function dttmcp_package_version( $story, $chapters ) {
    usort( $chapters, function ( $left, $right ) {
        return (int) $left->ID <=> (int) $right->ID;
    } );
    $values = array( 'story' => array( 'id' => (int) $story->ID, 'modified_gmt' => dttmcp_modified_gmt( $story ), 'title' => (string) $story->post_title, 'content' => (string) $story->post_content, 'status' => (string) $story->post_status ), 'chapters' => array() );
    foreach ( $chapters as $chapter ) $values['chapters'][] = array( 'id' => (int) $chapter->ID, 'modified_gmt' => dttmcp_modified_gmt( $chapter ), 'title' => (string) $chapter->post_title, 'content' => (string) $chapter->post_content, 'status' => (string) $chapter->post_status, 'number' => dttmcp_chapter_number( $chapter ) );
    $json = function_exists( 'wp_json_encode' ) ? wp_json_encode( $values ) : json_encode( $values );
    return hash( 'sha256', (string) $json );
}

function dttmcp_transient_get( $key ) {
    if ( function_exists( 'get_transient' ) ) return get_transient( $key );
    return isset( $GLOBALS['dttmcp_test_cache'][ $key ] ) ? $GLOBALS['dttmcp_test_cache'][ $key ] : false;
}

function dttmcp_transient_set( $key, $value, $ttl ) {
    if ( function_exists( 'set_transient' ) ) return set_transient( $key, $value, $ttl );
    $GLOBALS['dttmcp_test_cache'][ $key ] = $value;
    return true;
}

function dttmcp_transient_delete( $key ) {
    if ( function_exists( 'delete_transient' ) ) return delete_transient( $key );
    unset( $GLOBALS['dttmcp_test_cache'][ $key ] );
    return true;
}

function dttmcp_cache_key( $prefix, $key ) {
    return 'dttmcp_' . $prefix . '_' . hash( 'sha256', (string) $key );
}

function dttmcp_fingerprint( $value ) {
    if ( is_array( $value ) ) {
        unset( $value['confirmation_token'] );
        ksort( $value );
        foreach ( $value as $key => $item ) $value[ $key ] = dttmcp_fingerprint( $item );
    }
    $json = function_exists( 'wp_json_encode' ) ? wp_json_encode( $value ) : json_encode( $value );
    return hash( 'sha256', (string) $json );
}

function dttmcp_idempotency_check( $operation, $body ) {
    $key = isset( $body['idempotency_key'] ) ? trim( (string) $body['idempotency_key'] ) : '';
    if ( '' === $key ) return array( 'key' => '', 'fingerprint' => '', 'stored' => null );
    $fingerprint = dttmcp_fingerprint( $body );
    $stored = dttmcp_transient_get( dttmcp_cache_key( 'idempotency_' . $operation, $key ) );
    if ( false !== $stored && is_array( $stored ) ) {
        if ( ( $stored['fingerprint'] ?? '' ) !== $fingerprint ) return dttmcp_wp_error( 'IDEMPOTENCY_CONFLICT', 'The idempotency_key was already used for a different request.', 409 );
        return array( 'key' => $key, 'fingerprint' => $fingerprint, 'stored' => $stored['envelope'] ?? null );
    }
    return array( 'key' => $key, 'fingerprint' => $fingerprint, 'stored' => null );
}

function dttmcp_store_idempotency( $operation, $idempotency, $envelope ) {
    if ( empty( $idempotency['key'] ) ) return;
    $body = $envelope instanceof WP_REST_Response && method_exists( $envelope, 'get_data' ) ? $envelope->get_data() : array();
    dttmcp_transient_set( dttmcp_cache_key( 'idempotency_' . $operation, $idempotency['key'] ), array( 'fingerprint' => $idempotency['fingerprint'], 'envelope' => $body ), DTTMCP_IDEMPOTENCY_TTL );
}

function dttmcp_replay_idempotency( $request, $stored ) {
    if ( ! is_array( $stored ) ) return null;
    return dttmcp_response( $request, (bool) ( $stored['ok'] ?? false ), $stored['data'] ?? array(), array_merge( (array) ( $stored['warnings'] ?? array() ), array( 'IDEMPOTENT_REPLAY' ) ), $stored['error'] ?? null, (bool) ( $stored['ok'] ?? false ) ? 200 : 207 );
}

function dttmcp_confirmation_token() {
    try { return bin2hex( random_bytes( 32 ) ); } catch ( Throwable $exception ) { return wp_generate_password( 64, false, false ); }
}

function dttmcp_confirmation_record( $request, $body, $story, $chapters ) {
    $token = dttmcp_confirmation_token();
    $chapter_ids = array_map( 'intval', array_keys( $chapters ) );
    sort( $chapter_ids, SORT_NUMERIC );
    $version = dttmcp_package_version( $story, array_values( $chapters ) );
    $expires = time() + (int) apply_filters( 'dttmcp_confirmation_ttl', DTTMCP_CONFIRMATION_TTL );
    $record = array( 'truyen_id' => (int) $story->ID, 'chapter_ids' => $chapter_ids, 'content_version' => $version, 'expires_at' => $expires );
    dttmcp_transient_set( dttmcp_cache_key( 'confirmation', $token ), $record, max( 60, $expires - time() ) );
    dttmcp_audit( $request, 'pre_publish_story_package', array_merge( array( $story->ID ), $chapter_ids ), true, 'TOKEN_ISSUED' );
    return array( 'confirmation_token' => $token, 'expires_at' => gmdate( 'c', $expires ), 'truyen_id' => (int) $story->ID, 'chapter_ids' => $chapter_ids, 'content_version' => $version );
}

function dttmcp_consume_confirmation( $body, $story, $expected_chapter_ids, $request ) {
    $token = trim( (string) ( $body['confirmation_token'] ?? '' ) );
    if ( '' === $token ) return dttmcp_wp_error( 'CONFIRMATION_REQUIRED', 'A confirmation_token from pre_publish_story_package is required.', 422 );
    $record = dttmcp_transient_get( dttmcp_cache_key( 'confirmation', $token ) );
    if ( ! is_array( $record ) ) return dttmcp_wp_error( 'CONFIRMATION_INVALID_OR_EXPIRED', 'The confirmation token is invalid, expired, or already used.', 409 );
    if ( (int) ( $record['expires_at'] ?? 0 ) < time() ) { dttmcp_transient_delete( dttmcp_cache_key( 'confirmation', $token ) ); return dttmcp_wp_error( 'CONFIRMATION_INVALID_OR_EXPIRED', 'The confirmation token has expired.', 409 ); }
    $actual_ids = array_map( 'intval', (array) $expected_chapter_ids );
    sort( $actual_ids, SORT_NUMERIC );
    if ( (int) $record['truyen_id'] !== (int) $story->ID || $record['chapter_ids'] !== $actual_ids ) return dttmcp_wp_error( 'CONFIRMATION_SCOPE_MISMATCH', 'The confirmation token is not bound to this truyen_id and chapter_ids set.', 409 );
    $current_chapters = array();
    foreach ( $actual_ids as $id ) { $chapter = dttmcp_post( $id, 'chuong' ); if ( $chapter ) $current_chapters[ $id ] = $chapter; }
    if ( dttmcp_package_version( $story, array_values( $current_chapters ) ) !== (string) ( $record['content_version'] ?? '' ) ) return dttmcp_wp_error( 'CONTENT_VERSION_CHANGED', 'Content changed after pre-publish validation; issue a new confirmation token.', 409 );
    dttmcp_transient_delete( dttmcp_cache_key( 'confirmation', $token ) );
    return $record;
}

function dttmcp_validate_package( $story_id, $chapter_ids ) {
    $story = dttmcp_post( $story_id, 'truyen' );
    if ( ! $story ) return dttmcp_wp_error( 'TRUYEN_NOT_FOUND', 'Story not found.', 404 );
    $chapter_ids = array_values( array_unique( array_map( 'dttmcp_id', (array) $chapter_ids ) ) );
    $chapters = array();
    $errors = dttmcp_story_validation( $story );
    foreach ( $chapter_ids as $chapter_id ) {
        $chapter = dttmcp_post( $chapter_id, 'chuong' );
        if ( ! $chapter ) { $errors[] = 'CHAPTER_NOT_FOUND_' . $chapter_id; continue; }
        $parent = dttmcp_id( get_post_meta( $chapter_id, DTTMCP_RELATION_META_KEY, true ) );
        if ( $parent !== (int) $story->ID ) $errors[] = 'CHAPTER_PARENT_MISMATCH_' . $chapter_id;
        foreach ( dttmcp_chapter_validation( $chapter ) as $item ) $errors[] = $item . '_' . $chapter_id;
        $chapters[ $chapter_id ] = $chapter;
    }
    $numbers = array();
    foreach ( $chapters as $chapter ) { $number = dttmcp_chapter_number( $chapter ); if ( $number && isset( $numbers[ $number ] ) ) $errors[] = 'DUPLICATE_CHAPTER_NUMBER_' . $number; $numbers[ $number ] = true; }
    $ordered = array_values( $chapters );
    usort( $ordered, function ( $left, $right ) { $a = dttmcp_chapter_number( $left ); $b = dttmcp_chapter_number( $right ); return $a === $b ? (int) $left->ID <=> (int) $right->ID : $a <=> $b; } );
    return array( 'story' => $story, 'chapters' => $chapters, 'ordered' => $ordered, 'errors' => array_values( array_unique( $errors ) ), 'content_version' => dttmcp_package_version( $story, $ordered ) );
}

function dttmcp_schedule_data( $value ) {
    if ( null === $value || '' === trim( (string) $value ) ) return array();
    try {
        $timezone = function_exists( 'wp_timezone' ) ? wp_timezone() : new DateTimeZone( 'UTC' );
        $date = new DateTimeImmutable( (string) $value, $timezone );
        if ( $date->getTimestamp() <= time() ) return dttmcp_wp_error( 'INVALID_SCHEDULE', 'schedule_at must be in the future.', 422 );
        return array( 'post_date' => $date->setTimezone( $timezone )->format( 'Y-m-d H:i:s' ), 'post_date_gmt' => $date->setTimezone( new DateTimeZone( 'UTC' ) )->format( 'Y-m-d H:i:s' ) );
    } catch ( Throwable $exception ) { return dttmcp_wp_error( 'INVALID_SCHEDULE', 'schedule_at must be a valid ISO-8601 date.', 422 ); }
}

function dttmcp_status_write( $post_id, $status, $schedule = array() ) {
    $data = array_merge( array( 'ID' => (int) $post_id, 'post_status' => (string) $status ), $schedule );
    return wp_update_post( $data, true );
}

function dttmcp_snapshot( $post ) {
    return array( 'ID' => (int) $post->ID, 'post_status' => (string) $post->post_status, 'post_date' => (string) ( $post->post_date ?? '' ), 'post_date_gmt' => (string) ( $post->post_date_gmt ?? '' ) );
}

function dttmcp_restore( $snapshot ) {
    return wp_update_post( $snapshot, true );
}

function dttmcp_status_verified( $id, $status ) {
    $post = get_post( $id );
    return $post && (string) $post->post_status === (string) $status;
}

function dttmcp_endpoint_health( $request ) {
    $seo = dttmcp_seo_provider(); return dttmcp_response( $request, true, array( 'site' => function_exists( 'home_url' ) ? home_url() : '', 'plugin' => 'doctieuthuyet-mcp-bridge', 'version' => '4.2.0', 'tool_count' => 64, 'wordpress_editing_capabilities' => array( 'normal_post_draft', 'normal_post_patch', 'taxonomy', 'rank_math', 'internal_link_audit' ), 'post_types' => dttmcp_allowed_post_types(), 'taxonomies' => dttmcp_allowed_taxonomies(), 'relation_meta_key' => DTTMCP_RELATION_META_KEY, 'chapter_number_meta_mapping' => dttmcp_meta_key( 'chapter_number', 'chuong' ) ?: null, 'require_wp_capabilities' => defined( 'DOCTIEUTHUYET_MCP_REQUIRE_WP_CAPS' ) && DOCTIEUTHUYET_MCP_REQUIRE_WP_CAPS, 'features' => array( 'truyen' => true, 'chuong' => true, 'posts' => true, 'media' => true, 'taxonomies' => true, 'seo' => 'none' !== $seo ), 'seo' => array( 'provider' => $seo, 'active' => 'none' !== $seo ), 'capabilities' => array( 'edit_posts' => dttmcp_can( 'edit_posts' ), 'publish_posts' => dttmcp_can( 'publish_posts' ), 'upload_files' => dttmcp_can( 'upload_files' ), 'delete_posts' => dttmcp_can( 'delete_posts' ) ) ) );
}

function dttmcp_endpoint_get_truyen( $request ) {
    $id = dttmcp_id( dttmcp_body( $request )['truyen_id'] ?? 0 ); $post = dttmcp_post( $id, 'truyen' );
    if ( ! $post ) return dttmcp_error_response( $request, 'TRUYEN_NOT_FOUND', 'Story not found.', 404 );
    $permission = dttmcp_require_capability( $request, 'read', $id ); if ( $permission !== true ) return $permission;
    return dttmcp_response( $request, true, array( 'truyen' => dttmcp_post_payload( $post ) ) );
}

function dttmcp_endpoint_get_chuong( $request ) {
    $id = dttmcp_id( dttmcp_body( $request )['chuong_id'] ?? 0 ); $post = dttmcp_post( $id, 'chuong' );
    if ( ! $post ) return dttmcp_error_response( $request, 'CHUONG_NOT_FOUND', 'Chapter not found.', 404 );
    $permission = dttmcp_require_capability( $request, 'read', $id ); if ( $permission !== true ) return $permission;
    return dttmcp_response( $request, true, array( 'chuong' => dttmcp_post_payload( $post ) ) );
}

function dttmcp_endpoint_list_recent( $request ) {
    $body = dttmcp_body( $request ); $type = (string) ( $body['post_type'] ?? 'truyen' );
    if ( ! in_array( $type, dttmcp_allowed_post_types(), true ) ) return dttmcp_error_response( $request, 'POST_TYPE_NOT_ALLOWED', 'Only truyen and chuong are allowed.', 422 );
    $permission = dttmcp_require_capability( $request, 'read' ); if ( $permission !== true ) return $permission;
    $args = array( 'post_type' => $type, 'posts_per_page' => min( 100, max( 1, (int) ( $body['per_page'] ?? 10 ) ) ), 'orderby' => 'date', 'order' => 'DESC' );
    if ( 'chuong' === $type && ! empty( $body['truyen_id'] ) ) {
        $args['meta_key'] = DTTMCP_RELATION_META_KEY;
        $args['meta_value'] = (string) dttmcp_id( $body['truyen_id'] );
    }
    $items = array_map( 'dttmcp_post_payload', dttmcp_posts( $args ) );
    return dttmcp_response( $request, true, array( 'post_type' => $type, 'items' => $items, 'count' => count( $items ) ) );
}

function dttmcp_endpoint_list_the_loai( $request ) {
    $permission = dttmcp_require_capability( $request, 'read' ); if ( $permission !== true ) return $permission;
    if ( ! function_exists( 'get_terms' ) ) return dttmcp_response( $request, true, array( 'taxonomy' => 'the_loai', 'items' => array(), 'count' => 0 ) );
    $body = dttmcp_body( $request ); $terms = get_terms( array( 'taxonomy' => 'the_loai', 'hide_empty' => false, 'number' => min( 100, max( 1, (int) ( $body['per_page'] ?? 100 ) ) ), 'search' => dttmcp_sanitize_text( $body['search'] ?? '' ) ) );
    if ( is_wp_error( $terms ) ) return $terms;
    $items = array(); foreach ( (array) $terms as $term ) $items[] = array( 'id' => (int) $term->term_id, 'name' => (string) $term->name, 'slug' => (string) $term->slug, 'count' => (int) ( $term->count ?? 0 ) );
    return dttmcp_response( $request, true, array( 'taxonomy' => 'the_loai', 'items' => $items, 'count' => count( $items ) ) );
}

function dttmcp_endpoint_list_chuong_by_truyen( $request ) {
    $body = dttmcp_body( $request ); $id = dttmcp_id( $body['truyen_id'] ?? 0 ); if ( ! dttmcp_post( $id, 'truyen' ) ) return dttmcp_error_response( $request, 'TRUYEN_NOT_FOUND', 'Story not found.', 404 );
    $permission = dttmcp_require_capability( $request, 'read', $id ); if ( $permission !== true ) return $permission;
    $items = array_map( 'dttmcp_post_payload', dttmcp_related_chapters( $id, $body['per_page'] ?? 200 ) );
    return dttmcp_response( $request, true, array( 'truyen_id' => $id, 'items' => $items, 'count' => count( $items ) ) );
}

function dttmcp_endpoint_get_story_package( $request ) {
    $body = dttmcp_body( $request ); $id = dttmcp_id( $body['truyen_id'] ?? 0 ); $story = dttmcp_post( $id, 'truyen' ); if ( ! $story ) return dttmcp_error_response( $request, 'TRUYEN_NOT_FOUND', 'Story not found.', 404 );
    $permission = dttmcp_require_capability( $request, 'read', $id ); if ( $permission !== true ) return $permission;
    $chapters = array_map( 'dttmcp_post_payload', dttmcp_related_chapters( $id, $body['per_page'] ?? 200 ) );
    return dttmcp_response( $request, true, array( 'story' => dttmcp_post_payload( $story ), 'chapters' => $chapters, 'chapter_count' => count( $chapters ) ) );
}

function dttmcp_endpoint_create_truyen( $request ) {
    $body = dttmcp_body( $request ); $status = dttmcp_create_status_guard( $body ); if ( is_wp_error( $status ) ) return $status;
    $permission = dttmcp_require_capability( $request, 'edit_posts' ); if ( $permission !== true ) return $permission;
    $warnings = array(); $result = dttmcp_create_story_internal( $body, $warnings ); if ( is_wp_error( $result ) ) { dttmcp_audit( $request, 'create_truyen', array(), false, $result->get_error_code() ); return $result; }
    dttmcp_audit( $request, 'create_truyen', array( $result['id'] ), true, 'CREATED' );
    return dttmcp_response( $request, true, array( 'id' => $result['id'], 'action' => 'created', 'truyen' => dttmcp_post_payload( $result['post'] ) ), $warnings, null, 201 );
}

function dttmcp_endpoint_create_chuong( $request ) {
    $body = dttmcp_body( $request ); $status = dttmcp_create_status_guard( $body ); if ( is_wp_error( $status ) ) return $status;
    $parent_id = dttmcp_id( $body['truyen_id'] ?? 0 ); $permission = dttmcp_require_capability( $request, 'edit_posts', $parent_id ); if ( $permission !== true ) return $permission;
    $warnings = array(); $result = dttmcp_create_chapter_internal( $body, $parent_id, $warnings ); if ( is_wp_error( $result ) ) { dttmcp_audit( $request, 'create_chuong', array( $parent_id ), false, $result->get_error_code() ); return $result; }
    dttmcp_audit( $request, 'create_chuong', array( $result['id'], $parent_id ), true, 'CREATED' );
    return dttmcp_response( $request, true, array( 'id' => $result['id'], 'action' => 'created', 'chuong' => dttmcp_post_payload( $result['post'] ) ), $warnings, null, 201 );
}

function dttmcp_endpoint_update_truyen( $request ) {
    $body = dttmcp_body( $request ); $id = dttmcp_id( $body['truyen_id'] ?? 0 ); $post = dttmcp_post( $id, 'truyen' ); if ( ! $post ) return dttmcp_error_response( $request, 'TRUYEN_NOT_FOUND', 'Story not found.', 404 );
    $permission = dttmcp_require_capability( $request, 'edit_posts', $id ); if ( $permission !== true ) return $permission; $lock = dttmcp_expected_lock( $request, $post ); if ( $lock !== true ) return $lock;
    $warnings = array(); $updated = dttmcp_update_story_internal( $post, $body, $warnings ); if ( is_wp_error( $updated ) ) { dttmcp_audit( $request, 'update_truyen', array( $id ), false, $updated->get_error_code() ); return $updated; }
    dttmcp_audit( $request, 'update_truyen', array( $id ), true, 'UPDATED' ); return dttmcp_response( $request, true, array( 'id' => $id, 'action' => 'updated', 'truyen' => dttmcp_post_payload( $updated ) ), $warnings );
}

function dttmcp_endpoint_update_chuong( $request ) {
    $body = dttmcp_body( $request ); $id = dttmcp_id( $body['chuong_id'] ?? 0 ); $post = dttmcp_post( $id, 'chuong' ); if ( ! $post ) return dttmcp_error_response( $request, 'CHUONG_NOT_FOUND', 'Chapter not found.', 404 );
    $permission = dttmcp_require_capability( $request, 'edit_posts', $id ); if ( $permission !== true ) return $permission; $lock = dttmcp_expected_lock( $request, $post ); if ( $lock !== true ) return $lock;
    $warnings = array(); $updated = dttmcp_update_chapter_internal( $post, $body, $warnings ); if ( is_wp_error( $updated ) ) { dttmcp_audit( $request, 'update_chuong', array( $id ), false, $updated->get_error_code() ); return $updated; }
    dttmcp_audit( $request, 'update_chuong', array( $id ), true, 'UPDATED' ); return dttmcp_response( $request, true, array( 'id' => $id, 'action' => 'updated', 'chuong' => dttmcp_post_payload( $updated ) ), $warnings );
}

function dttmcp_endpoint_update_status( $request, $type ) {
    $body = dttmcp_body( $request ); $id_field = 'truyen' === $type ? 'truyen_id' : 'chuong_id'; $id = dttmcp_id( $body[ $id_field ] ?? 0 ); $post = dttmcp_post( $id, $type ); if ( ! $post ) return dttmcp_error_response( $request, 'truyen' === $type ? 'TRUYEN_NOT_FOUND' : 'CHUONG_NOT_FOUND', 'Post not found.', 404 );
    if ( 'publish' === (string) ( $body['status'] ?? '' ) ) return dttmcp_error_response( $request, 'PUBLISH_REQUIRES_CONFIRMATION', 'Use the explicit publish tool with a confirmation_token.', 422 );
    $status = (string) ( $body['status'] ?? '' ); if ( ! in_array( $status, array( 'draft', 'pending', 'private', 'future' ), true ) ) return dttmcp_error_response( $request, 'INVALID_STATUS', 'Only draft, pending, private, or future are allowed here.', 422 );
    $permission = dttmcp_require_capability( $request, 'edit_posts', $id ); if ( $permission !== true ) return $permission; $lock = dttmcp_expected_lock( $request, $post ); if ( $lock !== true ) return $lock;
    $schedule = array(); if ( 'future' === $status ) { $schedule = dttmcp_schedule_data( $body['schedule_at'] ?? null ); if ( is_wp_error( $schedule ) ) return $schedule; if ( empty( $schedule ) ) return dttmcp_error_response( $request, 'SCHEDULE_REQUIRED', 'future status requires schedule_at.', 422 ); }
    $updated = dttmcp_status_write( $id, $status, $schedule ); if ( is_wp_error( $updated ) ) { dttmcp_audit( $request, 'update_' . $type . '_status', array( $id ), false, $updated->get_error_code() ); return $updated; }
    dttmcp_audit( $request, 'update_' . $type . '_status', array( $id ), true, 'STATUS_UPDATED' ); return dttmcp_response( $request, true, array( 'id' => $id, 'status' => (string) get_post( $id )->post_status, 'post' => dttmcp_post_payload( get_post( $id ) ) ) );
}

function dttmcp_endpoint_update_truyen_status( $request ) { return dttmcp_endpoint_update_status( $request, 'truyen' ); }
function dttmcp_endpoint_update_chuong_status( $request ) { return dttmcp_endpoint_update_status( $request, 'chuong' ); }

function dttmcp_rollback_package_posts( $ids ) {
    $deleted = array(); $failed = array();
    foreach ( array_values( array_unique( array_map( 'dttmcp_id', (array) $ids ) ) ) as $id ) {
        if ( ! $id ) continue;
        $post = dttmcp_post( $id );
        if ( ! $post ) { $failed[] = $id; continue; }
        if ( function_exists( 'wp_delete_post' ) && wp_delete_post( $id, true ) ) $deleted[] = $id;
        else $failed[] = $id;
    }
    return array( 'ok' => empty( $failed ), 'deleted_ids' => $deleted, 'failed_ids' => $failed );
}

function dttmcp_endpoint_create_story_package( $request ) {
    $body = dttmcp_body( $request );
    $idempotency = dttmcp_idempotency_check( 'create_package', $body );
    if ( is_wp_error( $idempotency ) ) return $idempotency;
    if ( ! empty( $idempotency['stored'] ) ) return dttmcp_replay_idempotency( $request, $idempotency['stored'] );
    $story = is_array( $body['story'] ?? null ) ? $body['story'] : array();
    $chapters = is_array( $body['chapters'] ?? null ) ? $body['chapters'] : array();
    $status = dttmcp_create_status_guard( $story );
    if ( is_wp_error( $status ) ) return $status;
    foreach ( $chapters as $chapter ) {
        $status = dttmcp_create_status_guard( is_array( $chapter ) ? $chapter : array() );
        if ( is_wp_error( $status ) ) return $status;
    }
    if ( empty( $chapters ) ) return dttmcp_error_response( $request, 'CHAPTERS_REQUIRED', 'At least one chapter is required.', 400 );
    $permission = dttmcp_require_capability( $request, 'edit_posts' );
    if ( $permission !== true ) return $permission;

    $warnings = array();
    $story_result = dttmcp_create_story_internal( $story, $warnings );
    if ( is_wp_error( $story_result ) ) {
        $details = dttmcp_wp_error_details( $story_result );
        if ( ! empty( $details['created_id'] ) ) dttmcp_rollback_package_posts( array( $details['created_id'] ) );
        dttmcp_audit( $request, 'create_story_package', ! empty( $details['created_id'] ) ? array( $details['created_id'] ) : array(), false, $story_result->get_error_code() );
        return $story_result;
    }

    $story_id = dttmcp_id( $story_result['id'] );
    $created_chapter_ids = array();
    $chapter_results = array();
    $failed = 0;
    $next_number = 1;
    foreach ( $chapters as $index => $chapter ) {
        $chapter = is_array( $chapter ) ? $chapter : array();
        $number = dttmcp_id( $chapter['chapter_number'] ?? 0 );
        if ( ! $number ) {
            $number = $next_number;
            $chapter['chapter_number'] = $number;
        }
        $next_number = max( $next_number, $number + 1 );
        $result = dttmcp_create_chapter_internal( $chapter, $story_id, $warnings );
        if ( is_wp_error( $result ) ) {
            $failed++;
            $chapter_results[] = array( 'index' => $index, 'ok' => false, 'chapter_number' => $number, 'error' => array( 'code' => $result->get_error_code(), 'message' => dttmcp_wp_error_message( $result ) ) );
            break;
        }
        $created_chapter_ids[] = dttmcp_id( $result['id'] );
        $chapter_results[] = array( 'index' => $index, 'ok' => true, 'id' => $result['id'], 'chapter_number' => $number, 'action' => 'created' );
    }

    if ( $failed ) {
        $rollback = dttmcp_rollback_package_posts( array_merge( array( $story_id ), $created_chapter_ids ) );
        $data = array(
            'status' => $rollback['ok'] ? 'rolled_back' : 'partial',
            'story' => array( 'id' => $story_id, 'action' => $rollback['ok'] ? 'rolled_back' : 'created' ),
            'chapters' => array( 'created_before_rollback' => count( $created_chapter_ids ), 'updated' => 0, 'failed' => $failed, 'items' => $chapter_results ),
            'rolled_back' => (bool) $rollback['ok'],
            'rollback' => $rollback,
        );
        $error = $rollback['ok']
            ? array( 'code' => 'PACKAGE_ROLLED_BACK', 'message' => 'A chapter failed, so all newly created story-package drafts were rolled back.' )
            : array( 'code' => 'PARTIAL_FAILURE', 'message' => 'A chapter failed and rollback was incomplete; inspect the returned IDs before retrying.' );
        $response = dttmcp_response( $request, false, $data, $warnings, $error, 207 );
        dttmcp_store_idempotency( 'create_package', $idempotency, $response );
        dttmcp_audit( $request, 'create_story_package', array_merge( array( $story_id ), $created_chapter_ids ), false, $error['code'], array( 'rollback' => $rollback ) );
        return $response;
    }

    $data = array(
        'status' => 'created',
        'story' => array( 'id' => $story_id, 'action' => 'created' ),
        'chapters' => array( 'created' => count( $created_chapter_ids ), 'updated' => 0, 'failed' => 0, 'items' => $chapter_results ),
        'rolled_back' => false,
    );
    $response = dttmcp_response( $request, true, $data, $warnings );
    dttmcp_store_idempotency( 'create_package', $idempotency, $response );
    dttmcp_audit( $request, 'create_story_package', array_merge( array( $story_id ), $created_chapter_ids ), true, 'CREATED' );
    return $response;
}

function dttmcp_endpoint_validate_truyen( $request ) {
    $id = dttmcp_id( dttmcp_body( $request )['truyen_id'] ?? 0 ); $post = dttmcp_post( $id, 'truyen' ); if ( ! $post ) return dttmcp_error_response( $request, 'TRUYEN_NOT_FOUND', 'Story not found.', 404 );
    $errors = dttmcp_story_validation( $post ); $data = array( 'valid' => empty( $errors ), 'errors' => $errors, 'truyen' => dttmcp_post_payload( $post ) ); if ( $errors ) return dttmcp_error_response( $request, 'VALIDATION_FAILED', 'Story failed validation.', 422, array( 'errors' => $errors ), $data ); return dttmcp_response( $request, true, $data );
}

function dttmcp_endpoint_validate_chuong( $request ) {
    $id = dttmcp_id( dttmcp_body( $request )['chuong_id'] ?? 0 ); $post = dttmcp_post( $id, 'chuong' ); if ( ! $post ) return dttmcp_error_response( $request, 'CHUONG_NOT_FOUND', 'Chapter not found.', 404 );
    $errors = dttmcp_chapter_validation( $post ); $data = array( 'valid' => empty( $errors ), 'errors' => $errors, 'chuong' => dttmcp_post_payload( $post ) ); if ( $errors ) return dttmcp_error_response( $request, 'VALIDATION_FAILED', 'Chapter failed validation.', 422, array( 'errors' => $errors ), $data ); return dttmcp_response( $request, true, $data );
}

function dttmcp_endpoint_pre_publish( $request ) {
    $body = dttmcp_body( $request ); $story_id = dttmcp_id( $body['truyen_id'] ?? 0 ); $chapter_ids = array_values( array_unique( array_map( 'dttmcp_id', (array) ( $body['chapter_ids'] ?? array() ) ) ) ); $package = dttmcp_validate_package( $story_id, $chapter_ids ); if ( is_wp_error( $package ) ) return $package; if ( ! empty( $package['errors'] ) ) return dttmcp_error_response( $request, 'VALIDATION_FAILED', 'The story package is not ready to publish.', 422, array( 'errors' => $package['errors'] ), array( 'truyen_id' => $story_id, 'chapter_ids' => $chapter_ids ) );
    $permission = dttmcp_require_capability( $request, 'edit_posts', $story_id ); if ( $permission !== true ) return $permission;
    $data = dttmcp_confirmation_record( $request, $body, $package['story'], $package['chapters'] ); return dttmcp_response( $request, true, array_merge( $data, array( 'validated' => true ) ), array( 'TOKEN_IS_ONE_TIME_AND_EXPIRES' ) );
}

function dttmcp_endpoint_publish_truyen( $request ) {
    $body = dttmcp_body( $request ); $id = dttmcp_id( $body['truyen_id'] ?? 0 ); $story = dttmcp_post( $id, 'truyen' ); if ( ! $story ) return dttmcp_error_response( $request, 'TRUYEN_NOT_FOUND', 'Story not found.', 404 ); $ids = array_values( array_unique( array_map( 'dttmcp_id', (array) ( $body['chapter_ids'] ?? array() ) ) ) );
    $permission = dttmcp_require_capability( $request, 'publish_posts', $id ); if ( $permission !== true ) return $permission; $token = dttmcp_consume_confirmation( $body, $story, $ids, $request ); if ( is_wp_error( $token ) ) return $token;
    $before = (string) $story->post_status; $updated = dttmcp_status_write( $id, 'publish' ); if ( is_wp_error( $updated ) || ! dttmcp_status_verified( $id, 'publish' ) ) { $code = is_wp_error( $updated ) ? $updated->get_error_code() : 'PUBLISH_VERIFY_FAILED'; dttmcp_audit( $request, 'publish_truyen', array( $id ), false, $code ); return is_wp_error( $updated ) ? $updated : dttmcp_wp_error( $code, 'Story publish read-back verification failed.', 502 ); }
    dttmcp_audit( $request, 'publish_truyen', array( $id ), true, 'PUBLISHED' ); return dttmcp_response( $request, true, array( 'id' => $id, 'status_before' => $before, 'status_after' => 'publish', 'verified' => true, 'truyen' => dttmcp_post_payload( get_post( $id ) ) ) );
}

function dttmcp_endpoint_publish_chuong( $request ) {
    $body = dttmcp_body( $request ); $id = dttmcp_id( $body['chuong_id'] ?? 0 ); $chapter = dttmcp_post( $id, 'chuong' ); if ( ! $chapter ) return dttmcp_error_response( $request, 'CHUONG_NOT_FOUND', 'Chapter not found.', 404 ); $parent_id = dttmcp_id( $body['truyen_id'] ?? get_post_meta( $id, DTTMCP_RELATION_META_KEY, true ) ); $story = dttmcp_post( $parent_id, 'truyen' ); if ( ! $story ) return dttmcp_error_response( $request, 'TRUYEN_NOT_FOUND', 'Parent story not found.', 404 );
    $errors = dttmcp_chapter_validation( $chapter ); if ( $errors ) return dttmcp_error_response( $request, 'VALIDATION_FAILED', 'Chapter failed publishing validation.', 422, array( 'errors' => $errors ) ); $permission = dttmcp_require_capability( $request, 'publish_posts', $id ); if ( $permission !== true ) return $permission;
    $ids = array_values( array_unique( array_map( 'dttmcp_id', (array) ( $body['chapter_ids'] ?? array( $id ) ) ) ) ); $token = dttmcp_consume_confirmation( $body, $story, $ids, $request ); if ( is_wp_error( $token ) ) return $token;
    $before = (string) $chapter->post_status; $schedule = dttmcp_schedule_data( $body['schedule_at'] ?? null ); if ( is_wp_error( $schedule ) ) return $schedule; $updated = dttmcp_status_write( $id, empty( $schedule ) ? 'publish' : 'future', $schedule ); if ( is_wp_error( $updated ) || ! dttmcp_status_verified( $id, empty( $schedule ) ? 'publish' : 'future' ) ) { $code = is_wp_error( $updated ) ? $updated->get_error_code() : 'PUBLISH_VERIFY_FAILED'; dttmcp_audit( $request, 'publish_chuong', array( $id ), false, $code ); return is_wp_error( $updated ) ? $updated : dttmcp_wp_error( $code, 'Chapter publish read-back verification failed.', 502 ); }
    dttmcp_audit( $request, 'publish_chuong', array( $id ), true, empty( $schedule ) ? 'PUBLISHED' : 'SCHEDULED' ); return dttmcp_response( $request, true, array( 'id' => $id, 'status_before' => $before, 'status_after' => empty( $schedule ) ? 'publish' : 'future', 'verified' => true, 'chuong' => dttmcp_post_payload( get_post( $id ) ) ) );
}

function dttmcp_endpoint_publish_package( $request ) {
    $body = dttmcp_body( $request ); $idempotency = dttmcp_idempotency_check( 'publish_package', $body ); if ( is_wp_error( $idempotency ) ) return $idempotency; if ( ! empty( $idempotency['stored'] ) ) return dttmcp_replay_idempotency( $request, $idempotency['stored'] );
    $story_id = dttmcp_id( $body['truyen_id'] ?? 0 ); $chapter_ids = array_values( array_unique( array_map( 'dttmcp_id', (array) ( $body['chapter_ids'] ?? array() ) ) ) ); if ( empty( $chapter_ids ) ) return dttmcp_error_response( $request, 'CHAPTERS_REQUIRED', 'publish_story_package requires at least one chapter.', 422 ); $package = dttmcp_validate_package( $story_id, $chapter_ids ); if ( is_wp_error( $package ) ) return $package; if ( ! empty( $package['errors'] ) ) return dttmcp_error_response( $request, 'VALIDATION_FAILED', 'The story package is not ready to publish.', 422, array( 'errors' => $package['errors'] ) );
    $permission = dttmcp_require_capability( $request, 'publish_posts', $story_id ); if ( $permission !== true ) return $permission; $token = dttmcp_consume_confirmation( $body, $package['story'], $chapter_ids, $request ); if ( is_wp_error( $token ) ) return $token;
    $snapshots = array( $story_id => dttmcp_snapshot( $package['story'] ) ); foreach ( $package['ordered'] as $chapter ) $snapshots[ (int) $chapter->ID ] = dttmcp_snapshot( $chapter );
    $results = array( 'truyen' => array( 'id' => $story_id, 'status_before' => $package['story']->post_status, 'status_after' => null, 'ok' => false ), 'chapters' => array() ); $changed = array(); $failure = null;
    $updated = dttmcp_status_write( $story_id, 'publish' ); if ( is_wp_error( $updated ) || ! dttmcp_status_verified( $story_id, 'publish' ) ) { $failure = is_wp_error( $updated ) ? $updated : dttmcp_wp_error( 'PUBLISH_VERIFY_FAILED', 'Story publish read-back verification failed.', 502 ); } else { $results['truyen']['status_after'] = 'publish'; $results['truyen']['ok'] = true; $changed[] = $story_id; }
    if ( ! $failure ) foreach ( $package['ordered'] as $chapter ) {
        $id = (int) $chapter->ID; $entry = array( 'id' => $id, 'chapter_number' => dttmcp_chapter_number( $chapter ), 'status_before' => $chapter->post_status, 'status_after' => null, 'ok' => false ); $updated = dttmcp_status_write( $id, 'publish' ); if ( is_wp_error( $updated ) || ! dttmcp_status_verified( $id, 'publish' ) ) { $failure = is_wp_error( $updated ) ? $updated : dttmcp_wp_error( 'PUBLISH_VERIFY_FAILED', 'Chapter publish read-back verification failed.', 502 ); $entry['error'] = array( 'code' => $failure->get_error_code(), 'message' => dttmcp_wp_error_message( $failure ) ); $results['chapters'][] = $entry; break; } $entry['status_after'] = 'publish'; $entry['ok'] = true; $results['chapters'][] = $entry; $changed[] = $id;
    }
    $rolled_back = false;
    if ( $failure ) {
        $rolled_back = true; foreach ( array_reverse( $changed ) as $changed_id ) { $restored = dttmcp_restore( $snapshots[ $changed_id ] ); if ( is_wp_error( $restored ) || ! dttmcp_status_verified( $changed_id, $snapshots[ $changed_id ]['post_status'] ) ) $rolled_back = false; }
        $data = array( 'truyen_id' => $story_id, 'chapter_ids' => $chapter_ids, 'results' => $results, 'rolled_back' => $rolled_back, 'verified' => $rolled_back ); $response = dttmcp_response( $request, false, $data, array(), array( 'code' => $rolled_back ? 'PUBLISH_ROLLED_BACK' : 'PUBLISH_ROLLBACK_FAILED', 'message' => dttmcp_wp_error_message( $failure ) ), 207 ); dttmcp_store_idempotency( 'publish_package', $idempotency, $response ); dttmcp_audit( $request, 'publish_story_package', array_merge( array( $story_id ), $chapter_ids ), false, $rolled_back ? 'PUBLISH_ROLLED_BACK' : 'PUBLISH_ROLLBACK_FAILED', array( 'rolled_back' => $rolled_back ) ); return $response;
    }
    $verified = dttmcp_status_verified( $story_id, 'publish' ); foreach ( $chapter_ids as $id ) $verified = $verified && dttmcp_status_verified( $id, 'publish' );
    if ( ! $verified ) { $failure = dttmcp_wp_error( 'PUBLISH_VERIFY_FAILED', 'Package read-back verification failed.', 502 ); foreach ( array_reverse( $changed ) as $changed_id ) dttmcp_restore( $snapshots[ $changed_id ] ); $data = array( 'truyen_id' => $story_id, 'chapter_ids' => $chapter_ids, 'results' => $results, 'rolled_back' => true, 'verified' => false ); return dttmcp_response( $request, false, $data, array(), array( 'code' => $failure->get_error_code(), 'message' => dttmcp_wp_error_message( $failure ) ), 207 ); }
    $data = array( 'truyen_id' => $story_id, 'chapter_ids' => $chapter_ids, 'results' => $results, 'rolled_back' => false, 'verified' => true ); $response = dttmcp_response( $request, true, $data ); dttmcp_store_idempotency( 'publish_package', $idempotency, $response ); dttmcp_audit( $request, 'publish_story_package', array_merge( array( $story_id ), $chapter_ids ), true, 'PUBLISHED' ); return $response;
}

function dttmcp_endpoint_unpublish( $request, $type ) {
    $body = dttmcp_body( $request ); $field = 'truyen' === $type ? 'truyen_id' : 'chuong_id'; $id = dttmcp_id( $body[ $field ] ?? 0 ); $post = dttmcp_post( $id, $type ); if ( ! $post ) return dttmcp_error_response( $request, 'truyen' === $type ? 'TRUYEN_NOT_FOUND' : 'CHUONG_NOT_FOUND', 'Post not found.', 404 ); $permission = dttmcp_require_capability( $request, 'publish_posts', $id ); if ( $permission !== true ) return $permission; $lock = dttmcp_expected_lock( $request, $post ); if ( $lock !== true ) return $lock;
    $updated = dttmcp_status_write( $id, 'draft' ); if ( is_wp_error( $updated ) ) { dttmcp_audit( $request, 'unpublish_' . $type, array( $id ), false, $updated->get_error_code() ); return $updated; } dttmcp_audit( $request, 'unpublish_' . $type, array( $id ), true, 'UNPUBLISHED' ); return dttmcp_response( $request, true, array( 'id' => $id, 'status_before' => $post->post_status, 'status_after' => 'draft', 'verified' => dttmcp_status_verified( $id, 'draft' ), 'post' => dttmcp_post_payload( get_post( $id ) ) ) );
}
function dttmcp_endpoint_unpublish_truyen( $request ) { return dttmcp_endpoint_unpublish( $request, 'truyen' ); }
function dttmcp_endpoint_unpublish_chuong( $request ) { return dttmcp_endpoint_unpublish( $request, 'chuong' ); }

function dttmcp_endpoint_integrity( $request ) {
    $body = dttmcp_body( $request ); $story_id = dttmcp_id( $body['truyen_id'] ?? 0 ); $story = dttmcp_post( $story_id, 'truyen' ); if ( ! $story ) return dttmcp_error_response( $request, 'TRUYEN_NOT_FOUND', 'Story not found.', 404 ); $ids = isset( $body['chapter_ids'] ) ? array_values( array_unique( array_map( 'dttmcp_id', (array) $body['chapter_ids'] ) ) ) : array_map( function ( $post ) { return (int) $post->ID; }, dttmcp_related_chapters( $story_id ) ); $errors = array(); $numbers = array(); $ordered = array(); foreach ( $ids as $id ) { $chapter = dttmcp_post( $id, 'chuong' ); if ( ! $chapter ) { $errors[] = 'CHAPTER_NOT_FOUND_' . $id; continue; } $parent = dttmcp_id( get_post_meta( $id, DTTMCP_RELATION_META_KEY, true ) ); if ( $parent !== $story_id ) $errors[] = 'CHAPTER_PARENT_MISMATCH_' . $id; $number = dttmcp_chapter_number( $chapter ); if ( $number <= 0 ) $errors[] = 'CHAPTER_NUMBER_REQUIRED_' . $id; if ( isset( $numbers[ $number ] ) ) $errors[] = 'DUPLICATE_CHAPTER_NUMBER_' . $number; $numbers[ $number ] = $id; if ( trim( wp_strip_all_tags( (string) $chapter->post_content ) ) === '' ) $errors[] = 'CONTENT_REQUIRED_' . $id; $ordered[] = array( 'id' => $id, 'chapter_number' => $number ); } usort( $ordered, function ( $a, $b ) { return $a['chapter_number'] === $b['chapter_number'] ? $a['id'] <=> $b['id'] : $a['chapter_number'] <=> $b['chapter_number']; } ); $data = array( 'valid' => empty( $errors ), 'truyen_id' => $story_id, 'checked_chapter_ids' => $ids, 'ordered_chapters' => $ordered, 'errors' => array_values( array_unique( $errors ) ) ); if ( $errors ) return dttmcp_error_response( $request, 'STORY_INTEGRITY_FAILED', 'Story relationship integrity check failed.', 422, array( 'errors' => $errors ), $data ); return dttmcp_response( $request, true, $data );
}

function dttmcp_endpoint_find_truyen( $request ) { $body = dttmcp_body( $request ); $results = array(); foreach ( dttmcp_posts( array( 'post_type' => 'truyen', 'posts_per_page' => 200 ) ) as $post ) { if ( ! empty( $body['truyen_id'] ) && (int) $body['truyen_id'] !== (int) $post->ID ) continue; if ( ! empty( $body['slug'] ) && dttmcp_sanitize_slug( $body['slug'] ) !== $post->post_name ) continue; if ( ! empty( $body['title'] ) && dttmcp_normalize_title( $body['title'] ) !== dttmcp_normalize_title( $post->post_title ) ) continue; $results[] = dttmcp_post_payload( $post ); } return dttmcp_response( $request, true, array( 'items' => $results, 'count' => count( $results ) ) ); }
function dttmcp_endpoint_find_chuong( $request ) { $body = dttmcp_body( $request ); $posts = ! empty( $body['truyen_id'] ) ? dttmcp_related_chapters( dttmcp_id( $body['truyen_id'] ) ) : dttmcp_posts( array( 'post_type' => 'chuong', 'posts_per_page' => 200 ) ); $results = array(); foreach ( $posts as $post ) { if ( ! empty( $body['chapter_number'] ) && dttmcp_chapter_number( $post ) !== dttmcp_id( $body['chapter_number'] ) ) continue; if ( ! empty( $body['title'] ) && dttmcp_normalize_title( $body['title'] ) !== dttmcp_normalize_title( $post->post_title ) ) continue; if ( ! empty( $body['slug'] ) && dttmcp_sanitize_slug( $body['slug'] ) !== $post->post_name ) continue; $results[] = dttmcp_post_payload( $post ); } return dttmcp_response( $request, true, array( 'items' => $results, 'count' => count( $results ) ) ); }

/* v4 normal post/media/taxonomy/SEO surface. These routes deliberately use fixed
 * object types and fixed SEO mappings; callers cannot select arbitrary meta. */
function dttmcp_normal_post( $id ) { return dttmcp_post( $id, 'post' ); }
function dttmcp_seo_provider() {
    if ( defined( 'RANK_MATH_VERSION' ) || class_exists( 'RankMath\\Core' ) ) return 'rank_math';
    if ( defined( 'WPSEO_VERSION' ) || defined( 'WPSEO_FILE' ) ) return 'yoast';
    return 'none';
}
function dttmcp_seo_keys() {
    return 'rank_math' === dttmcp_seo_provider()
        ? array( 'seo_title' => '_rank_math_title', 'meta_description' => '_rank_math_description', 'focus_keyword' => '_rank_math_focus_keyword', 'canonical_url' => '_rank_math_canonical_url', 'facebook_title' => '_rank_math_facebook_title', 'facebook_description' => '_rank_math_facebook_description', 'facebook_image' => '_rank_math_facebook_image', 'twitter_title' => '_rank_math_twitter_title', 'twitter_description' => '_rank_math_twitter_description', 'twitter_image' => '_rank_math_twitter_image' )
        : ( 'yoast' === dttmcp_seo_provider() ? array( 'seo_title' => '_yoast_wpseo_title', 'meta_description' => '_yoast_wpseo_metadesc', 'focus_keyword' => '_yoast_wpseo_focuskw', 'canonical_url' => '_yoast_wpseo_canonical' ) : array() );
}
function dttmcp_allowed_robots( $value ) { return in_array( (string) $value, array( 'index,follow', 'noindex,follow', 'index,nofollow', 'noindex,nofollow' ), true ); }
function dttmcp_get_robots( $post_id ) { $provider = dttmcp_seo_provider(); if ( 'rank_math' === $provider ) { $stored = get_post_meta( $post_id, '_rank_math_robots', true ); if ( is_array( $stored ) ) return implode( ',', $stored ); return (string) $stored; } if ( 'yoast' === $provider ) { $noindex = '1' === (string) get_post_meta( $post_id, '_yoast_wpseo_meta-robots-noindex', true ); $nofollow = '1' === (string) get_post_meta( $post_id, '_yoast_wpseo_meta-robots-nofollow', true ); return ( $noindex ? 'noindex' : 'index' ) . ',' . ( $nofollow ? 'nofollow' : 'follow' ); } return ''; }
function dttmcp_set_robots( $post_id, $value ) { if ( ! dttmcp_allowed_robots( $value ) ) return dttmcp_wp_error( 'VALIDATION_ERROR', 'robots must be one of the four supported index/follow combinations.', 422 ); list( $index, $follow ) = explode( ',', $value, 2 ); if ( 'rank_math' === dttmcp_seo_provider() ) { update_post_meta( $post_id, '_rank_math_robots', array( $index, $follow ) ); return true; } if ( 'yoast' === dttmcp_seo_provider() ) { update_post_meta( $post_id, '_yoast_wpseo_meta-robots-noindex', 'noindex' === $index ? '1' : '2' ); update_post_meta( $post_id, '_yoast_wpseo_meta-robots-nofollow', 'nofollow' === $follow ? '1' : '0' ); return true; } return dttmcp_wp_error( 'SEO_PROVIDER_UNAVAILABLE', 'No supported SEO plugin is active.', 422 ); }
function dttmcp_seo_payload( $post_id ) {
    $keys = dttmcp_seo_keys(); $result = array( 'provider' => dttmcp_seo_provider(), 'active' => 'none' !== dttmcp_seo_provider() );
    foreach ( $keys as $field => $key ) $result[ $field ] = function_exists( 'get_post_meta' ) ? (string) get_post_meta( $post_id, $key, true ) : '';
    $result['robots'] = function_exists( 'get_post_meta' ) ? dttmcp_get_robots( $post_id ) : '';
    return $result;
}
function dttmcp_post_v4_payload( $post ) {
    $data = dttmcp_post_payload( $post );
    $data['categories'] = dttmcp_terms( $post->ID, 'category' );
    $data['tags'] = dttmcp_terms( $post->ID, 'post_tag' );
    $data['seo'] = dttmcp_seo_payload( $post->ID );
    $thumb = function_exists( 'get_post_thumbnail_id' ) ? dttmcp_id( get_post_thumbnail_id( $post->ID ) ) : 0;
    $data['featured_image'] = $thumb;
    if ( $thumb && function_exists( 'wp_get_attachment_image_url' ) ) $data['featured_image_url'] = wp_get_attachment_image_url( $thumb, 'full' );
    return $data;
}
function dttmcp_post_list_item( $post ) { return array( 'id' => (int) $post->ID, 'title' => (string) $post->post_title, 'slug' => (string) $post->post_name, 'status' => (string) $post->post_status, 'post_type' => (string) $post->post_type, 'modified' => dttmcp_modified_gmt( $post ), 'link' => function_exists( 'get_permalink' ) ? get_permalink( $post->ID ) : '' ); }
function dttmcp_identity_post_statuses() { return array( 'publish', 'future', 'draft', 'pending', 'private', 'trash' ); }
/**
 * Centralized normal-post identity validation.
 *
 * On updates, title and slug checks are opt-in per supplied field. This is
 * important because content/excerpt-only updates must not manufacture an
 * identity check from omitted fields. On creates, the required title is also
 * the WordPress slug fallback when no explicit slug was supplied.
 */
function dttmcp_post_duplicate( $body, $exclude = 0 ) {
    $has_title = array_key_exists( 'title', $body );
    $has_slug  = array_key_exists( 'slug', $body );
    $exclude   = dttmcp_id( $exclude );

    if ( $has_slug ) {
        $slug = dttmcp_sanitize_slug( $body['slug'] );
        if ( '' !== $slug ) {
            foreach ( dttmcp_posts( array( 'post_type' => 'post', 'post_status' => dttmcp_identity_post_statuses(), 'name' => $slug, 'posts_per_page' => 20 ) ) as $post ) {
                if ( (int) $post->ID !== $exclude ) return $post;
            }
        }
    } elseif ( $has_title ) {
        $slug = dttmcp_sanitize_slug( $body['title'] );
        if ( '' !== $slug ) {
            foreach ( dttmcp_posts( array( 'post_type' => 'post', 'post_status' => dttmcp_identity_post_statuses(), 'name' => $slug, 'posts_per_page' => 20 ) ) as $post ) {
                if ( (int) $post->ID !== $exclude ) return $post;
            }
        }
    }

    if ( $has_title ) {
        $normalized = dttmcp_normalize_title( $body['title'] );
        if ( '' !== $normalized ) {
            foreach ( dttmcp_posts( array( 'post_type' => 'post', 'post_status' => dttmcp_identity_post_statuses(), 'posts_per_page' => 5000 ) ) as $post ) {
                if ( (int) $post->ID !== $exclude && dttmcp_normalize_title( $post->post_title ) === $normalized ) return $post;
            }
        }
    }
    return null;
}

function dttmcp_post_duplicate_details( $post ) {
    return array(
        'matched_post_id' => (int) $post->ID,
        'matched_title'   => (string) $post->post_title,
        'matched_slug'    => (string) $post->post_name,
        'matched_status'  => (string) $post->post_status,
    );
}
function dttmcp_post_fields( $body, $id = 0 ) {
    $data = array( 'post_type' => 'post' ); if ( $id ) $data['ID'] = $id;
    foreach ( array( 'title', 'content', 'excerpt', 'slug' ) as $field ) if ( array_key_exists( $field, $body ) ) $data[ 'post_' . ( 'title' === $field ? 'title' : ( 'content' === $field ? 'content' : ( 'excerpt' === $field ? 'excerpt' : 'name' ) ) ) ] = 'content' === $field ? dttmcp_sanitize_html( $body[ $field ] ) : ( 'excerpt' === $field ? dttmcp_sanitize_html( $body[ $field ] ) : ( 'slug' === $field ? dttmcp_sanitize_slug( $body[ $field ] ) : dttmcp_sanitize_text( $body[ $field ] ) ) );
    return $data;
}

function dttmcp_html_is_void_tag( $tag ) {
    return in_array( strtolower( (string) $tag ), array( 'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr' ), true );
}

function dttmcp_html_tokens( $html ) {
    $html = (string) $html;
    $tokens = array();
    $length = strlen( $html );
    for ( $offset = 0; $offset < $length; $offset++ ) {
        if ( '<' !== $html[ $offset ] ) continue;
        $end = false;
        if ( 0 === strpos( substr( $html, $offset ), '<!--' ) ) {
            $comment_end = strpos( $html, '-->', $offset + 4 );
            $end = false === $comment_end ? $length - 1 : $comment_end + 2;
        } else {
            $next = $offset + 1 < $length ? $html[ $offset + 1 ] : '';
            if ( ! preg_match( '/[A-Za-z\/!]/', $next ) ) continue;
            $quote = '';
            for ( $cursor = $offset + 1; $cursor < $length; $cursor++ ) {
                $character = $html[ $cursor ];
                if ( $quote !== '' ) {
                    if ( $character === $quote ) $quote = '';
                    continue;
                }
                if ( '"' === $character || "'" === $character ) {
                    $quote = $character;
                } elseif ( '>' === $character ) {
                    $end = $cursor;
                    break;
                }
            }
            if ( false === $end ) $end = $length - 1;
        }
        $tokens[] = array( 'offset' => $offset, 'length' => $end - $offset + 1, 'text' => substr( $html, $offset, $end - $offset + 1 ) );
        $offset = $end;
    }
    return $tokens;
}

function dttmcp_html_attribute( $attributes, $name ) {
    $pattern = "/(?:^|\\s)" . preg_quote( (string) $name, '/' ) . "\\s*=\\s*(?:\"([^\"]*)\"|'([^']*)'|([^\\s\"'=<>`]+))/i";
    if ( ! preg_match( $pattern, (string) $attributes, $matches ) ) return null;
    $value = $matches[1] ?? ( $matches[2] ?? ( $matches[3] ?? '' ) );
    return html_entity_decode( (string) $value, ENT_QUOTES | ENT_HTML5, 'UTF-8' );
}

function dttmcp_html_tag_info( $token ) {
    $token = trim( (string) $token );
    if ( '' === $token || 0 === strpos( $token, '<!--' ) || '<!' === substr( $token, 0, 2 ) || '<?' === substr( $token, 0, 2 ) ) return null;
    $inner = trim( substr( $token, 1, -1 ) );
    $closing = false;
    if ( '/' === substr( $inner, 0, 1 ) ) {
        $closing = true;
        $inner = ltrim( substr( $inner, 1 ) );
    }
    $self_closing = false;
    if ( '/' === substr( rtrim( $inner ), -1 ) ) {
        $self_closing = true;
        $inner = rtrim( substr( rtrim( $inner ), 0, -1 ) );
    }
    if ( ! preg_match( '/^([A-Za-z][A-Za-z0-9:_-]*)(.*)$/s', $inner, $matches ) ) return null;
    return array(
        'name'         => strtolower( $matches[1] ),
        'attributes'   => $matches[2],
        'closing'      => $closing,
        'self_closing' => $self_closing,
    );
}

/** Find one balanced element by exact id without broad regex replacement. */
function dttmcp_html_element_range( $html, $section_id ) {
    $target_id = html_entity_decode( trim( (string) $section_id ), ENT_QUOTES | ENT_HTML5, 'UTF-8' );
    $target_start = null;
    $stack = array();
    foreach ( dttmcp_html_tokens( $html ) as $token ) {
        $info = dttmcp_html_tag_info( $token['text'] );
        if ( ! $info ) continue;
        if ( null === $target_start ) {
            if ( $info['closing'] || dttmcp_html_attribute( $info['attributes'], 'id' ) !== $target_id ) continue;
            $target_start = (int) $token['offset'];
            if ( $info['self_closing'] || dttmcp_html_is_void_tag( $info['name'] ) ) return array( $target_start, $target_start + (int) $token['length'] );
            $stack[] = $info['name'];
            continue;
        }
        if ( ! $info['closing'] ) {
            if ( ! $info['self_closing'] && ! dttmcp_html_is_void_tag( $info['name'] ) ) $stack[] = $info['name'];
            continue;
        }
        if ( ! empty( $stack ) ) array_pop( $stack );
        if ( empty( $stack ) ) return array( $target_start, (int) $token['offset'] + (int) $token['length'] );
    }
    return false;
}

function dttmcp_patch_content_string( $content, $operation ) {
    $allowed = array( 'append', 'prepend', 'replace_exact', 'insert_before', 'insert_after', 'remove_exact', 'replace_section_id' );
    if ( ! in_array( (string) ( $operation['operation'] ?? '' ), $allowed, true ) ) return dttmcp_wp_error( 'INVALID_OPERATION', 'operation is not supported.', 422 );
    $name = (string) $operation['operation'];
    $content = (string) $content;
    if ( array_key_exists( 'html', $operation ) && strlen( (string) $operation['html'] ) > 500000 ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'html exceeds the 500000-byte patch limit.', 422 );
    if ( array_key_exists( 'needle', $operation ) && strlen( (string) $operation['needle'] ) > 100000 ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'needle exceeds the 100000-byte patch limit.', 422 );
    $needs_html = in_array( $name, array( 'append', 'prepend', 'replace_exact', 'insert_before', 'insert_after', 'replace_section_id' ), true );
    if ( $needs_html && ( ! array_key_exists( 'html', $operation ) || '' === trim( (string) $operation['html'] ) ) ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'html is required and cannot be empty for this operation.', 422 );
    $fragment = $needs_html ? dttmcp_sanitize_html( $operation['html'] ) : '';
    if ( $needs_html && '' === trim( $fragment ) ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'html is empty after WordPress content sanitization.', 422 );

    if ( 'append' === $name ) return array( 'content' => $content . $fragment );
    if ( 'prepend' === $name ) return array( 'content' => $fragment . $content );
    if ( 'replace_section_id' === $name ) {
        $section_id = trim( (string) ( $operation['section_id'] ?? '' ) );
        if ( '' === $section_id || ! preg_match( '/^[A-Za-z0-9][A-Za-z0-9:_-]{0,120}$/', $section_id ) ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'section_id must be a safe HTML id.', 422 );
        $range = dttmcp_html_element_range( $content, $section_id );
        if ( false === $range ) return dttmcp_wp_error( 'SECTION_NOT_FOUND', 'The requested HTML section was not found.', 404, array( 'section_id' => $section_id ) );
        return array( 'content' => substr( $content, 0, $range[0] ) . $fragment . substr( $content, $range[1] ) );
    }

    $needle = array_key_exists( 'needle', $operation ) ? (string) $operation['needle'] : '';
    if ( '' === $needle ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'needle is required for this operation.', 422 );
    $occurrence = 1;
    if ( array_key_exists( 'occurrence', $operation ) ) {
        if ( ! is_numeric( $operation['occurrence'] ) || (int) $operation['occurrence'] < 1 || (float) $operation['occurrence'] !== (float) (int) $operation['occurrence'] ) return dttmcp_wp_error( 'INVALID_OCCURRENCE', 'occurrence must be a positive integer.', 422 );
        $occurrence = (int) $operation['occurrence'];
    }
    $offset = 0;
    $position = false;
    for ( $index = 1; $index <= $occurrence; $index++ ) {
        $position = strpos( $content, $needle, $offset );
        if ( false === $position ) return dttmcp_wp_error( 'NEEDLE_NOT_FOUND', 'The exact needle was not found for the requested occurrence.', 404, array( 'occurrence' => $occurrence ) );
        $offset = $position + strlen( $needle );
    }
    $replacement = 'remove_exact' === $name ? '' : ( 'replace_exact' === $name ? $fragment : ( 'insert_before' === $name ? $fragment . $needle : $needle . $fragment ) );
    return array( 'content' => substr( $content, 0, $position ) . $replacement . substr( $content, $position + strlen( $needle ) ) );
}

function dttmcp_post_lock_error( $post, $body ) {
    if ( ! array_key_exists( 'expected_modified_gmt', $body ) ) return true;
    $expected = trim( (string) $body['expected_modified_gmt'] );
    $actual = dttmcp_modified_gmt( $post );
    if ( '' === $expected ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'expected_modified_gmt cannot be empty.', 422 );
    if ( $expected !== $actual ) return dttmcp_wp_error( 'CONTENT_CONFLICT', 'The post was modified after the caller read it.', 409, array( 'expected_modified_gmt' => $expected, 'actual_modified_gmt' => $actual ) );
    return true;
}

function dttmcp_post_preflight( $body ) {
    $id = dttmcp_id( $body['post_id'] ?? 0 );
    $post = dttmcp_normal_post( $id );
    if ( ! $post ) return dttmcp_wp_error( 'POST_NOT_FOUND', 'Normal post was not found.', 404 );
    if ( ! dttmcp_can( 'edit_posts', $id ) ) return dttmcp_wp_error( 'PERMISSION_DENIED', 'The configured WordPress capability check denied this operation.', 403, array( 'capability' => 'edit_posts' ) );
    $lock = dttmcp_post_lock_error( $post, $body );
    if ( true !== $lock ) return $lock;
    return array( 'id' => $id, 'post' => $post );
}

function dttmcp_post_immutable_snapshot( $post ) {
    return array(
        'title'      => (string) $post->post_title,
        'slug'       => (string) $post->post_name,
        'status'     => (string) $post->post_status,
        'author'     => (int) $post->post_author,
        'categories' => dttmcp_terms( $post->ID, 'category' ),
        'tags'       => dttmcp_terms( $post->ID, 'post_tag' ),
        'seo'        => dttmcp_seo_payload( $post->ID ),
    );
}

function dttmcp_apply_content_patch( $body ) {
    $preflight = dttmcp_post_preflight( $body );
    if ( is_wp_error( $preflight ) ) return $preflight;
    $post = $preflight['post'];
    $before = dttmcp_post_immutable_snapshot( $post );
    $patched = dttmcp_patch_content_string( $post->post_content, $body );
    if ( is_wp_error( $patched ) ) return $patched;
    $updated = wp_update_post( array( 'ID' => $preflight['id'], 'post_content' => $patched['content'] ), true );
    if ( is_wp_error( $updated ) ) return $updated;
    $fresh = dttmcp_normal_post( $preflight['id'] );
    if ( ! $fresh || (string) $fresh->post_content !== (string) $patched['content'] || dttmcp_post_immutable_snapshot( $fresh ) !== $before ) return dttmcp_wp_error( 'PATCH_VERIFICATION_FAILED', 'Content patch read-back or immutable-field verification failed.', 502 );
    return array(
        'id'           => (int) $fresh->ID,
        'operation'    => (string) $body['operation'],
        'status'       => (string) $fresh->post_status,
        'slug'         => (string) $fresh->post_name,
        'link'         => function_exists( 'get_permalink' ) ? get_permalink( $fresh->ID ) : '',
        'modified'     => isset( $fresh->post_modified ) ? (string) $fresh->post_modified : '',
        'modified_gmt' => dttmcp_modified_gmt( $fresh ),
        'verification' => array( 'applied' => true ),
    );
}

function dttmcp_operation_error_data( $error ) {
    return array( 'code' => $error->get_error_code(), 'message' => dttmcp_wp_error_message( $error ), 'details' => dttmcp_wp_error_details( $error ) );
}

function dttmcp_normalize_host( $host ) {
    $host = strtolower( trim( (string) $host ) );
    return 0 === strpos( $host, 'www.' ) ? substr( $host, 4 ) : $host;
}

function dttmcp_site_url_parts() {
    static $parts = null;
    if ( null !== $parts ) return $parts;
    $home = function_exists( 'home_url' ) ? (string) home_url() : '';
    $parsed = parse_url( $home );
    $parts = is_array( $parsed ) ? $parsed : array();
    $parts['scheme'] = strtolower( (string) ( $parts['scheme'] ?? 'https' ) );
    $parts['host'] = dttmcp_normalize_host( $parts['host'] ?? '' );
    $parts['base'] = $parts['scheme'] . '://' . $parts['host'] . ( isset( $parts['port'] ) ? ':' . (int) $parts['port'] : '' );
    return $parts;
}

function dttmcp_link_info( $value ) {
    $raw = html_entity_decode( trim( (string) $value ), ENT_QUOTES | ENT_HTML5, 'UTF-8' );
    if ( '' === $raw ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'Link URL cannot be empty.', 422 );
    if ( strlen( $raw ) > 2048 ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'Link URL exceeds the 2048-byte limit.', 422 );
    $site = dttmcp_site_url_parts();
    if ( preg_match( '/^[A-Za-z][A-Za-z0-9+.-]*:/', $raw ) && ! preg_match( '/^[A-Za-z][A-Za-z0-9+.-]*:\/\//', $raw ) ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'Only normal http and https URLs are allowed.', 422 );
    if ( 0 === strpos( $raw, '//' ) ) $raw = $site['scheme'] . ':' . $raw;
    elseif ( ! preg_match( '/^[A-Za-z][A-Za-z0-9+.-]*:\/\//', $raw ) ) $raw = '/' === substr( $raw, 0, 1 ) ? $site['base'] . $raw : $site['base'] . '/' . $raw;
    $parsed = parse_url( $raw );
    $scheme = strtolower( (string) ( $parsed['scheme'] ?? '' ) );
    if ( ! in_array( $scheme, array( 'http', 'https' ), true ) ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'Only normal http and https URLs are allowed.', 422 );
    $host = dttmcp_normalize_host( $parsed['host'] ?? '' );
    if ( '' === $host || isset( $parsed['user'] ) || isset( $parsed['pass'] ) ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'The link URL is malformed or contains credentials.', 422 );
    $path = (string) ( $parsed['path'] ?? '/' );
    if ( '' === $path || '/' !== substr( $path, 0, 1 ) ) $path = '/' . $path;
    $path_key = strtolower( rtrim( rawurldecode( $path ), '/' ) );
    if ( '' === $path_key ) $path_key = '/';
    $internal = $host === ( $site['host'] ?? '' );
    $canonical = $internal ? $site['base'] . ( '/' === $path ? '/' : rtrim( $path, '/' ) . '/' ) : $scheme . '://' . $host . ( isset( $parsed['port'] ) ? ':' . (int) $parsed['port'] : '' ) . $path;
    if ( ! $internal && isset( $parsed['query'] ) && '' !== (string) $parsed['query'] ) $canonical .= '?' . $parsed['query'];
    return array( 'url' => $canonical, 'key' => $internal ? 'internal:' . $path_key : strtolower( $scheme . '://' . $host . $path . ( isset( $parsed['query'] ) ? '?' . $parsed['query'] : '' ) ), 'internal' => $internal, 'path' => $path );
}

function dttmcp_escape_html_text( $value ) {
    if ( function_exists( 'esc_html' ) ) return esc_html( (string) $value );
    return htmlspecialchars( (string) $value, ENT_QUOTES | ENT_HTML5, 'UTF-8' );
}

function dttmcp_escape_html_attr( $value ) {
    if ( function_exists( 'esc_attr' ) ) return esc_attr( (string) $value );
    return htmlspecialchars( (string) $value, ENT_QUOTES | ENT_HTML5, 'UTF-8' );
}

function dttmcp_extract_anchor_links( $html ) {
    $links = array();
    $active = null;
    foreach ( dttmcp_html_tokens( $html ) as $token ) {
        $info = dttmcp_html_tag_info( $token['text'] );
        if ( ! $info ) continue;
        if ( ! $info['closing'] && 'a' === $info['name'] ) {
            $href = dttmcp_html_attribute( $info['attributes'], 'href' );
            if ( null !== $href && '' !== trim( $href ) ) $active = array( 'href' => $href, 'content_start' => (int) $token['offset'] + (int) $token['length'] );
        } elseif ( $info['closing'] && 'a' === $info['name'] && is_array( $active ) ) {
            $inner = substr( (string) $html, $active['content_start'], (int) $token['offset'] - $active['content_start'] );
            $links[] = array( 'href' => (string) $active['href'], 'anchor' => dttmcp_sanitize_text( function_exists( 'wp_strip_all_tags' ) ? wp_strip_all_tags( $inner ) : strip_tags( $inner ) ) );
            $active = null;
        }
    }
    return $links;
}

function dttmcp_validate_related_links( $links ) {
    if ( ! is_array( $links ) || empty( $links ) ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'links must contain at least one link object.', 422 );
    if ( count( $links ) > 50 ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'links cannot contain more than 50 entries.', 422 );
    $result = array();
    $seen = array();
    foreach ( $links as $index => $link ) {
        if ( ! is_array( $link ) ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'Each related link must be an object.', 422, array( 'index' => $index ) );
        $info = dttmcp_link_info( $link['url'] ?? '' );
        if ( is_wp_error( $info ) ) return dttmcp_wp_error( 'INVALID_ARGUMENT', dttmcp_wp_error_message( $info ), 422, array( 'index' => $index ) );
        $anchor = dttmcp_sanitize_text( $link['anchor'] ?? '' );
        if ( '' === $anchor ) return dttmcp_wp_error( 'INVALID_ARGUMENT', 'Each related link requires a non-empty anchor.', 422, array( 'index' => $index ) );
        if ( isset( $seen[ $info['key'] ] ) ) continue;
        $seen[ $info['key'] ] = true;
        $result[] = array( 'url' => $info['url'], 'key' => $info['key'], 'anchor' => $anchor, 'description' => array_key_exists( 'description', $link ) ? dttmcp_sanitize_text( $link['description'] ) : '' );
    }
    return $result;
}

function dttmcp_related_links_html( $section_id, $heading, $links ) {
    $html = '<div class="wp-block-group dtt-related-links" id="' . dttmcp_escape_html_attr( $section_id ) . '"><h2>' . dttmcp_escape_html_text( $heading ) . '</h2><ul>';
    foreach ( $links as $link ) {
        $html .= '<li><a href="' . dttmcp_escape_html_attr( $link['url'] ) . '">' . dttmcp_escape_html_text( $link['anchor'] ) . '</a>';
        if ( '' !== $link['description'] ) $html .= ' <span class="description">' . dttmcp_escape_html_text( $link['description'] ) . '</span>';
        $html .= '</li>';
    }
    return $html . '</ul></div>';
}

function dttmcp_link_scan_posts( $status = 'any' ) {
    static $cache = array();
    $status = (string) $status;
    if ( isset( $cache[ $status ] ) ) return $cache[ $status ];
    $result = dttmcp_query_posts( array( 'post_type' => 'post', 'post_status' => $status, 'posts_per_page' => 5000, 'orderby' => 'ID', 'order' => 'ASC' ) );
    $posts = array();
    foreach ( $result['posts'] as $post ) if ( 'any' === $status || (string) $post->post_status === $status ) $posts[] = $post;
    $cache[ $status ] = $posts;
    return $posts;
}

function dttmcp_resolve_internal_link( $info ) {
    static $cache = array();
    if ( ! is_array( $info ) || empty( $info['internal'] ) ) return array( 'post' => null, 'reason' => null );
    if ( isset( $cache[ $info['key'] ] ) ) return $cache[ $info['key'] ];
    $id = function_exists( 'url_to_postid' ) ? dttmcp_id( url_to_postid( $info['url'] ) ) : 0;
    if ( ! $id ) {
        $slug = trim( basename( trim( (string) $info['path'], '/' ) ) );
        if ( '' !== $slug ) {
            $matches = dttmcp_posts( array( 'post_type' => 'post', 'post_status' => 'any', 'name' => dttmcp_sanitize_slug( $slug ), 'posts_per_page' => 20 ) );
            if ( ! empty( $matches ) ) $id = (int) $matches[0]->ID;
        }
    }
    $post = $id ? dttmcp_normal_post( $id ) : null;
    if ( ! $post ) return $cache[ $info['key'] ] = array( 'post' => null, 'reason' => 'TARGET_NOT_FOUND' );
    if ( 'trash' === (string) $post->post_status ) return $cache[ $info['key'] ] = array( 'post' => $post, 'reason' => 'TARGET_TRASHED' );
    if ( 'publish' !== (string) $post->post_status ) return $cache[ $info['key'] ] = array( 'post' => $post, 'reason' => 'TARGET_DRAFT' );
    return $cache[ $info['key'] ] = array( 'post' => $post, 'reason' => null );
}

function dttmcp_find_linking_posts_data( $target_id, $target_info, $status, $category_id, $exclude_id = 0 ) {
    $items = array();
    foreach ( dttmcp_link_scan_posts( $status ) as $post ) {
        if ( (int) $post->ID === (int) $exclude_id ) continue;
        if ( $category_id && function_exists( 'has_term' ) && ! has_term( $category_id, 'category', $post ) ) continue;
        $matches = array();
        foreach ( dttmcp_extract_anchor_links( $post->post_content ) as $link ) {
            $info = dttmcp_link_info( $link['href'] );
            if ( is_wp_error( $info ) ) continue;
            $matched = false;
            if ( $target_id ) {
                $resolved = dttmcp_resolve_internal_link( $info );
                $matched = $resolved['post'] && (int) $resolved['post']->ID === (int) $target_id;
            } elseif ( is_array( $target_info ) ) {
                $matched = $info['key'] === $target_info['key'];
            }
            if ( $matched ) $matches[] = array( 'href' => (string) $link['href'], 'anchor' => (string) $link['anchor'] );
        }
        if ( $matches ) $items[] = array( 'id' => (int) $post->ID, 'title' => (string) $post->post_title, 'slug' => (string) $post->post_name, 'status' => (string) $post->post_status, 'link' => function_exists( 'get_permalink' ) ? get_permalink( $post->ID ) : '', 'matching_links' => $matches );
    }
    return $items;
}

function dttmcp_audit_post_links_data( $post, $include_incoming_sources = false, $max_incoming_sources = 20 ) {
    $internal = array();
    $external = array();
    $broken = array();
    $self = array();
    $duplicates = array();
    $seen = array();
    foreach ( dttmcp_extract_anchor_links( $post->post_content ) as $link ) {
        $info = dttmcp_link_info( $link['href'] );
        if ( is_wp_error( $info ) || empty( $info['internal'] ) ) {
            if ( ! is_wp_error( $info ) ) $external[] = array( 'url' => (string) $link['href'], 'anchor' => (string) $link['anchor'] );
            continue;
        }
        $resolved = dttmcp_resolve_internal_link( $info );
        $item = array( 'url' => (string) $link['href'], 'anchor' => (string) $link['anchor'], 'target_post_id' => $resolved['post'] ? (int) $resolved['post']->ID : null, 'target_status' => $resolved['post'] ? (string) $resolved['post']->post_status : null );
        if ( $resolved['reason'] ) $item['reason'] = $resolved['reason'];
        $internal[] = $item;
        $duplicate_key = $resolved['post'] ? 'post:' . (int) $resolved['post']->ID : $info['key'];
        if ( isset( $seen[ $duplicate_key ] ) ) {
            $duplicates[] = array_merge( $item, array( 'occurrences' => $seen[ $duplicate_key ] + 1, 'reason' => 'DUPLICATE_LINK' ) );
            $seen[ $duplicate_key ]++;
        } else {
            $seen[ $duplicate_key ] = 1;
        }
        if ( $resolved['reason'] ) $broken[] = array_merge( $item, array( 'reason' => $resolved['reason'] ) );
        if ( $resolved['post'] && (int) $resolved['post']->ID === (int) $post->ID ) $self[] = array_merge( $item, array( 'reason' => 'SELF_LINK' ) );
    }
    $target_info = null;
    if ( function_exists( 'get_permalink' ) ) {
        $candidate = dttmcp_link_info( get_permalink( $post->ID ) );
        if ( ! is_wp_error( $candidate ) ) $target_info = $candidate;
    }
    $incoming_all = dttmcp_find_linking_posts_data( (int) $post->ID, $target_info, 'any', 0, (int) $post->ID );
    $incoming = array( 'incoming_internal_link_count' => count( $incoming_all ) );
    if ( $include_incoming_sources ) $incoming['incoming_sources'] = array_slice( $incoming_all, 0, max( 1, min( 100, (int) $max_incoming_sources ) ) );
    return array_merge( array(
        'post_id'                    => (int) $post->ID,
        'title'                      => (string) $post->post_title,
        'slug'                       => (string) $post->post_name,
        'link'                       => function_exists( 'get_permalink' ) ? get_permalink( $post->ID ) : '',
        'outbound_internal_links'    => $internal,
        'outbound_external_links'    => $external,
        'duplicate_internal_links'   => $duplicates,
        'self_links'                 => $self,
        'broken_internal_links'      => $broken,
    ), $incoming );
}

function dttmcp_update_seo_data( $body, $require_rank_math = false ) {
    $preflight = dttmcp_post_preflight( $body );
    if ( is_wp_error( $preflight ) ) return $preflight;
    $provider = dttmcp_seo_provider();
    if ( $require_rank_math && 'rank_math' !== $provider ) return dttmcp_wp_error( 'SEO_PROVIDER_UNAVAILABLE', 'Rank Math is not active on this WordPress site.', 422, array( 'provider' => $provider ) );
    $keys = dttmcp_seo_keys();
    if ( empty( $keys ) ) return dttmcp_wp_error( 'SEO_PROVIDER_UNAVAILABLE', 'No supported SEO plugin is active.', 422, array( 'provider' => $provider ) );
    foreach ( $keys as $field => $key ) {
        if ( ! array_key_exists( $field, $body ) ) continue;
        $value = 'canonical_url' === $field && function_exists( 'esc_url_raw' ) ? esc_url_raw( (string) $body[ $field ] ) : dttmcp_sanitize_text( $body[ $field ] );
        if ( 'canonical_url' === $field && '' === $value && '' !== (string) $body[ $field ] ) return dttmcp_wp_error( 'VALIDATION_ERROR', 'canonical_url must be a valid URL.', 422 );
        update_post_meta( $preflight['id'], $key, $value );
    }
    if ( array_key_exists( 'robots', $body ) ) {
        $robots = dttmcp_set_robots( $preflight['id'], (string) $body['robots'] );
        if ( is_wp_error( $robots ) ) return $robots;
    }
    $seo = dttmcp_seo_payload( $preflight['id'] );
    foreach ( array_keys( $keys ) as $field ) if ( array_key_exists( $field, $body ) && (string) ( $seo[ $field ] ?? '' ) !== (string) $body[ $field ] ) return dttmcp_wp_error( 'SEO_VERIFICATION_FAILED', 'SEO metadata read-back verification failed.', 502, array( 'field' => $field ) );
    if ( array_key_exists( 'robots', $body ) && (string) ( $seo['robots'] ?? '' ) !== (string) $body['robots'] ) return dttmcp_wp_error( 'SEO_VERIFICATION_FAILED', 'SEO robots read-back verification failed.', 502 );
    $fresh = dttmcp_normal_post( $preflight['id'] );
    return array_merge( $seo, array( 'post_id' => $preflight['id'], 'modified' => $fresh && isset( $fresh->post_modified ) ? (string) $fresh->post_modified : '', 'modified_gmt' => $fresh ? dttmcp_modified_gmt( $fresh ) : '' ) );
}

function dttmcp_update_terms_data( $body ) {
    $preflight = dttmcp_post_preflight( $body );
    if ( is_wp_error( $preflight ) ) return $preflight;
    $warnings = array();
    $result = dttmcp_set_post_terms_internal( $preflight['id'], $body, $warnings );
    if ( is_wp_error( $result ) ) return $result;
    $fresh = dttmcp_normal_post( $preflight['id'] );
    if ( ! $fresh ) return dttmcp_wp_error( 'POST_NOT_FOUND', 'Normal post disappeared during taxonomy read-back.', 502 );
    return array( 'post_id' => $preflight['id'], 'post' => dttmcp_post_v4_payload( $fresh ), 'warnings' => $warnings );
}
function dttmcp_endpoint_create_post( $request ) {
    $body = dttmcp_body( $request ); if ( array_key_exists( 'status', $body ) && 'draft' !== (string) $body['status'] ) return dttmcp_error_response( $request, 'CREATE_STATUS_FORBIDDEN', 'Normal post creation is draft-only.', 422 );
    $permission = dttmcp_require_capability( $request, 'edit_posts' ); if ( $permission !== true ) return $permission; if ( '' === dttmcp_sanitize_text( $body['title'] ?? '' ) ) return dttmcp_error_response( $request, 'VALIDATION_ERROR', 'title is required.', 422 );
    $term_validation = dttmcp_validate_post_terms( $body ); if ( is_wp_error( $term_validation ) ) return $term_validation;
    $duplicate = dttmcp_post_duplicate( $body ); if ( $duplicate ) return dttmcp_error_response( $request, 'DUPLICATE_POST', 'A post with the same slug or normalized title already exists.', 409, dttmcp_post_duplicate_details( $duplicate ) );
    $id = wp_insert_post( array_merge( dttmcp_post_fields( $body ), array( 'post_status' => 'draft' ) ), true ); if ( is_wp_error( $id ) ) return $id; $id = dttmcp_id( $id ); $warnings = array(); $terms = dttmcp_set_post_terms_internal( $id, $body, $warnings ); if ( is_wp_error( $terms ) ) { wp_delete_post( $id, true ); return dttmcp_wp_error( $terms->get_error_code(), dttmcp_wp_error_message( $terms ), dttmcp_wp_error_status( $terms, 422 ), array_merge( dttmcp_wp_error_details( $terms ), array( 'rolled_back' => true, 'created_id' => $id ) ) ); } $post = dttmcp_normal_post( $id ); dttmcp_audit( $request, 'create_post', array( $id ), true, 'CREATED' ); return dttmcp_response( $request, true, dttmcp_post_v4_payload( $post ), $warnings, null, 201 );
}
function dttmcp_endpoint_get_post( $request ) { $id = dttmcp_id( dttmcp_body( $request )['post_id'] ?? 0 ); $post = dttmcp_normal_post( $id ); if ( ! $post ) return dttmcp_error_response( $request, 'POST_NOT_FOUND', 'Normal post was not found.', 404 ); $permission = dttmcp_require_capability( $request, 'read', $id ); return true === $permission ? dttmcp_response( $request, true, dttmcp_post_v4_payload( $post ) ) : $permission; }
function dttmcp_endpoint_update_post( $request ) {
    $body = dttmcp_body( $request );
    $id = dttmcp_id( $body['post_id'] ?? 0 );
    $post = dttmcp_normal_post( $id );
    if ( ! $post ) return dttmcp_error_response( $request, 'POST_NOT_FOUND', 'Normal post was not found.', 404 );
    if ( array_key_exists( 'status', $body ) ) return dttmcp_error_response( $request, 'STATUS_UPDATE_SEPARATE', 'Use publish_post or unpublish_post for status changes.', 422 );
    $permission = dttmcp_require_capability( $request, 'edit_posts', $id ); if ( $permission !== true ) return $permission;
    $lock = dttmcp_post_lock_error( $post, $body ); if ( true !== $lock ) return dttmcp_error_response( $request, $lock->get_error_code(), dttmcp_wp_error_message( $lock ), dttmcp_wp_error_status( $lock ), dttmcp_wp_error_details( $lock ) );
    $duplicate = dttmcp_post_duplicate( $body, $id ); if ( $duplicate ) return dttmcp_error_response( $request, 'DUPLICATE_SLUG', 'Another post has the same slug or normalized title.', 409, dttmcp_post_duplicate_details( $duplicate ) );
    $updated = wp_update_post( dttmcp_post_fields( $body, $id ), true ); if ( is_wp_error( $updated ) ) return $updated;
    $fresh = dttmcp_normal_post( $id ); if ( ! $fresh ) return dttmcp_error_response( $request, 'UPDATE_VERIFICATION_FAILED', 'Post update read-back failed.', 502 );
    dttmcp_audit( $request, 'update_post', array( $id ), true, 'UPDATED' );
    return dttmcp_response( $request, true, dttmcp_post_v4_payload( $fresh ) );
}
function dttmcp_endpoint_list_posts( $request ) {
    $permission = dttmcp_require_capability( $request, 'read' ); if ( $permission !== true ) return $permission;
    $body = dttmcp_body( $request );
    $status = in_array( (string) ( $body['status'] ?? 'draft' ), array( 'draft', 'publish', 'pending', 'private', 'any' ), true ) ? (string) ( $body['status'] ?? 'draft' ) : 'draft';
    $per = min( 100, max( 1, dttmcp_id( $body['per_page'] ?? 20 ) ) ); $page = max( 1, dttmcp_id( $body['page'] ?? 1 ) );
    $query = dttmcp_query_posts( array( 'post_type' => 'post', 'post_status' => $status, 'posts_per_page' => $per, 'paged' => $page, 'orderby' => 'ID', 'order' => 'DESC' ) );
    $posts = $query['posts'];
    return dttmcp_response( $request, true, array( 'items' => array_map( 'dttmcp_post_list_item', $posts ), 'count' => count( $posts ), 'page' => $page, 'per_page' => $per, 'status' => $status, 'pagination' => dttmcp_pagination( $page, $per, $query['total'], count( $posts ) ) ) );
}
function dttmcp_endpoint_search_posts( $request ) {
    $permission = dttmcp_require_capability( $request, 'read' ); if ( $permission !== true ) return $permission;
    $body = dttmcp_body( $request );
    if ( array_key_exists( 'post_type', $body ) && 'post' !== (string) $body['post_type'] ) return dttmcp_error_response( $request, 'POST_TYPE_NOT_ALLOWED', 'Only the normal post type is supported by this tool.', 422 );
    $query = dttmcp_sanitize_text( $body['query'] ?? '' ); $title = dttmcp_sanitize_text( $body['title'] ?? '' ); $slug = dttmcp_sanitize_slug( $body['slug'] ?? '' );
    if ( '' === $query && '' === $title && '' === $slug ) return dttmcp_error_response( $request, 'VALIDATION_ERROR', 'Provide at least one of query, title, or slug.', 422 );
    $status = in_array( (string) ( $body['status'] ?? 'any' ), array( 'draft', 'publish', 'pending', 'private', 'any' ), true ) ? (string) ( $body['status'] ?? 'any' ) : 'any';
    $per = min( 100, max( 1, dttmcp_id( $body['per_page'] ?? 20 ) ) ); $page = max( 1, dttmcp_id( $body['page'] ?? 1 ) );
    $args = array( 'post_type' => 'post', 'post_status' => $status, 'posts_per_page' => ( '' !== $title ? 5000 : $per ), 'paged' => '' !== $title ? 1 : $page );
    $exclude_id = dttmcp_id( $body['exclude_post_id'] ?? 0 ); if ( $exclude_id ) $args['post__not_in'] = array( $exclude_id );
    if ( '' !== $slug ) $args['name'] = $slug;
    if ( '' !== $query ) $args['s'] = $query;
    if ( '' !== $title && '' === $query ) $args['s'] = $title;
    $query = dttmcp_query_posts( $args ); $posts = $query['posts'];
    $normalized_title = dttmcp_normalize_title( $title );
    if ( '' !== $normalized_title ) $posts = array_values( array_filter( $posts, function ( $post ) use ( $normalized_title ) { return false !== strpos( dttmcp_normalize_title( $post->post_title ), $normalized_title ); } ) );
    $total = '' !== $title ? count( $posts ) : $query['total'];
    if ( '' !== $title ) $posts = array_slice( $posts, ( $page - 1 ) * $per, $per );
    $items = array_map( function ( $post ) { $item = dttmcp_post_list_item( $post ); $item['excerpt'] = (string) $post->post_excerpt; return $item; }, $posts );
    return dttmcp_response( $request, true, array( 'items' => $items, 'count' => count( $items ), 'page' => $page, 'per_page' => $per, 'pagination' => dttmcp_pagination( $page, $per, $total, count( $items ) ) ) );
}
function dttmcp_validate_post_terms( $body ) { foreach ( array( 'categories' => 'category', 'tags' => 'post_tag' ) as $field => $taxonomy ) { if ( ! array_key_exists( $field, $body ) ) continue; if ( ! is_array( $body[ $field ] ) ) return dttmcp_wp_error( 'VALIDATION_ERROR', $field . ' must be an array of positive term IDs.', 422 ); foreach ( $body[ $field ] as $value ) { $term_id = dttmcp_id( $value ); if ( ! $term_id || ! function_exists( 'term_exists' ) || ! term_exists( $term_id, $taxonomy ) ) return dttmcp_wp_error( 'TERM_NOT_FOUND', 'A supplied ' . $taxonomy . ' term does not exist.', 422, array( 'taxonomy' => $taxonomy, 'term_id' => $term_id ) ); } } return true; }
function dttmcp_set_post_terms_internal( $id, $body, &$warnings ) { $validated = dttmcp_validate_post_terms( $body ); if ( is_wp_error( $validated ) ) return $validated; foreach ( array( 'categories' => 'category', 'tags' => 'post_tag' ) as $field => $tax ) if ( array_key_exists( $field, $body ) ) { if ( ! function_exists( 'wp_set_post_terms' ) ) continue; $terms = array_map( 'dttmcp_id', $body[ $field ] ); $result = wp_set_post_terms( $id, $terms, $tax, false ); if ( is_wp_error( $result ) ) return dttmcp_wp_error( 'TERM_NOT_FOUND', dttmcp_wp_error_message( $result ), 422 ); } return true; }
function dttmcp_endpoint_set_post_terms( $request ) {
    $body = dttmcp_body( $request );
    $result = dttmcp_update_terms_data( $body );
    if ( is_wp_error( $result ) ) return dttmcp_error_response( $request, $result->get_error_code(), dttmcp_wp_error_message( $result ), dttmcp_wp_error_status( $result ), dttmcp_wp_error_details( $result ) );
    return dttmcp_response( $request, true, $result['post'], $result['warnings'] );
}

function dttmcp_endpoint_patch_post_content( $request ) {
    $body = dttmcp_body( $request );
    $result = dttmcp_apply_content_patch( $body );
    if ( is_wp_error( $result ) ) return dttmcp_error_response( $request, $result->get_error_code(), dttmcp_wp_error_message( $result ), dttmcp_wp_error_status( $result ), dttmcp_wp_error_details( $result ) );
    dttmcp_audit( $request, 'patch_post_content', array( $result['id'] ), true, 'PATCHED' );
    return dttmcp_response( $request, true, $result );
}

function dttmcp_endpoint_bulk_patch_post_content( $request ) {
    $body = dttmcp_body( $request ); $operations = $body['operations'] ?? array();
    if ( ! is_array( $operations ) || empty( $operations ) || count( $operations ) > 20 ) return dttmcp_error_response( $request, 'INVALID_ARGUMENT', 'operations must contain between 1 and 20 patch objects.', 422 );
    $results = array(); $success = 0; $failure = 0;
    foreach ( $operations as $index => $operation ) {
        if ( ! is_array( $operation ) ) { $failure++; $results[] = array( 'index' => $index, 'post_id' => 0, 'ok' => false, 'error' => array( 'code' => 'INVALID_ARGUMENT', 'message' => 'Each operation must be an object.' ) ); continue; }
        $result = dttmcp_apply_content_patch( $operation );
        if ( is_wp_error( $result ) ) { $failure++; $results[] = array_merge( array( 'index' => $index, 'post_id' => dttmcp_id( $operation['post_id'] ?? 0 ), 'ok' => false, 'error' => dttmcp_operation_error_data( $result ) ) ); continue; }
        $success++; dttmcp_audit( $request, 'bulk_patch_post_content', array( $result['id'] ), true, 'PATCHED', array( 'index' => $index ) ); $results[] = array_merge( array( 'index' => $index, 'post_id' => $result['id'], 'ok' => true ), $result );
    }
    return dttmcp_response( $request, true, array( 'results' => $results, 'success_count' => $success, 'failure_count' => $failure ) );
}

function dttmcp_endpoint_upsert_post_related_links( $request ) {
    $body = dttmcp_body( $request );
    $section_id = trim( (string) ( $body['section_id'] ?? '' ) );
    if ( '' === $section_id || ! preg_match( '/^[A-Za-z0-9][A-Za-z0-9:_-]{0,120}$/', $section_id ) ) return dttmcp_error_response( $request, 'INVALID_ARGUMENT', 'section_id must be a safe HTML id.', 422 );
    $heading = dttmcp_sanitize_text( $body['heading'] ?? '' ); if ( '' === $heading ) return dttmcp_error_response( $request, 'INVALID_ARGUMENT', 'heading is required.', 422 );
    $links = dttmcp_validate_related_links( $body['links'] ?? array() ); if ( is_wp_error( $links ) ) return dttmcp_error_response( $request, $links->get_error_code(), dttmcp_wp_error_message( $links ), dttmcp_wp_error_status( $links ), dttmcp_wp_error_details( $links ) );
    $preflight = dttmcp_post_preflight( $body ); if ( is_wp_error( $preflight ) ) return dttmcp_error_response( $request, $preflight->get_error_code(), dttmcp_wp_error_message( $preflight ), dttmcp_wp_error_status( $preflight ), dttmcp_wp_error_details( $preflight ) );
    $range = dttmcp_html_element_range( $preflight['post']->post_content, $section_id );
    $created = false; $existing_links = array();
    if ( false !== $range ) {
        $section_html = substr( $preflight['post']->post_content, $range[0], $range[1] - $range[0] );
        foreach ( dttmcp_extract_anchor_links( $section_html ) as $existing ) {
            $info = dttmcp_link_info( $existing['href'] ); if ( is_wp_error( $info ) ) continue;
            $existing_links[] = array( 'url' => $info['url'], 'key' => $info['key'], 'anchor' => $existing['anchor'], 'description' => '' );
        }
    } else {
        $created = true;
    }
    $merged = array(); $seen = array();
    foreach ( array_merge( $existing_links, $links ) as $link ) { if ( isset( $seen[ $link['key'] ] ) ) { $merged[ $seen[ $link['key'] ] ] = $link; continue; } $seen[ $link['key'] ] = count( $merged ); $merged[] = $link; }
    $html = dttmcp_related_links_html( $section_id, $heading, $merged );
    $placement = (string) ( $body['placement'] ?? 'append' );
    if ( ! in_array( $placement, array( 'append', 'prepend', 'before', 'after' ), true ) ) return dttmcp_error_response( $request, 'INVALID_ARGUMENT', 'placement is invalid.', 422 );
    if ( in_array( $placement, array( 'before', 'after' ), true ) && '' === (string) ( $body['needle'] ?? '' ) ) return dttmcp_error_response( $request, 'INVALID_ARGUMENT', 'needle is required for before/after placement.', 422 );
    $operation = array( 'post_id' => $preflight['id'], 'operation' => false !== $range ? 'replace_section_id' : ( 'before' === $placement ? 'insert_before' : ( 'after' === $placement ? 'insert_after' : $placement ) ), 'html' => $html, 'section_id' => $section_id );
    if ( in_array( $placement, array( 'before', 'after' ), true ) ) $operation['needle'] = (string) $body['needle'];
    if ( array_key_exists( 'expected_modified_gmt', $body ) ) $operation['expected_modified_gmt'] = $body['expected_modified_gmt'];
    $result = dttmcp_apply_content_patch( $operation );
    if ( is_wp_error( $result ) ) return dttmcp_error_response( $request, $result->get_error_code(), dttmcp_wp_error_message( $result ), dttmcp_wp_error_status( $result ), dttmcp_wp_error_details( $result ) );
    $result['action'] = $created ? 'created' : 'updated'; $result['link_count'] = count( $merged ); $result['verification'] = array( 'applied' => true, 'section_id' => $section_id, 'link_count' => count( $merged ) );
    dttmcp_audit( $request, 'upsert_post_related_links', array( $result['id'] ), true, strtoupper( $result['action'] ) );
    return dttmcp_response( $request, true, $result );
}

function dttmcp_endpoint_bulk_set_rank_math_meta( $request ) {
    $operations = dttmcp_body( $request )['operations'] ?? array();
    if ( ! is_array( $operations ) || empty( $operations ) || count( $operations ) > 50 ) return dttmcp_error_response( $request, 'INVALID_ARGUMENT', 'operations must contain between 1 and 50 Rank Math objects.', 422 );
    $results = array(); $success = 0; $failure = 0;
    foreach ( $operations as $index => $operation ) {
        if ( ! is_array( $operation ) ) { $failure++; $results[] = array( 'index' => $index, 'post_id' => 0, 'ok' => false, 'error' => array( 'code' => 'INVALID_ARGUMENT', 'message' => 'Each operation must be an object.' ) ); continue; }
        $result = dttmcp_update_seo_data( $operation, true );
        if ( is_wp_error( $result ) ) { $failure++; $results[] = array( 'index' => $index, 'post_id' => dttmcp_id( $operation['post_id'] ?? 0 ), 'ok' => false, 'error' => dttmcp_operation_error_data( $result ) ); continue; }
        $success++; dttmcp_audit( $request, 'bulk_set_rank_math_meta', array( $result['post_id'] ), true, 'UPDATED', array( 'index' => $index ) ); $results[] = array_merge( array( 'index' => $index, 'post_id' => $result['post_id'], 'ok' => true ), $result );
    }
    return dttmcp_response( $request, true, array( 'results' => $results, 'success_count' => $success, 'failure_count' => $failure ) );
}

function dttmcp_endpoint_bulk_set_post_terms( $request ) {
    $operations = dttmcp_body( $request )['operations'] ?? array();
    if ( ! is_array( $operations ) || empty( $operations ) || count( $operations ) > 50 ) return dttmcp_error_response( $request, 'INVALID_ARGUMENT', 'operations must contain between 1 and 50 taxonomy objects.', 422 );
    $results = array(); $success = 0; $failure = 0;
    foreach ( $operations as $index => $operation ) {
        if ( ! is_array( $operation ) ) { $failure++; $results[] = array( 'index' => $index, 'post_id' => 0, 'ok' => false, 'error' => array( 'code' => 'INVALID_ARGUMENT', 'message' => 'Each operation must be an object.' ) ); continue; }
        $result = dttmcp_update_terms_data( $operation );
        if ( is_wp_error( $result ) ) { $failure++; $results[] = array( 'index' => $index, 'post_id' => dttmcp_id( $operation['post_id'] ?? 0 ), 'ok' => false, 'error' => dttmcp_operation_error_data( $result ) ); continue; }
        $success++; dttmcp_audit( $request, 'bulk_set_post_terms', array( $result['post_id'] ), true, 'UPDATED', array( 'index' => $index ) ); $results[] = array( 'index' => $index, 'post_id' => $result['post_id'], 'ok' => true, 'post' => $result['post'], 'warnings' => $result['warnings'] );
    }
    return dttmcp_response( $request, true, array( 'results' => $results, 'success_count' => $success, 'failure_count' => $failure ) );
}

function dttmcp_endpoint_find_posts_linking_to( $request ) {
    $permission = dttmcp_require_capability( $request, 'read' ); if ( $permission !== true ) return $permission;
    $body = dttmcp_body( $request ); $has_id = array_key_exists( 'target_post_id', $body ); $has_url = array_key_exists( 'target_url', $body );
    if ( $has_id === $has_url ) return dttmcp_error_response( $request, 'INVALID_ARGUMENT', 'Provide exactly one of target_post_id or target_url.', 422 );
    $target_id = 0; $target_info = null; $target_url = '';
    if ( $has_id ) { $target_id = dttmcp_id( $body['target_post_id'] ); $target = dttmcp_normal_post( $target_id ); if ( ! $target ) return dttmcp_error_response( $request, 'POST_NOT_FOUND', 'Target normal post was not found.', 404 ); $target_url = function_exists( 'get_permalink' ) ? get_permalink( $target_id ) : ''; $target_info = dttmcp_link_info( $target_url ); if ( is_wp_error( $target_info ) ) $target_info = null; }
    else { $target_info = dttmcp_link_info( $body['target_url'] ); if ( is_wp_error( $target_info ) ) return dttmcp_error_response( $request, 'INVALID_ARGUMENT', dttmcp_wp_error_message( $target_info ), 422 ); $target_url = $target_info['url']; }
    $status = in_array( (string) ( $body['status'] ?? 'any' ), array( 'draft', 'publish', 'pending', 'private', 'any' ), true ) ? (string) ( $body['status'] ?? 'any' ) : 'any';
    $per = min( 100, max( 1, dttmcp_id( $body['per_page'] ?? 20 ) ) ); $page = max( 1, dttmcp_id( $body['page'] ?? 1 ) ); $category_id = dttmcp_id( $body['category_id'] ?? 0 );
    $all = dttmcp_find_linking_posts_data( $target_id, $target_info, $status, $category_id, $target_id ); $items = array_slice( $all, ( $page - 1 ) * $per, $per );
    return dttmcp_response( $request, true, array( 'target' => array( 'post_id' => $target_id ?: null, 'url' => $target_url ), 'items' => $items, 'pagination' => dttmcp_pagination( $page, $per, count( $all ), count( $items ) ) ) );
}

function dttmcp_endpoint_audit_post_internal_links( $request ) {
    $body = dttmcp_body( $request ); $post = dttmcp_normal_post( dttmcp_id( $body['post_id'] ?? 0 ) ); if ( ! $post ) return dttmcp_error_response( $request, 'POST_NOT_FOUND', 'Normal post was not found.', 404 );
    $permission = dttmcp_require_capability( $request, 'read', $post->ID ); if ( $permission !== true ) return $permission;
    return dttmcp_response( $request, true, dttmcp_audit_post_links_data( $post, ! empty( $body['include_incoming_sources'] ), dttmcp_id( $body['max_incoming_sources'] ?? 20 ) ) );
}

function dttmcp_endpoint_bulk_audit_post_internal_links( $request ) {
    $body = dttmcp_body( $request ); $ids = $body['post_ids'] ?? array();
    if ( ! is_array( $ids ) || empty( $ids ) || count( $ids ) > 20 ) return dttmcp_error_response( $request, 'INVALID_ARGUMENT', 'post_ids must contain between 1 and 20 IDs.', 422 );
    $items = array(); $summary = array( 'total_posts' => count( $ids ), 'total_internal_links' => 0, 'total_broken_links' => 0, 'total_self_links' => 0, 'total_duplicate_links' => 0, 'orphan_post_count' => 0 );
    foreach ( $ids as $raw_id ) {
        $id = dttmcp_id( $raw_id ); $post = dttmcp_normal_post( $id );
        if ( ! $post ) { $items[] = array( 'post_id' => $id, 'ok' => false, 'error' => array( 'code' => 'POST_NOT_FOUND', 'message' => 'Normal post was not found.' ) ); continue; }
        if ( ! dttmcp_can( 'read', $id ) ) { $items[] = array( 'post_id' => $id, 'ok' => false, 'error' => array( 'code' => 'PERMISSION_DENIED', 'message' => 'The configured WordPress capability check denied this operation.' ) ); continue; }
        $audit = dttmcp_audit_post_links_data( $post, ! empty( $body['include_incoming_sources'] ), dttmcp_id( $body['max_incoming_sources'] ?? 20 ) );
        $summary['total_internal_links'] += count( $audit['outbound_internal_links'] ); $summary['total_broken_links'] += count( $audit['broken_internal_links'] ); $summary['total_self_links'] += count( $audit['self_links'] ); $summary['total_duplicate_links'] += count( $audit['duplicate_internal_links'] );
        if ( 'publish' === (string) $post->post_status && 0 === (int) $audit['incoming_internal_link_count'] ) $summary['orphan_post_count']++;
        $items[] = array_merge( array( 'post_id' => $id, 'ok' => true ), $audit );
    }
    return dttmcp_response( $request, true, array( 'items' => $items, 'summary' => $summary ) );
}
function dttmcp_endpoint_post_status( $request, $status ) { $id = dttmcp_id( dttmcp_body( $request )['post_id'] ?? 0 ); $post = dttmcp_normal_post( $id ); if ( ! $post ) return dttmcp_error_response( $request, 'POST_NOT_FOUND', 'Normal post was not found.', 404 ); $cap = 'publish' === $status ? 'publish_posts' : 'edit_posts'; $permission = dttmcp_require_capability( $request, $cap, $id ); if ( $permission !== true ) return $permission; $updated = wp_update_post( array( 'ID' => $id, 'post_status' => $status ), true ); if ( is_wp_error( $updated ) ) return $updated; $fresh = dttmcp_normal_post( $id ); if ( ! $fresh || $fresh->post_status !== $status ) return dttmcp_error_response( $request, 'STATUS_VERIFY_FAILED', 'Post status read-back verification failed.', 502 ); dttmcp_audit( $request, 'publish' === $status ? 'publish_post' : 'unpublish_post', array( $id ), true, strtoupper( $status ) ); return dttmcp_response( $request, true, array( 'id' => $id, 'status' => $status, 'published_at' => 'publish' === $status ? (string) $fresh->post_date_gmt : null, 'link' => function_exists( 'get_permalink' ) ? get_permalink( $id ) : '', 'post' => dttmcp_post_v4_payload( $fresh ) ) ); }
function dttmcp_endpoint_publish_post( $request ) { return dttmcp_endpoint_post_status( $request, 'publish' ); }
function dttmcp_endpoint_unpublish_post( $request ) { return dttmcp_endpoint_post_status( $request, 'draft' ); }
function dttmcp_endpoint_trash_post( $request ) { $id = dttmcp_id( dttmcp_body( $request )['post_id'] ?? 0 ); $post = dttmcp_normal_post( $id ); if ( ! $post ) return dttmcp_error_response( $request, 'POST_NOT_FOUND', 'Normal post was not found.', 404 ); $permission = dttmcp_require_capability( $request, 'delete_posts', $id ); if ( $permission !== true ) return $permission; if ( 'trash' === (string) $post->post_status ) return dttmcp_response( $request, true, array( 'id' => $id, 'status' => 'trash', 'trashed' => true, 'already_trashed' => true ) ); $deleted = wp_delete_post( $id, false ); if ( ! $deleted ) return dttmcp_error_response( $request, 'TRASH_FAILED', 'Post could not be moved to Trash.', 502 ); dttmcp_audit( $request, 'trash_post', array( $id ), true, 'TRASHED' ); return dttmcp_response( $request, true, array( 'id' => $id, 'status' => 'trash', 'trashed' => true ) ); }
function dttmcp_endpoint_taxonomy( $request, $taxonomy ) {
    $permission = dttmcp_require_capability( $request, 'read' ); if ( $permission !== true ) return $permission;
    $body = dttmcp_body( $request ); $per = min( 100, max( 1, dttmcp_id( $body['per_page'] ?? 100 ) ) ); $page = max( 1, dttmcp_id( $body['page'] ?? 1 ) ); $search = dttmcp_sanitize_text( $body['search'] ?? '' );
    $args = array( 'taxonomy' => $taxonomy, 'hide_empty' => false, 'number' => $per, 'offset' => ( $page - 1 ) * $per, 'search' => $search ); $terms = get_terms( $args ); if ( is_wp_error( $terms ) ) return $terms;
    $total = count( (array) $terms );
    if ( function_exists( 'wp_count_terms' ) ) { $count = wp_count_terms( array( 'taxonomy' => $taxonomy, 'hide_empty' => false, 'search' => $search ) ); if ( ! is_wp_error( $count ) ) $total = (int) $count; }
    $items = array(); foreach ( (array) $terms as $term ) $items[] = array( 'id' => (int) $term->term_id, 'name' => (string) $term->name, 'slug' => (string) $term->slug, 'description' => 'category' === $taxonomy ? (string) $term->description : null, 'parent' => 'category' === $taxonomy ? (int) $term->parent : null, 'count' => (int) $term->count );
    return dttmcp_response( $request, true, array( 'taxonomy' => $taxonomy, 'items' => $items, 'count' => count( $items ), 'page' => $page, 'per_page' => $per, 'pagination' => dttmcp_pagination( $page, $per, $total, count( $items ) ) ) );
}
function dttmcp_endpoint_get_post_terms( $request ) { $body = dttmcp_body( $request ); $id = dttmcp_id( $body['post_id'] ?? 0 ); if ( ! dttmcp_normal_post( $id ) ) return dttmcp_error_response( $request, 'POST_NOT_FOUND', 'Normal post was not found.', 404 ); $permission = dttmcp_require_capability( $request, 'read', $id ); if ( $permission !== true ) return $permission; return dttmcp_response( $request, true, array( 'post_id' => $id, 'categories' => dttmcp_terms( $id, 'category' ), 'tags' => dttmcp_terms( $id, 'post_tag' ) ) ); }
function dttmcp_endpoint_create_term( $request, $taxonomy ) { $body = dttmcp_body( $request ); $name = dttmcp_sanitize_text( $body['name'] ?? '' ); if ( '' === $name ) return dttmcp_error_response( $request, 'VALIDATION_ERROR', 'name is required.', 422 ); $slug = dttmcp_sanitize_slug( $body['slug'] ?? $name ); $existing = get_terms( array( 'taxonomy' => $taxonomy, 'hide_empty' => false, 'slug' => $slug, 'number' => 1 ) ); if ( ! is_wp_error( $existing ) && ! empty( $existing ) ) return dttmcp_error_response( $request, 'DUPLICATE_SLUG', 'A term with this slug already exists.', 409, array( 'existing_id' => (int) $existing[0]->term_id ) ); $permission = dttmcp_require_capability( $request, 'manage_categories' ); if ( $permission !== true ) return $permission; $args = array( 'slug' => $slug ); if ( 'category' === $taxonomy ) { $args['description'] = dttmcp_sanitize_html( $body['description'] ?? '' ); $args['parent'] = dttmcp_id( $body['parent'] ?? 0 ); } $result = wp_insert_term( $name, $taxonomy, $args ); if ( is_wp_error( $result ) ) return $result; return dttmcp_response( $request, true, array( 'id' => (int) $result['term_id'], 'name' => $name, 'slug' => $slug, 'taxonomy' => $taxonomy ), array(), null, 201 ); }
function dttmcp_media_payload( $media ) { $file = function_exists( 'get_attached_file' ) ? get_attached_file( $media->ID ) : ''; $metadata = function_exists( 'wp_get_attachment_metadata' ) ? wp_get_attachment_metadata( $media->ID ) : array(); return array( 'id' => (int) $media->ID, 'filename' => $file ? basename( $file ) : (string) $media->post_name, 'title' => (string) $media->post_title, 'caption' => (string) $media->post_excerpt, 'description' => (string) $media->post_content, 'mime_type' => (string) $media->post_mime_type, 'url' => function_exists( 'wp_get_attachment_url' ) ? wp_get_attachment_url( $media->ID ) : '', 'alt_text' => (string) get_post_meta( $media->ID, '_wp_attachment_image_alt', true ), 'width' => (int) ( is_array( $metadata ) ? ( $metadata['width'] ?? 0 ) : 0 ), 'height' => (int) ( is_array( $metadata ) ? ( $metadata['height'] ?? 0 ) : 0 ), 'modified_gmt' => dttmcp_modified_gmt( $media ) ); }
function dttmcp_endpoint_find_media( $request ) { $permission = dttmcp_require_capability( $request, 'read' ); if ( $permission !== true ) return $permission; $body = dttmcp_body( $request ); $posts = dttmcp_posts( array( 'post_type' => 'attachment', 'post_mime_type' => 'image', 's' => dttmcp_sanitize_text( $body['query'] ?? '' ), 'posts_per_page' => min( 100, max( 1, dttmcp_id( $body['per_page'] ?? 20 ) ) ) ) ); $items = array(); foreach ( $posts as $post ) $items[] = dttmcp_media_payload( $post ); return dttmcp_response( $request, true, array( 'items' => $items, 'count' => count( $items ) ) ); }
function dttmcp_endpoint_get_media( $request ) { $body = dttmcp_body( $request ); $id = dttmcp_id( $body['media_id'] ?? 0 ); $media = function_exists( 'get_post' ) ? get_post( $id ) : null; if ( ! $media || 'attachment' !== $media->post_type || 0 !== strpos( (string) $media->post_mime_type, 'image/' ) ) return dttmcp_error_response( $request, 'MEDIA_NOT_FOUND', 'Image attachment was not found.', 404 ); $permission = dttmcp_require_capability( $request, 'read', $id ); if ( $permission !== true ) return $permission; return dttmcp_response( $request, true, dttmcp_media_payload( $media ) ); }
function dttmcp_endpoint_update_media_metadata( $request ) { $body = dttmcp_body( $request ); $id = dttmcp_id( $body['media_id'] ?? 0 ); $media = get_post( $id ); if ( ! $media || 'attachment' !== $media->post_type || 0 !== strpos( (string) $media->post_mime_type, 'image/' ) ) return dttmcp_error_response( $request, 'MEDIA_NOT_FOUND', 'Image attachment was not found.', 404 ); $permission = dttmcp_require_capability( $request, 'upload_files', $id ); if ( $permission !== true ) return $permission; $data = array( 'ID' => $id ); foreach ( array( 'title' => 'post_title', 'caption' => 'post_excerpt', 'description' => 'post_content' ) as $field => $key ) if ( array_key_exists( $field, $body ) ) $data[ $key ] = dttmcp_sanitize_html( $body[ $field ] ); if ( count( $data ) > 1 ) wp_update_post( $data ); if ( array_key_exists( 'alt_text', $body ) ) update_post_meta( $id, '_wp_attachment_image_alt', dttmcp_sanitize_text( $body['alt_text'] ) ); return dttmcp_response( $request, true, array( 'id' => $id, 'url' => function_exists( 'wp_get_attachment_url' ) ? wp_get_attachment_url( $id ) : '', 'alt_text' => (string) get_post_meta( $id, '_wp_attachment_image_alt', true ) ) ); }
function dttmcp_endpoint_set_featured_image( $request ) { $body = dttmcp_body( $request ); $post_id = dttmcp_id( $body['post_id'] ?? 0 ); $media_id = dttmcp_id( $body['media_id'] ?? 0 ); if ( ! dttmcp_normal_post( $post_id ) ) return dttmcp_error_response( $request, 'POST_NOT_FOUND', 'Normal post was not found.', 404 ); $permission = dttmcp_require_capability( $request, 'edit_posts', $post_id ); if ( $permission !== true ) return $permission; if ( 0 === $media_id ) { delete_post_thumbnail( $post_id ); return dttmcp_response( $request, true, array( 'post_id' => $post_id, 'featured_image' => 0 ) ); } $media = get_post( $media_id ); if ( ! $media || 'attachment' !== $media->post_type || 0 !== strpos( (string) $media->post_mime_type, 'image/' ) ) return dttmcp_error_response( $request, 'MEDIA_NOT_FOUND', 'Image attachment was not found.', 404 ); set_post_thumbnail( $post_id, $media_id ); return dttmcp_response( $request, true, array( 'post_id' => $post_id, 'featured_image' => $media_id, 'image_url' => function_exists( 'wp_get_attachment_url' ) ? wp_get_attachment_url( $media_id ) : '', 'post_link' => function_exists( 'get_permalink' ) ? get_permalink( $post_id ) : '' ) ); }
function dttmcp_endpoint_remove_featured_image( $request ) { $body = dttmcp_body( $request ); $post_id = dttmcp_id( $body['post_id'] ?? 0 ); if ( ! dttmcp_normal_post( $post_id ) ) return dttmcp_error_response( $request, 'POST_NOT_FOUND', 'Normal post was not found.', 404 ); $permission = dttmcp_require_capability( $request, 'edit_posts', $post_id ); if ( $permission !== true ) return $permission; if ( function_exists( 'delete_post_thumbnail' ) ) delete_post_thumbnail( $post_id ); dttmcp_audit( $request, 'remove_featured_image', array( $post_id ), true, 'REMOVED' ); return dttmcp_response( $request, true, array( 'post_id' => $post_id, 'featured_image' => 0, 'removed' => true ) ); }
function dttmcp_media_extension_matches( $filename, $mime ) { $extension = strtolower( (string) pathinfo( (string) $filename, PATHINFO_EXTENSION ) ); $mapping = array( 'image/jpeg' => array( 'jpg', 'jpeg', 'jpe' ), 'image/png' => array( 'png' ), 'image/webp' => array( 'webp' ) ); return isset( $mapping[ $mime ] ) && in_array( $extension, $mapping[ $mime ], true ); }
function dttmcp_endpoint_upload_media( $request ) { $body = dttmcp_body( $request ); $permission = dttmcp_require_capability( $request, 'upload_files' ); if ( $permission !== true ) return $permission; $file = is_array( $body['file'] ?? null ) ? $body['file'] : array(); $name = sanitize_file_name( $file['filename'] ?? '' ); $mime = (string) ( $file['mime_type'] ?? ''); $allowed = array( 'image/jpeg', 'image/png', 'image/webp' ); if ( ! in_array( $mime, $allowed, true ) || ! dttmcp_media_extension_matches( $name, $mime ) ) return dttmcp_error_response( $request, 'INVALID_MIME_TYPE', 'The image filename extension and MIME type must match JPEG, PNG, or WebP.', 422 ); $raw = base64_decode( preg_replace( '/^data:[^;]+;base64,/', '', (string) ( $file['data_base64'] ?? '' ) ), true ); if ( false === $raw || strlen( $raw ) < 16 || strlen( $raw ) > 10 * 1024 * 1024 ) return dttmcp_error_response( $request, 'UPLOAD_FAILED', 'Invalid or oversized image data.', 422 ); $tmp = wp_tempnam( $name ); if ( ! $tmp || false === file_put_contents( $tmp, $raw ) ) return dttmcp_error_response( $request, 'UPLOAD_FAILED', 'Image could not be staged safely.', 422 ); $info = function_exists( 'wp_getimagesize' ) ? wp_getimagesize( $tmp ) : @getimagesize( $tmp ); if ( ! is_array( $info ) || ! isset( $info['mime'] ) || $info['mime'] !== $mime ) { @unlink( $tmp ); return dttmcp_error_response( $request, 'INVALID_MIME_TYPE', 'Image content, declared MIME type, and filename extension do not match.', 422 ); } require_once ABSPATH . 'wp-admin/includes/file.php'; require_once ABSPATH . 'wp-admin/includes/media.php'; require_once ABSPATH . 'wp-admin/includes/image.php'; $upload = wp_handle_sideload( array( 'name' => $name, 'type' => $mime, 'tmp_name' => $tmp, 'error' => 0, 'size' => strlen( $raw ) ), array( 'test_form' => false, 'mimes' => array( 'jpg|jpeg|jpe' => 'image/jpeg', 'png' => 'image/png', 'webp' => 'image/webp' ) ) ); if ( isset( $upload['error'] ) ) { @unlink( $tmp ); return dttmcp_error_response( $request, 'UPLOAD_FAILED', $upload['error'], 422 ); } $attachment = array( 'post_mime_type' => $mime, 'post_title' => dttmcp_sanitize_text( $body['title'] ?? pathinfo( $name, PATHINFO_FILENAME ) ), 'post_content' => dttmcp_sanitize_html( $body['description'] ?? '' ), 'post_excerpt' => dttmcp_sanitize_html( $body['caption'] ?? '' ), 'post_status' => 'inherit' ); $id = wp_insert_attachment( $attachment, $upload['file'] ); if ( is_wp_error( $id ) ) { if ( ! empty( $upload['file'] ) ) @unlink( $upload['file'] ); return $id; } $metadata = wp_generate_attachment_metadata( $id, $upload['file'] ); if ( $metadata ) wp_update_attachment_metadata( $id, $metadata ); if ( array_key_exists( 'alt_text', $body ) ) update_post_meta( $id, '_wp_attachment_image_alt', dttmcp_sanitize_text( $body['alt_text'] ) ); dttmcp_audit( $request, 'upload_media', array( $id ), true, 'UPLOADED' ); return dttmcp_response( $request, true, array( 'id' => (int) $id, 'filename' => $name, 'mime_type' => $mime, 'url' => function_exists( 'wp_get_attachment_url' ) ? wp_get_attachment_url( $id ) : '', 'alt_text' => (string) get_post_meta( $id, '_wp_attachment_image_alt', true ), 'width' => (int) ( $info[0] ?? 0 ), 'height' => (int) ( $info[1] ?? 0 ) ), array(), null, 201 ); }
function dttmcp_endpoint_update_seo_meta( $request ) { $body = dttmcp_body( $request ); $result = dttmcp_update_seo_data( $body, false ); if ( is_wp_error( $result ) ) return dttmcp_error_response( $request, $result->get_error_code(), dttmcp_wp_error_message( $result ), dttmcp_wp_error_status( $result ), dttmcp_wp_error_details( $result ) ); dttmcp_audit( $request, 'update_seo_meta', array( $result['post_id'] ), true, 'UPDATED' ); return dttmcp_response( $request, true, $result ); }

function dttmcp_endpoint_get_rank_math_meta( $request ) { if ( 'rank_math' !== dttmcp_seo_provider() ) return dttmcp_error_response( $request, 'SEO_PROVIDER_UNAVAILABLE', 'Rank Math is not active on this WordPress site.', 422, array( 'provider' => dttmcp_seo_provider() ) ); $body = dttmcp_body( $request ); $id = dttmcp_id( $body['post_id'] ?? 0 ); if ( ! dttmcp_normal_post( $id ) ) return dttmcp_error_response( $request, 'POST_NOT_FOUND', 'Normal post was not found.', 404 ); $permission = dttmcp_require_capability( $request, 'read', $id ); if ( $permission !== true ) return $permission; return dttmcp_response( $request, true, array_merge( array( 'post_id' => $id ), dttmcp_seo_payload( $id ) ) ); }
function dttmcp_endpoint_set_rank_math_meta( $request ) { $body = dttmcp_body( $request ); $result = dttmcp_update_seo_data( $body, true ); if ( is_wp_error( $result ) ) return dttmcp_error_response( $request, $result->get_error_code(), dttmcp_wp_error_message( $result ), dttmcp_wp_error_status( $result ), dttmcp_wp_error_details( $result ) ); dttmcp_audit( $request, 'set_rank_math_meta', array( $result['post_id'] ), true, 'UPDATED' ); return dttmcp_response( $request, true, $result ); }

function dttmcp_endpoint_upsert_truyen( $request ) { $body = dttmcp_body( $request ); $guard = dttmcp_create_status_guard( $body ); if ( is_wp_error( $guard ) ) return $guard; $permission = dttmcp_require_capability( $request, 'edit_posts' ); if ( $permission !== true ) return $permission; $existing = dttmcp_find_story_duplicate( $body ); $warnings = array(); if ( $existing ) { $lock = dttmcp_expected_lock( $request, $existing ); if ( $lock !== true ) return $lock; $updated = dttmcp_update_story_internal( $existing, $body, $warnings ); if ( is_wp_error( $updated ) ) return $updated; dttmcp_audit( $request, 'upsert_truyen', array( $existing->ID ), true, 'UPDATED' ); return dttmcp_response( $request, true, array( 'id' => (int) $existing->ID, 'action' => 'updated', 'truyen' => dttmcp_post_payload( $updated ) ), $warnings ); } $result = dttmcp_create_story_internal( $body, $warnings ); if ( is_wp_error( $result ) ) return $result; dttmcp_audit( $request, 'upsert_truyen', array( $result['id'] ), true, 'CREATED' ); return dttmcp_response( $request, true, array( 'id' => $result['id'], 'action' => 'created', 'truyen' => dttmcp_post_payload( $result['post'] ) ), $warnings, null, 201 ); }
function dttmcp_endpoint_upsert_chuong( $request ) { $body = dttmcp_body( $request ); $parent_id = dttmcp_id( $body['truyen_id'] ?? 0 ); $number = dttmcp_id( $body['chapter_number'] ?? 0 ); $existing = dttmcp_find_chapter_duplicate( $parent_id, $number ); $warnings = array(); $permission = dttmcp_require_capability( $request, 'edit_posts', $parent_id ); if ( $permission !== true ) return $permission; if ( $existing ) { $lock = dttmcp_expected_lock( $request, $existing ); if ( $lock !== true ) return $lock; $updated = dttmcp_update_chapter_internal( $existing, $body, $warnings ); if ( is_wp_error( $updated ) ) return $updated; dttmcp_audit( $request, 'upsert_chuong', array( $existing->ID ), true, 'UPDATED' ); return dttmcp_response( $request, true, array( 'id' => (int) $existing->ID, 'action' => 'updated', 'chuong' => dttmcp_post_payload( $updated ) ), $warnings ); } $result = dttmcp_create_chapter_internal( $body, $parent_id, $warnings ); if ( is_wp_error( $result ) ) return $result; dttmcp_audit( $request, 'upsert_chuong', array( $result['id'] ), true, 'CREATED' ); return dttmcp_response( $request, true, array( 'id' => $result['id'], 'action' => 'created', 'chuong' => dttmcp_post_payload( $result['post'] ) ), $warnings, null, 201 ); }
function dttmcp_endpoint_bulk_upsert( $request ) {
    $body = dttmcp_body( $request );
    $parent_id = dttmcp_id( $body['truyen_id'] ?? 0 );
    if ( ! dttmcp_post( $parent_id, 'truyen' ) ) return dttmcp_error_response( $request, 'TRUYEN_NOT_FOUND', 'Parent truyen was not found.', 404 );
    $permission = dttmcp_require_capability( $request, 'edit_posts', $parent_id );
    if ( $permission !== true ) return $permission;
    $items = array();
    $created = 0;
    $updated = 0;
    $failed = 0;
    foreach ( (array) ( $body['chapters'] ?? array() ) as $index => $chapter ) {
        if ( ! is_array( $chapter ) ) {
            $failed++;
            $items[] = array( 'index' => $index, 'ok' => false, 'error' => array( 'code' => 'INVALID_CHAPTER', 'message' => 'Each chapter must be an object.' ) );
            continue;
        }
        $chapter['truyen_id'] = $parent_id;
        $guard = dttmcp_create_status_guard( $chapter );
        $warnings = array();
        $result = $guard;
        $number = dttmcp_id( $chapter['chapter_number'] ?? 0 );
        if ( ! $number ) $number = dttmcp_extract_chapter_number( $chapter['title'] ?? '' );
        $existing = $number > 0 ? dttmcp_find_chapter_duplicate( $parent_id, $number ) : null;
        if ( ! is_wp_error( $result ) && $existing ) {
            if ( array_key_exists( 'expected_modified_gmt', $chapter ) && trim( (string) $chapter['expected_modified_gmt'] ) !== dttmcp_modified_gmt( $existing ) ) {
                $result = dttmcp_wp_error( 'OPTIMISTIC_LOCK_CONFLICT', 'The chapter was modified after the caller read it.', 409, array( 'expected_modified_gmt' => trim( (string) $chapter['expected_modified_gmt'] ), 'actual_modified_gmt' => dttmcp_modified_gmt( $existing ) ) );
            } else {
                $result = dttmcp_update_chapter_internal( $existing, $chapter, $warnings );
            }
        } elseif ( ! is_wp_error( $result ) ) {
            $result = dttmcp_create_chapter_internal( $chapter, $parent_id, $warnings );
        }
        if ( is_wp_error( $result ) ) {
            $failed++;
            dttmcp_audit( $request, 'bulk_upsert_chapters', array( $parent_id ), false, $result->get_error_code(), array( 'index' => $index ) );
            $items[] = array( 'index' => $index, 'ok' => false, 'error' => array( 'code' => $result->get_error_code(), 'message' => dttmcp_wp_error_message( $result ) ) );
            continue;
        }
        $action = $existing ? 'updated' : 'created';
        if ( 'updated' === $action ) $updated++; else $created++;
        dttmcp_audit( $request, 'bulk_upsert_chapters', array( (int) $result['id'] ), true, strtoupper( $action ), array( 'index' => $index ) );
        $items[] = array( 'index' => $index, 'ok' => true, 'action' => $action, 'id' => (int) $result['id'], 'warnings' => $warnings );
    }
    $data = array( 'truyen_id' => $parent_id, 'summary' => array( 'created' => $created, 'updated' => $updated, 'failed' => $failed ), 'items' => $items );
    return $failed ? dttmcp_response( $request, false, $data, array(), array( 'code' => 'PARTIAL_FAILURE', 'message' => 'One or more chapter upserts failed.' ), 207 ) : dttmcp_response( $request, true, $data );
}

function dttmcp_register_routes() {
    $routes = array(
        '/health' => 'dttmcp_endpoint_health', '/list-recent' => 'dttmcp_endpoint_list_recent', '/get-truyen' => 'dttmcp_endpoint_get_truyen', '/get-chuong' => 'dttmcp_endpoint_get_chuong', '/list-the-loai' => 'dttmcp_endpoint_list_the_loai', '/list-chuong-by-truyen' => 'dttmcp_endpoint_list_chuong_by_truyen', '/get-story-package' => 'dttmcp_endpoint_get_story_package', '/create-truyen' => 'dttmcp_endpoint_create_truyen', '/create-chuong' => 'dttmcp_endpoint_create_chuong', '/create-story-package' => 'dttmcp_endpoint_create_story_package', '/update-truyen' => 'dttmcp_endpoint_update_truyen', '/update-chuong' => 'dttmcp_endpoint_update_chuong', '/update-truyen-status' => 'dttmcp_endpoint_update_truyen_status', '/update-chuong-status' => 'dttmcp_endpoint_update_chuong_status', '/find-truyen' => 'dttmcp_endpoint_find_truyen', '/find-chuong' => 'dttmcp_endpoint_find_chuong', '/upsert-truyen' => 'dttmcp_endpoint_upsert_truyen', '/upsert-chuong' => 'dttmcp_endpoint_upsert_chuong', '/bulk-upsert-chapters' => 'dttmcp_endpoint_bulk_upsert', '/validate-truyen' => 'dttmcp_endpoint_validate_truyen', '/validate-chuong' => 'dttmcp_endpoint_validate_chuong', '/pre-publish-story-package' => 'dttmcp_endpoint_pre_publish', '/publish-truyen' => 'dttmcp_endpoint_publish_truyen', '/publish-chuong' => 'dttmcp_endpoint_publish_chuong', '/publish-story-package' => 'dttmcp_endpoint_publish_package', '/unpublish-truyen' => 'dttmcp_endpoint_unpublish_truyen', '/unpublish-chuong' => 'dttmcp_endpoint_unpublish_chuong', '/check-story-integrity' => 'dttmcp_endpoint_integrity',
        '/create-post' => 'dttmcp_endpoint_create_post',
        '/get-post' => 'dttmcp_endpoint_get_post',
        '/update-post' => 'dttmcp_endpoint_update_post',
        '/list-posts' => 'dttmcp_endpoint_list_posts',
        '/search-posts' => 'dttmcp_endpoint_search_posts',
        '/publish-post' => 'dttmcp_endpoint_publish_post',
        '/unpublish-post' => 'dttmcp_endpoint_unpublish_post',
        '/trash-post' => 'dttmcp_endpoint_trash_post',
        '/delete-post' => 'dttmcp_endpoint_trash_post',
        '/upload-media' => 'dttmcp_endpoint_upload_media',
        '/get-media' => 'dttmcp_endpoint_get_media',
        '/search-media' => 'dttmcp_endpoint_find_media',
        '/set-featured-image' => 'dttmcp_endpoint_set_featured_image',
        '/remove-featured-image' => 'dttmcp_endpoint_remove_featured_image',
        '/update-media-metadata' => 'dttmcp_endpoint_update_media_metadata',
        '/find-media' => 'dttmcp_endpoint_find_media',
        '/list-categories' => function ( $request ) { return dttmcp_endpoint_taxonomy( $request, 'category' ); },
        '/search-categories' => function ( $request ) { return dttmcp_endpoint_taxonomy( $request, 'category' ); },
        '/list-tags' => function ( $request ) { return dttmcp_endpoint_taxonomy( $request, 'post_tag' ); },
        '/search-tags' => function ( $request ) { return dttmcp_endpoint_taxonomy( $request, 'post_tag' ); },
        '/get-post-terms' => 'dttmcp_endpoint_get_post_terms',
        '/set-post-terms' => 'dttmcp_endpoint_set_post_terms',
        '/patch-post-content' => 'dttmcp_endpoint_patch_post_content',
        '/bulk-patch-post-content' => 'dttmcp_endpoint_bulk_patch_post_content',
        '/upsert-post-related-links' => 'dttmcp_endpoint_upsert_post_related_links',
        '/bulk-set-rank-math-meta' => 'dttmcp_endpoint_bulk_set_rank_math_meta',
        '/bulk-set-post-terms' => 'dttmcp_endpoint_bulk_set_post_terms',
        '/find-posts-linking-to' => 'dttmcp_endpoint_find_posts_linking_to',
        '/audit-post-internal-links' => 'dttmcp_endpoint_audit_post_internal_links',
        '/bulk-audit-post-internal-links' => 'dttmcp_endpoint_bulk_audit_post_internal_links',
        '/create-category' => function ( $request ) { return dttmcp_endpoint_create_term( $request, 'category' ); },
        '/create-tag' => function ( $request ) { return dttmcp_endpoint_create_term( $request, 'post_tag' ); },
        '/update-seo-meta' => 'dttmcp_endpoint_update_seo_meta',
        '/get-rank-math-meta' => 'dttmcp_endpoint_get_rank_math_meta',
        '/set-rank-math-meta' => 'dttmcp_endpoint_set_rank_math_meta',
    );
    foreach ( $routes as $route => $callback ) {
        register_rest_route( DTTMCP_NAMESPACE, $route, array( 'methods' => 'POST', 'callback' => dttmcp_guarded( $callback ), 'permission_callback' => function () { return true; } ) );
    }
}

add_action( 'rest_api_init', 'dttmcp_register_routes' );
