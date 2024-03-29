import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"keyboard.jpg", -1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
orgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
oShow = orgb.copy()
lines = cv2.HoughLines(edges, 1, np.pi / 180, 140)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(orgb, (x1, y1), (x2, y2), (255, 0, 0), 5)

plt.subplot(121)
plt.imshow(oShow)
plt.axis("off")
plt.subplot(122)
plt.imshow(orgb)
plt.axis("off")
plt.show()
