import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread(r"..\lena.jpg", 0)
# 傅里叶变换,图像=>负数数组(频谱信息)
f = np.fft.fft2(img)
# 原始频谱中的零频率分量移动到频域图像的中心位置
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("original")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title("result")
plt.axis("off")
plt.show()
