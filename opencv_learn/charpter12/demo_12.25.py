import cv2

# ----------------原始图像--------------------
o = cv2.imread("cs1.bmp")
cv2.imshow("original", o)

# ----------------获取凸包--------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
image = binary

hull = cv2.convexHull(contours[0])
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, (0, 255, 0), 2)

# ----------------内部点A到轮廓的距离--------------------
distA = cv2.pointPolygonTest(hull, (300, 250), False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'A', (300, 250), font, 1, (0, 255, 0), 3)
print("distA=", distA)

# ----------------内部点B到轮廓的距离--------------------
distB = cv2.pointPolygonTest(hull, (300, 350), False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'B', (300, 350), font, 1, (0, 250, 0), 3)
print("distB=", distB)

# ----------------正好处于轮廓上的点C到轮廓的距离--------------------
distC = cv2.pointPolygonTest(hull, (493, 159), False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'C', (493, 159), font, 1, (0, 255, 0), 3)
print("distC=", distC)
print(hull)
# ----------------显示--------------------

cv2.imshow("result1", image)
cv2.waitKey()
cv2.destroyAllWindows()
