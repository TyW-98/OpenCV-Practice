import numpy as np
import cv2
import matplotlib.pyplot as plt

def draw_circle(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(blank_img,(x,y),100, (54,52,7),-1)

# Connect draw_shape function to Image window
cv2.namedWindow(winname="Image")
cv2.setMouseCallback("Image",draw_circle)

blank_img = np.zeros(shape=(512,512,3),dtype=np.int8)

while True:
    
    cv2.imshow("Image",blank_img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()