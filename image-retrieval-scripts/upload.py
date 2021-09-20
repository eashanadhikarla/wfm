'''
!/usr/bin/env python
coding: utf-8

Lab:    WUME Lab, Lehigh Unviersity
Author: Eashan Adhikarla

Pick up the files from the repository and upload it to the respective google drive.

'''

import os,math, cv2
import time as t
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from datetime import datetime

gauth = GoogleAuth() # Authenticate to Google API
# gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication. 
gauth.CommandLineAuth()  # Creating local webserver from a remote connection.
drive = GoogleDrive(gauth)

rootdir = '~/covid19/src/'
# rootdir = "/Users/eashan22/Desktop/Summer20/Interdisciplinary/image-gathering/src/"

fids, folders = [], []

def get_fid(target):
    '''
    Shows all the contents of the google drive.
    
    '''
    f = drive.ListFile({"q": "mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in f:
        if (folder['title']==target):
            FolderID = folder['id']
            print('===> '+str(folder['title'])+' | '+FolderID)
    return FolderID

def make_folder(folder_name, FolderID):
    '''
    To create the folder by the name of the video and to upload it to the google drive.

    '''
    # Create folder
    folder_metadata = {'title' : folder_name, 'mimeType' : 'application/vnd.google-apps.folder', 'parents':[{'id': FolderID}] }
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()

    # Get folder info and print to screen
    foldertitle = folder['title']
    folderid = folder['id']
    fids.append(folderid)
    print('folder name: %s, id: %s' %(foldertitle, folderid))

    return fids

def upload_images(frame, idx):
    '''
    Uploads the file into the respective path in google drive.
    Meta-data can be specified for a different filename, etc.

    '''
    FID = fids[idx]
    file = drive.CreateFile(metadata={'title': frame, 'parents': [{'id': FID}]})
    file.SetContentFile(frame)
    file.Upload()

folderlist={}
ids_ = None
path = str(rootdir)+"webcam-list.csv"

target = 'Nov 21'
FolderID_ = get_fid(target)

# ids_ = ()

with open(path, 'r') as f: # Traversing the CSV file for Video links
    for row in f:
        names = row.split(',')[0] # Column 1
        folders.append(names[:-1])
        # ---------------------------------------------
        if ids_ == None:
            print ("Creating new FolderIDs")
            fids = make_folder(names, FolderID_)
        # ---------------------------------------------
        else:
            print ("Using existing FolderIDs")
            fids = list(ids_)
        # ---------------------------------------------
    print ('Found file-ids! Using - \n\n', fids)
    current = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    with open('fids_'+current+'.txt', 'w') as filehandle:
        filehandle.write(str(fids))
    
    print ('\n')
    print (f'Total Folders { len(fids)} for uploading to google dirve.')
    print ('--- Directories created ---\n') 

with open(path, 'r') as File:
    idx=0
    while True:
        directories=[d for d in os.listdir(os.path.abspath(".")) if os.path.isdir(d)]
        for idx, dirs in enumerate(directories):
            files=os.listdir(dirs)
            for frame in files:
                frame=os.path.join(dirs, frame)
                if frame.endswith(('.png','.jpg')):
                    print( 'Uploading '+str(frame) )
                    upload_images(frame, idx)
                    print( 'Removing '+str(frame)+' from local directory\n' )
                    os.remove(frame)
                    break
        print('=========================================')
        t.sleep(400.0)








