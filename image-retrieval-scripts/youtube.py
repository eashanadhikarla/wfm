'''
!/usr/bin/env python
coding: utf-8

Lab:    WUME Lab, Lehigh Unviersity
Author: Eashan Adhikarla

To pick list of videos from a directory and save every n-th frame
into the specified path. Doing in Breadth-first fashion.

== Some useful Folder Names and IDs ==
FaceDetection - '1vmny_vtQUkXPHKQMneJtrFOoG6SBIodo'
Webcam Image Gathering - '1AqtOinYVpS-Md7S4hodVhX_VVmXfa8A6'

'''
import os,math,cv2
import time as t
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from vidgear.gears import CamGear

gauth = GoogleAuth() # Authenticate to Google API
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication. 
# gauth.CommandLineAuth()  # Creating local webserver from a remote connection.
drive = GoogleDrive(gauth)

path, caps, fids = [],[],[]
csv_file = '~/list.csv'

start_time = t.time()

HEIGHT, WIDTH = 1920, 1080
FRAMERATE = 15 # frame rate
TIME = 300 # seconds
target = 'FaceDetection'
FolderID = 'tujrdcjyvjb' # root folder id
options = {"CAP_PROP_FRAME_WIDTH":WIDTH, "CAP_PROP_FRAME_HEIGHT":HEIGHT, "CAP_PROP_FPS":FRAMERATE}

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

def make_folder(folder_name):
    '''
    To create the folder by the name of the video and to upload it to the google drive.

    '''
    # FID = get_fid(target)
    # Create folder
    folder_metadata = {'title' : folder_name, 'mimeType' : 'application/vnd.google-apps.folder', 'parents':[{'id': FolderID}] }
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()

    # Get folder info and print to screen
    foldertitle = folder['title']
    folderid = folder['id']
    fids.append(folderid)
    
    print('folder name: %s, id: %s' % (foldertitle, folderid))

def upload_images(filename, frame, idx):
    '''
    Uploads the file into the respective path in google drive.
    Meta-data can be specified for a different filename, etc. 

    '''
    FID = fids[idx]
    file = drive.CreateFile(metadata={'title': frame, 'parents': [{'id': FID}]})
    file.SetContentFile( write(frame) )
    file.Upload()

def check_flag(links):
    '''
        links: Checking the URL to be Youtube URL.
    '''
    flag=True if links[12]=='y' else False
    url = links
    # url = links[:-1] if flag==True else links
    return url, flag

def write(filename, frame):
    '''
        Writing the frame as an image.
    '''
    cv2.imwrite(filename, frame)

# Traversing the CSV file for Video links
with open(csv_file, 'r') as f:
    for row in f:
        names = row.split(',')[0] # Column 1
        links = row.split(',')[1] # Column 2
        path.append((names,links))

        name = names[:-4] if names.find('.') != -1 else names
        try:
            # creating a folder named data
            os.makedirs(name) # remove extension in folder name
            make_folder(name)

        # if not created then raise error
        except OSError:
            print ('Error: Creating directory '+str(name))

for names, links in path: # path is a list of all the video samples
    url, flag = check_flag(links)
    cap = CamGear(source=url, y_tube=flag, **options).start()
    caps.append((cap, names))

currentframe=1
while True:
    frames = []
    for cap, name in caps:
        frame = cap.read()
        frames.append((frame, name))

    currentframe+=1
    if (currentframe % (TIME*math.floor(FRAMERATE)) == 0):
        print('\n')
        idx=0
        for frame, name in frames:
            end_time = t.time()
            filename = './'+str(name)+'/image'+str(int(currentframe))+'_'+str(round(end_time, 5))+'.jpg'
            print('Filename: '+filename+'   | Timestamp: '+str(round(end_time, 5))+' seconds')
            if frame is not None:
                upload_images(filename, frame, idx) # Write the file in the google drive
                idx+=1
                os.remove(filename)
                
        if cv2.waitKey(1)==27:
            # Release all the sape and windows once done
            for cap, _ in caps:
                cap.release()

print ("Done!")
print('\n=========================================================')
print("---Execution Time: %s seconds ---" % round(time.time()-start_time, 5) )
print('=========================================================\n')
