import cv2
import matplotlib.pylab as plt

o = cv2.imread("8.bmp")
g = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)

plt.figure("灰度图像显示演示")

plt.subplot(2, 2, 1)
plt.imshow(g, cmap=plt.cm.gray)

plt.subplot(2, 2, 2)
plt.imshow(g, cmap=plt.cm.gray_r)

plt.subplot(2, 2, 3)
plt.imshow(g, cmap='gray')

plt.subplot(2, 2, 4)
plt.imshow(g, cmap='gray_r')

plt.show()
