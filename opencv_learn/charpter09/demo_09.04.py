import cv2

o = cv2.imread("Sobel4.bmp", cv2.IMREAD_GRAYSCALE)
Sobely = cv2.Sobel(o, cv2.CV_64F, 0, 1)
Sobely = cv2.convertScaleAbs(Sobely)
cv2.imshow("original", o)
cv2.imshow("x", Sobely)
cv2.waitKey()
cv2.destroyAllWindows()
