import re

with open("tehi-theme/functions.php", "r", encoding="utf-8") as f:
    code = f.read()

points_code = """
/**
 * --- HỆ THỐNG REVENUE SHARE (AUTHOR POINTS) ---
 */
// 1. Ghi nhận Lượt Mở Đọc (View)
function tehi_record_view() {
    $post_id = isset($_POST['post_id']) ? intval($_POST['post_id']) : 0;
    if (!$post_id) wp_die();

    // Tăng views
    $views = (int)get_post_meta($post_id, '_views', true);
    update_post_meta($post_id, '_views', $views + 1);

    // Tính điểm cho Author
    $author_id = get_post_field('post_author', $post_id);
    if ($author_id) {
        $points = (int)get_user_meta($author_id, '_author_points', true);
        update_user_meta($author_id, '_author_points', $points + 1);
    }
    wp_send_json_success();
}
add_action('wp_ajax_tehi_record_view', 'tehi_record_view');
add_action('wp_ajax_nopriv_tehi_record_view', 'tehi_record_view');

// 2. Ghi nhận Lượt Chia sẻ (Share) 
function tehi_record_share() {
    $post_id = isset($_POST['post_id']) ? intval($_POST['post_id']) : 0;
    if (!$post_id) wp_die();

    // Tăng shares
    $shares = (int)get_post_meta($post_id, '_shares', true);
    update_post_meta($post_id, '_shares', $shares + 1);

    // Tính điểm cho Author (Ví dụ: 1 Share = 50 điểm)
    $author_id = get_post_field('post_author', $post_id);
    if ($author_id) {
        $points = (int)get_user_meta($author_id, '_author_points', true);
        update_user_meta($author_id, '_author_points', $points + 50);
    }
    wp_send_json_success(['new_shares' => $shares + 1]);
}
add_action('wp_ajax_tehi_record_share', 'tehi_record_share');
add_action('wp_ajax_nopriv_tehi_record_share', 'tehi_record_share');

// 3. Inject global AJAX URL cho Javascript
function tehi_frontend_ajax() {
    echo '<script>var tehi_ajax_url = "' . admin_url('admin-ajax.php') . '";</script>';
}
add_action('wp_head', 'tehi_frontend_ajax');
"""

if 'tehi_record_view' not in code:
    code = code.replace("function tehi_tailwind_cleanup()", points_code + "\nfunction tehi_tailwind_cleanup()")
    with open("tehi-theme/functions.php", "w", encoding="utf-8") as f:
        f.write(code)
    print("Added Revenue Share logic to functions.php")

# Next to single-truyen.php:
# 1. Add ID to post container so JS knows and add the JS script to ping `tehi_record_view`.
with open("tehi-theme/single-truyen.php", "r", encoding="utf-8") as f:
    truyen_code = f.read()

# Add a script at the bottom to record views and handle shares
record_js = """
<script>
    document.addEventListener("DOMContentLoaded", function() {
        const postId = <?php echo get_the_ID(); ?>;
        
        // Gọi API tăng View ngầm
        const viewFormData = new FormData();
        viewFormData.append('action', 'tehi_record_view');
        viewFormData.append('post_id', postId);
        fetch(tehi_ajax_url, { method: 'POST', body: viewFormData });

        // Nút Share
        const shareBtn = document.getElementById('btnSharePoints');
        if (shareBtn) {
            shareBtn.addEventListener('click', function() {
                // Mở cửa sổ share fb/zalo..
                window.open('https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(window.location.href), 'facebook-share-dialog', 'width=800,height=600');
                
                // Gọi API ghi nhận Share
                const shareFormData = new FormData();
                shareFormData.append('action', 'tehi_record_share');
                shareFormData.append('post_id', postId);
                fetch(tehi_ajax_url, { method: 'POST', body: shareFormData })
                .then(res => res.json())
                .then(data => {
                    if(data.success) {
                        alert("Cảm ơn bạn đã chia sẻ! Tác giả vừa nhận được 50 điểm hoa hồng.");
                    }
                });
            });
        }
    });
</script>
"""

# Replace Theo dõi button space to add Share Button
if 'id="btnSharePoints"' not in truyen_code:
    share_btn = """
    <button id="btnSharePoints" class="px-10 py-4 bg-surface-container-high text-on-surface rounded-full font-bold hover:bg-surface-container-highest transition-all flex items-center gap-2 group">
        <span class="material-symbols-outlined text-green-600 group-hover:scale-110 transition-transform">share</span>
        Chia sẻ
    </button>
    """
    truyen_code = truyen_code.replace('<div class="flex flex-wrap gap-4">\n<button', '<div class="flex flex-wrap gap-4">\n<button')
    # Actually wait, there is this block:
    btn_target = """<button class="px-10 py-4 border-2 border-outline-variant text-on-surface-variant rounded-full font-bold hover:bg-surface-container-low transition-all flex items-center gap-2">
<span class="material-symbols-outlined">bookmark</span>
                                Theo dõi
                            </button>"""
    truyen_code = truyen_code.replace(btn_target, btn_target + "\n" + share_btn)
    truyen_code += "\n" + record_js
    
    with open("tehi-theme/single-truyen.php", "w", encoding="utf-8") as f:
        f.write(truyen_code)
    print("Added Share button & View tracker to single-truyen.php")

