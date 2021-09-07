import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"..\lena.jpg", 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
ishift = np.fft.ifftshift(dftShift)
iImg = cv2.idft(ishift)
iImg = cv2.magnitude(iImg[:, :, 0], iImg[:, :, 1])

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(iImg, cmap="gray")
plt.title("result")
plt.axis("off")

plt.show()

print(img)
print("=" * 100)
print(iImg)
