import cv2

# ====================读取并显示原始图像=======================
o = cv2.imread("cc.bmp")
cv2.imshow("original", o)
# ====================获取轮廓=======================
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# ====================epsilon=0.2*周长=======================
adp = o.copy()
epsilon = 0.2 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv2.imshow("result0.2", adp)

# ====================epsilon=0.09*周长=======================
adp = o.copy()
epsilon = 0.09 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv2.imshow("result0.09", adp)

# ====================epsilon=0.055*周长=======================
adp = o.copy()
epsilon = 0.055 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv2.imshow("result0.055", adp)

# ====================epsilon=0.05*周长=======================
adp = o.copy()
epsilon = 0.05 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv2.imshow("result0.05", adp)

# ====================epsilon=0.02*周长=======================
adp = o.copy()
epsilon = 0.02 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv2.imshow("result0.02", adp)

# ====================epsilon=0.005*周长=======================
adp = o.copy()
epsilon = 0.005 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv2.imshow("result0.005", adp)

cv2.waitKey()
cv2.destroyAllWindows()
