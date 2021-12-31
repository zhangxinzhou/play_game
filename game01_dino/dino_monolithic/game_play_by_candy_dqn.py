import gc
import numpy as np
import win32gui
import time
import sys
import pyautogui
import cv2
from PyQt5.QtWidgets import QApplication
from public_utils import qpixmap_to_array
from concurrent.futures import ThreadPoolExecutor

import tensorflow as tf
from Deep_Q_Network import Deep_Q_Network

# tf2.x version  自适应显存占用
gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
for gpu in gpus:
    print(f"set gpu [{gpu}] memory growth")
    tf.config.experimental.set_memory_growth(gpu, True)

# 线程池
executor = ThreadPoolExecutor(max_workers=5)
# 游戏标题
game_title = r'chrome://dino/ - Google Chrome'
# 获取window句柄
handle = win32gui.FindWindow(None, game_title)
if handle == 0:
    print("=" * 100)
    print(f'can not find game [{game_title}]')
    print('exit!!!')
    print("=" * 100)
    exit()
else:
    print("=" * 100)
    print(f"success find game [{game_title}], handle = [{handle}]")
    print("=" * 100)

x0, y0, x1, y1 = win32gui.GetWindowRect(handle)
width = 500
height = 350
new_pos = (x0 + 8, y0 + 115, width, height - 155)
bird_pt1 = (100, 100)
bird_pt2 = (160, 120)
obstacle_pt1 = (100, 120)
obstacle_pt2 = (150, 150)
gm_pt1 = (135, 55)
gm_pt2 = (365, 75)

# 不修改坐标,修改游戏窗口尺寸
win32gui.MoveWindow(handle, x0, y0, width, height, False)
# 聚焦游戏窗口
win32gui.SetForegroundWindow(handle)

app = QApplication(sys.argv)
screen = app.primaryScreen()

# 行动空间
n_actions = 3
# 图像像素
n_features = new_pos[2] * new_pos[3]


# n_features = (None, new_pos[2], new_pos[3])


def game_over(game_frame):
    text_tmp = game_frame[gm_pt1[1]:gm_pt2[1], gm_pt1[0]:gm_pt2[0]]
    text_count = np.count_nonzero(text_tmp)
    return text_count >= 500


# 重置游戏,当game over之后,等待三秒,然后游戏重新开始
def game_reset():
    gc.collect()
    time.sleep(2)
    print("=" * 50, "reset game", "=" * 50)
    pyautogui.press('up')


def get_game_frame():
    q_pix_map = screen.grabWindow(0, new_pos[0], new_pos[1], new_pos[2], new_pos[3])
    game_frame = qpixmap_to_array.qpixmap_to_array(q_pix_map)
    return game_frame


# 行动,如果前方有障碍物就跳起来
def has_obstacle(image_candy):
    obstacle_img = image_candy[obstacle_pt1[1]:obstacle_pt2[1], obstacle_pt1[0]:obstacle_pt2[0]]
    bird_img = image_candy[bird_pt1[1]:bird_pt2[1], bird_pt1[0]:bird_pt2[0]]
    obstacle_count = np.count_nonzero(obstacle_img)
    bird_count = np.count_nonzero(bird_img)
    is_obstacle = obstacle_count >= 30
    is_bird = bird_count >= 30 and not is_obstacle
    return is_obstacle or is_bird


def get_reword(is_ob, do_action):
    # 无障碍物,采取行动0.1
    # 无障碍物,不行动1
    # 有障碍物,采取行动1
    if not is_ob and do_action > 0:
        return 0
    else:
        return 1


# 主程序
def main():
    RL = Deep_Q_Network(n_actions=n_actions, n_features=n_features)
    step = 0
    for episode in range(1000):
        game_reset()
        frame_previous = get_game_frame()
        gray_previous = cv2.cvtColor(frame_previous, cv2.COLOR_BGR2GRAY)
        candy_previous = cv2.Canny(gray_previous, 100, 200)
        input_matrix_previous = candy_previous.flatten() / 255.0
        print(input_matrix_previous.shape)
        print(input_matrix_previous)

        while True:
            t0 = time.time()
            action = RL.choose_action(input_matrix_previous)
            if action == 1:
                executor.submit(pyautogui.press, 'up')
            elif action == 2:
                executor.submit(pyautogui.press, 'down')

            # 当前帧
            frame_current = get_game_frame()
            gray_current = cv2.cvtColor(frame_current, cv2.COLOR_BGR2GRAY)
            candy_current = cv2.Canny(gray_current, 100, 200)
            input_matrix_current = candy_current.flatten() / 255.0
            # 游戏是否结束
            is_game_over = game_over(candy_current)
            # 奖励,只要活着就能得到奖励
            is_obstacle = has_obstacle(candy_current)
            reward = get_reword(is_obstacle, action)

            RL.store_transition(input_matrix_previous, action, reward, is_game_over, input_matrix_current)

            if (step > 200) and (step % 5 == 0):
                RL.learn()
                RL.soft_update(1)

            # 显示
            input_matrix_previous = input_matrix_current
            cv2.imshow("candy", candy_current)
            cv2.waitKey(1)

            t1 = time.time()
            print(f"action={action},is_obstacle={is_obstacle},reward={reward},cost=[{(t1 - t0) * 1000} ] ms")

            # break while loop when end of this episode
            if is_game_over:
                break
            step += 1
        print(f"episode {episode + 1}")
    # end of game
    print('game over')


if __name__ == '__main__':
    main()
