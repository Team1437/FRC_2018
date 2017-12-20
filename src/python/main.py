import cv2
from grip import GripPipeline
from networktables import NetworkTables

cap = cv2.VideoCapture(0)
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
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    grip.process(img)
    contour, idx = grip.publish()
    table.putNumberArray('Contour', contour)

    cv2.drawContours(frame, grip.convex_hulls_output, -1, (0, 255, 255), 3)
    cv2.drawContours(frame, grip.convex_hulls_output, idx, (255, 0, 255), 3)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()