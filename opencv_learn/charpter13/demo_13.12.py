import cv2
import matplotlib.pylab as plt

img = cv2.imread(r"..\lena.jpg", cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)
cv2.imshow("original", img)
cv2.imshow("result", equ)
plt.subplot(1, 2, 1)
plt.hist(img.ravel(), 256)
plt.subplot(1, 2, 2)
plt.hist(equ.ravel(), 256)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
