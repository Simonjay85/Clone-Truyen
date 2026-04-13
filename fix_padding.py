import glob, re
for f in glob.glob('/Users/aaronnguyen/TN/App/Clone Truyen/tehi-theme/*.php'):
    with open(f, 'r') as file:
        content = file.read()
    new_content = re.sub(r'(<main[^>]*class="[^"]*)\bpt-24\b', r'\1pt-20', content)
    if new_content != content:
        with open(f, 'w') as file:
            file.write(new_content)
        print(f"Fixed {f}")
