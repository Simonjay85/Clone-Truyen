import os

root_dir = "/Users/aaronnguyen/TN/App/doctieuthuyet"
matches = []

for root, dirs, files in os.walk(root_dir):
    for f in files:
        if "no-image-cover" in f or "no-image" in f:
            full_path = os.path.join(root, f)
            size_mb = os.path.getsize(full_path) / (1024 * 1024)
            matches.append((full_path, size_mb))

print(f"Found {len(matches)} files:")
for path, size in matches:
    print(f"Path: {path} -> Size: {size:.2f} MB")
