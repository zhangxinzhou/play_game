import numpy as np
from PyQt5.QtWidgets import QApplication
import os
import win32gui
import sys
import cv2
import time
import datetime
import threading
from concurrent.futures import ThreadPoolExecutor
from getkeys import key_check
from keys_control import key_to_index

game_title = r'Grand Theft Auto V'
hwnd = win32gui.FindWindow(None, game_title)
if hwnd == 0:
    print('can not find [{}]'.format(game_title))
    print('exit')
    exit()
app = QApplication(sys.argv)
screen = app.primaryScreen()

