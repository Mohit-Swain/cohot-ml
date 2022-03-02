import cv2
import numpy as np


img = cv2.imread('cat.jpg')
cv2.imshow('Cat',img)

blank = np.zeros(img.shape,dtype='uint8')
# cv2.imshow('Blank',blank)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

# ---
# blur = cv2.GaussianBlur(gray,(3,3),cv2.BORDER_DEFAULT)
# cv2.imshow('Blur',blur)

# canny = cv2.Canny(blur,125,175)
# cv2.imshow('Canny Edges',canny)
# ---

# OR

ret, thresh = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
cv2.imshow('Thresh',thresh)

contours, hierarchies = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print(len(contours))

cv2.drawContours(blank, contours, -1,(0,0,255),1)
cv2.imshow('Contours Drawn',blank)

cv2.waitKey(0)