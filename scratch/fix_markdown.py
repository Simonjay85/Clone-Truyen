import re

with open('danh_gia_truyen_2025-05-25.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    
    # 1. Fix MD038: spaces inside code span elements
    # `n ` -> `n` with space
    line = line.replace('`n `', '`n` (kèm khoảng trắng)')
    
    # 2. Fix MD049: asterisks for emphasis on line 342
    if 'Báo cáo được tạo tự động bởi script đánh giá' in line:
        line = line.replace('*', '_')
        if not line.rstrip().endswith('.'):
            # add period at the end to avoid MD036 (emphasis as heading)
            line = line.replace('\n', '.\n')

    # 3. Wrap bare URLs in <...>
    # Match doctieuthuyet.com URLs not already wrapped in <...> or [...]
    def wrap_url(match):
        url = match.group(0)
        start_idx = match.start()
        # check if it's already wrapped in <...> or (...)
        before = line[max(0, start_idx-1):start_idx]
        after = line[match.end():match.end()+1]
        if before == '<' and after == '>':
            return url
        if before == '(' and after == ')':
            return url
        if before == '"' or before == "'":
            return url
        return f"<{url}>"

    line = re.sub(r'https?://[^\s\)]+', wrap_url, line)
    
    # Fix spaces at the end of lines
    # Some lines have double trailing space for line break, which is fine,
    # but let's make sure we don't mess it up.
    
    new_lines.append(line)
    
    # 4. Fix MD022: blanks around headings
    # If the line is a heading, ensure the next line (if any) is empty
    if line.startswith('#'):
        # Check if next line is not empty and not already a heading or divider
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line and not next_line.startswith('#') and not next_line.startswith('---'):
                new_lines.append('\n')
                
    i += 1

# Let's write the intermediate result
content = "".join(new_lines)

# 5. Fix MD058 & MD032: blanks around tables and lists
# Make sure tables are preceded and followed by empty lines
# A table row starts with | and contains |
# We'll split the content by lines and inspect
content_lines = content.split('\n')
final_lines = []
for idx, l in enumerate(content_lines):
    is_table = l.strip().startswith('|')
    is_prev_table = content_lines[idx-1].strip().startswith('|') if idx > 0 else False
    is_next_table = content_lines[idx+1].strip().startswith('|') if idx+1 < len(content_lines) else False
    
    # If it is the start of a table
    if is_table and not is_prev_table:
        # check if the previous line is not empty
        if final_lines and final_lines[-1].strip() != '':
            final_lines.append('')
            
    # Add the current line
    final_lines.append(l)
    
    # If it is the end of a table
    if is_table and not is_next_table:
        # check if next line in content_lines is not empty
        if idx+1 < len(content_lines) and content_lines[idx+1].strip() != '':
            final_lines.append('')

# Format list padding for MD032 (Lists should be surrounded by blank lines)
# A list item starts with - or *
temp_lines = []
for idx, l in enumerate(final_lines):
    stripped = l.strip()
    is_list = stripped.startswith('- ') or stripped.startswith('* ') or re.match(r'^\d+\.\s', stripped)
    is_prev_list = temp_lines[-1].strip().startswith('- ') or temp_lines[-1].strip().startswith('* ') or re.match(r'^\d+\.\s', temp_lines[-1].strip()) if temp_lines else False
    
    is_next_list = False
    if idx+1 < len(final_lines):
        ns = final_lines[idx+1].strip()
        is_next_list = ns.startswith('- ') or ns.startswith('* ') or re.match(r'^\d+\.\s', ns)
        
    if is_list and not is_prev_list:
        if temp_lines and temp_lines[-1].strip() != '' and not temp_lines[-1].strip().startswith('###') and not temp_lines[-1].strip().startswith('##'):
            temp_lines.append('')
            
    temp_lines.append(l)
    
    if is_list and not is_next_list:
        if idx+1 < len(final_lines) and final_lines[idx+1].strip() != '':
            temp_lines.append('')

# Clean up any multiple consecutive blank lines
cleaned_lines = []
for l in temp_lines:
    if l.strip() == '':
        if not cleaned_lines or cleaned_lines[-1].strip() != '':
            cleaned_lines.append('')
    else:
        cleaned_lines.append(l)

# Let's format the markdown table cells spacing for MD060
# A table column format is | cell | cell |
# If there are missing spaces, we can clean them up.
for idx, l in enumerate(cleaned_lines):
    if l.strip().startswith('|'):
        parts = l.split('|')
        # Check if the second part is just dashes (like |---|---| or | --- | --- |)
        is_divider = all(c in '-:' for c in parts[1].strip()) if len(parts) > 2 else False
        if is_divider:
            # Format as | --- | --- |
            new_parts = ['']
            for p in parts[1:-1]:
                new_parts.append(' --- ')
            new_parts.append('')
            cleaned_lines[idx] = '|'.join(new_parts)
        else:
            # Format with spaces inside cells: | content | content |
            new_parts = ['']
            for p in parts[1:-1]:
                # strip space and re-add one space padding
                sp = p.strip()
                new_parts.append(f" {sp} ")
            new_parts.append('')
            cleaned_lines[idx] = '|'.join(new_parts)

with open('danh_gia_truyen_2025-05-25.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(cleaned_lines) + '\n')

print("Markdown Fixed successfully!")
