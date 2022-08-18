import pyautogui
import time
import os

from datetime import datetime

hero_lv_up = "detection_img/hero_lv_up.png"
skill_01 = "detection_img/skill_01.png"
skill_04 = "detection_img/skill_04.png"
skill_07 = "detection_img/skill_07.png"
skill_len = 70


def get_close_img_list():
    dir_path = "detection_img"
    img_list = os.listdir(dir_path)
    close_img_list = []
    for img in img_list:
        if img.startswith("close"):
            close_img_list.append(os.path.join(dir_path, img))
    return close_img_list


while True:
    print(datetime.now())
    time.sleep(1)
    # 关闭遮罩层
    close_list = get_close_img_list()
    for close_path in close_list:
        close_location = pyautogui.locateOnScreen(image=close_path)
        if close_location is not None:
            x, y = pyautogui.center(close_location)
            pyautogui.leftClick(x, y)

    # 先技能
    hero_lv_up_location = pyautogui.locateOnScreen(image=hero_lv_up)
    sk01_location = pyautogui.locateOnScreen(image=skill_01)
    sk04_location = pyautogui.locateOnScreen(image=skill_04)
    sk07_location = pyautogui.locateOnScreen(image=skill_07)
    if sk01_location is not None and sk04_location is not None and sk07_location is not None:
        x, y = pyautogui.center(sk01_location)
        for index in range(7):
            pyautogui.leftClick(x, y + skill_len * index)

    if hero_lv_up_location is not None:
        x, y = pyautogui.center(hero_lv_up_location)
        pyautogui.leftClick(x, y)

    if sk04_location is not None:
        if sk01_location is None:
            # 4技能OK,1技能不OK,啥都不干
            continue
    else:
        if sk01_location is not None:
            # 4技能不OK,1技能OK,使用1技能
            x, y = pyautogui.center(sk01_location)
            pyautogui.leftClick(x, y)
