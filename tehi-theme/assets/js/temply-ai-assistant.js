/**
 * Temply AI Assistant for Gutenberg
 */

(function($) {
    const { select, dispatch } = wp.data;
    const { createBlock } = wp.blocks;

    $(document).ready(function() {
        // Create the UI
        const aiWrapper = $(`
            <div id="temply-ai-assistant" style="position: fixed; bottom: 30px; right: 30px; z-index: 999999; font-family: 'Be Vietnam Pro', sans-serif;">
                
                <!-- Main Wand Button -->
                <button id="temply-ai-toggle" style="width: 56px; height: 56px; border-radius: 50%; background: linear-gradient(135deg, #6366f1, #a855f7); color: white; border: none; box-shadow: 0 10px 25px rgba(99, 102, 241, 0.4); cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 24px; transition: transform 0.3s ease;">
                    ✨
                </button>

                <!-- Panel -->
                <div id="temply-ai-panel" style="display: none; position: absolute; bottom: 70px; right: 0; width: 320px; background: white; border-radius: 16px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; overflow: hidden; transform-origin: bottom right; transition: all 0.3s ease;">
                    <div style="background: #1e1e2d; padding: 16px 20px; color: white;">
                        <h3 style="margin: 0; font-size: 16px; font-weight: 700; display: flex; align-items: center; gap: 8px; color:white;">
                            <span>🪄</span> Temply AI Magic
                        </h3>
                        <p style="margin: 4px 0 0; font-size: 12px; color: #a4a6b3;">Trợ lý sáng tác thông minh</p>
                    </div>
                    
                    <div style="padding: 16px; display: flex; flex-direction: column; gap: 10px;">
                        
                        <button class="ai-action-btn" data-action="rewrite_block" style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px; border-radius: 10px; text-align: left; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 10px;">
                            <span style="font-size: 18px; background: #e0e7ff; color: #4f46e5; width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center;">📝</span>
                            <div>
                                <div style="font-weight: 600; font-size: 13px; color: #1e293b;">Tái tạo đoạn đã chọn</div>
                                <div style="font-size: 11px; color: #64748b; margin-top:2px;">Viết lại đoạn văn đang bôi đen</div>
                            </div>
                        </button>

                        <button class="ai-action-btn" data-action="rewrite_all" style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px; border-radius: 10px; text-align: left; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 10px;">
                            <span style="font-size: 18px; background: #fce7f3; color: #db2777; width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center;">🌪️</span>
                            <div>
                                <div style="font-weight: 600; font-size: 13px; color: #1e293b;">Viết lại toàn bộ</div>
                                <div style="font-size: 11px; color: #64748b; margin-top:2px;">Xào lại nội dung cả chương</div>
                            </div>
                        </button>

                        <button class="ai-action-btn" data-action="thumbnail" style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px; border-radius: 10px; text-align: left; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 10px;">
                            <span style="font-size: 18px; background: #fef3c7; color: #d97706; width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center;">🖼️</span>
                            <div>
                                <div style="font-weight: 600; font-size: 13px; color: #1e293b;">Tạo Thumbnail AI</div>
                                <div style="font-size: 11px; color: #64748b; margin-top:2px;">Tạo ảnh bìa dựa trên cốt truyện</div>
                            </div>
                        </button>

                        <button class="ai-action-btn" data-action="seo_generate" style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px; border-radius: 10px; text-align: left; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 10px;">
                            <span style="font-size: 18px; background: #dcfce7; color: #16a34a; width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center;">🎯</span>
                            <div>
                                <div style="font-weight: 600; font-size: 13px; color: #1e293b;">Tối ưu SEO (RankMath)</div>
                                <div style="font-size: 11px; color: #64748b; margin-top:2px;">Tạo tự động Title, Slug, Des</div>
                            </div>
                        </button>

                        <button class="ai-action-btn" data-action="split_chapters" style="background: #f8fafc; border: 1px dashed #6366f1; padding: 12px; border-radius: 10px; text-align: left; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 10px;">
                            <span style="font-size: 18px; background: #ede9fe; color: #8b5cf6; width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center;">✂️</span>
                            <div>
                                <div style="font-weight: 700; font-size: 13px; color: #4338ca;">Chia thành các Chương</div>
                                <div style="font-size: 11px; color: #64748b; margin-top:2px;">Cắt văn bản hiện tại thành các chương con tự động</div>
                            </div>
                        </button>

                    </div>

                    <!-- Loader overlay -->
                    <div id="ai-loader" style="display: none; position: absolute; top:0; left:0; width: 100%; height: 100%; background: rgba(255,255,255,0.9); backdrop-filter: blur(2px); flex-direction: column; align-items: center; justify-content: center; z-index: 10;">
                        <div style="width: 40px; height: 40px; border: 4px solid #e0e7ff; border-top: 4px solid #6366f1; border-radius: 50%; animation: aiSpin 1s linear infinite;"></div>
                        <p style="margin-top: 12px; font-weight: 600; color: #4f46e5; font-size: 13px;">AI đang xử lý phép thuật...</p>
                    </div>
                </div>
            </div>
            
            <style>
                @keyframes aiSpin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
                .ai-action-btn:hover { background: #fff !important; border-color: #6366f1 !important; box-shadow: 0 4px 12px rgba(99,102,241,0.1); transform: translateY(-1px); }
                .ai-action-btn:active { transform: translateY(0); }
                #temply-ai-toggle:hover { transform: scale(1.1); }
            </style>
        `);

        $('body').append(aiWrapper);

        // Toggle logic
        $('#temply-ai-toggle').on('click', function() {
            $('#temply-ai-panel').fadeToggle(200);
        });

        // Hover effect for AI button
        $('.ai-action-btn').on('mouseenter', function() {
            $(this).css('background', '#fff');
            $(this).css('border-color', '#6366f1');
        }).on('mouseleave', function() {
            $(this).css('background', '#f8fafc');
            $(this).css('border-color', '#e2e8f0');
        });

        // Action Handlers
        $('.ai-action-btn').on('click', function() {
            const action = $(this).data('action');
            if(action === 'rewrite_block') {
                processRewriteBlock();
            } else if (action === 'rewrite_all') {
                processRewriteAll();
            } else if (action === 'thumbnail') {
                processThumbnail();
            } else if (action === 'seo_generate') {
                processSEO();
            } else if (action === 'split_chapters') {
                processSplitChapters();
            }
        });

        // ==========================
        //  AI FUNCTIONS
        // ==========================

        function showAILoader() { $('#ai-loader').css('display', 'flex'); }
        function hideAILoader() { $('#ai-loader').css('display', 'none'); }

        function showNotification(msg, isErr = false) {
            if(dispatch('core/notices')) {
                if(isErr) {
                    dispatch('core/notices').createErrorNotice(msg, { type: 'snackbar' });
                } else {
                    dispatch('core/notices').createSuccessNotice(msg, { type: 'snackbar' });
                }
            } else {
                alert(msg);
            }
        }

        // 1. REWRITE SELECTED BLOCK
        function processRewriteBlock() {
            const selectedBlock = select('core/block-editor').getSelectedBlock();
            
            if(!selectedBlock || !selectedBlock.attributes || !selectedBlock.attributes.content) {
                showNotification('Vui lòng click chọn một đoạn văn bản để AI viết lại!', true);
                return;
            }

            const oldContent = typeof selectedBlock.attributes.content === 'string' 
                ? selectedBlock.attributes.content 
                : selectedBlock.attributes.content.toString();

            if(!oldContent) return;

            showAILoader();

            $.post(templyAIParams.ajaxurl, {
                action: 'temply_ai_rewrite',
                action_nonce: templyAIParams.nonce,
                content: oldContent,
                mode: 'paragraph'
            }, function(response) {
                hideAILoader();
                if(response.success) {
                    dispatch('core/block-editor').updateBlock(selectedBlock.clientId, {
                        attributes: { content: response.data.rewritten_content }
                    });
                    showNotification('Đoạn văn đã được tái tạo thành công!');
                    $('#temply-ai-panel').fadeOut();
                } else {
                    showNotification(response.data.message || 'Lỗi kết nối AI', true);
                }
            }).fail(function() {
                hideAILoader();
                showNotification('Lỗi server. Vui lòng thử lại.', true);
            });
        }

        // 2. REWRITE ALL CONTENT
        function processRewriteAll() {
            if(!confirm("Việc này sẽ thay đổi TOÀN BỘ nội dung truyện hiện tại. Bạn có chắc chắn muốn AI viết lại tất cả?")) {
                return;
            }

            const blocks = select('core/block-editor').getBlocks();
            if(blocks.length === 0) {
                showNotification('Không có nội dung để viết lại.', true);
                return;
            }

            let fullText = blocks.map(b => (b.attributes && b.attributes.content) ? b.attributes.content : '').join('\n\n');

            showAILoader();

            $.post(templyAIParams.ajaxurl, {
                action: 'temply_ai_rewrite',
                action_nonce: templyAIParams.nonce,
                content: fullText,
                mode: 'all'
            }, function(response) {
                hideAILoader();
                if(response.success) {
                    const newContent = response.data.rewritten_content;
                    const newBlocks = [createBlock('core/paragraph', { content: newContent })];
                    const clientIds = blocks.map(b => b.clientId);
                    dispatch('core/block-editor').replaceBlocks(clientIds, newBlocks);

                    showNotification('Toàn bộ truyện đã được viết lại!');
                    $('#temply-ai-panel').fadeOut();
                } else {
                    showNotification('Lỗi kết nối AI', true);
                }
            }).fail(function() {
                hideAILoader();
                showNotification('Lỗi server', true);
            });
        }

        // 3. GENERATE THUMBNAIL
        function processThumbnail() {
            const title = select('core/editor').getEditedPostAttribute('title');
            const keyword = prompt("Nhập từ khoá phong cách ảnh (VD: Anime, Cinematic, Dark Fantasy...) \nĐể trống để AI tự phân tích:", "Anime style, high quality");
            
            if (keyword === null) return; // user cancelled

            showAILoader();

            $.post(templyAIParams.ajaxurl, {
                action: 'temply_ai_generate_thumbnail',
                action_nonce: templyAIParams.nonce,
                post_id: templyAIParams.postId,
                title: title,
                keyword: keyword
            }, function(response) {
                hideAILoader();
                if(response.success) {
                    if(response.data.attachment_id > 0) {
                        dispatch('core/editor').editPost({ featured_media: response.data.attachment_id });
                        showNotification('Ảnh bìa AI đã được gán thành công!');
                    } else {
                        showNotification('Ảnh bìa đã tạo, nhưng không tìm thấy ID để gán. (Mock Fallback)', true);
                    }
                    $('#temply-ai-panel').fadeOut();
                } else {
                    showNotification(response.data.message || 'Lỗi tạo ảnh', true);
                }
            }).fail(function() {
                hideAILoader();
                showNotification('Lỗi server AI', true);
            });
        }

        // 4. GENERATE SEO
        function processSEO() {
            const title = select('core/editor').getEditedPostAttribute('title');
            const blocks = select('core/block-editor').getBlocks();
            let fullText = blocks.map(b => (b.attributes && b.attributes.content) ? b.attributes.content : '').join(' ').substring(0, 1500);

            if(!fullText && !title) {
                showNotification('Không có nội dung để tối ưu SEO.', true);
                return;
            }

            showAILoader();

            $.post(templyAIParams.ajaxurl, {
                action: 'temply_ai_generate_seo',
                action_nonce: templyAIParams.nonce,
                post_id: templyAIParams.postId,
                title: title,
                content: fullText
            }, function(response) {
                hideAILoader();
                if(response.success) {
                    const seo = response.data;
                    
                    // 1. Write direct to meta for WP Core
                    try {
                        wp.data.dispatch('core/editor').editPost({ 
                            slug: seo.slug,
                            meta: {
                                rank_math_title: seo.title,
                                rank_math_description: seo.description
                            }
                        });
                    } catch(e) {}

                    // 2. Force DOM updates for RankMath inputs with React Synthetic Events
                    const setNativeValue = (element, value) => {
                        const valueSetter = Object.getOwnPropertyDescriptor(element, 'value').set;
                        const prototype = Object.getPrototypeOf(element);
                        const prototypeValueSetter = Object.getOwnPropertyDescriptor(prototype, 'value') ? Object.getOwnPropertyDescriptor(prototype, 'value').set : null;
                        
                        if (valueSetter && valueSetter !== prototypeValueSetter) {
                            prototypeValueSetter.call(element, value);
                        } else {
                            valueSetter.call(element, value);
                        }
                    };

                    const titleInputs = document.querySelectorAll('input[id*="rank_math_title"], input.components-text-control__input[id*="rank_math"]');
                    titleInputs.forEach(el => {
                        if(el.closest('.rank-math-title-snippet, .rank-math-snippet-editor')) {
                            setNativeValue(el, seo.title);
                            el.dispatchEvent(new Event('input', { bubbles: true }));
                        }
                    });

                    const descInputs = document.querySelectorAll('textarea[id*="rank_math_description"], textarea.components-textarea-control__input[id*="rank_math"]');
                    descInputs.forEach(el => {
                        if(el.closest('.rank-math-description-snippet, .rank-math-snippet-editor')) {
                            setNativeValue(el, seo.description);
                            el.dispatchEvent(new Event('input', { bubbles: true }));
                        }
                    });

                    showNotification('Đã tạo và gắn Tiêu đề, Slug, Mô tả SEO thành công!');
                    $('#temply-ai-panel').fadeOut();
                } else {
                    showNotification(response.data.message || 'Lỗi SEO AI', true);
                }
            }).fail(function() {
                hideAILoader();
                showNotification('Lỗi server AI', true);
            });
        }

        // 5. SPLIT CHAPTERS
        function processSplitChapters() {
            if(!confirm("Hệ thống sẽ dựa vào các tựa đề (Ví dụ: 'Chương 1: ABC') trong bài viết để chia tách thành các bài viết con (Chương truyện). Văn bản hiện tại trong Editor này KHÔNG BỊ XOÁ để đảm bảo an toàn. Bạn có chắc chắn muốn Tách Chương ngay bây giờ?")) {
                return;
            }

            const blocks = select('core/block-editor').getBlocks();
            if(blocks.length === 0) {
                showNotification('Trình soạn thảo đang trống, không có gì để cắt.', true);
                return;
            }

            // Serialize blocks back to raw HTML for backend parsing
            const rawHTML = wp.blocks.serialize(blocks);

            showAILoader();
            $('#ai-loader p').text('Đang nhào nặn & cắt chương...');

            $.post(templyAIParams.ajaxurl, {
                action: 'temply_ai_split_chapters',
                action_nonce: templyAIParams.nonce,
                post_id: templyAIParams.postId, // ID of the parent 'truyen'
                content: rawHTML
            }, function(response) {
                hideAILoader();
                $('#ai-loader p').text('AI đang xử lý phép thuật...'); // Reset string

                if(response.success) {
                    const message = `Tuyệt vời! Đã phân tách thành công ${response.data.count} chương con. Mở danh sách bài viết để xem.`;
                    showNotification(message);
                    $('#temply-ai-panel').fadeOut();

                    // Prompt if they want to clear the master text
                    setTimeout(() => {
                        if(confirm(`Quá trình cắt thành công ${response.data.count} chương! Bạn có muốn xoá bỏ toàn bộ văn bản trong Trình soạn thảo này cho gọn không? (Nên xoá nếu Master Story đã sinh xong chương)`)) {
                            dispatch('core/block-editor').resetBlocks([]);
                            dispatch('core/editor').savePost();
                        }
                    }, 500);

                } else {
                    showNotification(response.data.message || 'Lỗi khi chia chương. Hãy đảm bảo bạn có cú pháp "Chương 1", "Chương 2"... trong bài.', true);
                }
            }).fail(function(xhr, status, error) {
                hideAILoader();
                $('#ai-loader p').text('AI đang xử lý phép thuật...');
                showNotification('Lỗi kết nối máy chủ khi cắt chương.', true);
                console.error(error);
            });
        }

    });
})(jQuery);
