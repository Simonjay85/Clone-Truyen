<?php
require_once('../../../wp-load.php');

$args = [
    'post_type' => 'truyen',
    'post_status' => 'publish',
    'posts_per_page' => -1
];
$truyens = get_posts($args);

$report = [];

foreach ($truyens as $t) {
    $t_id = $t->ID;
    
    $args_chaps = [
        'post_type' => 'chuong',
        'meta_key' => '_truyen_id',
        'meta_value' => $t_id,
        'posts_per_page' => -1
    ];
    $chaps = get_posts($args_chaps);
    
    $chap_count = count($chaps);
    $flags = [];
    
    if ($chap_count == 0) {
        $flags[] = "Trống (0 chương)";
    } elseif ($chap_count > 25) {
        $flags[] = "Bị Lặp Vô Tận ($chap_count chương)";
    }
    
    // Check repetition
    if ($chap_count > 0) {
        $titles = array_map(function($c) { return $c->post_title; }, $chaps);
        $title_str = implode(" ", $titles);
        $words = str_word_count(strtolower($title_str), 1);
        $word_counts = array_count_values($words);
        // Exclude common words
        $common = ['chương', 'của', 'trong', 'và', 'sự', 'cuộc', 'chiến', 'những', 'kẻ'];
        $duplicates = 0;
        foreach($word_counts as $word => $count) {
            if(!in_array($word, $common) && strlen($word) > 4 && $count >= 5) {
                // If a specific 5-letter+ word is repeated in more than 5 chapters
                $duplicates++;
            }
        }
        if ($duplicates >= 1) {
            $flags[] = "Lặp từ vựng kịch bản (Title Repetition)";
        }
    }
    
    $report[] = [
        'id' => $t_id,
        'title' => $t->post_title,
        'chaps' => $chap_count,
        'flags' => implode(", ", $flags)
    ];
}

echo "=== DIAGNOSTIC REPORT ===\n";
foreach($report as $r) {
    $flag_str = empty($r['flags']) ? "Bình thường" : "LỖI: " . $r['flags'];
    echo "- ID {$r['id']} | {$r['title']} | {$r['chaps']} chương | Trạng thái: $flag_str\n";
}
