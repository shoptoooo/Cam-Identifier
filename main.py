import cv2
from PIL import Image
from util import get_limits

red = [255,255,0]

webcam = cv2.VideoCapture(0)
while True:
    ret,frame = webcam.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit,upperLimit = get_limits(color=red)

    mask = cv2.inRange(hsvImage,lowerLimit,upperLimit)
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1,y1,x2,y2 = bbox
        frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),5)
        
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(40) & 0xFF == ord('q'):#wait 40ms for every frame and stop visualizing when we press q
        break

webcam.release()
cv2.destroyAllWindows()