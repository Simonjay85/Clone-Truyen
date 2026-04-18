files = [
    "src/components/MicroDramaView.tsx",
    "src/components/GeminiDramaView.tsx",
    "src/components/GrokDramaView.tsx",
    "src/components/ClaudeDramaView.tsx",
    "src/components/ComboEconomicView.tsx",
    "src/components/ComboRoyalView.tsx"
]

target_str = "                             {grading && grading.grading && ("
fixed_str = "                             </div>\n                             {grading && grading.grading && ("

for p in files:
    with open(p, "r") as f:
        c = f.read()
    
    # Simple check to avoid double-adding if there's already a </div> right before it.
    idx = c.find(target_str)
    if idx != -1:
        # Check the characters immediately preceding target_str
        preceding = c[max(0, idx - 20):idx]
        if "</div>" not in preceding:
            c = c.replace(target_str, fixed_str)
            with open(p, "w") as f:
                f.write(c)
            print("Fixed missing div in " + p)
        else:
            print("Already fixed in " + p)
