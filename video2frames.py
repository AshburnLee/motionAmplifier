import numpy as np
import cv2
import argparse
import os

"""
Saving frames from a video
"""
#construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--inputFilePath", required=True, help="Where is your video")
ap.add_argument("-o", "--outpuFilePath", required=True, help="Where are your frames stored")
args = vars(ap.parse_args())

# armguments
inputPath = args['inputFilePath']
outputPath = args['outpuFilePath']


# clear directory
os.system('rm -rf %s/*' % outputPath)

# do the job
cap = cv2.VideoCapture(inputPath)
count = 0

while (cap.isOpened()):
    ret, frame = cap.read()
    
    if ret:
        # save frames. Frame manipulation 
        cv2.imwrite(outputPath + "frame%d.jpeg" % count, frame) 
    
    #
    if not ret:
        cap.release()
        break

    count += 1
    print("frame {} saved".format(count))

print("total frames: {}".format(count))

