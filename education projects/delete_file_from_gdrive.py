from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)
fileID = False
fileList = drive.ListFile().GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
   # Get the folder ID that you want

  if(file['title'] == 'all_data.xlsx'):
      fileID = file['id']

# Initialize GoogleDriveFile instance with file id.
if fileID:
    file2 = drive.CreateFile({'id': fileID})
    file2.Delete()  # Permanently delete the file.
