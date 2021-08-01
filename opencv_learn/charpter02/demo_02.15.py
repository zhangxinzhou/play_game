import cv2

cat = cv2.imread(r"..\cat.jpg", cv2.IMREAD_UNCHANGED)
dollar = cv2.imread(r"..\dollar.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("cat", cat)
cv2.imshow("dollar", dollar)
face = cat[220:400, 250:350]
dollar[160:340, 200:300] = face
cv2.imshow("result", dollar)
cv2.waitKey()
cv2.destroyAllWindows()
