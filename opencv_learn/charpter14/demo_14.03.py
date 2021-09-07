import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread(r"..\lena.jpg", 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0
ishift = np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(iimg, cmap="gray")
plt.title("result")
plt.axis("off")

plt.show()

print(img)
print("=" * 100)
print(iimg)
