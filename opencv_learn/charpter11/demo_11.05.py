import cv2

o = cv2.imread(r"..\lena.jpg")
go = o
g1 = cv2.pyrDown(go)
g2 = cv2.pyrDown(g1)
g3 = cv2.pyrDown(g2)
l0 = go - cv2.pyrUp(g1)
l1 = g1 - cv2.pyrUp(g2)
l2 = g2 - cv2.pyrUp(g3)
print("l0.shape=", l0.shape)
print("l1.shape=", l1.shape)
print("l2.shape=", l2.shape)
cv2.imshow("l0", l0)
cv2.imshow("l1", l1)
cv2.imshow("l2", l2)
cv2.waitKey()
cv2.destroyAllWindows()
