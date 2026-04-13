from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get("https://tehitruyen.com/trieu-dinh-khong-dung-nu-nhan-ta-la-ngoai-le.html?chuong=1", headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

print(len(soup.text))
c1 = soup.find('div', id='noi_dung_truyen')
if c1: print("Found id=noi_dung_truyen")

c2 = soup.select_one('.mdv-chapter-noidung')
if c2: print("Found .mdv-chapter-noidung")

