import cv2

o = cv2.imread(r"..\lena.jpg")
r = cv2.bilateralFilter(o, 55, 100, 100)
cv2.imshow("original", o)
cv2.imshow("result", r)
cv2.waitKey()
cv2.destroyAllWindows()
