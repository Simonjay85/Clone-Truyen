import ftplib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, help='Upload a specific file')
args = parser.parse_args()

files_to_upload = [
    ("tehi-theme/header.php", "/wp-content/themes/tehi-theme/header.php"),
    ("tehi-theme/footer.php", "/wp-content/themes/tehi-theme/footer.php"),
    ("tehi-theme/functions.php", "/wp-content/themes/tehi-theme/functions.php"),
    ("tehi-theme/live_functions.php", "/wp-content/themes/tehi-theme/live_functions.php"),
    ("tehi-theme/single-truyen.php", "/wp-content/themes/tehi-theme/single-truyen.php"),
    ("tehi-theme/single-chuong.php", "/wp-content/themes/tehi-theme/single-chuong.php"),
    ("tehi-theme/index.php", "/wp-content/themes/tehi-theme/index.php"),
    ("tehi-theme/front-page.php", "/wp-content/themes/tehi-theme/front-page.php"),
    ("tehi-theme/header-home.php", "/wp-content/themes/tehi-theme/header-home.php"),
    ("tehi-theme/footer-home.php", "/wp-content/themes/tehi-theme/footer-home.php"),
    ("tehi-theme/assets/css/style.css", "/wp-content/themes/tehi-theme/assets/css/style.css"),
    ("tehi-theme/page-directory.php", "/wp-content/themes/tehi-theme/page-directory.php"),
    ("tehi-theme/page-completed.php", "/wp-content/themes/tehi-theme/page-completed.php"),
    ("tehi-theme/taxonomy-the_loai.php", "/wp-content/themes/tehi-theme/taxonomy-the_loai.php"),
    ("tehi-theme/live_taxonomy-the_loai.php", "/wp-content/themes/tehi-theme/live_taxonomy-the_loai.php"),
    ("tehi-theme/page-bangxephang.php", "/wp-content/themes/tehi-theme/page-bangxephang.php"),
    ("tehi-theme/page-bxh.php", "/wp-content/themes/tehi-theme/page-bxh.php"),
    ("tehi-theme/page-latest.php", "/wp-content/themes/tehi-theme/page-latest.php"),
    ("tehi-theme/page-profile.php", "/wp-content/themes/tehi-theme/page-profile.php"),
    ("tehi-theme/search.php", "/wp-content/themes/tehi-theme/search.php"),
    ("temply-ai-factory/includes/backfill.php", "/wp-content/plugins/temply-ai-factory/includes/backfill.php"),
]

if args.file:
    # Just upload the specific file
    files_to_upload = [(args.file, f"/wp-content/themes/tehi-theme/{args.file.split('/')[-1]}")]

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    for local, remote in files_to_upload:
        try:
            parts = remote.rsplit("/", 1)
            ftp.cwd("/")
            if len(parts) > 1:
                for folder in parts[0][1:].split('/'):
                    try:
                        ftp.cwd(folder)
                    except:
                        pass
            with open(local, 'rb') as f:
                ftp.storbinary(f'STOR {parts[1]}', f)
            print(f"✓ {local}")
        except Exception as file_e:
            print(f"Bỏ qua {local} vì lỗi {file_e}")
    ftp.quit()
    print("Upload completed!")
except Exception as e:
    print(f"Lỗi: {e}")
