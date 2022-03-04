import cv2

family = cv2.imread('family1.jpg')
cv2.imshow('Family',family)
gray = cv2.cvtColor(family,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

haar_cascade = cv2.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10)

for (x,y,w,h) in faces_rect:
  cv2.rectangle(family,(x,y),(x+w,y+h),(0,0,255),thickness=2)
cv2.imshow('Faces',family)
cv2.waitKey(0)