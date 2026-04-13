import ftplib

# WordPress Nginx rewrite rules for the extension directory
WP_NGINX_CONF = """# WordPress rewrite rules
location / {
    try_files $uri $uri/ /index.php?$args;
}

location ~ \\.php$ {
    try_files $uri =404;
    fastcgi_pass unix:/tmp/php-cgi-85.sock;
    fastcgi_index index.php;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    include fastcgi_params;
}
"""

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    # Check the extension directory
    print("Checking extension dir:")
    try:
        ftp.cwd("/www/server/panel/vhost/nginx/extension/doctieuthuyet.com")
        ftp.retrlines('LIST')
    except Exception as e:
        print("Extension dir:", e)
        # Try to create it
        try:
            ftp.mkd("/www/server/panel/vhost/nginx/extension/doctieuthuyet.com")
            print("Created extension dir")
        except:
            pass
    
    # Check rewrite dir
    print("\nChecking rewrite dir:")
    try:
        ftp.cwd("/www/server/panel/vhost/rewrite")
        ftp.retrlines('LIST')
        lines = []
        ftp.retrlines('RETR doctieuthuyet.com.conf', lines.append)
        print("\nRewrite file content:", "\n".join(lines))
    except Exception as e:
        print("Rewrite dir:", e)
    
    ftp.quit()
except Exception as e:
    print("FTP Error:", e)
