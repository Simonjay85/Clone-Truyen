const fs = require('fs');
const glob = require('glob'); // Use generic traversal or manual fs.readdirSync if glob not available
const files = fs.readdirSync('./src/components').filter(f => f.endsWith('View.tsx') || f.includes('Drama'));

for (let file of files) {
  let path = './src/components/' + file;
  let content = fs.readFileSync(path, 'utf8');

  // Replace hook destructuring to ensure we get the additional keys
  if (!content.includes('geminiPaidKey')) {
      content = content.replace(
        /const\s+{\s*([^}]+)\s*}\s*=\s*useStore\(\);/,
        "const { $1, geminiKey, geminiKey2, geminiKey3, geminiPaidKey, usePaidAPI } = useStore();"
      );
  }

  // Add the key resolver variables
  if (!content.includes('const resolvedGKey1')) {
     content = content.replace(
        /const\s+\[refineFeedback/g,
        `const resolvedGKey1 = (usePaidAPI && geminiPaidKey) ? geminiPaidKey : geminiKey;
  const resolvedGKey2 = (usePaidAPI && geminiPaidKey) ? undefined : geminiKey2;
  const resolvedGKey3 = (usePaidAPI && geminiPaidKey) ? undefined : geminiKey3;
  const [refineFeedback`
     );
  }

  // Find all /api/gemini fetch bodies and replace their keys
  content = content.replace(/apiKey:\s*geminiKey\s*,/g, "apiKey: resolvedGKey1,\n              apiKey2: resolvedGKey2,\n              apiKey3: resolvedGKey3,");
  
  // Find agentConceptScorer and agentPitchRefiner calls
  content = content.replace(/agentConceptScorer\('gemini',\s*geminiKey,\s*([^,]+),\s*([^\)]+)\)/g, "agentConceptScorer('gemini', resolvedGKey1, $1, $2, resolvedGKey2, resolvedGKey3)");
  content = content.replace(/agentPitchRefiner\('gemini',\s*geminiKey,\s*([^,]+),\s*([^,]+),\s*([^\)]+)\)/g, "agentPitchRefiner('gemini', resolvedGKey1, $1, $2, $3, resolvedGKey2, resolvedGKey3)");

  fs.writeFileSync(path, content);
  console.log('Patched', path);
}
