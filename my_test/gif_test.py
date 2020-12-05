import cv2

cap = cv2.VideoCapture('test.gif')
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('window', frame)
    cv2.waitKey(0)
