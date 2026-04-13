<?php get_header(); ?>

<main class="flex-grow w-full bg-surface-container dark:bg-black pb-20">
    <?php if(have_posts()): while(have_posts()): the_post(); ?>
    
    <!-- Hero Header -->
    <div class="relative w-full h-auto flex flex-col items-center justify-center overflow-hidden pt-20 pb-4">
        <?php if(has_post_thumbnail()): ?>
            <div class="absolute inset-0 w-full h-full pointer-events-none">
                <img src="<?php echo get_the_post_thumbnail_url(get_the_ID(), 'full'); ?>" class="w-full h-full object-cover blur-xl opacity-40 dark:opacity-20 scale-110" alt="Cover">
                <div class="absolute inset-0 bg-gradient-to-t from-surface-container via-surface-container/60 to-transparent dark:from-black dark:via-black/70"></div>
            </div>
        <?php else: ?>
            <div class="absolute inset-0 bg-gradient-to-br from-primary-container to-tertiary-container dark:from-indigo-950 dark:to-slate-900 opacity-80 pointer-events-none"></div>
        <?php endif; ?>
        
        <div class="relative z-10 text-center px-4 max-w-4xl mx-auto">
            <div class="inline-flex items-center justify-center gap-2 px-4 py-1.5 rounded-full bg-white/30 dark:bg-black/40 backdrop-blur-md border border-white/20 dark:border-white/10 text-sm font-bold tracking-wide mb-6 text-on-surface uppercase shadow-sm">
                <span class="material-symbols-outlined text-[18px]">article</span> Chuyên mục Hệ thống
            </div>
            <h1 class="text-4xl md:text-5xl lg:text-5xl font-black text-on-surface mb-4 !leading-tight text-balance drop-shadow-sm">
                <?php the_title(); ?>
            </h1>
            <p class="text-on-surface-variant font-medium text-lg flex items-center justify-center gap-2 pb-16">
                <span class="material-symbols-outlined text-sm">update</span> Cập nhật lần cuối: <?php echo get_the_modified_date('d/m/Y'); ?>
            </p>
        </div>
    </div>

    <!-- Content Area -->
    <div class="w-full max-w-[95%] 2xl:max-w-[1600px] mx-auto px-8 sm:px-10 relative z-20 -mt-10">
        <div class="bg-[#F8F9FA] dark:bg-[#111315] rounded-[2rem] p-8 sm:p-12 md:p-16 shadow-2xl w-full border border-slate-200/60 dark:border-white/5 ring-1 ring-black/5 dark:ring-white/5">
            <div class="prose prose-slate dark:prose-invert max-w-4xl mx-auto text-justify prose-p:text-justify prose-headings:font-extrabold md:prose-h2:text-3xl md:prose-h3:text-2xl prose-h2:text-slate-800 prose-h2:dark:text-white prose-h2:mt-10 prose-h3:text-slate-700 prose-h3:dark:text-slate-200 prose-h3:mt-8 prose-a:text-blue-600 prose-img:rounded-2xl text-[17px] leading-[1.8] font-medium prose-p:text-slate-700 dark:prose-p:text-slate-300 prose-li:text-slate-700 dark:prose-li:text-slate-300">
                <?php the_content(); ?>
            </div>
        </div>
    </div>
    
    <?php endwhile; endif; ?>
</main>

<?php get_footer(); ?>
