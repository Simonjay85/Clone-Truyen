import glob

files = glob.glob("tehi-theme/*.php")

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if 'max-w-7xl' in content:
        new_content = content.replace('max-w-7xl', 'w-full max-w-[95%] 2xl:max-w-[1600px]')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filepath}")

# Also check single-chuong for reading text width
filepath = "tehi-theme/single-chuong.php"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()
if 'max-w-4xl' in content:
    new_content = content.replace('max-w-4xl', 'w-full max-w-[95%] lg:max-w-[6xl]')
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated chap width {filepath}")
