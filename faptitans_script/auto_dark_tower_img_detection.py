import pyautogui
import time
import os

from datetime import datetime

# 关闭安全模式
pyautogui.FAILSAFE

confidence = 0.95
tower_go = "detection_img/tower_go.png"
tower_relic = "detection_img/tower_relic.png"
skill_01 = "detection_img/skill_01.png"
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
    print(datetime.now())
    time.sleep(1)

    # 点击go
    location = pyautogui.locateOnScreen(image=tower_go, confidence=confidence)
    if location is not None:
        x, y = pyautogui.center(location)
        pyautogui.leftClick(x, y)
        continue

    # 打开箱子
    location = pyautogui.locateOnScreen(image=tower_relic, confidence=confidence)
    if location is not None:
        x, y = pyautogui.center(location)
        pyautogui.leftClick(x, y)
        continue

    # 技能1
    location = pyautogui.locateOnScreen(image=skill_01, confidence=confidence)
    if location is not None:
        x, y = pyautogui.center(location)
        pyautogui.leftClick(x, y)
        continue

    # 关闭遮罩层
    img_path_list = get_close_img_list()
    for img_path in img_path_list:
        location = pyautogui.locateOnScreen(image=img_path, confidence=confidence)
        if location is not None:
            x, y = pyautogui.center(location)
            pyautogui.leftClick(x, y)
            continue
