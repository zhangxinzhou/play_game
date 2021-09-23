import cv2
import numpy as np


def Demo(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("单击了鼠标左键")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("单机了鼠标右键")
    elif event == cv2.EVENT_FLAG_LBUTTON:
        print("按住左键拖动了鼠标")
    elif event == cv2.EVENT_MBUTTONDOWN:
        print("单机了中间键")


events = [i for i in dir(cv2) if 'EVENT' in i]
print("=" * 30, "events", "=" * 30)
for e in events:
    print(e)
print("=" * 30, "events", "=" * 30)

# 创建名称为Demo的响应(回调)函数OnMouseAction
# 将响应函数Demo与窗口建立连接(实现绑定)
img = np.ones((300, 300, 3), np.uint8) * 255

cv2.namedWindow("Demo19.9")
cv2.setMouseCallback("Demo19.9", Demo)
cv2.imshow("Demo19.9", img)
cv2.waitKey()
cv2.destroyAllWindows()
