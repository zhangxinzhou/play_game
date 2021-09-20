import cv2
import numpy as np
import matplotlib.pylab as plt

o = cv2.imread(r"..\lena.jpg")
orgb = cv2.cvtColor(o, cv2.COLOR_BGR2RGB)
mask = np.zeros(o.shape[:2], np.uint8)
bgd = np.zeros((1, 65), np.float64)
fgd = np.zeros((1, 65), np.float64)
rect = (50, 50, 550, 700)
cv2.grabCut(o, mask, rect, bgd, fgd, 5, cv2.GC_INIT_WITH_RECT)
mask2 = cv2.imread("mask.jpg", 0)
mask2Show = cv2.imread("mask.jpg", -1)
m2rgb = cv2.cvtColor(mask2Show, cv2.COLOR_BGR2RGB)
mask[mask2 == 0] = 0
mask[mask2 == 255] = 1
mask, bgd, fgd = cv2.grabCut(o, mask, None, bgd, fgd, 5, cv2.GC_INIT_WITH_MASK)
mask = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
ogc = o * mask[:, :, np.newaxis]
ogc = cv2.cvtColor(ogc, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.imshow(orgb)
plt.axis("off")
plt.subplot(122)
plt.imshow(ogc)
plt.axis("off")
plt.show()
