# encoding=utf-8

import time
import datetime
import pyautogui
import script_utils

# 关闭安全模式
pyautogui.FAILSAFE

# =====坐标=====
# 基准xy(偏移量 )
base_xy = (360, 103)
# 图片宽度
img_width = 1200
# 图片高度
img_height = 640
# 图片区域
img_region = (base_xy[0], base_xy[1], img_width, img_height)

# 英雄坐标
hero_base_xy = (150, 340)
hero_offset_x = 240
hero_offset_y = 140
hero_top01_xy = (hero_base_xy[0], hero_base_xy[1])
hero_top02_xy = (hero_base_xy[0] + hero_offset_x, hero_base_xy[1])
hero_top03_xy = (hero_base_xy[0], hero_base_xy[1] + hero_offset_y)
hero_top04_xy = (hero_base_xy[0] + hero_offset_x, hero_base_xy[1] + hero_offset_y)
hero_list = [hero_top01_xy, hero_top02_xy, hero_top03_xy, hero_top04_xy]

# 再现boss
boss_xy = (858, 442)

# 技能坐标
skill_base_xy = (545, 140)
skill_offset_x = 0
skill_offset_y = 71
skill01_xy = (skill_base_xy[0] + skill_offset_x, skill_base_xy[1] + skill_offset_y * 0)
skill02_xy = (skill_base_xy[0] + skill_offset_x, skill_base_xy[1] + skill_offset_y * 1)
skill03_xy = (skill_base_xy[0] + skill_offset_x, skill_base_xy[1] + skill_offset_y * 2)
skill04_xy = (skill_base_xy[0] + skill_offset_x, skill_base_xy[1] + skill_offset_y * 3)
skill05_xy = (skill_base_xy[0] + skill_offset_x, skill_base_xy[1] + skill_offset_y * 4)
skill06_xy = (skill_base_xy[0] + skill_offset_x, skill_base_xy[1] + skill_offset_y * 5)
skill07_xy = (skill_base_xy[0] + skill_offset_x, skill_base_xy[1] + skill_offset_y * 6)

# 判断遮罩层的坐标
shade_cover_xy = (1140, 580)

# =====颜色=====
hero_ok_color = (151, 212, 80)
skill_ok_color = (246, 233, 184)
shade_cover_color = (115, 115, 115)


# 点击坐标=基准坐标+根据图形获取的坐标
def get_click_xy(xy):
    result = (base_xy[0] + xy[0], base_xy[1] + xy[1])
    return result


# 游戏截图
def get_img():
    return pyautogui.screenshot('screen.png', img_region)


# 关闭弹窗
# TODO 待实现
def find_close_button_position():
    # 通过open_cv找到弹窗关闭按钮的位置
    pop_xy = (0, 0)
    return pop_xy


# 处理遮罩层
def handle_shade_cover():
    # 尝试次数
    try_times = 10
    for i in try_times:
        img = get_img()
        is_cover = script_utils.img_position_match_color(img, shade_cover_xy, shade_cover_color)
        if is_cover:
            close_button_xy = find_close_button_position(img)
            click_xy = get_click_xy(close_button_xy)
            pyautogui.click(click_xy)
        else:
            break

    # 如果尝试了N次,仍然无法关闭弹窗,则使用终极大发,F5刷新页面,然后再关闭弹窗
    pyautogui.press("f5")
    time.sleep(10)
    # 再来关闭一遍弹窗
    for i in try_times:
        img = get_img()
        is_cover = script_utils.img_position_match_color(img, shade_cover_xy, shade_cover_color)
        if is_cover:
            close_button_xy = find_close_button_position(img)
            click_xy = get_click_xy(close_button_xy)
            pyautogui.click(click_xy)
        else:
            break

    # 如果还是不行,则保存当时出问题的截图,然后程序退出
    pyautogui.screenshot('exception.png', img_region)
    exit(-1)


# 爬塔
def handle_dark_tower():
    # 如果有遮罩层,先处理遮罩层
    # handle_shade_cover()

    pass


def handle_game():
    pass


if __name__ == '__main__':
    while True:
        handle_game()
        print(datetime.datetime.now())
        time.sleep(10)
