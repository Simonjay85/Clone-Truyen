from bs4 import BeautifulSoup
import sys

with open('/Users/aaronnguyen/TN/App/Clone Truyen/tehi-theme/page-story-studio.php', 'r') as f:
    html = f.read()

# Only analyze the part after the first <body> tag of the studio (ignore auth wall)
parts = html.split('<body>')
if len(parts) > 2:
    html = parts[2]
else:
    html = parts[1]

soup = BeautifulSoup(html, 'html.parser')
layout = soup.find('div', class_='studio-layout')
if layout:
    # See what elements are in layout
    children = [child.name for child in layout.children if child.name]
    print(f"Children of studio-layout: {children}")
else:
    print("studio-layout not found")

