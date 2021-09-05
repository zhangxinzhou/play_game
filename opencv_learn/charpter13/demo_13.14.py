import cv2
import matplotlib.pylab as plt

o = cv2.imread(r"..\lena.jpg")
g = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)

cv2.imshow("g", g)
cv2.imshow("o", o)

plt.figure("显示结果")

plt.subplot(2, 3, 1)
plt.imshow(o)
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(o, cmap=plt.cm.gray)
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(g)
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(g, cmap=plt.cm.gray)
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.show()
