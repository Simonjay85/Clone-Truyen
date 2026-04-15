import re

with open('page-bxh.php', 'r') as f:
    text = f.read()

# Replace custom color classes with standard tailwind classes
replacements = {
    'bg-primary/10': 'bg-blue-600/10',
    'bg-primary': 'bg-blue-600',
    'text-primary': 'text-blue-600',
    'border-primary': 'border-blue-600',
    'border-primary/20': 'border-blue-600/20',
    'border-primary/30': 'border-blue-600/30',
    'border-primary/50': 'border-blue-600/50',
    'shadow-primary': 'shadow-blue-600',
    'from-primary': 'from-blue-600',
    
    'bg-surface-container-low': 'bg-gray-100',
    'bg-surface-container-highest': 'bg-gray-50',
    'bg-surface-container-lowest': 'bg-white',
    
    'text-on-surface-variant': 'text-gray-500',
    'text-on-surface': 'text-gray-900',
    
    'text-outline-variant': 'text-gray-400',
    'border-outline-variant/10': 'border-gray-200',
    'border-outline-variant/20': 'border-gray-200',
    'border-outline-variant/30': 'border-gray-300',
}

for old, new in replacements.items():
    text = text.replace(old, new)

# And let's make the active Time tab stand out more by adding bg-blue-600 text-white
text = text.replace("echo $active ? 'bg-white shadow-[0_2px_8px_rgba(0,0,0,0.06)] text-blue-600", "echo $active ? 'bg-blue-600 shadow-[0_2px_8px_rgba(0,0,0,0.06)] text-white")

# Also the top buttons active state
# 'bg-blue-600 text-white border-blue-600 shadow-md shadow-blue-600/20' is already formed!

with open('page-bxh.php', 'w') as f:
    f.write(text)

print("Color patch applied.")
