import cv2

img = cv2.imread(r"..\lena.jpg")
r = cv2.blur(img, (5, 5))
cv2.imshow("img", img)
cv2.imshow("result", r)
cv2.waitKey()
cv2.destroyAllWindows()
