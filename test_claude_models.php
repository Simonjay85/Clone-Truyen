<?php
// *** XOA FILE NAY SAU KHI TEST ***
// Liệt kê các Claude model có thể dùng được với API key hiện tại
$api_key = isset($_GET['key']) ? $_GET['key'] : '';
if(empty($api_key)) die('Them ?key=sk-ant-xxx vao URL');

$ch = curl_init('https://api.anthropic.com/v1/models');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT        => 15,
    CURLOPT_SSL_VERIFYPEER => false,
    CURLOPT_HTTPHEADER     => [
        'x-api-key: ' . $api_key,
        'anthropic-version: 2023-06-01',
    ]
]);
$response = curl_exec($ch);
$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);
curl_close($ch);

header('Content-Type: text/plain');
echo "HTTP: $http_code\n";
if ($err) echo "CURL ERROR: $err\n";
echo "RESPONSE:\n" . $response;
