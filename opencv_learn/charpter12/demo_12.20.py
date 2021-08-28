import cv2

o = cv2.imread("contours.bmp")
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[0])
print("returnPoints为默认True时返回hull的值:\n", hull)
hull2 = cv2.convexHull(contours[0], returnPoints=False)
print("returnPoints为False返回值hull的值:\n", hull2)
