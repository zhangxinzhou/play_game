import numpy as np
import cv2

cap = cv2.VideoCapture("S01E01.rmvb")
while cap.isOpened():
    ret, frame_0 = cap.read()
    frame_1 = cv2.Canny(frame_0, 100, 200)
    cv2.imshow("frame_0", frame_0)
    cv2.imshow("frame_1", frame_1)
    c = cv2.waitKey(1)
    if c == 27:
        break
cap.release()
cv2.destroyWindow()
