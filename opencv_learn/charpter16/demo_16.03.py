import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("chess.jpeg", 0)
imgo = cv2.imread("chess.jpeg", -1)
o = cv2.cvtColor(imgo, cv2.COLOR_BGR2RGB)
oshow = o.copy()
img = cv2.medianBlur(img, 5)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 200, param1=50, param2=30, minRadius=100, maxRadius=200)

for i in circles[0, :]:
    print(i)
    center = (int(i[0]), int(i[1]))
    cv2.circle(o, center, int(i[2]), (255, 0, 0), 12)
    cv2.circle(o, center, 2, (255, 0, 0), 12)

plt.subplot(121)
plt.imshow(oshow)
plt.axis("off")
plt.subplot(122)
plt.imshow(o)
plt.axis("off")
plt.show()
