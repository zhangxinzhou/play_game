import cv2

cat = cv2.imread(r"..\cat720x720.jpg")
lena = cv2.imread(r"..\lena.jpg")
result = cv2.addWeighted(cat, 0.6, lena, 0.4, 0)
cv2.imshow("cat", cat)
cv2.imshow("lena", lena)
cv2.imshow("result", result)
cv2.waitKey()
cv2.destroyAllWindows()
