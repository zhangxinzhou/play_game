import numpy as np
import cv2

while True:
    img = np.random.randint(0, 256, size=[256, 256], dtype=np.uint8)
    cv2.imshow("demo", img)
    key = cv2.waitKey(100)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
