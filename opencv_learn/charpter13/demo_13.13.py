import cv2
import matplotlib.pylab as plt

imgRGB = cv2.imread(r"..\lena.jpg")
img = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2GRAY)

cv2.imshow("img", img)
cv2.imshow("imgRGB", imgRGB)

plt.figure("显示结果")
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(imgRGB)
plt.axis("off")
plt.show()
