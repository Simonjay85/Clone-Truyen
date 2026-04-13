import re
import os

path = "tehi-theme/single-chuong.php"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the broken CSS
content = content.replace('. {\n                        display: none;\n                    }', '')

# Wait, if there are scripts causing Uncaught SyntaxError: Unexpected token ')'
# Let's search for "});" in the file where there might be a dangling parenthesis.
# I already fixed the double slideToggle duplicate, but maybe there's a dangling ')' somewhere else.
    
# Let's check for dangling close parens:
content_lines = content.split('\n')
for i, line in enumerate(content_lines):
    if '});' in line and len(line.strip()) <= 4:
        # It's a risk to just delete, so let's check
        pass

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
