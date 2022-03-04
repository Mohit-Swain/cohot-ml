import cv2
import numpy as np

img = cv2.imread('cat.jpg')
cv2.imshow('Cats',img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)
# Simple Threshloading
threshold, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
cv2.imshow('Thresh',thresh)

threshold2, thresh2 = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Thresh2',thresh2)

# Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3)
cv2.imshow('Adaptive thresh',adaptive_thresh)
cv2.waitKey(0)