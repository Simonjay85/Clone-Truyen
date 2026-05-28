#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_live_js.py — Download the live jQuery and SweetAlert JS files from the website to see what they contain.
"""

import requests

def main():
    urls = [
        "https://doctieuthuyet.com/wp-content/themes/tehi-theme/assets/js/jquery.min.js",
        "https://doctieuthuyet.com/wp-content/themes/tehi-theme/templates/module/sweetalert/sweetalert2.min.js"
    ]
    
    for url in urls:
        print(f"\nFetching: {url}")
        try:
            response = requests.get(url, timeout=30)
            print("Status Code:", response.status_code)
            print("Response Length:", len(response.content))
            print("First 100 chars:", response.text[:100])
            print("Last 100 chars:", response.text[-100:])
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
