# CSV-File-Pull
Program that logs into a CSV server directory, downloads all files in the directory into a main local directory 
and a backup local directory, and then clears the files off the CSV server.

This program assumes that you will be logging directly into the FTP directory that contains the files you wish to download. 
If you need to navigate to a different directory on the FTP server to retreive the files simply use the following code after
the initial FTP login:

ftp.cwd('DIRECTORY NAME')

NOTE: You will need to add a FilesIn_backup folder and a FilesIn folder to the local directory where you will be running 
CSV_Pull.py from.
