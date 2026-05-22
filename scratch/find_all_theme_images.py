import os

root_dir = "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme"
matches = []

for root, dirs, files in os.walk(root_dir):
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        if ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']:
            full_path = os.path.join(root, f)
            size_kb = os.path.getsize(full_path) / 1024
            matches.append((os.path.relpath(full_path, root_dir), size_kb))

print(f"Found {len(matches)} image files in theme:")
for rel_path, size in matches:
    print(f"File: {rel_path} -> {size:.2f} KB")
