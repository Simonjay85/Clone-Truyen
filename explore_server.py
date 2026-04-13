import ftplib

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    
    # Check root
    ftp.cwd("/")
    items = []
    ftp.retrlines('LIST', items.append)
    print("Root:", items)
    
    # The FTP user probably doesn't have access to /www/server
    # Let's check what the FTP root maps to
    ftp.cwd("/www/wwwroot/doctieuthuyet.com")
    print("\nWWWROOT doctieuthuyet:")
    ftp.retrlines('LIST')
    
    ftp.quit()
except Exception as e:
    print("Error:", e)
