import re

with open("tehi-theme/page-bangxephang.php", "r", encoding="utf-8") as f:
    code = f.read()

# Replace the Static "Vinh Danh Dịch Giả" block with WP_User_Query
user_query_php = """
                <div class="space-y-6">
                    <?php
                    // Query authors ordered by _author_points
                    $user_args = array(
                        'meta_key' => '_author_points',
                        'orderby'  => 'meta_value_num',
                        'order'    => 'DESC',
                        'number'   => 5,
                    );
                    $user_query = new WP_User_Query($user_args);
                    $authors = $user_query->get_results();
                    
                    if (!empty($authors)) {
                        $top_colors = ['bg-primary/10 text-primary', 'bg-slate-200 text-slate-700', 'bg-orange-100 text-orange-700'];
                        $rank = 1;
                        foreach ($authors as $author) {
                            $points = (int)get_user_meta($author->ID, '_author_points', true);
                            if ($points <= 0 && $rank > 3) continue; // Skip 0 point users if not top 3
                            
                            $avatar = get_avatar_url($author->ID);
                            $name = $author->display_name;
                            $formatted_points = number_format($points) . " Điểm";
                            
                            if ($rank <= 3) {
                                $rank_class = $top_colors[$rank-1];
                                $bg_class = $rank == 1 ? "bg-surface-container-lowest shadow-sm hover:translate-x-1" : "bg-surface-container-lowest/60 hover:bg-surface-container-lowest hover:translate-x-1";
                                $ring = $rank == 1 ? "border-2 border-primary ring-4 ring-primary/5" : "border-2 border-outline-variant";
                                
                                echo '
                                <div class="flex items-center gap-4 p-4 rounded-2xl '.$bg_class.' transition-transform cursor-pointer">
                                    <div class="w-14 h-14 rounded-full overflow-hidden '.$ring.' flex-shrink-0 bg-slate-200">
                                        <img class="w-full h-full object-cover" src="'.esc_url($avatar).'" />
                                    </div>
                                    <div class="flex-grow">
                                        <div class="font-bold text-on-background line-clamp-1">'.esc_html($name).'</div>
                                        <div class="text-xs text-on-surface-variant font-medium">Hoa hồng: '.esc_html($formatted_points).'</div>
                                    </div>
                                    <div class="'.$rank_class.' px-3 py-1 rounded-full font-bold text-xs flex-shrink-0">TOP '.$rank.'</div>
                                </div>';
                            } else {
                                echo '
                                <div class="pt-2 border-t border-slate-200/60 mt-2">
                                    <div class="flex justify-between items-center px-2 py-2 hover:bg-surface-container hover:rounded-lg">
                                        <span class="text-sm font-medium text-on-surface-variant">#'.$rank.' '.esc_html($name).'</span>
                                        <span class="text-xs font-bold text-primary">'.esc_html($formatted_points).'</span>
                                    </div>
                                </div>';
                            }
                            $rank++;
                        }
                    } else {
                        echo '<p class="text-sm text-center opacity-50 py-4">Chưa có dữ liệu Dịch Giả</p>';
                    }
                    ?>
                </div>
"""

# Find the block <div class="space-y-6"> ... <!-- Top Group 1 --> ... </section>
code = re.sub(r'<div class="space-y-6">.*?</div>\n\s*</section>', user_query_php + '\n            </section>', code, flags=re.DOTALL)

with open("tehi-theme/page-bangxephang.php", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated page-bangxephang.php with dynamic authors")
