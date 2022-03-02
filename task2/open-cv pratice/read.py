import cv2

def rescaleFrame(frame,scale=0.75):
  # for images , videos , live video
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)

  dimensions = (width,height)

  return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)

capture = cv2.VideoCapture(0)
def changeRes(width,height):
  # only for live video
  capture.set(3,width)
  capture.set(4,height)
  
# changeRes(200,100)

while True:
  isTrue, frame = capture.read()
  # frame_resized = rescaleFrame(frame)
  # cv2.imshow('camera2',frame_resized)
  cv2.imshow('camera',frame)

  if cv2.waitKey(20) & 0xFF == ord('d'):
    break

capture.release()
cv2.destroyAllWindows()