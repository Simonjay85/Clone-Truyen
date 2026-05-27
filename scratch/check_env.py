import os
print("--- Environment Variables ---")
for k, v in os.environ.items():
    if "key" in k.lower() or "secret" in k.lower() or "auth" in k.lower() or "token" in k.lower():
        print(f"{k}: {v[:10]}...")
    else:
        print(f"{k}: {v}")
