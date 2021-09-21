import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('I', '4', '2', '0')
out = cv2.VideoWriter('output.avi', fourcc, 20, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        break
cap.release()
out.release()
cv2.destroyWindow()
