import cv2
import numpy as np

img = cv2.imread('cat.jpg')

cv2.imshow('Cat',img)

def translate(img, x, y):
  transMat = np.float32([[1,0,x],[0,1,y]])
  dimensions = (img.shape[1], img.shape[0])
  return cv2.warpAffine(img,transMat,dimensions)

# -x --> left
# -y --> Up
# +x -> right
# +y -> down

# translated = translate(img,100,100)
# cv2.imshow('Translated',translated)

#Rotation
def rotate(img, angle, rotPoint = None):
  (height,width) = img.shape[:2]
  if rotPoint is None:
    rotPoint = (width//2,height//2)
  rotMat = cv2.getRotationMatrix2D(rotPoint,angle,1.0)
  dimensions = (width,height)

  return cv2.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img,180)
# cv2.imshow('Rotated',rotated)

# Flipping
# 0-> vertical
# 1-> horizontal
# -1 -> both vertical and horizontal

# flip = cv2.flip(img,0)
# cv2.imshow('flip',flip)
 
cv2.waitKey(0)