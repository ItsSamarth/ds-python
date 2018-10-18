import numpy as np
import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray) #imgshow

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
