import argparse
import ftplib
from pathlib import Path


FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"


def ensure_dir(ftp, path):
    current = ""
    for part in path.strip("/").split("/"):
        current += "/" + part
        try:
            ftp.mkd(current)
        except Exception:
            pass


def upload_file(ftp, local_path, remote_path):
    remote_dir = str(Path(remote_path).parent).replace("\\", "/")
    ensure_dir(ftp, remote_dir)
    with open(local_path, "rb") as handle:
        ftp.storbinary(f"STOR {remote_path}", handle)
    print(f"Uploaded {remote_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cleanup", action="store_true")
    parser.add_argument("--covers-dir", default="generated_covers")
    args = parser.parse_args()

    ftp = ftplib.FTP(FTP_HOST, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)

    if args.cleanup:
        try:
            ftp.delete("/process_missing_cover_assets.php")
            print("Deleted /process_missing_cover_assets.php")
        except Exception as exc:
            print(f"Cleanup skipped: {exc}")
        ftp.quit()
        return

    for cover in sorted(Path(args.covers_dir).glob("*.jpg")):
        upload_file(ftp, cover, f"/wp-content/uploads/temp_covers/{cover.name}")

    for avatar in sorted(Path("tehi-theme/templates/images").glob("team*.jpeg")):
        upload_file(ftp, avatar, f"/wp-content/themes/tehi-theme/templates/images/{avatar.name}")

    upload_file(ftp, "tehi-theme/front-page.php", "/wp-content/themes/tehi-theme/front-page.php")
    upload_file(ftp, "process_missing_cover_assets.php", "/process_missing_cover_assets.php")

    ftp.quit()


if __name__ == "__main__":
    main()
