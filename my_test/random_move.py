import keys_control
import random
import time


def go():
    for i in range(100):
        index = random.randint(0, 8)
        key_choice = keys_control.index_to_key(index)
        for j in range(10):
            print("step : {}, choice : {}".format(i, key_choice))
            time.sleep(0.05)


if __name__ == '__main__':
    for i in range(9)[::-1]:
        time.sleep(1)
        print("{}".format(i + 1))

    print("=" * 10, "start", "=" * 10)
    go()
