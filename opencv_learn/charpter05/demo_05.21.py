import cv2
import numpy as np

img = np.random.randint(0, 256, size=[8, 8], dtype=np.uint8)
rows, cols = img.shape[:2]
mapx = np.zeros(img.shape[:2], np.float32)
mapy = np.zeros(img.shape[:2], np.float32)
for i in range(rows):
    for j in range(cols):
        if 0.25 * cols < i < 0.75 * cols and 0.25 * rows < j < 0.75 * rows:
            mapx.itemset((i, j), 2 * (j - cols * 0.25) + 0.5)
            mapy.itemset((i, j), 2 * (i - rows * 0.25) + 0.5)
        else:
            mapx.itemset((i, j), 0)
            mapy.itemset((i, j), 0)
rst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

print("img=\n", img)
print("mapx=\n", mapx)
print("mapy=\n", mapy)
print("rst=\n", rst)
