<?php
// *** XOA FILE NAY SAU KHI TEST ***
$api_key = 'REPLACE_WITH_YOUR_CLAUDE_KEY';

$payload = json_encode([
    'model'      => 'claude-3-haiku-20240307',
    'max_tokens' => 100,
    'messages'   => [
        ['role' => 'user', 'content' => 'Say: working']
    ]
]);

$ch = curl_init('https://api.anthropic.com/v1/messages');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_POSTFIELDS     => $payload,
    CURLOPT_TIMEOUT        => 30,
    CURLOPT_SSL_VERIFYPEER => false,
    CURLOPT_HTTPHEADER     => [
        'content-type: application/json',
        'x-api-key: ' . $api_key,
        'anthropic-version: 2023-06-01'
    ]
]);

$response = curl_exec($ch);
$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$curl_error = curl_error($ch);
curl_close($ch);

echo '<pre>';
echo 'HTTP Code: ' . $http_code . "\n";
if ($curl_error) echo 'CURL Error: ' . $curl_error . "\n";
echo 'Response: ' . $response;
echo '</pre>';
