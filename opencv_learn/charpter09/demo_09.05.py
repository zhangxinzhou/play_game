import cv2

o = cv2.imread("Sobel4.bmp", cv2.IMREAD_GRAYSCALE)
Sobelxy = cv2.Sobel(o, cv2.CV_64F, 1, 1)
Sobelxy = cv2.convertScaleAbs(Sobelxy)
cv2.imshow("original", o)
cv2.imshow("x", Sobelxy)
cv2.waitKey()
cv2.destroyAllWindows()
