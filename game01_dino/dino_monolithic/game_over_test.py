import cv2

# 判断中间白色占比超过50%即可
mat = cv2.imread("buff.jpg")

cv2.imshow('window', mat)
cv2.waitKey()
