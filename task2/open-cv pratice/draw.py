import cv2
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# img = cv2.imread('cat.jpg')
# blank[:] = (0,255,0)

# blank[200:300,300:400] = (0,0,255)

#left top , right bottom, color
# cv2.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2) # to fill, thickness = cv2.FILLED or -1

# center,radius,color
# cv2.circle(blank,(250,250),40,(0,0,255),thickness = -1)

# point1,point2, color
# cv2.line(blank,(0,0),(250,250),(0,255,0),thickness=2)

# text
# text,origin, fontFace,fontscale,color,thickness
# cv2.putText(blank,'Hello',(225,225),cv2.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv2.imshow('blank',blank)

cv2.waitKey(0)
cv2.destroyAllWindows()
