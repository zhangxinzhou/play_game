import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"..\lena.jpg", 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
mask = np.zeros((rows, cols, 2), np.uint8)
# 两个通道,与频域图像匹配
mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1
fShift = dftShift * mask
ishift = np.fft.ifftshift(fShift)
iImg = cv2.idft(ishift)
iImg = cv2.magnitude(iImg[:, :, 0], iImg[:, :, 1])

plt.subplot(1, 3, 1)
plt.imshow(img, cmap="gray")
plt.title("original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(iImg, cmap="gray")
plt.title("inverse")
plt.axis("off")

plt.show()
