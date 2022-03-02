import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cat.jpg')
cv2.imshow('Cat',img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

blank = np.zeros(img.shape[:2],dtype='uint8')
mask = cv2.circle(blank,(img.shape[1]//2 - 60,img.shape[0]//2 -85),50,255,-1)
masked_img = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('Masked Img',masked_img)
# # Grayscale histogram
# gray_hist = cv2.calcHist([gray],[0],mask, [256],[0,256])
# plt.figure()
# plt.title('Gray Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# -- COLOR HISTOGRAM
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.xlim([0,256])
colors = ('b','g','r')
for i, col in enumerate(colors):
  hist = cv2.calcHist([img],[i],mask,[256],[0,256])
  plt.plot(hist,color = col)
plt.show()
cv2.waitKey(0)