import cv2
import matplotlib.pylab as plt

o = cv2.imread(r"..\lena.jpg")
plt.hist(o.ravel(), 16)
plt.show()
print("o=\n", o)
print("o.shape=\n", o.shape)
print("o.ravel()=\n", o.ravel())
print("o.ravel().shape=\n", o.ravel().shape)
