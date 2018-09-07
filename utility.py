import os
import re

"""
For file names like 'image12.jpg' 
"""


"""
Extract the number from file name
"""
def cvtStr2Int(imgName):
    strName = imgName.split(".")[0]
    p = re.compile(r'\d+')
    numName = p.findall(strName)
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
    mlist.sort()
    
    
    for i in mlist:
        seq = [front, str(i), end]
        newImages.append("".join(seq))
    
    return newImages
