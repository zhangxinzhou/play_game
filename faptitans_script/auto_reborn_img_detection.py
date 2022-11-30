import pyautogui
import time
import script_utils

from datetime import datetime
from pynput import keyboard

# 关闭安全模式
pyautogui.FAILSAFE = False
# 延迟设置
pyautogui.PAUSE = 0.0001

hero_lv_up = "detection_img/hero_lv_up.png"
boss = "detection_img/boss.png"
minion = "detection_img/minion.png"
skill_01 = "detection_img/skill_01.png"
skill_04 = "detection_img/skill_04.png"
skill_interval_y_axis = 70

# 开关,控制,如果监听到esc按键被按下,整个程序就会停止
switch = True
pause = False


def on_press(key):
    print(key)
    print(type(key))
    if key == keyboard.Key.esc:
        global switch
        switch = False
        print("*" * 50, f"监听到{key}按键被按下...", "*" * 50)
        print("*" * 50, "程序将在本次训练完毕后结束...", "*" * 50)
        return False
    elif key == keyboard.Key.tab:
        global pause
        pause = not pause
        if pause:
            print("*" * 50, f"监听到{key}按键被按下...", "*" * 50)
            print("*" * 50, "开始", "*" * 50)
        else:
            print("*" * 50, f"监听到{key}按键被按下...", "*" * 50)
            print("*" * 50, "暂停", "*" * 50)


listener = keyboard.Listener(on_press=on_press)
listener.start()

while switch:
    print(datetime.now())
    time.sleep(1)
    if pause:
        continue

    # 鼠标移动到某个不影响图片判断的位置
    script_utils.back_position()

    # 是否有遮罩层
    click_able = script_utils.click_able()
    if not click_able:
        # 关闭弹窗
        script_utils.close_prompt()
    else:
        # 先处理技能
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
            script_utils.click_img(img_path=boss)
            continue
        elif sk04_location is not None and sk01_location is not None:
            # 如果技能4ok,技能1不ok,则等待技能(什么都不做)
            pass
        elif sk01_location is not None:
            # 如果技能1ok,则点击技能1
            x, y = pyautogui.center(sk01_location)
            pyautogui.leftClick(x, y)
            # 处理boss再现
            script_utils.click_img(img_path=boss)
            continue

        # 英雄升级
        click_result = script_utils.click_img(img_path=hero_lv_up)
        if click_result:
            continue

        # 点击小怪
        minion_location = pyautogui.locateOnScreen(image=minion, confidence=0.9)
        if minion_location is not None:
            x, y = pyautogui.center(minion_location)
            pyautogui.leftClick(x - 50, y)
            pyautogui.moveTo(x=100, y=100)
