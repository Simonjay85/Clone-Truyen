import re

with open("tehi-theme/single-chuong.php", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Make the 'x' button more prominent
code = code.replace(
    '<button id="closeSettings" class="w-8 h-8 rounded-full hover:bg-surface-container-high flex items-center justify-center text-on-surface-variant transition-colors"><span class="material-symbols-outlined text-sm">close</span></button>',
    '<button id="closeSettings" class="w-8 h-8 rounded-full bg-surface-container-high hover:bg-red-500 hover:text-white flex items-center justify-center text-on-surface transition-colors shadow-sm"><span class="material-symbols-outlined text-lg font-bold">close</span></button>'
)

# 2. Add click-outside logic to JS
click_outside_js = """
    // Close settings when clicking outside
    document.addEventListener('click', (event) => {
        const isClickInsidePanel = settingsPanel.contains(event.target);
        const isClickOnToggle = toggleSettingsBtn && toggleSettingsBtn.contains(event.target);
        
        if (!isClickInsidePanel && !isClickOnToggle && !settingsPanel.classList.contains('hidden')) {
            settingsPanel.classList.add('hidden');
        }
    });
"""

# Insert click_outside_js right after where we added the close logic
# "const closeSettings = document.getElementById('closeSettings');\n    if(closeSettings) closeSettings.addEventListener('click', () => settingsPanel.classList.add('hidden'));"

target = "if(closeSettings) closeSettings.addEventListener('click', () => settingsPanel.classList.add('hidden'));"
new_target = target + "\n" + click_outside_js

code = code.replace(target, new_target)

with open("tehi-theme/single-chuong.php", "w", encoding="utf-8") as f:
    f.write(code)

print("Added click outside and highlighted X")
