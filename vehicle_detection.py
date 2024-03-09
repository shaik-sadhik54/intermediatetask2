import numpy as np
import cv2

# Load the video file
video_path = 'Delhi.mp4'
cap = cv2.VideoCapture(video_path)

# Load the cascade classifier for vehicle detection
car_cascade = cv2.CascadeClassifier('/home/aman/opncv_tutorials/cars3.xml')

# Number of frames to process
number_of_frames_to_load = 500

# Loop through each frame
for frame_id in range(number_of_frames_to_load):
    # Read the frame
    ret, frame = cap.read()

    # Crop the frame to focus only on the road area
    frame = frame[120:, :-20]

    # Detect vehicles using the cascade classifier
    cars = car_cascade.detectMultiScale(frame, 1.1, 5)

    # Initialize variables for emergency vehicles and traffic violators
    emergency_vehicles = []
    traffic_violators = []

    # Loop through the detected cars
    for (x, y, w, h) in cars:
        # Draw rectangles around the detected vehicles
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        is_emergency_vehicle = False
        if criteria_for_emergency_vehicle:
            is_emergency_vehicle = True
            emergency_vehicles.append((x, y, w, h))

        # Example: Check if the vehicle is violating traffic rules
        is_traffic_violator = False
        if criteria_for_traffic_violation:
            is_traffic_violator = True
            traffic_violators.append((x, y, w, h))

    # Display the processed frame
    cv2.imshow('frame', frame)
    cv2.waitKey(10)

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
