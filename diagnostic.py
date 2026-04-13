import mysql.connector
import os
import re

# Since I can't run WP/PHP, I'll try to find the DB credentials from wp-config.php
def get_db_creds():
    try:
        with open('wp-config.php', 'r') as f:
            content = f.read()
            db_name = re.search(r"define\(\s*'DB_NAME',\s*'([^']+)'\s*\);", content).group(1)
            db_user = re.search(r"define\(\s*'DB_USER',\s*'([^']+)'\s*\);", content).group(1)
            db_pass = re.search(r"define\(\s*'DB_PASSWORD',\s*'([^']+)'\s*\);", content).group(1)
            db_host = re.search(r"define\(\s*'DB_HOST',\s*'([^']+)'\s*\);", content).group(1)
            return db_name, db_user, db_pass, db_host
    except Exception as e:
        print(f"Error reading wp-config: {e}")
        return None

creds = get_db_creds()
if creds:
    db_name, db_user, db_pass, db_host = creds
    try:
        conn = mysql.connector.connect(host=db_host, user=db_user, password=db_pass, database=db_name)
        cursor = conn.cursor(dictionary=True)
        
        # Check a sample chapter
        cursor.execute("SELECT ID, post_title, post_type, post_content FROM wp_posts WHERE post_type='chuong' LIMIT 1")
        row = cursor.fetchone()
        if row:
            print(f"Chapter ID: {row['ID']}")
            print(f"Title: {row['post_title']}")
            print(f"Content Length: {len(row['post_content'])}")
            print(f"Content Start: {row['post_content'][:100]}")
            
            # Check meta
            cursor.execute("SELECT meta_key, meta_value FROM wp_postmeta WHERE post_id=%s", (row['ID'],))
            metas = cursor.fetchall()
            print("Metas:")
            for m in metas:
                print(f"  {m['meta_key']}: {m['meta_value']}")
        else:
            print("No chapters found in DB.")
        
        conn.close()
    except Exception as e:
        print(f"DB Error: {e}")
else:
    print("Could not get DB credentials.")
