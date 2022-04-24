import cv2
import numpy as np
cap = cv2.VideoCapture("F:\\vehicle-detection-main\\project_video.mp4")
ret, current_frame = cap.read()
previous_frame = current_frame

result = cv2.VideoWriter('filename.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         3000, (1280, 720))

while(cap.isOpened()):
    img = current_frame
    imshape = img.shape
    vertices = np.array([[(0, imshape[0]-60), (9*imshape[1]/20, 11*imshape[0]/18),
                        (11*imshape[1]/20, 11*imshape[0]/18), (imshape[1], imshape[0]-60)]], dtype=np.int32)
    ignore_mask_color = 255
    # Convert the image to gray-scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Find the edges in the image using canny detector
    edges = cv2.Canny(gray, 50, 200)
    # Detect points that form a line

    # REGION MASK
    mask = np.zeros_like(edges)
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked = cv2.bitwise_and(edges, mask)

    lines = cv2.HoughLinesP(masked, rho=3.4, theta=1*np.pi/180,
                            threshold=100, minLineLength=150, maxLineGap=200)
    # Draw lines on the image
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
    # Show result
    cv2.imshow("Result Image", img)
    result.write(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    previous_frame = current_frame.copy()
    ret, current_frame = cap.read()

result.release()
