import cv2

gray = cv2.imread(r"..\lena.jpg", 0)
color = cv2.imread(r"..\lena.jpg")
print("图形gray属性:")
print("gray.shape=", gray.shape)
print("gray.size=", gray.size)
print("gray.dtype=", gray.dtype)
print("图形color属性:")
print("color.shape=", color.shape)
print("color.size=", color.size)
print("color.dtype=", color.dtype)
