import hashlib

file_local = "/Users/aaronnguyen/TN/App/doctieuthuyet/tehi-theme/front-page.php"
file_remote = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/remote_front-page.php"

with open(file_local, "r", encoding="utf-8") as f:
    local_content = f.read()

with open(file_remote, "r", encoding="utf-8") as f:
    remote_content = f.read()

local_md5 = hashlib.md5(local_content.encode('utf-8')).hexdigest()
remote_md5 = hashlib.md5(remote_content.encode('utf-8')).hexdigest()

print(f"Local front-page.php size:  {len(local_content)} bytes, MD5: {local_md5}")
print(f"Remote front-page.php size: {len(remote_content)} bytes, MD5: {remote_md5}")

if local_md5 == remote_md5:
    print("✅ The live front-page.php matches the local front-page.php!")
else:
    print("⚠️ MISMATCH! Live and local front-page.php are different.")
    # Check what is different
    local_lines = local_content.splitlines()
    remote_lines = remote_content.splitlines()
    
    print(f"Local has {len(local_lines)} lines.")
    print(f"Remote has {len(remote_lines)} lines.")
    
    # Print the first few differences
    diff_count = 0
    for idx, (l, r) in enumerate(zip(local_lines, remote_lines)):
        if l != r:
            print(f"\nLine {idx+1} is different:")
            print(f"  Local:  {repr(l)}")
            print(f"  Remote: {repr(r)}")
            diff_count += 1
            if diff_count >= 10:
                print("... truncated more differences ...")
                break
