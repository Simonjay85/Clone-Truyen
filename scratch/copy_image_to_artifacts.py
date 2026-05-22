import shutil
import os

src = "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme/img_data/images/no-image-cover.png"
dst_dir = "/Users/aaronnguyen/.gemini/antigravity-ide/brain/12ea8d69-8883-4c0b-9ecb-fc7822e46167"
dst = os.path.join(dst_dir, "no-image-cover-check.png")

if os.path.exists(src):
    shutil.copy2(src, dst)
    print(f"Successfully copied {src} to {dst}")
    
    # check its size in MB
    size_mb = os.path.getsize(dst) / (1024 * 1024)
    print(f"Size of file is {size_mb:.2f} MB")
else:
    print(f"Source file {src} does not exist!")
