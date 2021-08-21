import cv2
import numpy as np

o = cv2.imread('Sobel4.bmp', cv2.IMREAD_GRAYSCALE)
# error: (-215:Assertion failed) dx >= 0 && dy >= 0 && dx+dy == 1 in function 'cv::getScharrKernels'
Scharrxy11 = cv2.Scharr(o, cv2.CV_64F, 1, 1)
cv2.imshow("original", o)
cv2.imshow("xy11", Scharrxy11)
cv2.waitKey()
cv2.destroyAllWindows()
