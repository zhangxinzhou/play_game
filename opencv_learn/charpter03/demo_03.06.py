import cv2

lena = cv2.imread(r"..\lena.jpg", cv2.IMREAD_UNCHANGED)
dollar = cv2.imread(r"..\dollar.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("lena", lena)
cv2.imshow("dollar", dollar)
face1 = lena[220:400, 250:350]
face2 = dollar[160:340, 200:300]
add = cv2.addWeighted(face1, 0.6, face2, 0.4, 0)
dollar[240:(240 + 180), 580:680] = add
cv2.imshow("result", dollar)
cv2.waitKey()
cv2.destroyAllWindows()
