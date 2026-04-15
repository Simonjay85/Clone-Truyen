<?php
$html = file_get_contents('/Users/aaronnguyen/TN/App/Clone Truyen/tehi-theme/page-story-studio.php');
$parts = explode('<body', $html);
$body_html = '<body' . $parts[2];

libxml_use_internal_errors(true);
$dom = new DOMDocument();
$dom->loadHTML('<?xml encoding="UTF-8">' . $body_html, LIBXML_HTML_NOIMPLIED | LIBXML_HTML_NODEFDTD);

$xpath = new DOMXPath($dom);
$layouts = $xpath->query('//div[contains(@class, "studio-layout")]');

if ($layouts->length > 0) {
    echo "Children of studio-layout:\n";
    foreach ($layouts->item(0)->childNodes as $child) {
        if ($child->nodeType === XML_ELEMENT_NODE) {
            echo "- " . $child->nodeName . " id=" . $child->getAttribute('id') . " class=" . $child->getAttribute('class') . "\n";
        }
    }
}
?>
