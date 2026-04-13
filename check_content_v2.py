import mysql.connector
import os
import re

def get_db_creds():
    try:
        with open('wp-config.php', 'r') as f:
            content = f.read()
            db_name = re.search(r"define\(\s*'DB_NAME',\s*'([^']+)'\s*\);", content).group(1)
            db_user = re.search(r"define\(\s*'DB_USER',\s*'([^']+)'\s*\);", content).group(1)
            db_pass = re.search(r"define\(\s*'DB_PASSWORD',\s*'([^']+)'\s*\);", content).group(1)
            db_host = re.search(r"define\(\s*'DB_HOST',\s*'([^']+)'\s*\);", content).group(1)
            return db_name, db_user, db_pass, db_host
    except Exception:
        return None

creds = get_db_creds()
if creds:
    db_name, db_user, db_pass, db_host = creds
    try:
        conn = mysql.connector.connect(host=db_host, user=db_user, password=db_pass, database=db_name)
        cursor = conn.cursor(dictionary=True)
        
        # Check 'chuong-1' content
        cursor.execute("SELECT ID, post_title, post_status, post_content FROM wp_posts WHERE post_name='chuong-1' OR post_title LIKE '%Chương 1%' LIMIT 1")
        row = cursor.fetchone()
        if row:
            print(f"ID: {row['ID']}")
            print(f"Title: {row['post_title']}")
            print(f"Status: {row['post_status']}")
            print(f"Content Length: {len(row['post_content'])}")
            print(f"First 200 chars: {repr(row['post_content'][:200])}")
        else:
            print("Chapter not found.")
        conn.close()
    except Exception as e:
        print(f"DB Error: {e}")
