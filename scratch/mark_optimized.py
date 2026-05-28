import openpyxl
import json

wb = openpyxl.load_workbook("danh_sach_truyen_doctieuthuyet.xlsx")
ws = wb.active

with open("scratch/story_categories.json", "r", encoding="utf-8") as f:
    categories = json.load(f)

# Mark all "mark_only" stories as fixed
count = 0
for entry in categories["mark_only"]:
    row = entry["row"]
    ws.cell(row=row, column=14).value = "☑️ Đã sửa"
    count += 1
    print(f"  ✅ STT {entry['stt']} — ID={entry['id']} — {entry['title'][:60]}")

wb.save("danh_sach_truyen_doctieuthuyet.xlsx")
print(f"\n✅ Đánh dấu {count} truyện đã tối ưu 10/10 thành '☑️ Đã sửa'")
