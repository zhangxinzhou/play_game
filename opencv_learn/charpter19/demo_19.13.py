import cv2

Type = 0  # 阈值处理方式
Value = 0  # 使用的阈值


def onType(a):
    Type = cv2.getTrackbarPos(tType, windowName)
    Value = cv2.getTrackbarPos(tValue, windowName)
    ret, dst = cv2.threshold(o, Value, 255, Type)
    cv2.imshow(windowName, dst)


def onValue(a):
    Type = cv2.getTrackbarPos(tType, windowName)
    Value = cv2.getTrackbarPos(tValue, windowName)
    ret, dst = cv2.threshold(o, Value, 255, Type)
    cv2.imshow(windowName, dst)


o = cv2.imread(r'..\lena.jpg', 0)
windowName = "Demo19.13"
cv2.namedWindow(windowName)
cv2.imshow(windowName, o)
# 创建两个滚动条
tType = "Type"
tValue = "Value"
cv2.createTrackbar(tType, windowName, 0, 4, onType)
cv2.createTrackbar(tValue, windowName, 0, 255, onValue)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
