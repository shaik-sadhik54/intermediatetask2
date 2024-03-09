import numpy as np
import cv2

# Open the video file for processing
cap = cv2.VideoCapture('Delhi.mp4')

# Define a kernel for morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

# Create a Background Subtractor object
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

# Main loop for processing each frame of the video
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Apply background subtraction to detect moving objects
    fgmask = fgbg.apply(frame)

    # Perform morphological opening to remove noise
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    # Display the processed frame
    cv2.imshow('Smart Traffic Management System', fgmask)
    
    # Check for the 'ESC' key press to exit the loop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
