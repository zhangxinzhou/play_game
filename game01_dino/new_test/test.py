import keyboard
import time
from keyboard._keyboard_event import KeyboardEvent

stop = True


def game_exit(key_event: KeyboardEvent):
    global stop
    print(type(key_event))
    stop = False


keyboard.hook_key("esc", game_exit)

for i in range(10):
    print(stop)
    time.sleep(2)
