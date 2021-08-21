import cv2

o = cv2.imread("Sobel4.bmp", cv2.IMREAD_GRAYSCALE)
Sobelx = cv2.Sobel(o, cv2.CV_64F, 1, 0)
Sobelx = cv2.convertScaleAbs(Sobelx)
cv2.imshow("original", o)
cv2.imshow("x", Sobelx)
cv2.waitKey()
cv2.destroyAllWindows()
