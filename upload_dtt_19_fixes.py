import ftplib
import os
import re
from datetime import datetime


FILES_TO_UPLOAD = [
    ("tehi-theme/header.php", "/wp-content/themes/tehi-theme/header.php"),
    ("tehi-theme/functions.php", "/wp-content/themes/tehi-theme/functions.php"),
    ("tehi-theme/footer.php", "/wp-content/themes/tehi-theme/footer.php"),
    ("tehi-theme/front-page.php", "/wp-content/themes/tehi-theme/front-page.php"),
    ("tehi-theme/single-chuong.php", "/wp-content/themes/tehi-theme/single-chuong.php"),
    ("tehi-theme/single-truyen.php", "/wp-content/themes/tehi-theme/single-truyen.php"),
    ("tehi-theme/assets/css/style-mongdaovien.css", "/wp-content/themes/tehi-theme/assets/css/style-mongdaovien.css"),
    ("temply-ai-factory/temply-ai-factory.php", "/wp-content/plugins/temply-ai-factory/temply-ai-factory.php"),
    ("temply-ai-factory/includes/backfill.php", "/wp-content/plugins/temply-ai-factory/includes/backfill.php"),
]


def load_existing_ftp_credentials():
    """Reuse the existing repo FTP configuration without duplicating secrets here."""
    with open("upload_fixes.py", "r", encoding="utf-8") as handle:
        source = handle.read()

    host_match = re.search(r'ftplib\.FTP\("([^"]+)"\)', source)
    login_match = re.search(r'ftp\.login\("([^"]+)",\s*"([^"]+)"\)', source)
    if not host_match or not login_match:
        raise RuntimeError("Cannot find FTP credentials in existing upload_fixes.py")

    return host_match.group(1), login_match.group(1), login_match.group(2)


def ensure_cwd(ftp, remote_dir):
    ftp.cwd("/")
    for part in remote_dir.strip("/").split("/"):
        if not part:
            continue
        try:
            ftp.cwd(part)
        except ftplib.error_perm:
            ftp.mkd(part)
            ftp.cwd(part)


def backup_remote_file(ftp, remote_path, backup_root):
    local_backup = os.path.join(backup_root, remote_path.lstrip("/"))
    os.makedirs(os.path.dirname(local_backup), exist_ok=True)
    remote_dir, filename = remote_path.rsplit("/", 1)
    try:
        ensure_cwd(ftp, remote_dir)
        with open(local_backup, "wb") as handle:
            ftp.retrbinary(f"RETR {filename}", handle.write)
        print(f"backup {remote_path} -> {local_backup}")
    except ftplib.error_perm as exc:
        print(f"backup skip {remote_path}: {exc}")


def upload_file(ftp, local_path, remote_path):
    remote_dir, filename = remote_path.rsplit("/", 1)
    ensure_cwd(ftp, remote_dir)
    with open(local_path, "rb") as handle:
        ftp.storbinary(f"STOR {filename}", handle)
    print(f"upload {local_path} -> {remote_path}")


def main():
    missing = [local for local, _ in FILES_TO_UPLOAD if not os.path.exists(local)]
    if missing:
        raise RuntimeError("Missing local files: " + ", ".join(missing))

    host, username, password = load_existing_ftp_credentials()
    backup_root = os.path.join("/private/tmp", "dtt_ftp_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S"))

    ftp = ftplib.FTP(host, timeout=30)
    try:
        ftp.login(username, password)
        for _, remote_path in FILES_TO_UPLOAD:
            backup_remote_file(ftp, remote_path, backup_root)
        for local_path, remote_path in FILES_TO_UPLOAD:
            upload_file(ftp, local_path, remote_path)
    finally:
        ftp.quit()

    print("done")
    print("backup_dir:", backup_root)


if __name__ == "__main__":
    main()
