import cv2

# create a VideoCapture object to capture from the default camera (index 0)
cap = cv2.VideoCapture(0)

# loop over frames from the video stream
while True:
    # read a frame from the video stream
    ret, frame = cap.read()
    
    # if the frame was not successfully read, break out of the loop
    if not ret:
        break
    
    # display the frame in a window called "Camera Feed"
    cv2.imshow("Camera Feed", frame)
    
    # wait for a key press (useful for setting up an exit key)
    key = cv2.waitKey(1) & 0xFF
    
    # if the 'q' key is pressed, break out of the loop
    if key == ord("q"):
        break

# release the resources used by the VideoCapture object
cap.release()

# close all windows created by OpenCV
cv2.destroyAllWindows()

