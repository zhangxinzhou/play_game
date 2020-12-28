from PyQt5.QtWidgets import QApplication
import tensorflow as tf
import win32gui
import sys
import time
import cv2

import tf_obj.tf_obj_detection_utils as od_utils


def obj_detection_test(game_title, img_show=True):
    hwnd = win32gui.FindWindow(None, game_title)
    if hwnd == 0:
        print('can not find [{}]'.format(game_title))
        print('exit')
        exit()
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    while True:
        t0 = time.time()
        q_pix_map = screen.grabWindow(hwnd)
        img_name = 'buff.jpg'
        q_pix_map.save(img_name)
        img_mat0 = cv2.imread(img_name)
        img_mat1 = od_utils.get_object_detection_img(img_mat0)
        t1 = time.time()
        cost = 1000 * (t1 - t0)
        if img_show:
            text = 'hwnd : {} ,cost : {:.6f} ms'.format(hwnd, cost)
            cv2.putText(img_mat1, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow('window', img_mat1)
            cv2.waitKey(1)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    # 显存按需分配
    gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)

    train_mode = False
    game_title = r'Grand Theft Auto V'
    obj_detection_test(game_title)
