import pyautogui
import time
import os

from datetime import datetime
from pynput import keyboard

# 关闭安全模式
pyautogui.FAILSAFE

confidence = 0.95
tower_go = "detection_img/tower_go.png"
tower_relic = "detection_img/tower_relic.png"
tower_add_time = "detection_img/tower_add_time.png"
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


# 开关,控制,如果监听到esc按键被按下,整个程序就会停止
switch = True


def on_press(key):
    if key == keyboard.Key.esc:
        global switch
        switch = False
        return False


listener = keyboard.Listener(on_press=on_press)
listener.start()

count = 0
while switch:
    print(datetime.now())
    time.sleep(1)

    # 点击go
    location = pyautogui.locateOnScreen(image=tower_go, confidence=confidence)
    if location is not None and count < 10:
        x, y = pyautogui.center(location)
        pyautogui.leftClick(x, y)
        count += 1
        continue
    count = 0

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

    # 主动点击
    location = pyautogui.locateOnScreen(image=tower_add_time, confidence=confidence)
    if location is not None:
        x, y = pyautogui.center(location)
        pyautogui.click(x, y - 100, clicks=11, interval=0.01)
        continue

    # 关闭遮罩层
    img_path_list = get_close_img_list()
    for img_path in img_path_list:
        location = pyautogui.locateOnScreen(image=img_path, confidence=confidence)
        if location is not None:
            x, y = pyautogui.center(location)
            pyautogui.leftClick(x, y)
            continue
