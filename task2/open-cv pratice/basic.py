import cv2
img = cv2.imread('cat.jpg')
cv2.imshow('Cat',img)

# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray Cat',gray)

# blur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
# cv2.imshow('Blur',blur)

#Edge cascade
# canny = cv2.Canny(img,125,175)
# cv2.imshow('canny',canny)

# # dialeting the image
# dilated = cv2.dilate(canny,(7,7),iterations=3)
# cv2.imshow('dialated',dilated)

# #eroding
# erode = cv2.erode(dialated,(7,7),iterations=3)
# cv2.imshow('erode',erode)

#resize
# resized = cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA)
# cv2.imshow('resized',resized)

#cropped
# cropped = img[50:200,200:400]
# cv2.imshow('cropped',cropped)
cv2.waitKey(0)