import ftplib

HTACCESS_CONTENT = """# BEGIN WordPress
# The directives (lines) between "BEGIN WordPress" and "END WordPress" are
# dynamically generated, and should only be modified via WordPress filters.
# Any changes to the directives between these markers will be overwritten.
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>

# END WordPress
"""

with open("temp_htaccess", "w") as f:
    f.write(HTACCESS_CONTENT)

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    with open("temp_htaccess", "rb") as f:
        ftp.storbinary('STOR .htaccess', f)
    ftp.quit()
    print("Done uploading .htaccess")
except Exception as e:
    print(e)
