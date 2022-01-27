import cv2

"""# Pre-trained car
car_pretrained = 'car_detector.xml'
carDetection = cv2.CascadeClassifier(car_pretrained)

# test image mode

# Video test

# video = cv2.VideoCapture('')

# Read image

image = cv2.imread('car4.png')

# Conver it to gray scale for the haar algorithm 
grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



all_cars = carDetection.detectMultiScale(grayscaled)

for (x, y, w, h) in all_cars:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Car Detection", image)

cv2.waitKey()
"""


img1 = "car4.png "

car_pretrained = 'car_detector.xml'


image = cv2.imread(img1)

grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

carDetection = cv2.CascadeClassifier(car_pretrained)

all_cars = carDetection.detectMultiScale(grayscaled)


#for (x, y, w, h) in all_cars
car1 = all_cars[0]
(x, y, w, h) = car1

cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow("Car Detection", image)

cv2.waitKey()


