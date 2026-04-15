import re

files = ['page.php', 'page-library.php']

replacements = {
    'bg-primary/10': 'bg-blue-600/10',
    'bg-primary/5': 'bg-blue-600/5',
    'bg-primary': 'bg-blue-600',
    'text-primary': 'text-blue-600',
    'border-primary/20': 'border-blue-600/20',
    'border-primary': 'border-blue-600',
    'shadow-primary': 'shadow-blue-600',
    'from-primary': 'from-blue-600',
    'to-primary': 'to-blue-600',
    
    'bg-primary-container/30': 'bg-blue-100/30',
    'border-primary-container': 'border-blue-200',
    'from-primary-container': 'from-blue-100',
    'to-primary-container': 'to-blue-100',
    'text-primary-container': 'text-blue-200',
    
    'bg-secondary-container': 'bg-indigo-100',
    'bg-secondary-container/20': 'bg-indigo-100/20',
    'text-on-secondary-container': 'text-indigo-800',
    'to-tertiary-container': 'to-purple-100',
    
    'bg-surface-container-low': 'bg-gray-50',
    'bg-surface-container-highest': 'bg-gray-100',
    'bg-surface-container-lowest': 'bg-white',
    'bg-surface-container': 'bg-white',
    'bg-surface-variant/50': 'bg-gray-100',
    
    'text-on-surface-variant': 'text-gray-500',
    'text-on-surface': 'text-gray-900',
    'text-on-background': 'text-gray-900',
    
    'text-outline-variant': 'text-gray-300',
    'border-outline-variant/10': 'border-gray-200',
    'border-outline-variant/20': 'border-gray-200',
    'border-outline-variant/30': 'border-gray-300',
    'text-outline': 'text-gray-400',
}

for file in files:
    with open(file, 'r') as f:
        text = f.read()

    for old, new in replacements.items():
        text = text.replace(old, new)
        
    # Inject tailwind
    if "global $tehi_tailwind_page;" not in text:
        text = text.replace("get_header();", "global $tehi_tailwind_page;\n$tehi_tailwind_page = true;\nget_header();")

    with open(file, 'w') as f:
        f.write(text)

