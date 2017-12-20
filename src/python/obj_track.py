import sys
import cv2
from grip import GripPipeline
from networktables import NetworkTables

cap = cv2.VideoCapture(0)
NetworkTables.initialize(server='roboRIO-1437-FRC.local')
table = NetworkTables.getTable('Vision')
#Clear the table
for key in table.getKeys():
    table.delete(key)

# Set up tracker.
# Instead of MIL, you can also use

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW']
tracker_type = tracker_types[2]

if tracker_type == 'BOOSTING':
    tracker = cv2.TrackerBoosting_create()
if tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create()
if tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create()
if tracker_type == 'TLD':
    tracker = cv2.TrackerTLD_create()
if tracker_type == 'MEDIANFLOW':
    tracker = cv2.TrackerMedianFlow_create()
if tracker_type == 'GOTURN':
    tracker = cv2.TrackerGOTURN_create()

# Exit if video not opened.
if not cap.isOpened():
    print "Could not open video"
    sys.exit()

for _ in xrange(10):
    ret, frame = cap.read()
    if not ret:
        raise Exception("could not load image !")


# Define an initial bounding box
# bbox = (287, 23, 86, 320)

# Uncomment the line below to select a different bounding box
bbox = cv2.selectROI(frame, False)

# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, bbox)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        raise Exception("could not load image !")
    # Our operations on the frame come here
    #height, width, channels = frame.shape
    #print(width)

    # Start timer
    timer = cv2.getTickCount()

    # Update tracker
    ok, bbox = tracker.update(frame)

    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

    # Draw bounding box
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display tracker type on frame
    cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

    # Display result
    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()