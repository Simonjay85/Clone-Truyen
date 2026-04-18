import re

with open("src/components/SettingsView.tsx", "r") as f:
    text = f.read()

# We need to remove the first injected <div> from "return (" to the start of the old content.
# The old content started with `<div className="max-w-4xl mx-auto py-10`

idx1 = text.find('return (\n    <div className="max-w-7xl mx-auto py-10 animation-fade-in flex flex-col h-[calc(100vh-80px)] px-4">')
idx2 = text.find('<div className="max-w-4xl mx-auto py-10 animation-fade-in space-y-6">')

if idx1 != -1 and idx2 != -1:
    injected_ui = text[idx1:idx2]
    old_ui = text[idx2:]
    
    # Now we need to wrap the old_ui inside the keys tab of injected_ui
    # The end of injected_ui is `<div className={activeTab === 'keys' ? 'block' : 'hidden'}>\n           {/* OLD SETTINGS RESTORED */}`
    
    # Fix the old_ui: replace its root `<div>` with just `<div className="space-y-6">`
    old_ui = old_ui.replace('<div className="max-w-4xl mx-auto py-10 animation-fade-in space-y-6">', '<div className="space-y-6">', 1)
    
    # We must remove the very last closing tags of old_ui, which are `</div>\n    </div>\n  );\n}`
    # Actually just `</div>\n  );\n}` or `</div>\n</div>\n  );\n}`
    old_ui = re.sub(r'</div>\s*</div>\s*\);\s*}', '', old_ui)
    
    # Assemble
    final_text = text[:idx1] + injected_ui + old_ui + '\n        </div>\n      </div>\n    </div>\n  );\n}\n'
    
    with open("src/components/SettingsView.tsx", "w") as f:
        f.write(final_text)
    print("Fixed syntax error")
else:
    print("Could not find patterns")

