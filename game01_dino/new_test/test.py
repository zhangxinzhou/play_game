# import keyboard
# import time
import random

# from keyboard._keyboard_event import KeyboardEvent
#
# stop = True
#
#
# def game_exit(key_event: KeyboardEvent):
#     global stop
#     print(type(key_event))
#     stop = False
#
#
# keyboard.hook_key("esc", game_exit)
#
# for i in range(10):
#     print(stop)
#     time.sleep(2)

if __name__ == '__main__':
    arr_old = [100, 101, 102, 103, 104, 105]
    length = len(arr_old)
    index1 = random.randint(0, length)
    index2 = random.randint(0, length)
    while index1 == index2:
        index2 = random.randint(0, length)
    arr_new = []
    index_offset = 0
    for index_old in range(length - 1):
        index_new = index_old + index_offset
        val = 0
        if index_offset == 0 and (index_old == index1 or index_old == index2):
            index_offset += 1
            val = arr_old[index1] + arr_old[index2]
        else:
            val = arr_old[index_new]
        arr_new.append(val)
    print(index1)
    print(index2)
    print(arr_new)
