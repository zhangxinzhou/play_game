import cv2
import matplotlib.pylab as plt

o = cv2.imread(r"..\lena.jpg")
histB = cv2.calcHist([o], [0], None, [256], [0, 255])
plt.plot(histB)
plt.show()
