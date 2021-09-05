import cv2
import matplotlib.pylab as plt

img = cv2.imread(r"..\lena.jpg", cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)
cv2.imshow("original", img)
cv2.imshow("result", equ)
plt.figure("原图图像的直方图")
plt.hist(img.ravel(), 256)
plt.figure("均衡化结果的直方图")
plt.hist(equ.ravel(), 256)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
