from ComputerVision.Files.laneDetection import edgeDetection
import numpy as np
import cv2
import math
from preProcess import *
from laneDetection import *

def laneFit(points,frame):
    lines = cv2.HoughLinesP(points, 1, np.pi/180, 5, maxLineGap=100)
    # Hough Transformation is used to find a line using the edge points 
    frame2D = frame[:,:,0]
    image = frame2D.copy()
    lanePoints =[]
    #lanePoints stores the co-ordinates of the lane points
    laneCenter = 0
    # The lane center can be calculated as the mean of the x co-ordinates 
    # of the lane pixels
    numOfLines = len(lines)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        laneCenter += x1+x2
        lanePoints.append([x1,y1])
        lanePoints.append([x2,y2])
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)

    laneCenter = laneCenter/numOfLines

    return image,lanePoints,laneCenter

def laneWrap(points,frame):
    frame2D = frame[:,:,0]
    laneImage = frame2D.copy()
    image,lanePoints,laneCenter = laneFit(points,frame)
    imageCenter = frame.shape[1]/2
    # The center of the vehicle is taken as the center of the image
    # Lane departure can be calcuated as the difference between the position of
    # the lane Center and image Center
    difference = abs(imageCenter-laneCenter)
    if(difference >= 30):
        # If the difference is greater than a threshold, lane Departure Warning is given
        cv2.fillConvexPoly(laneImage, lanePoints, color=[0,255,255])
    
    else:
        cv2.fillConvexPoly(laneImage, lanePoints, color=[255,0,255])

    return laneImage



