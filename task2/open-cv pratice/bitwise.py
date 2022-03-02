import cv2
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv2.rectangle(blank.copy(),(30,30),(370,370),255,-1)
cv2.imshow('Reactangle',rectangle)

circle = cv2.circle(blank.copy(),(200,200),200,255,-1)
cv2.imshow('circle', circle)

# Bitwise and
bitwise_and = cv2.bitwise_and(rectangle,circle)
cv2.imshow('bitwise and',bitwise_and)

#Bitwise or
bitwise_or = cv2.bitwise_or(rectangle,circle)
cv2.imshow('bitwise or',bitwise_or)

#Bitwise not
bitwise_not1 = cv2.bitwise_not(rectangle)
cv2.imshow('bitwise not rect',bitwise_not1)

bitwise_not2 = cv2.bitwise_not(circle)
cv2.imshow('bitwise not circle',bitwise_not2)
# bitwise xor
bitwise_xor = cv2.bitwise_xor(rectangle,circle)
cv2.imshow('bitwise xor',bitwise_xor)
cv2.waitKey(0)