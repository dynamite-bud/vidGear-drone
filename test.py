import cv2
cap = cv2.VideoCapture('autovideosrc ! videoconvert ! appsink')
while True:
    ret,frame = cap.read()
    cv2.imshow('',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()