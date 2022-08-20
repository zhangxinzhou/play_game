import pyautogui
import time
import os

from datetime import datetime

tower_go = "detection_img/tower_go.png"
tower_relic = "detection_img/tower_relic.png"
tower_close_01 = "detection_img/tower_close_01.png"


def get_close_img_list():
    dir_path = "detection_img"
    img_list = os.listdir(dir_path)
    close_img_list = []
    for img in img_list:
        if img.startswith("tower_close"):
            close_img_list.append(os.path.join(dir_path, img))
    return close_img_list


while True:
    time.sleep(1)

    location = pyautogui.locateOnScreen(image=tower_go, confidence=0.9)
    if location is not None:
        x, y = pyautogui.center(location)
        pyautogui.leftClick(x, y)
        continue

    location = pyautogui.locateOnScreen(image=tower_relic, confidence=0.9)
    if location is not None:
        x, y = pyautogui.center(location)
        pyautogui.leftClick(x, y)
        continue

    # 关闭遮罩层
    img_path_list = get_close_img_list()
    for img_path in img_path_list:
        location = pyautogui.locateOnScreen(image=img_path, confidence=0.9)
        if location is not None:
            x, y = pyautogui.center(location)
            pyautogui.leftClick(x, y)
            continue
