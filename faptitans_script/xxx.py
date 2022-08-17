import pyautogui
import time

for i in range(100):
    img_location = pyautogui.locateOnScreen(image="detection_img/hero_level_up.png")
    if img_location:
        x, y = pyautogui.center(img_location)
        pyautogui.leftClick(x, y)
        print(img_location)
        print(type(img_location))
