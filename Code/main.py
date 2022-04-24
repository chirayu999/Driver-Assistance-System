import os
import re
from os.path import isfile, join
import cv2
import numpy as np
import glob
from preProcess import *
from laneDetection import *
from laneFitting import *

frames = []
for frame in glob.glob('frames/*.png'):
    # We will read each frame from the list
    img = cv2.imread(frame)
    frames.append(img)

frameNumber =0

for frame in frames:

    smoothedImage = smooth(frame)
    # Smooth function takes care of every pre processing step starting from 
    # masking to smoothing the image

    edgePoints = edgeDetection(smoothedImage)

    # edgePoints are the pixels that are considered for fitting edges to them

    laneImage = laneWrap(edgePoints,frame)
    # Finally, laneImage is the result which shows lanes on the image and alerts in the
    # situation of a lane departure event.
    
    cv2.imwrite('outputFrames/'+str(frameNumber)+'.png',laneImage)

# Now we will sticth all the frames with lane detected to a video
inputDirectory = 'outputFrames/'

outputDirectory = 'result.mp4'

framesPerSecond = 30
# The original video was 30fps so we will create the result as a 30fps video

files = [file for file in os.listdir(inputDirectory) if isfile(join(inputDirectory, file))]

files.sort(key=lambda frameNo: int(re.sub('\D', '', frameNo)))

imageList = []

for i in range(len(files)):
    #We will find the path of each frame, add it to a list of images
    frameName=inputDirectory + files[i]
    image = cv2.imread(frameName)
    column,rows,channels = img.shape
    dimension = (rows,column)
    imageList.append(image)


# Then we will use VideWriter Function to append all the frames chronologically to the video.

finalResult = cv2.VideoWriter(outputDirectory,cv2.VideoWriter_fourcc(*'DIVX'), framesPerSecond, dimension)

for i in range(len(imageList)):
    finalResult.write(imageList[i])

finalResult.release()


