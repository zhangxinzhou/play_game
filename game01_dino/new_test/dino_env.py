from abc import ABC

from game_env import GameEnv
from PyQt5.QtWidgets import QApplication
import numpy as np
import random
import cv2
import gc
import time
import win32gui
import sys
import game_utils
import pyautogui

# 延迟时间修改
pyautogui.PAUSE = 0.0001
# 游戏标题
game_title = r'chrome://dino/ - Google Chrome'
# 获取window句柄
handle = win32gui.FindWindow(None, game_title)
if handle == 0:
    print("=" * 100)
    print(f'find game [{game_title}] fail')
    print('exit!!!')
    print("=" * 100)
    exit()
else:
    print("=" * 100)
    print(f"find game [{game_title}] success, handle = [{handle}]")
    print("=" * 100)

width = 500
height = 350
left, top, right, bottom = win32gui.GetWindowRect(handle)
left_offset = left + 8
top_offset = top + 115
width_offset = width
height_offset = height - 155
game_over_detection_position1 = (135, 55)
game_over_detection_position2 = (365, 75)

# 不修改坐标,修改游戏窗口尺寸
win32gui.MoveWindow(handle, left, top, width, height, False)
# 聚焦游戏窗口
win32gui.SetForegroundWindow(handle)
app = QApplication(sys.argv)
# 主屏幕
screen = app.primaryScreen()


class DinoEnv(GameEnv, ABC):

    def __init__(self):
        self.game_frame_dim = width_offset * height_offset
        self.game_action_dim = 5
        self.q_pix_map = None
        self.game_frame = None
        self.game_frame_candy = None
        self.step_count = 0

        self.time_start = time.time()
        self.time_end = time.time()
        self.time_cost = 0

        self.action = None
        self.reward = None
        self.is_game_over = None
        # 最近四帧
        self.game_last4_frame = []
        # 最近四帧
        self.game_last4_frame_candy = []

    def step(self, action):
        # 0什么都不做
        # 1按住上
        # 2松开下
        # 3按住下
        # 4松开下
        if action == 1:
            pyautogui.keyDown('up')
        elif action == 2:
            pyautogui.keyUp('up')
        elif action == 3:
            pyautogui.keyUp('down')
        elif action == 4:
            pyautogui.keyDown('down')

        self.step_count += 1
        self.action = action
        self.q_pix_map = screen.grabWindow(0, left_offset, top_offset, width_offset, height_offset)
        self.game_frame = game_utils.qpixmap_to_array(self.q_pix_map)
        self.game_frame_candy = game_utils.img_to_candy(self.game_frame)

        # 奖励,乱动有惩罚
        self.reward = 1 if action == 0 else 0.8
        # 游戏是否结束,检测game over文字
        text_detection = self.game_frame_candy[
                         game_over_detection_position1[1]:game_over_detection_position2[1],
                         game_over_detection_position1[0]:game_over_detection_position2[0]
                         ]
        pixel_count = np.count_nonzero(text_detection)
        self.is_game_over = pixel_count >= 500

        time_current = time.time()
        self.time_cost = time_current - self.time_end
        self.time_end = time_current

        return self.game_frame, self.reward, self.is_game_over, self.step_count, self.time_cost

    def reset(self):
        gc.collect()
        print("=" * 50, "reset game", "=" * 50)
        pyautogui.press('up')
        self.step_count = 0
        self.time_start = time.time()
        self.time_end = time.time()

    def render(self):
        cv2.imshow("candy", self.game_frame_candy)
        cv2.waitKey(1)

    def close(self):
        # 关闭游戏
        pass

    def test_random_action(self):
        arr = [0, 1, 2, 3, 4]
        for i in range(5):
            print(f"episode: [{i}]")
            self.reset()
            while True:
                action = random.choice(arr)
                game_frame, reward, is_game_over, step_count, time_cost = self.step(action)
                print(
                    f"step_count={step_count}, game_frame.shape={game_frame.shape}, reward={reward}, is_game_over={is_game_over}, time_cost={int(time_cost * 1000)}ms")
                self.render()
                if is_game_over:
                    print("=" * 50, "game over", "=" * 50)
                    # 暂停两秒,因为游戏game over后有两秒时间无法操作
                    time.sleep(2)
                    break


if __name__ == '__main__':
    env = DinoEnv()
    env.test_random_action()
