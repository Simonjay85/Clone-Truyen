import re

with open('/Users/aaronnguyen/TN/App/Clone Truyen/tehi-theme/page-story-studio.php', 'r') as f:
    lines = f.readlines()

stack = []
for i, line in enumerate(lines):
    if '<!--' in line and '-->' in line:
        pass
    else:
        tags = re.findall(r'<(/?div[^>]*)>', line)
        for t in tags:
            if t.startswith('/div'):
                if not stack:
                    print(f"Extra closing div on line {i+1}")
                else:
                    stack.pop()
            else:
                stack.append(i+1)

print(f"Remaining open divs: {stack}")
