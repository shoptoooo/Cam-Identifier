import cv2
webcam = cv2.VideoCapture(0)
while True:
    ret,frame = webcam.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):#wait 40ms for every frame and stop visualizing when we press q
        break
webcam.release()
cv2.destroyAllWindows()