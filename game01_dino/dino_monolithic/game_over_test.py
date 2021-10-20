import cv2
import numpy as np


# 判断中间白色占比超过50%即可
def is_game_over(img):
    return np.mean(img[100:130, 230:270, :]) > 125


if __name__ == '__main__':
    mat = cv2.imread("buff.jpg")
    is_game_over = is_game_over(mat)
    print(is_game_over)
