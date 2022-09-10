import pyautogui
import time
from datetime import datetime
from pynput import keyboard

switch = True


def on_press(key):
    print(key)
    if key == keyboard.Key.esc:
        global switch
        switch = False
        return False


switch = True
keyboard.Listener(on_press=lambda x: x).start()
while switch:
    time.sleep(1)
    print(datetime.now())
