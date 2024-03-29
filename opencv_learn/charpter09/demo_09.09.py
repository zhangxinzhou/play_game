import cv2

o = cv2.imread("Sobel4.bmp", cv2.IMREAD_GRAYSCALE)
Scharry = cv2.Scharr(o, cv2.CV_64F, 0, 1)
Scharry = cv2.convertScaleAbs(Scharry)
cv2.imshow("original", o)
cv2.imshow("y", Scharry)
cv2.waitKey()
cv2.destroyAllWindows()
