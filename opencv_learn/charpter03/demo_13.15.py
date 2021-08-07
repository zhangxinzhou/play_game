import cv2
import numpy as np

# 读取原始图像
lena = cv2.imread(r"..\lena.jpg", 0)
# 读取水印
watermark = cv2.imread(r"..\watermark.bmp", 0)
# 将水印图像内的值255处理为1,以方便嵌入
w = watermark[:, :] > 0
watermark[w] = 1
# 读取原始载体图像的shape值
r, c = lena.shape
# ===========嵌入过程=============
# 生产元素值都是254的数组
t254 = np.ones((r, c), dtype=np.uint8) * 254
# 获取lena图像的高7位
lenaH7 = cv2.bitwise_and(lena, t254)
# 将watermark嵌入lenaH7内
e = cv2.bitwise_or(lenaH7, watermark)
# ===========提取过程=============
# 生成元素都是1的数组
t1 = np.ones((r, c), dtype=np.uint8)
# 从载体图像内提取水印图像
wm = cv2.bitwise_and(e, t1)
print(wm)
# 将水印图像内的1处理为255,以方便显示
w = wm[:, :] > 0
wm[w] = 255
# ===========显示=============
cv2.imshow("lena", lena)
cv2.imshow("watermark", watermark * 255)
cv2.imshow("e", e)
cv2.imshow("wm", wm)
cv2.waitKey()
cv2.destroyAllWindows()
