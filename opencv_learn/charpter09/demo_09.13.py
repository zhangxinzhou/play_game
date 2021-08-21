import cv2

o = cv2.imread(r"..\lena.jpg", cv2.IMREAD_GRAYSCALE)

Sobelx = cv2.Sobel(o, cv2.CV_64F, 1, 0, ksize=3)
Sobelx = cv2.convertScaleAbs(Sobelx)
Sobely = cv2.Sobel(o, cv2.CV_64F, 0, 1, ksize=3)
Sobely = cv2.convertScaleAbs(Sobely)
Sobelxy = cv2.addWeighted(Sobelx, 0.5, Sobely, 0.5, 0)

Scharrx = cv2.Scharr(o, cv2.CV_64F, 1, 0)
Scharrx = cv2.convertScaleAbs(Scharrx)
Scharry = cv2.Scharr(o, cv2.CV_64F, 0, 1)
Scharry = cv2.convertScaleAbs(Scharry)
Scharrxy = cv2.addWeighted(Scharrx, 0.5, Scharrx, 0.5, 0)

cv2.imshow("original", o)
cv2.imshow("Sobelxy", Sobelxy)
cv2.imshow("Scharrxy", Scharrxy)
cv2.waitKey()
cv2.destroyAllWindows()
