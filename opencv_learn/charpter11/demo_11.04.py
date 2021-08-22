import cv2

o = cv2.imread(r"..\lena.jpg", cv2.IMREAD_GRAYSCALE)
up = cv2.pyrUp(o)
down = cv2.pyrDown(up)
diff = down - o
print("o.shape=", o.shape)
print("down.shape", up.shape)
cv2.imshow("original", o)
cv2.imshow("down", down)
cv2.imshow("difference", diff)
cv2.waitKey()
cv2.destroyAllWindows()
