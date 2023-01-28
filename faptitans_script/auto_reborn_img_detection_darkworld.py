import pyautogui
import time
import script_utils

from datetime import datetime
from pynput import keyboard

# 关闭安全模式
pyautogui.FAILSAFE = False
# 延迟设置
pyautogui.PAUSE = 0.0001

hero_lv_up = "detection_img/hero_lv_up_darkworld.png"
boss_darkworld = "detection_img/boss_darkworld.png"
minion = "detection_img/minion.png"
skill_01 = "detection_img/skill_01.png"
skill_04 = "detection_img/skill_04.png"
to_darkworld = "detection_img/to_darkworld.png"
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

boss_count = 0
while switch:
    print(datetime.now())
    time.sleep(1)
    if pause:
        continue

    # 是否有遮罩层
    click_able = script_utils.click_able()
    if not click_able:
        # 关闭弹窗
        script_utils.close_prompt()

    # 鼠标移动到某个不影响图片判断的位置
    script_utils.back_position()

    # 先切换到dark world
    click_result = script_utils.click_img(img_path=to_darkworld)
    if click_result:
        continue

    # 先处理技能(不需要)

    # 英雄升级
    click_result = script_utils.click_img(img_path=hero_lv_up)
    if click_result:
        continue

    # 处理boss再现
    boss_count += 1
    if boss_count >= 20:
        boss_count = 0
        script_utils.click_img(img_path=boss_darkworld)
