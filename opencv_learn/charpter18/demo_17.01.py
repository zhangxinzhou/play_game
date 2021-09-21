import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    c = cv2.waitKey(1)
    if c == 27:
        break
cap.release()
cv2.destroyWindow()
