from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)
fileID = False
fileList = drive.ListFile().GetList()
for file in fileList:
  if(file['title'] == 'all_data.xlsx'):
      fileID = file['id']

# Initialize GoogleDriveFile instance with file id.
if fileID:
    file2 = drive.CreateFile({'id': fileID})
    file2.Delete()  # Permanently delete the file.


drive = GoogleDrive(gauth)
textfile = drive.CreateFile()
textfile.SetContentFile('all_data.xlsx')
textfile.Upload()
print (textfile)




