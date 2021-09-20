'''
!/usr/bin/env python
coding: utf-8

Lab:    WUME Lab, Lehigh Unviersity
Author: Eashan Adhikarla

To pick list of videos from a directory and save every n-th frame
into the specified path. Doing in Breadth-first fashion.

== Some useful Folder Names and IDs ==
FaceDetection - '---'
Webcam Image Gathering - '---'

This is a simple HLS Manifest Parser written in Python 3.6, no dependency is required.
It is made for a personal use and provide some extra function as I need.

This parser was made using RFC 8216
This is the final RFC not a draft and some Tags were removed from previous versions of the protocol HLS but for retro compatibilities I decided to maintain them.

The parser is not checking if you are respecting the HLS Protocol, therefor you are the one responsible if you create/modify a manifest that doesn't fit your player.

'''

import os, cv2, streamlink
import time as t
import ffmpeg

def checker(stream_link):

    try:
        streams = streamlink.streams(stream_link)
        res1 = False if streams is None else True
        q = list(streams.keys())[0]
        stream = streams['%s' % q]
        video_cap = cv2.VideoCapture(stream.url)
        res2 = False if video_cap is None else True
    except:
        res1 = False

    res = True if res1 == True and res2 == True else False
    return res

def capture_frame(stream_link, image_index, image_prefix="stream", mprob=30, time_interval=10):

    i=0
    while True:
        
        try:
            streams = streamlink.streams(stream_link)
            if streams is None:
                raise ValueError("cannot open the stream link %s" % stream_link)
            q = list(streams.keys())[0]
            stream = streams['%s' % q]
        
        except IndexError as error:
            
            if i<=10:
                print('Index out of bound')
                i=i+1
                continue
                sleep(2.0)
            
            else:
                return None
        break
    
    target_img_path = os.getcwd()
    dir_path = os.path.join(target_img_path, image_prefix)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    j=0
    while True:
        try:
            video_cap = cv2.VideoCapture(stream.url) # ffmpeg.input(stream.url)
        except:
            if j <= 10:
                print(f"Caught exception for '{stream}', trying again!")
                j=j+1
                # continue
                t.sleep(1.0)
                
                streams = streamlink.streams(stream_link)
                q = list(streams.keys())[0]
                stream = streams['%s' % q]

                continue
            else:
                return None
        break

    dir_path = os.path.join(target_img_path, image_prefix)

    if video_cap is None:
        print("Open webcam [%s] failed." % stream.url)
        return None
    else:
        ret, frame = video_cap.read()

        if not ret:
            print("Captured frame is broken.")
            video_cap.release()
            return None
        else:
            print("-----------------------------------------------------")
            current_time = t.time()

            print("Capturing frame %d => %s." % (image_index, image_prefix))
            target_img_name = "{}{}_{}.png".format(image_prefix, image_index, current_time)
            cv2.imwrite(os.path.join(dir_path, target_img_name), frame)

            print("The current time in frame %d (%s):" %(image_index, target_img_name), current_time)

            img = cv2.imread(os.path.join(dir_path, target_img_name))
            cv2.imwrite(os.path.join(dir_path, target_img_name), img)
            video_cap.release()
        return img


print("=== Starting ===")
img = 0
time_interval = 400.0
webcams, new_webcams = [], []
webcamlist = "~/webcam-list.csv"
print(f"========================\nReading links from the path => '{webcamlist}'\n========================\n")

with open(webcamlist, 'r') as f: # Traversing the CSV file for Video links
    for row in f:
        names = row.split(',')[0] # Column 1
        links = row.split(',')[1] # Column 2
        if links[12:12+8]=='earthcam':
            webcams.append((names,links))

for name, link in webcams:
    check = checker(stream_link=link)
    if check:
        new_webcams.append((name, link))

print(f"Number of Links (working/not working): {len(webcams)}/{len(new_webcams)}")

while True:
    for name, link in new_webcams:
        capture_frame(stream_link=link, image_index=img, image_prefix=name, time_interval=time_interval)
    print('=======================================')
    img += 1
    t.sleep(time_interval)
print('=== Exit ===')


















