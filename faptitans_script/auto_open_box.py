import pyautogui
import time
import os

from datetime import datetime
from pynput import keyboard

# 关闭安全模式
pyautogui.FAILSAFE
# 延迟设置
pyautogui.PAUSE = 0.0001

confidence = 0.9
box_open = "detection_img/box_open.png"
box_free = "detection_img/box_free.png"
box_next = "detection_img/box_next.png"
box_take = "detection_img/box_take.png"


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

    # 开箱子
    location = pyautogui.locateOnScreen(image=box_free, confidence=confidence)
    if location is not None:
        x, y = pyautogui.center(location)
        pyautogui.leftClick(x, y)
        continue

    # 下一组箱子
    location = pyautogui.locateOnScreen(image=box_next, confidence=confidence)
    if location is not None:
        x, y = pyautogui.center(location)
        pyautogui.leftClick(x, y)
        continue

    # 收集图片
    location = pyautogui.locateOnScreen(image=box_take, confidence=confidence)
    if location is not None:
        x, y = pyautogui.center(location)
        pyautogui.leftClick(x, y)
        continue

    # 关闭遮罩层
    close_list = get_close_img_list()
    for close_path in close_list:
        close_location = pyautogui.locateOnScreen(image=close_path, confidence=confidence)
        if close_location is not None:
            x, y = pyautogui.center(close_location)
            pyautogui.leftClick(x, y)

    # 进入开箱子界面
    location = pyautogui.locateOnScreen(image=box_open, confidence=confidence)
    if location is not None:
        x, y = pyautogui.center(location)
        pyautogui.leftClick(x, y)
        continue
