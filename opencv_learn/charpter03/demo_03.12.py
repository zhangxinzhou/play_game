import cv2
import numpy as np

img1 = np.zeros((4, 4), dtype=np.uint8) * 3
img2 = np.zeros((4, 4), dtype=np.uint8) * 5
img3 = cv2.add(img1, img2)
img4 = cv2.add(img1, 6)
img5 = cv2.add(6, img2)
print("img1=\n", img1)
print("img2=\n", img2)
print("img3=\n", img3)
print("img4=\n", img4)
print("img5=\n", img5)
