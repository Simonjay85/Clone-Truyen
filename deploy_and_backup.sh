#!/bin/bash

# Configuration
THEME_DIR="tehi-theme"
BACKUP_DIR="backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="${BACKUP_DIR}/tehi-theme_backup_${TIMESTAMP}.zip"

# Create backups directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

echo "=========================================="
echo "🚀 Bắt đầu quá trình Backup & Upload Theme"
echo "=========================================="

echo "[1/3] Đang nén thư mục $THEME_DIR..."
# Zip the theme folder, excluding node_modules/git/etc
zip -qr "$BACKUP_FILE" "$THEME_DIR" -x "*.DS_Store" "*node_modules*" "*.git*"

if [ $? -eq 0 ]; then
    echo "✅ Backup thành công: $BACKUP_FILE"
    
    # Also commit to Git as a secondary backup
    echo "[2/3] Đang lưu Snapshot vào Git..."
    git add .
    git commit -m "Auto-backup trước khi Deploy - $TIMESTAMP" > /dev/null 2>&1
    echo "✅ Snapshot Git đã lưu!"

    echo "[3/3] Đang Upload nguyên liệu lên Server..."
    # Call the python upload script
    python3 upload_theme_files.py
    
    if [ $? -eq 0 ]; then
        echo "=========================================="
        echo "🎉 Xong! Website đã được cập nhật an toàn."
        echo "Nếu có lỗi, hãy giải nén lại file $BACKUP_FILE để khôi phục."
        echo "=========================================="
    else
        echo "❌ Lỗi: Upload thất bại!"
    fi
else
    echo "❌ Lỗi: Không thể nén thư mục $THEME_DIR. Đã huỷ Upload để bảo vệ dữ liệu."
    exit 1
fi
