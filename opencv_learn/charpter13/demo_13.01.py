import cv2
import matplotlib.pylab as plt

o = cv2.imread(r"..\lena.jpg")
cv2.imshow("original", o)
plt.hist(o.ravel(), 256)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
