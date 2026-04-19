import os
import ftplib

files_to_patch = [
    "tehi-theme/page-directory.php",
    "tehi-theme/taxonomy-the_loai.php"
]

for file_path in files_to_patch:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Breadcrumb "Trang chủ"
    content = content.replace('text-gray-500 mb-4 uppercase', 'text-red-500 mb-4 uppercase')
    content = content.replace('hover:text-gray-900', 'hover:text-red-700')
    content = content.replace('text-blue-600 border-b border-blue-600/30">Danh mục', 'text-blue-500 border-b border-blue-500/30">Danh mục')

    # 2. Inactive Genre Chips
    content = content.replace('bg-gray-100 text-gray-500 hover:text-blue-600 hover:bg-blue-50', 'bg-gray-100 text-red-500 hover:text-red-600 hover:bg-red-50')
    
    # 3. Label "Trạng thái", "Sắp xếp", Checkboxes to red
    # Wait, earlier I replaced part of the TRẠNG THÁI chunk, so let's simplify:
    content = content.replace('text-gray-400 uppercase tracking-widest">Sắp xếp', 'text-red-500 uppercase tracking-widest">Sắp xếp')
    content = content.replace('text-gray-400 uppercase tracking-widest">Trạng thái', 'text-red-500 uppercase tracking-widest">Trạng thái')
    content = content.replace('text-gray-400 font-semibold', 'text-red-500 font-semibold')
    content = content.replace('text-blue-600 border-gray-300 focus:ring-blue-600', 'text-red-500 border-gray-300 focus:ring-red-500')

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
    print("Done uploading red text fixes.")
except Exception as e:
    print("Error:", e)
