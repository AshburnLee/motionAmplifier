#!/usr/local/bin/python3

import cv2
import argparse
import os
import re

"""
Extract the number from file name
"""
def cvtStr2Int(imgName):
    strName = imgName.split(".")[0]
    # get numbers from file name
    p = re.compile(r'\d+')
    numName = p.findall(strName)
    # Convert it to integer
    intName = int(numName[0])
    
    return intName

"""
Sort and construct new name
"""
def sortFrameName(images):
    front = 'frame'
    end = '.jpeg'
    
    newImages = []
    mlist = [cvtStr2Int(i) for i in images]
    #Sort 
    mlist.sort()
    
    for i in mlist:
        seq = [front, str(i), end]
        # Construct the file name
        newImages.append("".join(seq))
    
    return newImages


# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-ext", "--extension", required=False, default='jpeg', help="extension name. default is 'jpeg'.")
ap.add_argument("-o", "--output", required=False, default='output.avi', help="output video file")
args = vars(ap.parse_args())

# Arguments
dir_path = './video2frame/'
ext = args['extension']
output = args['output']

images = []
for f in os.listdir(dir_path):
    if f.endswith(ext):
        images.append(f)

# Determine the width and height from the first image
image_path = os.path.join(dir_path, images[0])
frame = cv2.imread(image_path)
cv2.imshow('video',frame)
height, width, channels = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID') # fourCC save video as .avi format !!!
out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

# Sort frame's name
images = sortFrameName(images)
print("Frame files have been sorted")

for image in images:

    image_path = os.path.join(dir_path, image)
    frame = cv2.imread(image_path)

    out.write(frame) # Write out frame to video

    cv2.imshow('video',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
        break

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()

print("The output video is {}".format(output))
