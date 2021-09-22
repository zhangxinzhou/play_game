import cv2
import numpy as np

n = 300
img = np.zeros((n + 1, n + 2, 3), np.uint8)
img = cv2.line(img, (0, 0), (n, n), (255, 0, 0), 3)
img = cv2.line(img, (0, 100), (n, 100), (0, 255, 0), 1)
img = cv2.line(img, (100, 0), (100, n), (0, 0, 255), 6)
winname = "Demo19.01"
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
