import cv2
import numpy as np

n = 300
img = np.zeros((n, n, 3), np.uint8) * 255
img = cv2.rectangle(img, (50, 50), (n - 100, n - 50), (0, 0, 255), -1)

winname = "Demo19.01"
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
