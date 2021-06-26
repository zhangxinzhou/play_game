# encoding=UTF-8

import pyautogui
import sys
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

window_offset = 1920

xy_skill1 = (window_offset - 985, 271)
xy_skill2 = (window_offset - 985, 340)
xy_skill3 = (window_offset - 985, 413)
xy_skill4 = (window_offset - 985, 473)
xy_skill5 = (window_offset - 985, 553)
xy_skill6 = (window_offset - 985, 613)
xy_skill7 = (window_offset - 985, 694)
xy_boss = (window_offset - 685, 547)
xy_level_up_top1 = (window_offset - 1367, 444)
xy_close_reward = (window_offset - 935, 433)
xy_close_rank_change = (window_offset - 706, 211)


def xy_click(xy):
    pyautogui.click(xy)


def window_clean():
    # 关闭收集奖励/排名变化
    xy_click(xy_close_rank_change)
    xy_click(xy_close_reward)
    xy_click(xy_close_reward)
    xy_click(xy_close_rank_change)


def hero_level_up():
    window_clean()
    # 打怪
    pyautogui.click(xy_boss[0], xy_boss[1] - 100, clicks=30, interval=0.1)
    # 购买/升级英雄
    xy_click(xy_level_up_top1)


def skill_click_all():
    # 关闭收集奖励/排名变化
    window_clean()
    # 购买/升级英雄
    pyautogui.click(xy_level_up_top1, clicks=5, interval=1)
    # 点击再现boss
    xy_click(xy_boss)
    # 开始点击技能
    xy_click(xy_skill2)
    xy_click(xy_skill3)
    xy_click(xy_skill5)
    xy_click(xy_skill6)
    # 最后点技能7,4,1,防止弹出排名
    xy_click(xy_skill4)
    xy_click(xy_skill7)
    xy_click(xy_skill1)


def job_hero_level_up():
    now = datetime.now()
    method_name = sys._getframe().f_code.co_name
    sss = now.strftime('%Y-%m-%d %H:%M:%S') + " => " + method_name
    print('*' * 20, sss, '*' * 20)
    hero_level_up()


def job_auto_use_skill_all():
    now = datetime.now()
    method_name = sys._getframe().f_code.co_name
    sss = now.strftime('%Y-%m-%d %H:%M:%S') + " => " + method_name
    print('*' * 20, sss, '*' * 20)
    skill_click_all()


if __name__ == '__main__':
    pyautogui.FAILSAFE = False
    scheduler = BlockingScheduler()
    # scheduler.add_job(job_hero_level_up, 'cron', second="7/20")
    scheduler.add_job(job_auto_use_skill_all, 'interval', minutes=12)
    scheduler.start()
