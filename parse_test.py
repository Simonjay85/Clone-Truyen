from bs4 import BeautifulSoup
with open('test_novel.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

title = soup.find('div', class_='mdv-san-pham-show-name')
print("Title:", title.text.strip() if title else "NOT FOUND")

intro = soup.select_one('.mdv-san-pham-show-dsc-noidung-full')
print("Intro length:", len(intro.text) if intro else "NOT FOUND")

chapters = []
for a in soup.select('.mdv-san-pham-show-dsc-table-chuong a'):
    chapters.append(a.text.strip())
print(len(chapters), "chapters found:", chapters[:3])
