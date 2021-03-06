import numpy as np
import cv2
import time
import face_recognition

cap = cv2.VideoCapture(0)
count = 0
time.sleep(5)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if count > 5 and count<10:
        cv2.imwrite("frame%d.jpg" %count, frame)
        face_locations = face_recognition.face_locations(frame)
        counter = len(face_locations)
        print(counter)
    count +=1
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
