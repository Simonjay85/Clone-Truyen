<?php
require_once('../../../wp-load.php');

$prompt = "Chủ tịch giả nghèo 10 năm đi nhặt rác để thử lòng vợ nhà giàu, rốt cuộc phát hiện vợ lấy mình chỉ vì nhầm tưởng mình là con ruột của trùm giang hồ. Cả gia đình vợ sỉ nhục, ép anh ly hôn trong ngày sinh nhật của cô ta. Hôm sau dàn xe bọc thép mạ vàng tiến vào đón anh.";
$genre = "Đô Thị, Vả Mặt";
$tone = "Giật gân, kịch tính, dồn dập, máu chó";
$art = "Realistic";
$target_chaps = 5;

$config = get_option('temply_auto_pilot_queue_config', false);
if (!$config) $config = ['queue' => [], 'status' => 'stopped'];

$config['queue'][] = [
    'mode' => 'single',
    'action' => 'setup_story',
    'raw_prompt' => $prompt,
    'genre' => $genre,
    'tone' => $tone,
    'art' => $art,
    'target_chapters' => $target_chaps,
    'chapters_left' => $target_chaps,
    'status' => 'pending', // Trạng thái pending sẽ được process bóc ra thành draft_outline
    'title' => '',
    'truyen_id' => 0
];
$config['status'] = 'running';
update_option('temply_auto_pilot_queue_config', $config);

// Trigger first step
if (function_exists('temply_process_auto_pilot')) {
    temply_process_auto_pilot();
    echo "Task injected and process started.";
} else {
    echo "Wait, function temply_process_auto_pilot not found?!";
}
