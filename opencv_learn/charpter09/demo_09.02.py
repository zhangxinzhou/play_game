import cv2

o = cv2.imread("Sobel4.bmp", cv2.IMREAD_GRAYSCALE)
Sobelx = cv2.Sobel(o, -1, 1, 0)
cv2.imshow("original", o)
cv2.imshow("x", Sobelx)
cv2.waitKey()
cv2.destroyAllWindows()
