import cv2

img = cv2.imread(r"..\lena.jpg")
r5 = cv2.blur(img, (5, 5))
r30 = cv2.blur(img, (30, 30))
cv2.imshow("img", img)
cv2.imshow("result5", r5)
cv2.imshow("result30", r30)
cv2.imshow("result30min", cv2.resize(r30, None, fx=0.1, fy=0.1))
cv2.waitKey()
cv2.destroyAllWindows()
