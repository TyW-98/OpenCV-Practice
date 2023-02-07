import cv2

image_1 = cv2.imread("../../Course-Resource/DATA/00-puppy.jpg")

while True:
    
    cv2.imshow("puppy image",image_1)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()