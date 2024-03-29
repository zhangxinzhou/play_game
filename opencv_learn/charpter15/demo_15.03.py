import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"..\lena_x4.jpg", 0)
template = cv2.imread(r"..\lena_eyes.png", 0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), 255, 1)
plt.imshow(img, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()
