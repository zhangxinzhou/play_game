import pyautogui
import time
import script_utils

from datetime import datetime
from pynput import keyboard

# 关闭安全模式
pyautogui.FAILSAFE = False
# 延迟设置
pyautogui.PAUSE = 0.0001

confidence = 0.9
box_open = "detection_img/box_open.png"
box_free = "detection_img/box_free.png"
box_next = "detection_img/box_next.png"
box_take = "detection_img/box_take.png"
error = "detection_img/prompt_lv00_08.png"

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

    # 错误
    click_result = script_utils.click_img(img_path=error)
    if click_result:
        continue

    # 开箱子
    click_result = script_utils.click_img(img_path=box_free)
    if click_result:
        continue

    # 下一组箱子
    click_result = script_utils.click_img(img_path=box_next)
    if click_result:
        continue

    # 收集图片
    click_result = script_utils.click_img(img_path=box_take)
    if click_result:
        continue

    # 关闭弹窗
    script_utils.close_prompt()

    # 进入开箱子界面
    click_result = script_utils.click_img(img_path=box_open)
    if click_result:
        continue
