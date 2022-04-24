import cv2
from preProcess import *




def imageThreshold(smoothedImage):
    thresholdValue, thresholdImage = cv2.threshold(smoothedImage, 120, 255, cv2.THRESH_BINARY)
    #Now, we will threshold the smoothened image to detect the bright pixels.
    #Any pixel above the value of 120 will be assigned 255 and the rest will be 0
    return thresholdImage

def edgeDetection(smoothedImage):
    thresholdImage = imageThreshold(smoothedImage)
    edgePoints = cv2.Canny(thresholdImage,100,200)
    #Finally, Canny edge detector is used to find the points that will be considered as 
    #for edge

    return edgePoints






