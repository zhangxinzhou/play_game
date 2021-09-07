import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread(r"..\lena.jpg", 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
ishift = np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(img, cmap="gray")
plt.title("iimg")
plt.axis("off")

plt.show()
