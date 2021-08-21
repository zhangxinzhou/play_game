import cv2

o = cv2.imread("Sobel4.bmp", cv2.IMREAD_GRAYSCALE)
Sobelx = cv2.Sobel(o, cv2.CV_64F, 1, 0)
Sobely = cv2.Sobel(o, cv2.CV_64F, 0, 1)
Sobelx = cv2.convertScaleAbs(Sobelx)
Sobely = cv2.convertScaleAbs(Sobely)
Sobelxy = cv2.addWeighted(Sobelx, 0.5, Sobely, 0.5, 0)
cv2.imshow("original", o)
cv2.imshow("xy", Sobelxy)
cv2.waitKey()
cv2.destroyAllWindows()
