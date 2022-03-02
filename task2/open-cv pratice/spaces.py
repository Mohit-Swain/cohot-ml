import cv2
import matplotlib.pyplot as plt

img = cv2.imread('cat.jpg')
cv2.imshow('Cat',img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',hsv)

lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imshow('LAB',lab)

rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('RGB',rgb)
# plt.imshow(rgb)
# plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()