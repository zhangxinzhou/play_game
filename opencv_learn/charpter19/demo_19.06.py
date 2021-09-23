import cv2
import numpy as np

d = 400
img = np.ones((d, d, 3), dtype=np.uint8) * 255
pts = np.array([[200, 50], [300, 200], [200, 350], [100, 200]], np.int32)
pts = pts.reshape(-1, 1, 2)
cv2.polylines(img, [pts], True, (0, 255, 0), 8)

winname = "Demo19.01"
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
