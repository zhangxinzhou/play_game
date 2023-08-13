import pyautogui
import time
import script_utils

from datetime import datetime
from pynput import keyboard

# 关闭安全模式
pyautogui.FAILSAFE = False
# 延迟设置
pyautogui.PAUSE = 0.0001

# 开关,控制,如果监听到esc按键被按下,整个程序就会停止
switch = True


def on_press(key):
    print(key)
    print(type(key))
    if key == keyboard.Key.esc:
        global switch
        switch = False
        print("*" * 50, f"监听到{key}按键被按下...", "*" * 50)
        print("*" * 50, "程序将在本次训练完毕后结束...", "*" * 50)
        return False
    elif key == keyboard.Key.space:
        print("*" * 50, f"监听到{key}按键被按下...", "*" * 50)
        print("*" * 50, "开始", "*" * 50)
        pyautogui.click(clicks=30)


# listener = keyboard.Listener(on_press=on_press)
# listener.start()
with keyboard.Listener(keys='', on_press=on_press) as listener:
    listener.join()
