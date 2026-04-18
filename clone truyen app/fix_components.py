import re
import os

files = [
    'src/components/GrokDramaView.tsx',
    'src/components/ClaudeDramaView.tsx',
    'src/components/ComboEconomicView.tsx',
    'src/components/ComboRoyalView.tsx'
]

draft_pattern = re.compile(r"  const draft = draftSpaces\['.*?'\] \|\| \{\};\n\n  React\.useEffect\(\(\) => \{[\s\S]*?\}, \[title, prompt, targetChapters, pitchOptions, gradingStatus\]\);\n")

for filepath in files:
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r') as f:
        content = f.read()
        
    match = draft_pattern.search(content)
    if match:
        block = match.group(0)
        content = content.replace(block, "")
        
        if "  const toggleGenre =" in content:
            content = content.replace("  const toggleGenre =", block + "\n  const toggleGenre =")
        elif "  const handleGenerateOutline =" in content:
            content = content.replace("  const handleGenerateOutline =", block + "\n  const handleGenerateOutline =")
        else:
            content = content.replace("  return (", block + "\n  return (")
            
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Fixed {filepath}")
