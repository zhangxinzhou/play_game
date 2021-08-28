import cv2

# ----------------------读取并绘制原始图像-------------------------
o = cv2.imread("hand.bmp")
cv2.imshow("original", o)
# ----------------------提取轮廓-------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# ----------------------凸包-------------------------
image1 = o.copy()
hull = cv2.convexHull(contours[0])
cv2.polylines(image1, [hull], True, (0, 255, 0), 2)
print("使用函数cv2.convexHull()构造的多边形是否时凸形的: ", cv2.isContourConvex(hull))
cv2.imshow("result1", image1)
# ----------------------逼近多边形-------------------------
image2 = o.copy()
epsilon = 0.01 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
image2 = cv2.drawContours(image2, [approx], 0, (0, 0, 255), 2)
print("使用函数cv.approxPolyDP()构造的多边形是否时凸形: ", cv2.isContourConvex(approx))
cv2.imshow("result2", image2)

cv2.waitKey()
cv2.destroyAllWindows()
