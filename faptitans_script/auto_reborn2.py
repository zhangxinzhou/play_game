# encoding=UTF-8

import pyautogui


def handle_mask_layer():
    '''
    处理遮罩层
    :return:
    '''
    pass


def handle_hero():
    '''
    处理英雄 => 购买,升级英雄
    :return:
    '''
    pass


def handle_skill():
    '''
    处理技能
    :return:
    '''
    pass


def handle_game():
    # 检测是否有遮罩层
    have_mask_layer = True
    if have_mask_layer:
        # 处理遮罩层
        handle_mask_layer()
    else:
        handle_hero()
