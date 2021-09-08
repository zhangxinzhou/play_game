import cv2
import numpy as np
import matplotlib.pylab as plt

original_img = cv2.imread(r"..\lena.jpg", 0)
# 傅里叶变换,图像=>负数数组(频谱信息)
original_fft = np.fft.fft2(original_img)
# 原始频谱中的零频率分量移动到频域图像的中心位置
original_fft_shift = np.fft.fftshift(original_fft)

original_fft_ = 20 * np.log(np.abs(original_fft))
original_fft_shift_ = 20 * np.log(np.abs(original_fft_shift))

plt.subplot(1, 3, 1)
plt.imshow(original_img, cmap='gray')
plt.title("original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(original_fft_, cmap='gray')
plt.title("original_fft_")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(original_fft_shift_, cmap='gray')
plt.title("original_fft_shift_")
plt.axis("off")

plt.show()
