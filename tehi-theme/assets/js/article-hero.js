(function () {
    'use strict';

    var sliders = document.querySelectorAll('[data-dtt-article-hero]');

    if (!sliders.length) {
        return;
    }

    var initAttempts = 0;

    function initArticleHero() {
        if (typeof window.Swiper !== 'function') {
            if (initAttempts >= 125) {
                return;
            }
            initAttempts += 1;
            window.setTimeout(initArticleHero, 80);
            return;
        }

        sliders.forEach(function (sliderElement) {
            if (sliderElement.swiper) {
                return;
            }

            var slides = sliderElement.querySelectorAll('.swiper-slide');
            var reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

            new window.Swiper(sliderElement, {
                a11y: {
                    enabled: true,
                    nextSlideMessage: 'Bài viết tiếp theo',
                    prevSlideMessage: 'Bài viết trước',
                    paginationBulletMessage: 'Đến bài viết {{index}}'
                },
                allowTouchMove: slides.length > 1,
                grabCursor: slides.length > 1,
                keyboard: {
                    enabled: true,
                    onlyInViewport: true
                },
                loop: slides.length > 1,
                navigation: {
                    nextEl: sliderElement.querySelector('.swiper-button-next'),
                    prevEl: sliderElement.querySelector('.swiper-button-prev')
                },
                pagination: {
                    clickable: true,
                    el: sliderElement.querySelector('.swiper-pagination')
                },
                speed: reducedMotion ? 0 : 560,
                watchOverflow: true
            });
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initArticleHero, { once: true });
    } else {
        initArticleHero();
    }
}());
