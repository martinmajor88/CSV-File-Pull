#! Python 2.7

import ftplib
import os
import os.path

Path = os.getcwd()

ftp = ftplib.FTP('HOST ADDRESS HERE', 'USER NAME HERE', 'PASSWORD HERE')
files = ftp.nlst()

for backup_files in files:
    local_directory = os.path.join(Path, 'FilesIn_backup/', os.path.basename(backup_files))
    with open(local_directory, 'wb') as backup:
        ftp.retrbinary("RETR " + backup_files, backup.write)
    backup.close()

for files_in in files:
    local_directory = os.path.join(Path, 'FilesIn/', os.path.basename(files_in))
    with open(local_directory, 'wb') as In:
        ftp.retrbinary("RETR " + files_in, In.write)
    In.close()
    ftp.delete(files_in)
ftp.quit()