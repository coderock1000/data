#Create a Python script using OpenCV to resize an image into three predefined sizes, display each resized image, and save it.

import cv2
image = cv2.imread('example.jpg')
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL) 
cv2.resizeWindow('Loaded Image', 8000, 1000 ) 
cv2.imshow('Loaded Image', image)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
print(f"Image Dimensions: {image.shape}") 