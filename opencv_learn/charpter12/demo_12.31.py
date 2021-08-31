import cv2
import numpy as np

o = cv2.imread("cc.bmp")
cv2.imshow("original", o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(o, contours[0], -1, (0, 0, 255), 3)
cntArea = cv2.contourArea(contours[0])
equiDiameter = np.sqrt(4 * cntArea / np.pi)
print(equiDiameter)

cv2.circle(o, (150, 150), int(equiDiameter / 2), (0, 0, 255), 3)

cv2.imshow("result", o)
cv2.waitKey()
cv2.destroyAllWindows()
