# encoding=UTF-8
import time

import pyautogui
import random
from datetime import datetime

xy_tower = (-685, 637)
xy_choose_relic = [(-1158, 530), (-961, 530), (-754, 530)]
xy_close_relic = (-654, 197)
xy_close_rank_change = (-706, 211)


def click_tower():
    time.sleep(5)
    pyautogui.moveTo(xy_tower[0], xy_tower[1])
    pyautogui.click()


def click_relic():
    time.sleep(1)
    xy_relic = random.choice(xy_choose_relic)
    # 点击relic
    pyautogui.moveTo(xy_relic[0], xy_relic[1])
    pyautogui.click()
    # 关闭relic
    time.sleep(0.5)
    pyautogui.moveTo(xy_close_relic[0], xy_close_relic[1])
    pyautogui.click()
    # 关闭执行变更
    time.sleep(0.5)
    pyautogui.moveTo(xy_close_rank_change[0], xy_close_rank_change[1])
    pyautogui.click()


def job_dark_tower():
    now = datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    count = 5
    while count > 0:
        count = count - 1
        click_tower()
    click_relic()


if __name__ == '__main__':
    tmp = 100
    while tmp > 0:
        time.sleep(0.1)
        job_dark_tower()
