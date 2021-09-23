import cv2
import numpy as np

d = 400
# 白色背景
img = np.ones((d, d, 3), dtype=np.uint8) * 255
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCv', (0, 200), font, 3, (0, 255, 0), 15)
cv2.putText(img, 'OpenCv', (0, 200), font, 3, (0, 0, 255), 5)

winname = "Demo19.01"
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
