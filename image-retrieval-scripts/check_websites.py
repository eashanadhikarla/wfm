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

'''

import os
import cv2
import streamlink
import time as t

webcams, new_webcams = [], []
webcamlist = '~/webcam-list.csv'

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

print(len(webcams), len(new_webcams))
for cams in new_webcams:
    print(cams)















