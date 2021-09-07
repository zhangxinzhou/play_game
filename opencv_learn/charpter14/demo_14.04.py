import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"..\lena.jpg", 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
result = 20 * np.log(cv2.magnitude(dftShift[:, :, 0], dftShift[:, :, 1]))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(result, cmap="gray")
plt.title("result")
plt.axis("off")

plt.show()
