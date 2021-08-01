import cv2

lena = cv2.imread(r"..\lena.jpg")
b, g, r = cv2.split(lena)
cv2.imshow("original", lena)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
cv2.waitKey()
cv2.destroyAllWindows()
