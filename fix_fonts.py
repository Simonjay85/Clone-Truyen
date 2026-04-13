import re
import os

css_files = [
    "tehi-theme/style.css",
    "tehi-theme/templates/css/style.css",
    "tehi-theme/assets/css/style.css"
]

for file_path in css_files:
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove @font-face for Lato-Black
    content = re.sub(r'@font-face\s*{[^}]*Lato-Black[^}]*}', '', content, flags=re.IGNORECASE)
    
    # Replace lato-black font-family
    content = content.replace("lato-black", "'Outfit', sans-serif")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Font fixes complete.")
