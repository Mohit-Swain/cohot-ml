#allows us to focus on certain parts of image
import cv2
import numpy as np
img = cv2.imread('cat.jpg')
cv2.imshow('Cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
mask = cv2.circle(blank,(img.shape[1]//2 - 60,img.shape[0]//2 -85),100,255,-1)
cv2.imshow('mask',mask)

masked = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('Masked',masked)
cv2.waitKey(0)
