import cv2
import numpy as np

d = 400
img = np.zeros((d, d, 3), np.uint8) * 255
# 生成白色背景
for r in range(5, round(d / 2), 12):
    centerX = np.random.randint(0, high=d)
    # 生成随机圆心centerX,确保在画布img内
    centerY = np.random.randint(0, high=d)
    # 生成随机圆心centerY,确保在画布img内
    radius = np.random.randint(5, high=d / 5)
    # 生成随机班级,值范围为[5,d/5),最大半径是d/5
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    # 生成随机颜色,3个[0,256]的随机叔
    cv2.circle(img, (centerX, centerY), radius, color, -1)

winname = "Demo19.01"
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
