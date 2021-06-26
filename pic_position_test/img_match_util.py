from PyQt5.QtWidgets import QApplication
import win32gui
import cv2
import sys

screen_path = "screen.png"
img0 = cv2.imread('img0.png')


def get_hwnd(app_title):
    return win32gui.FindWindow(None, app_title)


def get_screen(hwnd):
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    q_pix_map = screen.grabWindow(hwnd)
    q_pix_map.save(screen_path)
    # return cv2.imread(screen_path)


def get_position(screen, img):
    screen_height, screen_width = screen.shape[:2]
    img_height, img_width = img.shape[:2]
    # 执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(img, screen, cv2.TM_SQDIFF_NORMED)
    # 归一化处理
    cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)
    # 寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 匹配值转换为字符串
    # 对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    # 对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    position = (min_loc[0] + screen_width, min_loc[1] + screen_height)
    return position


if __name__ == '__main__':
    app_title = "Fap Titans - Google Chrome"
    app_title = '下议院II'
    hwnd = get_hwnd(app_title)
    if hwnd == 0:
        print("can not find the app_title, exit!")
        exit(-1)

    print(hwnd)
    screen = get_screen(hwnd)
    print(screen)

    position = get_position(screen, img0)
    print((position))
