import os

theme_path = "tehi-theme"
for root, dirs, files in os.walk(theme_path):
    for file in files:
        if file.endswith((".php", ".css", ".js")):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Final text cleanup
            # Replace tehitruyen.com URLs with home_url
            content = content.replace("https://Đọc Tiểu Thuyết.com", "<?php echo home_url('/'); ?>")
            content = content.replace("doctieuthuyet.com/", "<?php echo home_url('/'); ?>")
            
            if content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
