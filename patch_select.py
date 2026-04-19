import os
import ftplib

files_to_patch = [
    "tehi-theme/page-directory.php",
    "tehi-theme/taxonomy-the_loai.php",
    "tehi-theme/page-completed.php"
]

for file_path in files_to_patch:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Change text-gray-500 to text-gray-700 in paragraphs
    content = content.replace('p class="text-gray-500 text-lg font-medium', 'p class="text-gray-700 text-lg font-medium')
    
    # 2. Fix the select dropdown (replace BETA and fix layout)
    old_select = """<select class="bg-gray-50 border-none text-gray-900 text-sm rounded-lg focus:ring-blue-500 block w-full p-2 font-semibold ring-1 ring-gray-200">
                        <option>Mới cập nhật</option>
                        <option disabled>Xem nhiều (BETA)</option>
                    </select>"""
    
    # For page-completed.php it's slightly different:
    old_select_comp = """<select class="bg-transparent border-none focus:ring-0 text-primary cursor-pointer font-bold outline-none -ml-1">
                        <option>Mới cập nhật</option>
                        <option disabled>Lượt xem nhiều</option>
                    </select>"""

    new_select = """<select class="mkm-native-select bg-gray-50 border-none text-gray-900 text-sm rounded-lg focus:ring-blue-500 block w-full py-2 px-3 font-semibold ring-1 ring-gray-200" style="appearance: auto; -webkit-appearance: auto;">
                        <option>Mới cập nhật</option>
                        <option>Xem nhiều</option>
                    </select>
                    <style>.mkm-native-select { display: block !important; } .mkm-native-select + .nice-select, .mkm-native-select + .select2-container { display: none !important; }</style>"""

    new_select_comp = """<select class="mkm-native-select bg-transparent border-none focus:ring-0 text-primary cursor-pointer font-bold outline-none -ml-1" style="appearance: auto; -webkit-appearance: auto;">
                        <option>Mới cập nhật</option>
                        <option>Lượt xem nhiều</option>
                    </select>
                    <style>.mkm-native-select { display: inline-block !important; } .mkm-native-select + .nice-select, .mkm-native-select + .select2-container { display: none !important; }</style>"""

    if old_select in content:
        content = content.replace(old_select, new_select)
    elif old_select_comp in content:
        content = content.replace(old_select_comp, new_select_comp)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# FTP Upload
try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    remote_dir = "/wp-content/themes/tehi-theme"
    try:
        ftp.cwd(remote_dir)
    except:
        pass
        
    for local_file in files_to_patch:
        filename = os.path.basename(local_file)
        with open(local_file, 'rb') as f:
            ftp.storbinary(f'STOR {filename}', f)
        print(f"Uploaded {filename}")
        
    ftp.quit()
    print("Done uploading fixes.")
except Exception as e:
    print("Error:", e)

