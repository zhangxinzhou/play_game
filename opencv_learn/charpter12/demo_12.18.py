import cv2

o = cv2.imread("cc.bmp")
cv2.imshow("original", o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
area, trgl = cv2.minEnclosingTriangle(contours[0])
print("area=", area)
print("trgl=", trgl)
for i in range(0, 3):
    p1 = tuple(int(i) for i in trgl[i][0])
    p2 = tuple(int(i) for i in trgl[(i + 1) % 3][0])
    print("===========", i)
    print(p1)
    print(p2)
    cv2.line(o, p1, p2, (2555, 255, 255), 2)

cv2.imshow("result", o)
cv2.waitKey()
cv2.destroyAllWindows()
