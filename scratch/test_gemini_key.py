import requests

GEMINI_KEY = "AIzaSyDD7JDTkTp9872jQkKGT2A6PPOhfp5M4Q4"

def main():
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": "Hello, write a one sentence greeting in Vietnamese."}
                ]
            }
        ]
    }
    try:
        res = requests.post(url, json=payload, headers=headers, timeout=10)
        print("Status:", res.status_code)
        print("Response:", res.text)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
