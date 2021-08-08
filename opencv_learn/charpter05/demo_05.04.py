import cv2

img = cv2.imread(r"..\lena.jpg")
x = cv2.flip(img, 0)
y = cv2.flip(img, 1)
xy = cv2.flip(img, -1)
cv2.imshow("img", img)
cv2.imshow("x", x)
cv2.imshow("y", y)
cv2.imshow("xy", xy)
cv2.waitKey()
cv2.destroyAllWindows()
