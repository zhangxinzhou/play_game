import cv2
import numpy as np
import matplotlib.pylab as plt

image = cv2.imread(r"..\lena.jpg", cv2.IMREAD_GRAYSCALE)
mask = np.zeros(image.shape, np.uint8)
mask[200:400, 200:400] = 255
histImage = cv2.calcHist([image], [0], None, [256], [0, 255])
histMI = cv2.calcHist([image], [0], mask, [256], [0, 255])
plt.plot(histImage, color='r')
plt.plot(histMI, color='g')
plt.show()
