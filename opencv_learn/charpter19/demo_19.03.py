import cv2
import numpy as np

n = 400
img = np.zeros((n, n, 3), np.uint8) * 255
(centerX, centerY) = (round(img.shape[1] / 2), round(img.shape[0] / 2))
# 将图像的中心作为圆心,实际值为d/2
red = (0, 0, 255)
for r in range(5, round(n / 2), 12):
    cv2.circle(img, (centerX, centerY), r, red, 3)

winname = "Demo19.01"
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
