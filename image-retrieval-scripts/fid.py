import os,math,cv2
import time as t
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from vidgear.gears import CamGear

gauth = GoogleAuth() # Authenticate to Google API
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
# gauth.CommandLineAuth() # Creating local webserver from a remote connection. 
drive = GoogleDrive(gauth) # Object handler of google drive.

def show_contents(target):
    '''
    Shows all the contents of the google drive.
    
    '''    
    contents = drive.ListFile({"q": "mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folders in contents:
        if (folders['title']==target):
            for folder in folders:
                print(folder['title'], folder['id'])
    return folder['id']

def get_folder_id(target):
    '''
    Returns the folder id of the 'dst' folder name.

    '''
    f = drive.ListFile({"q": "mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in f:
        if (folder['title']==target):
            print(folder['title'], folder['id'])
    return folder['id']

def ListFolder(target_id):
  
  filelist=[]
  file_list = drive.ListFile({'q': "'%s' in parents and trashed=false"%target_id}).GetList()
  for f in file_list:
    if f['mimeType']=='application/vnd.google-apps.folder':
        print(f['title'],f['id'])


target = '' # 'Maryland_Broadwalk'

# show_contents(target)
target_id = get_folder_id(target)
ListFolder(target_id)




