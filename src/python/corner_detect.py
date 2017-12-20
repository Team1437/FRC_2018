import cv2
import numpy as np
from grip import GripPipeline
from networktables import NetworkTables

cap = cv2.VideoCapture(1)
NetworkTables.initialize(server='roboRIO-1437-FRC.local')
table = NetworkTables.getTable('Vision')
#Clear the table
for key in table.getKeys():
    table.delete(key)

grip = GripPipeline()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        raise Exception("could not load image !")
    # Our operations on the frame come here
    #height, width, channels = frame.shape
    #print(width)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 15, 0.01, 10)
    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(frame, (x, y), 3, 255, -1)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()