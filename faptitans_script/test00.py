import pyautogui
import time
from pynput import keyboard

switch = True


def on_press(key):
    if key == keyboard.Key.esc:
        global switch
        switch = False
        return False


listener = keyboard.Listener(on_press=on_press)
listener.start()

while switch:
    time.sleep(1)
    print("aaa")
