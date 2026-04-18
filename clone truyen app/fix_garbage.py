import re

files = [
    "src/components/MicroDramaView.tsx",
    "src/components/GeminiDramaView.tsx",
    "src/components/GrokDramaView.tsx",
    "src/components/ClaudeDramaView.tsx",
    "src/components/ComboEconomicView.tsx",
    "src/components/ComboRoyalView.tsx"
]

# The garbage usually looks like:
#                                 <div><h4 className="text-rose-400 font-bold mb-1 text-xs uppercase tracking-wide">...</h4><p>{pitch....}</p></div>
#                              </div>

for p in files:
    with open(p, "r") as f:
        c = f.read()

    # Find the end of the space-y-4 div normally:
    # it ends with closing the textarea block for overallSizzle, then </div> for the item, then </div> for the space-y-4.
    
    # Let's cleanly remove ANY loose <div><h4>...</h4><p>...</p></div> that sits alone right before {grading...
    # We can match `                             </div>\n\n\n                                <div><h4...`
    # and carefully strip everything between the end of the textareas and the `{grading` line.
    
    # A safe pattern: from `value={pitch.overallSizzle || ''} onChange={(e) => updatePitch(idx, 'overallSizzle', e.target.value)} />\n                                </div>\n                             </div>`
    # up to `\n                             {grading && grading.grading && (`
    
    pattern = r'(updatePitch\(idx,\s*\'overallSizzle\',\s*e\.target\.value\)\s*}\s*/>\s*</div>\s*</div>).*?(?=\s*\{grading && grading\.grading && \()'
    
    c_new = re.sub(pattern, r'\1', c, flags=re.DOTALL)
    
    if c_new != c:
        with open(p, "w") as f:
            f.write(c_new)
        print("Scrubbed garbage in " + p)
    else:
        print("No garbage in " + p)

