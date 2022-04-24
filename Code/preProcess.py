import numpy as np
import cv2



def blackCanvas(frame):
    channel1 = frame[:,:,0]
    canvas = np.zeros_like(channel1)
    # This method outputs a canvas full of black color which has
    # a shape just like the 1st channel of the frame
    return canvas

def regionOfInterest():
    coOrdinates = np.array([[50,270], [220,160], [360,160], [480,270]])
    # We define these co-ordinates that will convert the region inside it
    # to white and the region outside it as black
    return coOrdinates

def mask(frame):
    canvas = blackCanvas(frame)
    points = regionOfInterest()
    cv2.fillConvexPoly(canvas, points, 1)
    image2D = frame[:,:,0]
    image = cv2.bitwise_and(image2D,image2D,mask=canvas)
    #This function applies a mask to the frame so as only the region of interest is
    # visible and the rest is covered black
    return image

def smooth(frame):
    maskedImage = mask(frame)
    smoothedImage = cv2.medianBlur(maskedImage,3)
    #Now, we will smooth the image so as to remove noise and unwanted objects
    return smoothedImage




    
