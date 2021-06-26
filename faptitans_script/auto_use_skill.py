# encoding=UTF-8

import pyautogui
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

xy_skill1 = (-985, 271)
xy_skill2 = (-985, 340)
xy_skill3 = (-985, 413)
xy_skill4 = (-985, 473)
xy_skill5 = (-985, 553)
xy_skill6 = (-985, 613)
xy_skill7 = (-985, 694)
xy_boss = (-685, 547)
xy_level_up_top1 = (-1364, 444)
xy_close_reward = (-935, 433)
xy_close_rank_change = (-706, 211)


def skill_click(xy):
    pyautogui.moveTo(xy[0], xy[1], duration=0.2)
    pyautogui.click()


def skill_click_all():
    # 关闭收集奖励/排名变化
    skill_click(xy_close_rank_change)
    skill_click(xy_close_reward)
    skill_click(xy_close_reward)
    skill_click(xy_close_rank_change)
    # 点击再现boss
    skill_click(xy_boss)
    # 开始点击技能
    skill_click(xy_skill2)
    skill_click(xy_skill3)
    skill_click(xy_skill5)
    skill_click(xy_skill6)
    # 最后点技能7,4,1,防止弹出排名
    skill_click(xy_skill4)
    skill_click(xy_skill7)
    skill_click(xy_skill1)


def skill_click_1():
    # 关闭收集奖励/排名变化
    skill_click(xy_close_rank_change)
    skill_click(xy_close_reward)
    skill_click(xy_close_reward)
    skill_click(xy_close_rank_change)
    # 点技能1
    skill_click(xy_skill1)
    # 升级
    skill_click(xy_level_up_top1)


def job_auto_use_skill_all():
    now = datetime.now()
    sss = now.strftime('%Y-%m-%d %H:%M:%S') + " => use skill all"
    print('*' * 20, sss, '*' * 20)
    skill_click_all()


def job_auto_use_skill1():
    now = datetime.now()
    sss = now.strftime('%Y-%m-%d %H:%M:%S') + " => use skill 1"
    print('*' * 20, sss, '*' * 20)
    skill_click_1()


if __name__ == '__main__':
    arr = []
    for i in range(60):
        if i % 3 == 0:
            arr.append(i)
    print(arr)

    job_auto_use_skill_all()

    scheduler = BlockingScheduler()
    scheduler.add_job(job_auto_use_skill_all, 'cron', minute='0/20')
    scheduler.add_job(job_auto_use_skill1, 'cron', minute='3, 6, 9, 12, 15, 24, 27, 30, 33, 36, 45, 48, 51, 54')
    scheduler.start()


