const fs = require('fs');

const files = [
  'src/components/GrokDramaView.tsx',
  'src/components/ClaudeDramaView.tsx',
  'src/components/ComboEconomicView.tsx',
  'src/components/ComboRoyalView.tsx'
];

files.forEach(file => {
  if (!fs.existsSync(file)) return;
  
  let content = fs.readFileSync(file, 'utf8');
  
  // Extract the draftSpaces block
  const draftRegex = /  const draft = draftSpaces\['.*?'\] \|\| \{\};\n\n  React\.useEffect\(\(\) => \{[\s\S]*?\}, \[title, prompt, targetChapters, pitchOptions, gradingStatus\]\);\n/;
  const match = content.match(draftRegex);
  
  if (match) {
    // Remove it from its current position
    content = content.replace(draftRegex, '');
    
    // Find the end of useState declarations. We can just insert it right before "const toggleGenre =" or "const handleGenerateOutline ="
    // Since some files have toggleGenre and others don't, we can just find "  const handle" or "  const toggleGenre"
    if (content.includes('  const toggleGenre = ')) {
      content = content.replace('  const toggleGenre = ', match[0] + '\n  const toggleGenre = ');
    } else if (content.includes('  const handleGenerate')) {
      content = content.replace('  const handleGenerate', match[0] + '\n  const handleGenerate');
    } else {
      // Fallback: just put it right before "return ("
      content = content.replace('  return (', match[0] + '\n  return (');
    }
    
    fs.writeFileSync(file, content);
    console.log(`Fixed ${file}`);
  }
});
