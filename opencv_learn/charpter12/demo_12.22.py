import cv2

# ----------------------读取并绘制原始图像-------------------------
o = cv2.imread("hand.bmp")
cv2.imshow("original", o)
# ----------------------提取轮廓-------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# ----------------------寻找凸包,得到凸包的角点-------------------------
cnt = contours[0]
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)
print("defects=\n", defects)
# ----------------------构造凸缺陷-------------------------
for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(o, start, end, [0, 255, 0], 2)
    cv2.circle(o, far, 5, [255, 0, 0], -1)
# ----------------------显示凸包-------------------------
cv2.imshow("result", o)
cv2.waitKey()
cv2.destroyAllWindows()
