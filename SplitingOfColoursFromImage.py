import cv2

Original_Image = cv2.imread('Lakshmanaprakash.jpg')
cv2.imshow("Original Image", Original_Image)
blue,green,red = cv2.split(Original_Image)
cv2.imshow("Blue is splited", blue)
cv2.imshow("Green is splited", green)
cv2.imshow("Red is splited", red)

cv2.waitKey(0)