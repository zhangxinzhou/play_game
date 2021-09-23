import cv2
import numpy as np

d = 400
img = np.ones((d, d, 3), np.uint8) * 255
# 生成白色背景
center = (round(d / 2), round(d / 2))
size = (100, 200)

for i in range(0, 10):
    angle = np.random.randint(0, 361)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    thickness = np.random.randint(1, 9)
    cv2.ellipse(img, center, size, angle, 0, 360, color, thickness)

winname = "Demo19.01"
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
