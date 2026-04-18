files = [
    ("src/components/MicroDramaView.tsx", "gpt-4o-mini"),
    ("src/components/GeminiDramaView.tsx", "gemini-2.5-flash"),
    ("src/components/GrokDramaView.tsx", "grok-base"),
    ("src/components/ClaudeDramaView.tsx", "claude-3-5-sonnet"),
    ("src/components/ComboEconomicView.tsx", "gemini-2.5-flash"),
    ("src/components/ComboRoyalView.tsx", "claude-3-5-sonnet")
]

for p, default_mod in files:
    with open(p, "r") as f:
        c = f.read()

    # The hardcoded model line to replace
    # We want to replace exactly the `model: 'gpt-4o-mini'` inside the fetch body
    # Let's replace precisely "model: 'gpt-4o-mini'" with "model: selectedModel || '...'"
    
    # Wait, earlier I might have blindly copied it, but let's check if it exists in all
    c = c.replace("model: 'gpt-4o-mini'", f"model: selectedModel || '{default_mod}'")
    
    with open(p, "w") as f:
        f.write(c)
    print("Fixed model in", p)

