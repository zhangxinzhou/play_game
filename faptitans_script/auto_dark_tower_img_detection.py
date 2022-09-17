import pyautogui
import time
import script_utils

from datetime import datetime
from pynput import keyboard

# 关闭安全模式
pyautogui.FAILSAFE = False
# 延迟设置
pyautogui.PAUSE = 0.0001

confidence = 0.95
tower_in = "detection_img/tower_in.png"
tower_go = "detection_img/tower_go.png"
tower_relic = "detection_img/tower_relic.png"
tower_add_time = "detection_img/tower_add_time.png"
skill_01 = "detection_img/skill_01.png"

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

    # 是否有遮罩层
    click_able = script_utils.click_able()
    if not click_able:
        # 进入dark tower
        click_result = script_utils.click_img(img_path=tower_in)
        if click_result:
            continue

        # 打开箱子
        click_result = script_utils.click_img(img_path=tower_relic)
        if click_result:
            continue

        # 关闭弹窗
        script_utils.close_prompt()
    else:
        # 点击go
        click_result = script_utils.click_img(img_path=tower_go)
        if click_result and count < 10:
            count += 1
            continue
        count = 0

        # 技能1
        click_result = script_utils.click_img(img_path=skill_01)
        if click_result:
            continue

        # 主动点击
        location = pyautogui.locateOnScreen(image=tower_add_time, confidence=confidence)
        if location is not None:
            x, y = pyautogui.center(location)
            pyautogui.click(x, y - 100, clicks=11, interval=0.01)
            continue
