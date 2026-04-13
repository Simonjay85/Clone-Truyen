jQuery(document).ready(function($) {
    const $btn = $('#temply-start-btn');
    const $console = $('#temply-console');
    const $loader = $('#temply-loader');

    window.temply_warmup_queue = window.temply_warmup_queue || [];
    window.temply_warmup_total = window.temply_warmup_total || 0;
    window.temply_warmup_done = window.temply_warmup_done || 0;
    window.is_warming_up = window.is_warming_up || false;

    function processWarmupQueue() {
        if (window.temply_warmup_queue.length === 0) {
            if (window.temply_warmup_total > 0 && window.temply_warmup_done >= window.temply_warmup_total) {
                logTerminal(`🎉 [Ghost Preloader] HOÀN TẤT VẼ NGẦM (${window.temply_warmup_done}/${window.temply_warmup_total} KHUNG HÌNH)! Bạn có thể chuyển Tab an toàn.`, 'success');
                window.temply_warmup_total = 0;
                window.temply_warmup_done = 0;
            }
            return;
        }
        if (window.is_warming_up) return;
        window.is_warming_up = true;
        
        const currentUrl = window.temply_warmup_queue.shift();
        const img = new Image();
        
        img.onload = function() {
            window.is_warming_up = false;
            window.temply_warmup_done++;
            
            // Cứ 5 ảnh thì báo cáo 1 lần cho đỡ spam màn hình
            if (window.temply_warmup_done % 5 === 0) {
                logTerminal(`- [Ghost Preloader] Đã Cache thành công ${window.temply_warmup_done} / ${window.temply_warmup_total} Cảnh truyện...`, 'info');
            }
            
            setTimeout(processWarmupQueue, 1500); // Đợi 1.5s cho an toàn
        };

        img.onerror = function() {
            window.is_warming_up = false;
            // Nếu bị 429 or lỗi mạng -> Đẩy lại vào hàng đợi để thử lại
            window.temply_warmup_queue.unshift(currentUrl + '&r=' + Math.random());
            setTimeout(processWarmupQueue, 4000); // 429 Queue Full -> Đợi hẳn 4 giây rồi mới chọt tiếp
        };

        img.src = currentUrl;
    }

    function logTerminal(message, type = 'info') {
        let colorClass = 'text-slate-300';
        if (type === 'success') colorClass = 'text-green-400';
        if (type === 'error') colorClass = 'text-red-400';
        if (type === 'action') colorClass = 'text-blue-400 font-bold';
        if (type === 'warning') colorClass = 'text-yellow-400';
        
        $console.append(`<div class="${colorClass}">${message}</div>`);
        $console.scrollTop($console[0].scrollHeight);
    }

    // Brainstorm Handler
    const $brainstormBtn = $('#temply-brainstorm-btn');
    $brainstormBtn.on('click', function(e) {
        e.preventDefault();
        const aiModel = $("#temply-ai-model").val();
        const genre = $('#temply-genre').val() || 'Tiên hiệp';
        const keywords = $('#temply-keywords').val();
        
        if (!keywords || keywords.trim().split(/\s+/).length < 2) {
            alert('Vui lòng gõ ít nhất 2 chữ để AI dựa vào đó Brainstorm nha anh.');
            return;
        }

        $brainstormBtn.prop('disabled', true).text('Đang nghĩ...');
        
        $.post(temply_ai_ajax.ajax_url, {
            action: 'temply_step_brainstorm',
            nonce: temply_ai_ajax.nonce, ai_model: aiModel,
            genre: genre,
            keywords: keywords
        }).done(function(res) {
            $brainstormBtn.prop('disabled', false).html('<svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg> Brainstorm AI');
            if (res.success && res.data.options) {
                const list = $('#brainstorm-list');
                list.empty();
                res.data.options.forEach(opt => {
                    list.append(`
                        <div class="p-2 bg-white rounded border border-purple-100 text-xs text-slate-700 cursor-pointer hover:border-purple-300 hover:shadow-sm" onclick="addHook(this)">
                            ${opt}
                        </div>
                    `);
                });
                $('#brainstorm-results').removeClass('hidden');
            } else {
                alert(res.data.message || 'Lỗi Brainstorm');
            }
        }).fail(function() {
            $brainstormBtn.prop('disabled', false).text('Lỗi Kết Nối');
        });
    });

    // Brainstorm World Handler
    const $brainstormWorldBtn = $('#temply-brainstorm-world-btn');
    $brainstormWorldBtn.on('click', function(e) {
        e.preventDefault();
        const aiModel = $("#temply-ai-model").val();
        const genre = $('#temply-genre').val() || 'Tiên hiệp';
        const keywords = $('#temply-keywords').val();
        
        $brainstormWorldBtn.prop('disabled', true).text('Đang nghĩ bối cảnh...');
        
        $.post(temply_ai_ajax.ajax_url, {
            action: 'temply_step_brainstorm_world',
            nonce: temply_ai_ajax.nonce, 
            ai_model: aiModel,
            genre: genre,
            keywords: keywords || 'Thế giới mở'
        }).done(function(res) {
            $brainstormWorldBtn.prop('disabled', false).html('<svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg> Brainstorm AI');
            if (res.success && res.data.options) {
                const list = $('#brainstorm-world-list');
                list.empty();
                res.data.options.forEach(opt => {
                    list.append(`
                        <div class="p-2 bg-white rounded border border-purple-100 text-xs text-slate-700 cursor-pointer hover:border-purple-300 hover:shadow-sm" onclick="addWorld(this)">
                            ${opt}
                        </div>
                    `);
                });
                $('#brainstorm-world-results').removeClass('hidden');
            } else {
                alert(res.data.message || 'Lỗi Brainstorm');
            }
        }).fail(function() {
            $brainstormWorldBtn.prop('disabled', false).text('Lỗi Kết Nối');
        });
    });

    // Tính năng: Phân Tích Kịch Bản Nguồn
    const $analyzeBtn = $('#temply-analyze-source-btn');
    $analyzeBtn.on('click', function(e) {
        e.preventDefault();
        const aiModel = $("#temply-ai-model").val();
        const sourceText = $('#temply-source-text').val().trim();
        if (!sourceText) {
            alert('Vui lòng dán nội dung truyện nguồn vào ô trước khi phân tích!');
            return;
        }

        const originalText = $analyzeBtn.html();
        $analyzeBtn.prop('disabled', true).html('<svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg> Đang hít hà content...');

        $.post(temply_ai_ajax.ajax_url, {
            action: 'temply_step_analyze_source',
            nonce: temply_ai_ajax.nonce, ai_model: aiModel,
            source_text: sourceText
        }).done(function(res) {
            $analyzeBtn.prop('disabled', false).html(originalText);
            if (res.success && res.data.result) {
                const data = res.data.result;
                // Auto-fill
                if(data.genre) $('#temply-genre').val(data.genre).trigger('change');
                if(data.tone) $('#temply-tone').val(data.tone).trigger('change');
                if(data.keywords) {
                    $('#temply-keywords').val(data.keywords);
                    // Hiệu ứng flash xanh lá để báo hiệu đã điền
                    $('#temply-keywords').addClass('bg-teal-50 border-teal-400 text-teal-900').removeClass('bg-slate-50 border-slate-300');
                    setTimeout(() => {
                        $('#temply-keywords').removeClass('bg-teal-50 border-teal-400 text-teal-900').addClass('bg-slate-50 border-slate-300');
                    }, 1500);
                }
                
                // Nếu cào được comment thật thì điền vô UI và bật lên
                if (data.extracted_comments && data.extracted_comments.trim() !== '') {
                    $('#temply-source-comments').val(data.extracted_comments);
                    $('#source-comments-group').removeClass('hidden').addClass('flex');
                } else {
                    $('#temply-source-comments').val('');
                    $('#source-comments-group').addClass('hidden').removeClass('flex');
                }
                
                alert('Tadaa! AI đã phân tích và tự động điền các thông số kịch bản cho bạn.');
            } else {
                alert(res.data.message || 'Lỗi Phân Tích');
            }
        }).fail(function() {
            $analyzeBtn.prop('disabled', false).html(originalText);
            alert('Lỗi Kết Nối Máy Chủ');
        });
    });

    let currentBatch = 1;
    let totalBatch = 1;

    $btn.on('click', function(e) {
        e.preventDefault();
        
        const aiModel = $("#temply-ai-model").val();
        const genre = $('#temply-genre').val();
        const tone = $('#temply-tone').val();
        
        if (!genre || !tone) {
            alert('Vui lòng chọn đầy đủ Thể loại và Văn phong.');
            return;
        }

        currentBatch = 1;
        totalBatch = parseInt($('#temply-batch-size').val()) || 1;

        $btn.prop('disabled', true).addClass('opacity-50 cursor-not-allowed').text('Đang Cày Máy Cấy...');
        $console.html(''); 
        $loader.removeClass('hidden');

        runAgenticFlow();
    });

    function runAgenticFlow() {
        const aiModel = $("#temply-ai-model").val();
        const genre = $('#temply-genre').val();
        const tone = $('#temply-tone').val();
        const mode = $('#temply-mode').val();
        const art = $('#temply-art').val();
        const comicSeed = Math.floor(Math.random() * 1000000);
        const keywords = $('#temply-keywords').val();
        const worldBuilding = $('#temply-world-building').val();
        const numChapters = $('#temply-num-chapters').val().trim();

        logTerminal(`> BẮT ĐẦU CHUỖI SIÊU AGENTIC (Bộ ${currentBatch}/${totalBatch})...`, 'action');
        
        let worldData = '';
        let charData = '';
        let outlineArr = [];
        let truyenId = 0;

        // AJAX 1
        logTerminal(`> [STEP 1] The Oracle (World-building)...`, 'warning');
        $.post(temply_ai_ajax.ajax_url, {
            action: 'temply_step_oracle', nonce: temply_ai_ajax.nonce, ai_model: aiModel, genre: genre, tone: tone, keywords: keywords, world_building: worldBuilding
        }).done(function(res1) {
            if (!res1.success) return abort(res1.data.message);
            worldData = res1.data.result;
            logTerminal(`[The Oracle] Xong!`, 'success');

            // AJAX 2
            logTerminal(`> [STEP 2] The Puppet Master (Characters)...`, 'warning');
            $.post(temply_ai_ajax.ajax_url, {
                action: 'temply_step_puppet', nonce: temply_ai_ajax.nonce, ai_model: aiModel, world: worldData, keywords: keywords
            }).done(function(res2) {
                if (!res2.success) return abort(res2.data.message);
                charData = res2.data.result;
                logTerminal(`[The Puppet Master] Xong!`, 'success');

                // AJAX 3
                logTerminal(`> [STEP 3] The Architect (Outline ${numChapters} Chương Json)...`, 'warning');
                $.post(temply_ai_ajax.ajax_url, {
                    action: 'temply_step_architect', nonce: temply_ai_ajax.nonce, ai_model: aiModel, world: worldData, characters: charData, num_chapters: numChapters, keywords: keywords
                }).done(function(res3) {
                    if (!res3.success) return abort(res3.data.message);
                    outlineArr = res3.data.result; // Expect Array of length 5
                    if(!Array.isArray(outlineArr) || outlineArr.length === 0) return abort('Lỗi Parse Outline.');
                    logTerminal(`[The Architect] Outline ${outlineArr.length} Chương Đã Chốt!`, 'success');

                    // --- PHẦN HÀM XỬ LÝ VIẾT TRUYỆN ---
                    function renderOutlineReviewer() {
                        const listDiv = $('#temply-outline-list');
                        listDiv.empty();

                        outlineArr.forEach((chap, idx) => {
                            listDiv.append(`
                                <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm outline-card" data-idx="${idx}">
                                    <h4 class="font-bold text-slate-700 mb-2">Chương ${chap.chap_num}</h4>
                                    <input type="text" class="w-full px-4 py-2 border border-slate-300 rounded mb-3 font-semibold text-blue-700 outline-title" value="${chap.title}" placeholder="Tên chương">
                                    <textarea class="w-full px-4 py-2 border border-slate-300 rounded text-sm text-slate-600 outline-summary" rows="3" placeholder="Tóm tắt chương">${chap.summary}</textarea>
                                </div>
                            `);
                        });
                        
                        $('#temply-outline-reviewer').removeClass('hidden').addClass('flex');
                    }

                    // Nút Thêm chương thủ công
                    $('#add-chapter-btn').off('click').on('click', function() {
                        // Gather dữ liệu vừa sửa để không bị mất khi render lại
                        $('.outline-card').each(function() {
                            const idx = $(this).data('idx');
                            outlineArr[idx].title = $(this).find('.outline-title').val();
                            outlineArr[idx].summary = $(this).find('.outline-summary').val();
                        });
                        
                        // Đẩy chương mới tinh tươm vào
                        outlineArr.push({
                            chap_num: outlineArr.length + 1,
                            title: '',
                            summary: ''
                        });
                        
                        renderOutlineReviewer(); // Vẽ lại giao diện
                        
                        // Cuộn xuống kịch kim
                        setTimeout(() => {
                            const list = $('#temply-outline-list');
                            list.scrollTop(list[0].scrollHeight);
                        }, 50);
                    });

                    // Gắn sự kiện Bấm Tiếp Tục TRƯỚC KHI bị return early
                    $('#temply-resume-btn').off('click').on('click', function() {
                        // Gather dữ liệu vừa sửa
                        $('.outline-card').each(function() {
                            const idx = $(this).data('idx');
                            outlineArr[idx].title = $(this).find('.outline-title').val();
                            outlineArr[idx].summary = $(this).find('.outline-summary').val();
                        });
                        
                        $('#temply-outline-reviewer').removeClass('flex').addClass('hidden');
                        logTerminal(`> [User Approved] Đã chốt lại Dàn Ý. Bắt đầu kích hoạt máy viết...`, 'success');
                        resumeWorkflowFromStep4();
                    });
                    
                    $('#close-outline-reviewer').off('click').on('click', function() {
                        if(confirm('Bạn có chắc muốn đóng và Huỷ tiến trình này?')) {
                            $('#temply-outline-reviewer').removeClass('flex').addClass('hidden');
                            abort('Tiến trình bị huỷ bởi người dùng.');
                        }
                    });

                    // Xử lý luồng chạy
                    const isPauseForReview = $('#temply-pause-outline').is(':checked');
                    if(isPauseForReview) {
                        logTerminal(`> TẠM DỪNG: Đang chờ User kiểm duyệt Dàn Ý tại màn hình...`, 'action');
                        renderOutlineReviewer();
                        return; // Ngắt để chờ user Submit ở box ngoài
                    } else {
                        resumeWorkflowFromStep4();
                    }

                    function resumeWorkflowFromStep4() {
                        // AJAX 4: Create Story (Parent) + Image
                        logTerminal(`> [STEP 4] The Publisher (Tạo Truyện & Dùng AI Đẻ Ảnh Bìa)...`, 'warning');
                    $.post(temply_ai_ajax.ajax_url, {
                        action: 'temply_step_create_story', nonce: temply_ai_ajax.nonce, ai_model: aiModel, world: worldData, characters: charData, genre: genre, tone: tone, art: art, keywords: keywords
                    }).done(function(res4) {
                        if (!res4.success) return abort(res4.data.message);
                        truyenId = res4.data.truyen_id;
                        logTerminal(`[The Publisher] Đã tạo Truyện: ${res4.data.title}`, 'success');
                        logTerminal(`[The Publisher] Thuộc tính AI Khác: ${res4.data.thumb}`, 'success');
                        
                        // LOOP AJAX 5: Write Chapters Sequentially
                        logTerminal(`> [STEP 5] Kích hoạt Vòng Lặp The Ghostwriter (Tạo tự động ${outlineArr.length} Chương)`, 'action');
                        
                        let currentChapIndex = 0;
                        let chapRetryCount = 0;
                        const MAX_RETRIES = 2;

                        function loopChapter() {
                            if(currentChapIndex >= outlineArr.length) {
                                logTerminal(`> HOÀN TẤT ĐÚC SIÊU TÁC PHẨM (Bộ ${currentBatch}/${totalBatch})!`, 'action');
                                logTerminal(`> <a href="/wp-admin/post.php?post=${truyenId}&action=edit" target="_blank" class="text-blue-400 underline">Bấm Khám Phá Quả Trứng Bạn Vừa Sinh!</a>`, 'action');
                                
                                if (currentBatch < totalBatch) {
                                    currentBatch++;
                                    logTerminal(`\n> >>> [AUTO-PILOT] CHUẨN BỊ ĐÚC BỘ TIẾP THEO (${currentBatch}/${totalBatch}) SAU 5 GIÂY <<<`, 'warning');
                                    setTimeout(runAgenticFlow, 5000);
                                } else {
                                    logTerminal(`\n> 🎉 HOÀN TẤT TOÀN BỘ CHUỖI ĐÚC MẺ (${totalBatch} Bộ). Chúc mừng!`, 'success');
                                    resetUI('Thật Kì Diệu! Đúc Tiếp!');
                                }
                                return;
                            }
                            
                            let chapMeta = outlineArr[currentChapIndex];
                            if(chapRetryCount === 0) {
                                logTerminal(`Đang cày cuốc Chương ${chapMeta.chap_num}... (Khoảng 30s-40s)`, 'warning');
                            } else {
                                logTerminal(`⟳ Thử lại Chương ${chapMeta.chap_num} (lần ${chapRetryCount}/${MAX_RETRIES})...`, 'warning');
                            }
                            
                            $.post(temply_ai_ajax.ajax_url, {
                                action: mode === 'comic' ? 'temply_step_write_comic_chapter' : 'temply_step_write_chapter', 
                                nonce: temply_ai_ajax.nonce, ai_model: aiModel,
                                mode: mode, art: art, seed: comicSeed, 
                                truyen_id: truyenId, 
                                chap_num: chapMeta.chap_num, 
                                chap_title: chapMeta.title,
                                summary: chapMeta.summary,
                                custom_comments: $('#temply-source-comments').val(),
                                world: worldData, characters: charData,
                                genre: genre, tone: tone, keywords: keywords,
                                is_final_chapter: (currentChapIndex === outlineArr.length - 1 ? 1 : 0)
                            }).done(function(resChap) {
                                if (!resChap.success) {
                                    // Thử lại nếu chưa hết lượt retry
                                    if(chapRetryCount < MAX_RETRIES) {
                                        chapRetryCount++;
                                        logTerminal(`⚠ Chương ${chapMeta.chap_num} lỗi: ${resChap.data.message}. Tự thử lại sau 3 giây...`, 'error');
                                        setTimeout(loopChapter, 3000);
                                    } else {
                                        // Bỏ qua chương này, tiếp tục chương sau
                                        logTerminal(`✗ Bỏ qua Chương ${chapMeta.chap_num} (thử ${MAX_RETRIES} lần thất bại). Tiếp tục...`, 'error');
                                        chapRetryCount = 0;
                                        currentChapIndex++;
                                        setTimeout(loopChapter, 1000);
                                    }
                                    return;
                                }

                                chapRetryCount = 0; // Reset retry counter khi thành công
                                logTerminal(`✓ Xong [${resChap.data.title}] - ID: ${resChap.data.chuong_id}`, 'success');
                                
                                if (resChap.data.warmup_urls && resChap.data.warmup_urls.length > 0) {
                                    window.temply_warmup_total += resChap.data.warmup_urls.length;
                                    window.temply_warmup_queue.push(...resChap.data.warmup_urls);
                                    logTerminal(`[Ghost Preloader] Đã hút thêm ${resChap.data.warmup_urls.length} link ảnh, đang nạp ngầm vào Cache...`, 'info');
                                    processWarmupQueue();
                                }

                                currentChapIndex++;
                                loopChapter(); // Đệ quy bước tiếp
                            }).fail(() => {
                                // Lỗi mạng - thử lại
                                if(chapRetryCount < MAX_RETRIES) {
                                    chapRetryCount++;
                                    logTerminal(`⚠ Mất kết nối Chương ${chapMeta.chap_num}. Thử lại sau 5 giây...`, 'error');
                                    setTimeout(loopChapter, 5000);
                                } else {
                                    logTerminal(`✗ Bỏ tự động viết Chương ${chapMeta.chap_num} sau ${MAX_RETRIES} lần đứt mạng.`, 'error');
                                    chapRetryCount = 0; currentChapIndex++; setTimeout(loopChapter, 1000);
                                }
                            });
                        }

                        loopChapter(); // Kick-off the writing loop
                    }).fail(() => abort('Lỗi mạng The Publisher')); // End AJAX 4
                } // End function resumeWorkflowFromStep4

                }).fail(() => abort('Lỗi mạng The Architect'));

            }).fail(() => abort('Lỗi mạng Puppet Master'));

        }).fail(() => abort('Lỗi mạng The Oracle'));
    }

    function abort(msg) {
        logTerminal(`X LỖI: ${msg}`, 'error');
        resetUI('Khôi phục Thử Lại');
    }

    function resetUI(text) {
        $btn.prop('disabled', false).removeClass('opacity-50 cursor-not-allowed').text(text);
        $loader.addClass('hidden');
    }
    
    // Text to Comic Converter Magic
    const $magicBtn = $('#temply-magic-convert-btn');
    const $magicSelect = $('#temply-magic-source-truyen');
    
    $magicBtn.on('click', function(e) {
        e.preventDefault();
        let source_id = $magicSelect.val();
        let num_panels = $('#temply-magic-num-panels').val(); // Get num panels option
        if(!source_id) return alert("Vui lòng chọn 1 Truyện!");
        let aiModel = $('#temply-ai-model').val();
        
        $magicBtn.prop('disabled', true).addClass('opacity-50 cursor-not-allowed').text('Đang Chuẩn Bị...');
        logTerminal(`[TRUYỆN TRANH HÓA] Bắt đầu lấy dữ liệu truyện ID: ${source_id}`, 'warning');
        
        $.post(temply_ai_ajax.ajax_url, {
            action: 'temply_step_convert_comic_init',
            nonce: temply_ai_ajax.nonce,
            source_id: source_id
        }).done(function(res) {
            if(!res.success) {
                $magicBtn.prop('disabled', false).removeClass('opacity-50 cursor-not-allowed').html('LỖI. THỬ LẠI');
                return logTerminal('Lỗi: ' + res.data.message, 'error');
            }
            
            let truyenId = res.data.truyen_id;
            let chapters = res.data.chapters;
            if(!chapters || chapters.length === 0) {
               $magicBtn.prop('disabled', false).removeClass('opacity-50 cursor-not-allowed').html('Manga Hóa!');
               return logTerminal('Truyện này rỗng, không có chương nào để vẽ!', 'error');
            }
            logTerminal(`[TRUYỆN TRANH HÓA] Đã khởi tạo rễ "${res.data.title}" thành công. Truyện gốc có ${chapters.length} chương.`, 'success');
            
            let currentChap = 0;
            function loopConvert() {
                if(currentChap >= chapters.length) {
                    logTerminal(`[TRUYỆN TRANH HÓA] HOÀN TẤT CHUYỂN ĐỔI ${chapters.length} CHƯƠNG!`, 'action');
                    $magicBtn.prop('disabled', false).removeClass('opacity-50 cursor-not-allowed').html('HOÀN TẤT!');
                    return;
                }
                
                let text_chap = chapters[currentChap];
                logTerminal(`Đang Đạo diễn và vẽ Chương ${currentChap + 1}/${chapters.length}... (Chờ ~45s/Chương)`, 'warning');
                
                $.post(temply_ai_ajax.ajax_url, {
                    action: 'temply_step_convert_comic_chapter',
                    nonce: temply_ai_ajax.nonce,
                    ai_model: aiModel,
                    truyen_id: truyenId,
                    chap_source_id: text_chap.id,
                    chap_num: currentChap + 1,
                    num_panels: num_panels, // Send num panels info!
                    art: 'Manga Đen trắng Nhật Bản'
                }).done(function(cRes) {
                    if(!cRes.success) {
                        logTerminal(`[LỖI] Chương ${currentChap+1}: ${cRes.data.message}. Bỏ qua & Khựng lại 5s...`, 'error');
                        currentChap++;
                        setTimeout(loopConvert, 5000); // Retry next
                        return;
                    }
                    logTerminal(`✓ Đã Phù Phép: ${cRes.data.title}`, 'success');
                    
                    if (cRes.data.warmup_urls && cRes.data.warmup_urls.length > 0) {
                        window.temply_warmup_total += cRes.data.warmup_urls.length;
                        window.temply_warmup_queue.push(...cRes.data.warmup_urls);
                        processWarmupQueue();
                    }
                    
                    currentChap++;
                    loopConvert();
                }).fail(function() {
                    logTerminal(`[MẠNG LỖI] Lỗi kết nối ở chương ${currentChap+1}. Thử lại sau 5s...`, 'error');
                    setTimeout(loopConvert, 5000);
                });
            }
            loopConvert();
        }).fail(function() {
            logTerminal('Mạng lỗi! Không thể Init.', 'error');
            $magicBtn.prop('disabled', false).removeClass('opacity-50 cursor-not-allowed').html('MẠNG LỖI. THỬ LẠI');
        });
    });
});
