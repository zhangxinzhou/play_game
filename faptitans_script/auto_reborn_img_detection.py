import pyautogui
import time
import os

from datetime import datetime
from pynput import keyboard

# 关闭安全模式
pyautogui.FAILSAFE
# 延迟设置
pyautogui.PAUSE = 0.0001

hero_lv_up = "detection_img/hero_lv_up.png"
boss = "detection_img/boss.png"
skill_01 = "detection_img/skill_01.png"
skill_04 = "detection_img/skill_04.png"
skill_interval_y_axis = 70


def get_close_img_list():
    dir_path = "detection_img"
    img_list = os.listdir(dir_path)
    close_img_list = []
    for img in img_list:
        if img.startswith("close"):
            close_img_list.append(os.path.join(dir_path, img))
    return close_img_list


# 开关,控制,如果监听到esc按键被按下,整个程序就会停止
switch = True


def on_press(key):
    if key == keyboard.Key.esc:
        global switch
        switch = False
        return False


listener = keyboard.Listener(on_press=on_press)
listener.start()

while switch:
    print(datetime.now())
    time.sleep(1)
    # 先技能
    hero_lv_up_location = pyautogui.locateOnScreen(image=hero_lv_up)
    sk01_location = pyautogui.locateOnScreen(image=skill_01)
    sk04_location = pyautogui.locateOnScreen(image=skill_04)

    #  技能处理
    if sk04_location is not None and sk01_location is not None:
        # 如果技能4ok,技能1ok,则点击技能1~7
        x, y = pyautogui.center(sk01_location)
        pyautogui.leftClick(x, y + skill_interval_y_axis * (7 - 1))
        pyautogui.leftClick(x, y + skill_interval_y_axis * (1 - 1))
        pyautogui.leftClick(x, y + skill_interval_y_axis * (2 - 1))
        pyautogui.leftClick(x, y + skill_interval_y_axis * (3 - 1))
        pyautogui.leftClick(x, y + skill_interval_y_axis * (4 - 1))
        pyautogui.leftClick(x, y + skill_interval_y_axis * (5 - 1))
        pyautogui.leftClick(x, y + skill_interval_y_axis * (6 - 1))
        # 处理boss再现
        boss_location = pyautogui.locateOnScreen(image=boss)
        if boss_location is not None:
            x, y = pyautogui.center(boss_location)
            pyautogui.leftClick(x, y)
        continue
    elif sk04_location is not None and sk01_location is not None:
        # 如果技能4ok,技能1不ok,则等待技能(什么都不做)
        pass
    elif sk01_location is not None:
        # 如果技能1ok,则点击技能1
        x, y = pyautogui.center(sk01_location)
        pyautogui.leftClick(x, y)
        # 处理boss再现
        boss_location = pyautogui.locateOnScreen(image=boss)
        if boss_location is not None:
            x, y = pyautogui.center(boss_location)
            pyautogui.leftClick(x, y)
        continue

    # 处理技能升级
    if hero_lv_up_location is not None:
        x, y = pyautogui.center(hero_lv_up_location)
        pyautogui.leftClick(x, y)
        continue

    # 关闭遮罩层
    close_list = get_close_img_list()
    for close_path in close_list:
        close_location = pyautogui.locateOnScreen(image=close_path, confidence=0.9)
        if close_location is not None:
            x, y = pyautogui.center(close_location)
            pyautogui.leftClick(x, y)
