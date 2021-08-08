import cv2

img = cv2.imread(r"..\lena.jpg")
rows, cols = img.shape[:2]
size = (int(cols * 0.9), int(rows * 0.5))
rst = cv2.resize(img, size)
print(size)
print("img.shape=", img.shape)
print("rst.shape=", rst.shape)
