import re

with open('tehi-theme/single-chuong.php', 'r') as f:
    text = f.read()

new_scripts = """
<script>
// --- Nghe Truyện (TTS API) ---
const appTTS = {
    isPlaying: false,
    utterance: null,
    paragraphs: [],
    currentIndex: 0,
    
    init() {
        this.paragraphs = Array.from(document.querySelectorAll('.r-para-wrap')).map(el => el.textContent.replace('💬', '').trim()).filter(t => t.length > 0);
    },
    
    toggle() {
        if (!('speechSynthesis' in window)) return alert('Trình duyệt của bạn không hỗ trợ đọc Text-to-Speech!');
        if (this.paragraphs.length === 0) this.init();
        
        const btnL = document.getElementById('ttsLabel');
        if (this.isPlaying) {
            window.speechSynthesis.cancel();
            this.isPlaying = false;
            btnL.textContent = 'Nghe truyện';
            this.currentIndex = 0;
            return;
        }
        
        this.isPlaying = true;
        btnL.textContent = 'Đang đọc (Chạm dừng)';
        this.playNext();
    },
    
    playNext() {
        if (!this.isPlaying) return;
        if (this.currentIndex >= this.paragraphs.length) {
            this.isPlaying = false;
            document.getElementById('ttsLabel').textContent = 'Nghe truyện';
            this.currentIndex = 0;
            return;
        }
        
        const text = this.paragraphs[this.currentIndex];
        this.utterance = new SpeechSynthesisUtterance(text);
        this.utterance.lang = 'vi-VN';
        this.utterance.rate = 1.0;
        this.utterance.pitch = 1.0;
        
        // Highlight paragraph
        document.querySelectorAll('.r-para-wrap').forEach(el => el.style.backgroundColor = 'transparent');
        const currentParaHtml = document.querySelectorAll('.r-para-wrap')[this.currentIndex];
        if(currentParaHtml) {
            currentParaHtml.style.backgroundColor = 'rgba(99, 102, 241, 0.1)';
            currentParaHtml.scrollIntoView({behavior:'smooth', block:'center'});
        }
        
        this.utterance.onend = () => {
            this.currentIndex++;
            this.playNext();
        };
        
        this.utterance.onerror = () => {
            console.error('SpeechSynthesis API Error');
            this.currentIndex++;
            this.playNext();
        };
        
        window.speechSynthesis.speak(this.utterance);
    }
};

// --- Yêu Thích ---
const appLike = {
    toggle() {
        let lkey = 'liked_' + <?php echo $truyen_id; ?>;
        if (localStorage.getItem(lkey)) return alert('Bạn đã thích truyện này rồi!');
        
        const fd = new FormData();
        fd.append('action', 'temply_like_chapter');
        fd.append('post_id', <?php echo $truyen_id; ?>);
        
        fetch('<?php echo admin_url('admin-ajax.php'); ?>', { method: 'POST', body: fd })
        .then(r => r.json())
        .then(res => {
            if (res.success) {
                document.getElementById('likeCount').textContent = res.data.likes;
                document.getElementById('likeIcon').style.fill = '#ef4444';
                localStorage.setItem(lkey, '1');
            }
        });
    }
};

// Modify pCmt to support mode 'all'
if (typeof pCmt !== 'undefined') {
    pCmt.openMode = function(mode) {
        if (mode === 'all') {
            document.getElementById('cmtPanelTitle').textContent = `💬 Bình luận chung`;
            this.currentP = -1; // -1 represents global chapter comment
            document.getElementById('cmtPanel').classList.add('open');
            document.getElementById('cmtOverlay').classList.add('open');
            document.body.style.overflow = 'hidden';
            this.load(-1);
            document.querySelector('.r-speed-dial').classList.remove('open');
        } else {
            this.open(mode);
        }
    };
    
    // Check if already liked
    window.addEventListener('DOMContentLoaded', () => {
        if (localStorage.getItem('liked_' + <?php echo $truyen_id; ?>)) {
            document.getElementById('likeIcon').style.fill = '#ef4444';
        }
    });
}
</script>
"""

# Replace the closing script tag of pCmt so we can inject safely
text = text.replace('<?php get_footer(); ?>', new_scripts + '\n<?php get_footer(); ?>')

with open('tehi-theme/single-chuong.php', 'w') as f:
    f.write(text)

print("Patch applied for JS")
