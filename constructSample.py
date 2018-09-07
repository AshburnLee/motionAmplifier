import cv2
import numpy as np
import os
import re
from utility import cvtStr2Int


# Read file name into a list

images = []
filePath = './video2frame/'

for f in os.listdir(filePath):
    if f.endswith('.jpeg'):
        images.append(f)

# sort the files and pick the needed
tmp = [cvtStr2Int(i) for i in images]
tmp.sort()
need = tmp[70:371]

# reconstruct file names
pickedFrame = []
for i in need:
    seq = ['frame', str(i), '.jpeg']
    pickedFrame.append("".join(seq))


# get the wisth and height of frames
imgPath = os.path.join(filePath, pickedFrame[0])
sample = cv2.imread(imgPath)

fourcc = cv2.VideoWriter_fourcc(*'XVID') # fourCC save video as .avi format !!!
out = cv2.VideoWriter('./slice.avi', fourcc, 20.0, (640, 480))

# Show frame by frame
for image in pickedFrame:

    image_path = os.path.join(filePath, image)
    frame = cv2.imread(image_path)

    out.write(frame) # Write out frame to video

    cv2.imshow('video',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
        break

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()


