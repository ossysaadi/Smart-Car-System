import cv2

# Import the pre trained car by the Haar algorithm
preTrained_car_detector = "car_detector.xml"

# Import the pre trained full ody by the Haar algorithm
preTrained_fullbody_detetctor = "haarcascade_fullbody.xml"

# Import Video from the file
video_1 = "video3.mp4"

# Capture the video
video = cv2.VideoCapture(video_1)

# Create the Car classifier for the Algorithm

car_detector = cv2.CascadeClassifier(preTrained_car_detector)
# Create the fullbody classifier for the Algorithm
human_detector = cv2.CascadeClassifier(preTrained_fullbody_detetctor)

# Run the program to detetct all cars
while True:
    # Read the frame for the vieo
    (succesful_read, frame) = video.read()

    # If the Reading was succesful convert the frame to Gray (black and white)
    if succesful_read:
        # Conver the frame to gray scale
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # If it failed to show a new frame break
    else:
        break

    # Detect all cars even small ones
    all_cars = car_detector.detectMultiScale(gray_scale)

    # Detetct all human even small ones
    all_human = human_detector.detectMultiScale(gray_scale)

    # Draw rectangles around the Cars
    for (x, y, w, h) in all_cars:
        cv2.rectangle(frame, (x+1, y+2), (x+w, y+h), (255, 0 , 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0 , 255), 2)
    
    for (x, y, w, h) in all_human:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255 , 0), 2)

    # Display the whol video with detection and stuff
    cv2.imshow('Smart Car system', frame)

    # Wait key 1 is 1 millisecond
    key = cv2.waitKey()

    if key==81 or key==133:
        break

video.release()
