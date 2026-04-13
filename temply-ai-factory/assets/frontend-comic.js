(function() {
    'use strict';

    function initComicContainer(container) {
        if (container.dataset.init) return;
        container.dataset.init = '1';

        var images = container.querySelectorAll('img.pollination-lazy');
        if (!images || images.length === 0) return;

        var currentIndex = 0;

        function loadNextImage() {
            if (currentIndex >= images.length) return;

            var img = images[currentIndex];
            var src = img.getAttribute('data-src');

            if (!src) {
                currentIndex++;
                loadNextImage();
                return;
            }

            // Xóa placeholder text ngay khi bắt đầu load
            var placeholderSpan = img.parentElement ? img.parentElement.querySelector('span.absolute') : null;
            if (placeholderSpan) placeholderSpan.textContent = 'Đang tải...';

            img.onload = function () {
                if (img.parentElement) {
                    img.parentElement.style.background = 'transparent';
                    var span = img.parentElement.querySelector('span.absolute');
                    if (span) span.style.display = 'none';
                    var layer = img.parentElement.querySelector('.bubbles-layer');
                    if (layer) layer.classList.remove('hidden');
                }
                currentIndex++;
                setTimeout(loadNextImage, 600);
            };

            img.onerror = function () {
                // Retry sau 4 giây nếu bị 429
                setTimeout(function () {
                    img.src = src + '&retry=' + Math.random();
                }, 4000);
            };

            img.src = src;
        }

        loadNextImage();
    }

    function scanAndInit() {
        var containers = document.querySelectorAll('.comic-container');
        containers.forEach(initComicContainer);
    }

    // 1. Chạy ngay khi DOM sẵn sàng
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', scanAndInit);
    } else {
        scanAndInit();
    }

    // 2. Chạy thêm lần nữa sau khi tất cả tài nguyên load xong (dành cho AJAX theme)
    window.addEventListener('load', scanAndInit);

    // 3. Quét lại mỗi 1.5 giây trong 15 giây đầu để bắt AJAX/PJAX lazy content
    var scanCount = 0;
    var scanInterval = setInterval(function () {
        scanAndInit();
        scanCount++;
        if (scanCount >= 10) clearInterval(scanInterval); // Dừng sau 15 giây
    }, 1500);

    // 4. MutationObserver: bắt nội dung bị inject bởi AJAX theme
    var observer = new MutationObserver(function (mutations) {
        mutations.forEach(function (mutation) {
            mutation.addedNodes.forEach(function (node) {
                if (node.nodeType !== 1) return;
                if (node.classList && node.classList.contains('comic-container')) {
                    initComicContainer(node);
                } else {
                    node.querySelectorAll && node.querySelectorAll('.comic-container').forEach(initComicContainer);
                }
            });
        });
    });

    observer.observe(document.body, { childList: true, subtree: true });
})();
