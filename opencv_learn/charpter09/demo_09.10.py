import cv2

o = cv2.imread("Sobel4.bmp", cv2.IMREAD_GRAYSCALE)
Scharrx = cv2.Scharr(o, cv2.CV_64F, 1, 0)
Scharrx = cv2.convertScaleAbs(Scharrx)
Scharry = cv2.Scharr(o, cv2.CV_64F, 0, 1)
Scharry = cv2.convertScaleAbs(Scharry)
Scharrxy = cv2.addWeighted(Scharrx, 0.5, Scharry, 0.5, 0)
cv2.imshow("original", o)
cv2.imshow("xy", Scharrxy)
cv2.waitKey()
cv2.destroyAllWindows()
