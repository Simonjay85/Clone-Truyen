(function (window) {
  "use strict";

  function installVHSkeleton($) {
    // WordPress runs jQuery in noConflict mode; do not depend on window.$.
    if (typeof $ !== "function") {
      console.warn(
        "[VH Skeleton] jQuery is unavailable; skeleton initialization skipped."
      );
      return false;
    }

    function handleSkeletonLoad(selector) {
      $(selector + "+img")
        .on("load", function () {
          const img = $(this);
          const skeleton = img.siblings(selector);
          const container = img.parent(); // Đảm bảo container được gán giá trị

          // Trì hoãn 1.5 giây trước khi ẩn skeleton và hiển thị ảnh
          setTimeout(function () {
            skeleton.fadeOut(300, function () {
              $(this).remove(); // Xóa skeleton
              img.removeClass("d-none"); // Hiển thị ảnh mờ dần
              container.addClass("loaded"); // Hiển thị các phần tử con
            });
          }, 600);
        })
        .each(function () {
          if (this.complete) $(this).trigger("load");
        });

      // Đảm bảo kích thước của skeleton khớp với nội dung container
      $(".vh-skeleton-container").each(function () {
        const container = $(this); // Gán giá trị container
        const skeleton = container.find(selector);

        skeleton.width(container.width());
        // Khi skeleton biến mất, nội dung fadeIn mượt mà
        setTimeout(function () {
          skeleton.fadeOut(300, function () {
            $(this).remove(); // Xóa skeleton
            container.addClass("loaded"); // Hiển thị các phần tử con
          });
          container.removeClass("mt-1"); // Xóa skeleton
        }, 600);
      });
    }

    function initializeVHSkeleton() {
      const skeletonTypes = [
        ".vh-skeleton-image",
        ".vh-skeleton-avatar",
        ".vh-skeleton-text",
      ];

      skeletonTypes.forEach(function (selector) {
        handleSkeletonLoad(selector);
      });
    }

    function initializeSkeletonOnScroll() {
      const gsap = window.gsap;
      if (!gsap || !gsap.utils || !gsap.to) {
        return;
      }

      const skeletonItems = gsap.utils.toArray(
        ".vh-skeleton-container-scroll"
      );

      skeletonItems.forEach(function (item) {
        const itemTrigger = $(item).find(
          ".vh-skeleton-container-scroll-trigger"
        );

        gsap.to(item, {
          scrollTrigger: {
            trigger: itemTrigger,
            start: "top 75%",
            onEnter: function () {
              setTimeout(function () {
                const skeleton = $(item).find(".vh-skeleton");
                skeleton.fadeOut(300, function () {
                  $(this).remove();
                  $(item).children().fadeIn();
                });
              }, 600);
            },
          },
        });
      });
    }

    // header.php invokes these functions by their global names.
    window.handleSkeletonLoad = handleSkeletonLoad;
    window.initializeVHSkeleton = initializeVHSkeleton;
    window.initializeSkeletonOnScroll = initializeSkeletonOnScroll;
    return true;
  }

  function tryInstallVHSkeleton() {
    return installVHSkeleton(window.jQuery);
  }

  // Normally WordPress jQuery is already available before deferred scripts run.
  // Retry once at window load so a delayed jQuery response fails safely too.
  if (!tryInstallVHSkeleton()) {
    window.addEventListener("load", tryInstallVHSkeleton, { once: true });
  }
})(window);
