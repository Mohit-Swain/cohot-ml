import cv2

img = cv2.imread('cat.jpg')
cv2.imshow('Cat',img)
# Averaging
average = cv2.blur(img,(3,3))
cv2.imshow('Average',average)
#Gaussian
gauss = cv2.GaussianBlur(img,(3,3),0)
cv2.imshow('Gauss',gauss)
#Median
median = cv2.medianBlur(img,3)
cv2.imshow('Median',median)
#Bilateral ## It retains the edges
bilateral = cv2.bilateralFilter(img, 7, 15, 15)
cv2.imshow('Bilateral',bilateral)
cv2.waitKey(0)