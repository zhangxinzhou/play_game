import cv2

lena = cv2.imread(r"..\lena.jpg")
cv2.imshow("cat1", lena)
b = lena[:, :, 0]
g = lena[:, :, 1]
r = lena[:, :, 2]
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
lena[:, :, 0] = 0
cv2.imshow("catb0", lena)
lena[:, :, 1] = 0
cv2.imshow("catb0g0", lena)
cv2.waitKey()
cv2.destroyAllWindows()
