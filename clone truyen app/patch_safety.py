import re
import os

files = [
    'src/components/MicroDramaView.tsx',
    'src/components/GeminiDramaView.tsx',
    'src/components/GrokDramaView.tsx',
    'src/components/ClaudeDramaView.tsx'
]

def safe_replace(match):
    val = match.group(1)
    return f"{{typeof {val} === 'object' ? JSON.stringify({val}) : {val}}}"

for filepath in files:
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Replace {pitch.suggestedGenres}
    content = re.sub(r'\{([A-Za-z0-9_.]*pitch\.suggestedGenres[A-Za-z0-9_.]*)\}', safe_replace, content)
    # Replace {pitch.suggestedChapters}
    content = re.sub(r'\{([A-Za-z0-9_.]*pitch\.suggestedChapters[A-Za-z0-9_.]*)\}', safe_replace, content)
    # Replace title={...} rendering inside <td>...</td>
    content = re.sub(r'\{(item\.pitch\.super_title \|\| item\.pitch\.protagonist)\}', safe_replace, content)
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Patched {filepath}")
