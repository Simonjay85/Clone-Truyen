(function (wp) {
    const { registerPlugin } = wp.plugins;
    const { PluginSidebar } = wp.editPost;
    const { createElement: el, useState, useEffect } = wp.element;
    const { PanelBody, TextareaControl, TextControl, Button, Spinner, Notice } = wp.components;
    const { useSelect, useDispatch } = wp.data;

    const TemplyStoryMasterSidebar = ({ postId }) => {
        const [isFetching, setIsFetching] = useState(true);
        const [isProcessing, setIsProcessing] = useState(false);
        const [statusMsg, setStatusMsg] = useState('');
        
        const [world, setWorld] = useState('');
        const [characters, setCharacters] = useState('');
        const [genre, setGenre] = useState('');
        const [chapterList, setChapterList] = useState([]);
        const [progressCount, setProgressCount] = useState({ done: 0, total: 0 });

        // Tải Context từ server
        useEffect(() => {
            setIsFetching(true);
            const fd = new FormData();
            fd.append('action', 'temply_step_get_story_master_context');
            fd.append('nonce', temply_ai_ajax.nonce);
            fd.append('truyen_id', postId);

            fetch(temply_ai_ajax.ajax_url, { method: 'POST', body: fd })
                .then(res => res.json())
                .then(res => {
                    if (res.success) {
                        setWorld(res.data.world || '');
                        setCharacters(res.data.characters || '');
                        setGenre(res.data.genre || '');
                        setChapterList(res.data.chapter_list || []);
                    } else {
                        setStatusMsg(res.data.message);
                    }
                })
                .catch(err => setStatusMsg('Lỗi kết nối tải Tổng Trạm'))
                .finally(() => setIsFetching(false));
        }, [postId]);

        const saveMasterContext = () => {
            return new Promise((resolve, reject) => {
                const sums = {};
                chapterList.forEach(c => { sums[c.id] = c.summary; });
                
                const fd = new FormData();
                fd.append('action', 'temply_step_save_story_master_context');
                fd.append('nonce', temply_ai_ajax.nonce);
                fd.append('truyen_id', postId);
                fd.append('world', world);
                fd.append('characters', characters);
                fd.append('chapter_summaries', JSON.stringify(sums));
                
                fetch(temply_ai_ajax.ajax_url, { method: 'POST', body: fd })
                    .then(r => r.json())
                    .then(res => res.success ? resolve() : reject(res.data.message))
                    .catch(err => reject('Network error'));
            });
        };

        const processRegenerateChapter = async (chapterId, summary) => {
            const fd = new FormData();
            fd.append('action', 'temply_step_regenerate_chapter');
            fd.append('nonce', temply_ai_ajax.nonce);
            fd.append('chuong_id', chapterId);
            fd.append('custom_world', world);
            // Character + genre are loaded from truyen_id in backend if not passed directly, but we pass custom_world. Wait, backend regenerate only reads custom_world if we pass it, but it automatically reads from DB if we don't. We just saved it! So AI will read latest DB values!
            
            const res = await fetch(temply_ai_ajax.ajax_url, { method: 'POST', body: fd });
            const data = await res.json();
            if(!data.success) throw new Error(data.data.message);
            return data;
        };

        const handleMasterRegenerate = async () => {
            if(!chapterList.length) return alert('Truyện chưa có chương nào để viết!');
            if(!confirm('CẢNH BÁO TỐI CAO: Hành động này sẽ LƯU DÀN Ý, rồi quét Toàn bộ danh sách Chương và cầu xin AI XOÁ ĐI VIẾT LẠI TOÀN BỘ. Có thể mất tới vài phút đến cả tiếng. Chắc chắn không?')) return;
            
            setIsProcessing(true);
            setStatusMsg('Đang lưu dữ liệu Tổng Trạm (World, Nhân vật, Dàn Ý)...');
            
            try {
                await saveMasterContext();
                setStatusMsg('Đã lưu! Tiến hành nhốt AI vào phòng viết từng chương một...');
                
                setProgressCount({ done: 0, total: chapterList.length });
                let count = 0;
                for(const ch of chapterList) {
                    setStatusMsg(`Đang cày ẩu chương: ${ch.title}... Xin đừng đóng tab!`);
                    await processRegenerateChapter(ch.id, ch.summary);
                    count++;
                    setProgressCount({ done: count, total: chapterList.length });
                }
                setStatusMsg('THÀNH CÔNG RỰC RỠ! Toàn bộ tiểu thuyết đã được đập đi xây lại.');
            } catch(e) {
                setStatusMsg(`[LỖI GÃY GÁNH]: ${e}`);
            } finally {
                setIsProcessing(false);
            }
        };

        const handleRegenerateCover = async () => {
            if(!confirm('Tính năng này sẽ nhờ AI phân tích lại tên truyện và bối cảnh để vẽ ra Ảnh Bìa (Featured Image) mới. Tốn khoảng 15 giây. Bắt đầu?')) return;
            
            setIsProcessing(true);
            setStatusMsg('Đang tưởng tượng mảng màu và gọi Họa Sĩ AI (Pollinations)...');
            
            const fd = new FormData();
            fd.append('action', 'temply_step_regenerate_story_cover');
            fd.append('nonce', temply_ai_ajax.nonce);
            fd.append('truyen_id', postId);
            
            fetch(temply_ai_ajax.ajax_url, { method: 'POST', body: fd })
                .then(r => r.json())
                .then(res => {
                    if (res.success) {
                        setStatusMsg(res.data.message);
                        setTimeout(() => window.location.reload(), 2000);
                    } else {
                        setStatusMsg(`[LỖI HỌA SĨ]: ${res.data.message}`);
                    }
                })
                .catch(err => setStatusMsg('Lỗi mạng khi vẽ bìa!'))
                .finally(() => setIsProcessing(false));
        };

        return el('div', { className: 'temply-ai-sidebar-content', style: { padding: '16px', background: '#f5f5f5' } },
            el('h3', { style: { marginTop: 0, marginBottom: '20px', color: '#1d2327', borderBottom: '2px solid #2271b1', paddingBottom: '10px' } }, 'TỔNG TRẠM DÀN Ý'),
            el('p', { style: { marginBottom: '20px', color: '#666', fontSize: '13px' } }, 'Quản trị viên đang ở cấp độ Mạch Truyện. Bạn có thể sửa rễ cốt lõi và dàn ý tất cả các Chương ở đây.'),
            
            isFetching ? el(Spinner) : el('div', {},
                el(TextControl, {
                    label: 'Thể loại truyện (System Rule)',
                    value: genre,
                    readOnly: true,
                    style: { background: '#e0e0e0', color: '#555' }
                }),
                el(TextareaControl, {
                    label: 'Bối cảnh Thế Giới',
                    value: world,
                    onChange: (val) => setWorld(val),
                    rows: 3
                }),
                el(TextareaControl, {
                    label: 'Hồ Sơ Nhân Vật Toàn Truyện',
                    value: characters,
                    onChange: (val) => setCharacters(val),
                    rows: 4
                }),

                el('div', { style: { margin: '20px 0', borderTop: '1px solid #ccc', paddingTop: '20px' } }, 
                    el('h4', { style: { background: '#1d2327', color: 'white', padding: '5px 10px', borderRadius: '4px' } }, `DÀN Ý CÁC CHƯƠNG (${chapterList.length})`),
                    chapterList.map((ch, idx) => {
                        return el('div', { key: ch.id, style: { background: 'white', padding: '10px', marginBottom: '10px', border: '1px solid #ddd', borderRadius: '4px', borderLeft: '4px solid #2271b1' } },
                            el('h5', { style: { margin: '0 0 10px 0', color: '#2271b1' } }, ch.title),
                            el(TextareaControl, {
                                value: ch.summary,
                                onChange: (val) => {
                                    const newList = [...chapterList];
                                    newList[idx].summary = val;
                                    setChapterList(newList);
                                },
                                rows: 5,
                                style: { fontSize: '12px', lineHeight: '1.4' }
                            }),
                            el('a', { href: ch.edit_url, target: '_blank', style: { fontSize: '12px', textDecoration: 'none', color: '#d63638', fontWeight: 'bold' } }, 'Mở sửa riêng chương này ↗')
                        );
                    })
                ),
                
                statusMsg && el('p', { style: { background: '#fff', borderLeft: '4px solid #d63638', padding: '10px', fontWeight: 'bold', margin: '20px 0' } }, statusMsg),
                
                isProcessing && el('div', { style: { background: '#fff', border: '1px solid #2271b1', borderRadius: '4px', overflow: 'hidden', height: '10px', marginBottom: '10px' } },
                    el('div', { style: { width: `${(progressCount.done / progressCount.total)*100}%`, background: '#2271b1', height: '100%', transition: 'width 0.3s' } })
                ),

                el(Button, {
                    isPrimary: true,
                    isBusy: isProcessing,
                    disabled: isProcessing,
                    onClick: handleMasterRegenerate,
                    style: { width: '100%', justifyContent: 'center', marginBottom: '10px', background: isProcessing ? '#999' : '#d63638', borderColor: isProcessing ? '#999' : '#d63638', padding: '20px 10px', fontWeight: 'bold', fontSize: '14px' }
                }, isProcessing ? `Đang Viết (${progressCount.done}/${progressCount.total})` : '🔥 LƯU MẠCH TRUYỆN & REGENERATE TOÀN BỘ CHƯƠNG'),

                el(Button, {
                    isSecondary: true,
                    isBusy: isProcessing,
                    disabled: isProcessing,
                    onClick: handleRegenerateCover,
                    style: { width: '100%', justifyContent: 'center', marginBottom: '20px', padding: '15px 10px', fontWeight: 'bold' }
                }, '🖼️ VẼ LẠI ẢNH BÌA TRUYỆN BẰNG AI')
            )
        );
    };

    const TemplyAiSidebar = () => {
        // Lấy ID an toàn
        const postId = useSelect((select) => {
            const editor = select('core/editor');
            return editor ? editor.getCurrentPostId() : null;
        });
        const postType = useSelect((select) => {
            const editor = select('core/editor');
            return editor ? editor.getCurrentPostType() : null;
        });
        
        const [isLoading, setIsLoading] = useState(false);
        const [isFetching, setIsFetching] = useState(true);
        const [statusMsg, setStatusMsg] = useState('');
        
        const [chapId, setChapId] = useState('');
        const [truyenId, setTruyenId] = useState(0);
        const [world, setWorld] = useState('');
        const [characters, setCharacters] = useState('');
        const [genre, setGenre] = useState('');
        const [summary, setSummary] = useState('');
        const [chapterList, setChapterList] = useState([]);

        // Tải Context từ server
        useEffect(() => {
            if (postType !== 'chuong') {
                setIsFetching(false);
                return;
            }

            setIsFetching(true);
            const fd = new FormData();
            fd.append('action', 'temply_step_get_chapter_context');
            fd.append('nonce', temply_ai_ajax.nonce);
            fd.append('chuong_id', postId);

            fetch(temply_ai_ajax.ajax_url, { method: 'POST', body: fd })
                .then(res => res.json())
                .then(res => {
                    if (res.success) {
                        setChapId(postId);
                        setTruyenId(res.data.truyen_id || 0);
                        setWorld(res.data.world || '');
                        setCharacters(res.data.characters || '');
                        setGenre(res.data.genre || '');
                        setSummary(res.data.summary || '');
                        setChapterList(res.data.chapter_list || []);
                    } else {
                        setStatusMsg(res.data.message);
                    }
                })
                .catch(err => setStatusMsg('Lỗi kết nối tải Dàn Ý'))
                .finally(() => setIsFetching(false));

        }, [postId, postType]);

        const handleRegenerate = () => {
            if (!confirm('Hành động này sẽ XÓA SẠCH Nội Dung trong Editor của chương và yêu cầu AI viết lại ngay lập tức. Sau khi viết xong trang sẽ Tự Động Tải Lại. Bạn chốt chứ?')) return;
            
            setIsLoading(true);
            setStatusMsg('Đang nhốt AI vào phòng tối để viết truyện...');
            
            const fd = new FormData();
            fd.append('action', 'temply_step_regenerate_chapter');
            fd.append('nonce', temply_ai_ajax.nonce);
            fd.append('chuong_id', postId);
            fd.append('custom_world', world);
            fd.append('custom_characters', characters);
            fd.append('custom_summary', summary);
            
            fetch(temply_ai_ajax.ajax_url, { method: 'POST', body: fd })
                .then(res => res.json())
                .then(res => {
                    if (res.success) {
                        setStatusMsg('XONG! Đang tải lại bài viết...');
                        window.location.reload();
                    } else {
                        setStatusMsg('LỖI: ' + res.data.message);
                        setIsLoading(false);
                    }
                })
                .catch(() => {
                    setStatusMsg('Lỗi kết nối mạng.');
                    setIsLoading(false);
                });
        };

        const handleNextChapter = () => {
            if (!confirm('AI sẽ tự động đọc đoạn cuối của chương NÀY để phát triển rễ mạch sang Chương MỚI. Bắt đầu?')) return;
            
            setIsLoading(true);
            setStatusMsg('Đang kích hoạt Mạng lưới Nơron suy luận Chương Mới...');
            
            const fd = new FormData();
            fd.append('action', 'temply_step_generate_next_chapter');
            fd.append('nonce', temply_ai_ajax.nonce);
            fd.append('chuong_id', postId); // dự phòng
            fd.append('truyen_id', truyenId); 
            
            fetch(temply_ai_ajax.ajax_url, { method: 'POST', body: fd })
                .then(res => res.json())
                .then(res => {
                    if (res.success) {
                        setStatusMsg('Xong! Đang nhảy sang trang chỉnh sửa Chương mới...');
                        window.location.href = res.data.redirect_url;
                    } else {
                        setStatusMsg('LỖI: ' + res.data.message);
                        setIsLoading(false);
                    }
                })
                .catch(() => {
                    setStatusMsg('Lỗi kết nối mạng.');
                    setIsLoading(false);
                });
        }

        if (postType === 'truyen') {
            return el(TemplyStoryMasterSidebar, { postId: postId });
        }

        if (postType !== 'chuong') {
            return el('div', { style: { padding: '20px' } }, 'Bảng năng lực AI Toolkit chỉ hiển thị khi Soạn Thảo CHƯƠNG hoặc TRUYỆN.');
        }

        return el('div', { className: 'temply-ai-sidebar-content', style: { padding: '16px' } },
            el('p', { style: { marginBottom: '20px', color: '#666', fontSize: '13px' } }, 'Chỉ đạo đường đi nước bước cho Trí Tuệ Nhân Tạo ngay tại đây thay vì gõ chữ bằng tay.'),
            
            isFetching ? el(Spinner) : el('div', {},
                el(TextControl, {
                    label: 'Thể loại truyện (System Rule)',
                    value: genre,
                    readOnly: true,
                    style: { background: '#f0f0f1', color: '#555' }
                }),
                el(TextareaControl, {
                    label: 'Bối cảnh Thế Giới',
                    value: world,
                    onChange: (val) => setWorld(val),
                    rows: 3
                }),
                el(TextareaControl, {
                    label: 'Hồ Sơ Nhân Vật',
                    value: characters,
                    onChange: (val) => setCharacters(val),
                    rows: 3
                }),
                el(TextareaControl, {
                    label: '🔥 CHỈ ĐẠO DÀN Ý / TÓM TẮT',
                    help: 'AI sẽ dựa vào Dàn ý này để phóng tác. Hãy gõ chỉ đạo cốt truyện sát sao vào đây trước khi nhấn Regenerate.',
                    value: summary,
                    onChange: (val) => setSummary(val),
                    rows: 6,
                    style: { border: '1px solid #d63638', background: '#fcf0f1' }
                }),
                
                statusMsg && el('p', { style: { color: '#d63638', fontWeight: 'bold', margin: '15px 0' } }, statusMsg),
                
                el(Button, {
                    isPrimary: true,
                    isBusy: isLoading,
                    disabled: isLoading,
                    onClick: handleRegenerate,
                    style: { width: '100%', justifyContent: 'center', marginBottom: '10px', background: '#d63638', borderColor: '#d63638' }
                }, isLoading ? 'Đang viết...' : '📝 LƯU & VIẾT LẠI CHƯƠNG NÀY'),

                el(Button, {
                    isSecondary: true,
                    disabled: isLoading,
                    onClick: handleNextChapter,
                    style: { width: '100%', justifyContent: 'center' }
                }, '✨ ÉP ĐẺ CHƯƠNG TIẾP (N+1)'),

                chapterList && chapterList.length > 0 && el('div', { style: { marginTop: '30px', paddingTop: '20px', borderTop: '1px solid #ddd' } },
                    el('h4', { style: { marginBottom: '10px' } }, 'Bấm Để Nhảy Nhanh Sang Chương Khác'),
                    el('div', { style: { maxHeight: '200px', overflowY: 'auto', background: '#f0f0f1', padding: '10px', borderRadius: '8px' } },
                        chapterList.map(item => {
                            const isCurrent = item.id === postId;
                            return el('a', {
                                key: item.id,
                                href: item.edit_url,
                                style: { 
                                    display: 'block', 
                                    padding: '8px', 
                                    marginBottom: '4px',
                                    background: isCurrent ? '#fff' : 'transparent',
                                    fontWeight: isCurrent ? 'bold' : 'normal',
                                    color: isCurrent ? '#d63638' : '#2271b1',
                                    borderRadius: '4px',
                                    textDecoration: 'none',
                                    boxShadow: isCurrent ? '0 1px 2px rgba(0,0,0,0.1)' : 'none'
                                }
                            }, item.title);
                        })
                    )
                )
            )
        );
    };

    try {
        registerPlugin('temply-ai-sidebar', {
            icon: 'superhero', // fallback to valid dashicon superhero or admin-customizer
            render: function () {
                return el(PluginSidebar,
                    {
                        name: 'temply-ai-sidebar',
                        title: 'Quyền Năng AI',
                    },
                    el(TemplyAiSidebar)
                );
            }
        });
    } catch(e) { console.error('Temply AI Sidebar Error Registration', e); }

})(window.wp);
