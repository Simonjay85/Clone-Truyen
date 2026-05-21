import novel_editor
import random

escaped_prompt = "masterpiece, highly detailed book cover, anime illustration style, vivid lighting, typography text 'Trong Sinh Lam Trum Tra Sua' written prominently on the cover".replace(' ', '%20')
cover_url = f"https://image.pollinations.ai/prompt/{escaped_prompt}?width=2000&height=2000&seed={random.randint(1, 99999)}"

novel_editor.upload_helper()
print("Updating Cover with:", cover_url)
cover_res = novel_editor.update_story_cover(2190, cover_url)
print(cover_res)
novel_editor.remove_helper()
