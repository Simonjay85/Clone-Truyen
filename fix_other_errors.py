import sys
import glob

files = glob.glob("tehi-theme/**/*.php", recursive=True)

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()

    modified = False
    
    # 1. khoiTaoToolTip
    if 'khoiTaoToolTip();' in content:
        content = content.replace('khoiTaoToolTip();', '// khoiTaoToolTip();')
        modified = True
        
    # 2. icon-hoa.png
    if 'templates/images/icon-hoa.png' in content:
        # replace with fontawesome icon or a generic transparent pixel (data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=)
        content = content.replace('src="<?php echo get_template_directory_uri(); ?>/templates/images/icon-hoa.png"', 'src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="')
        modified = True

    # 3. nen_trang.jpg
    if 'nen_trang.jpg' in content:
        content = content.replace("url('https://tehitruyen.com/img_data/images/nen_trang.jpg')", "none")
        modified = True

    if modified:
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Fixed {filepath}")
