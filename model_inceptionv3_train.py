from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint, TensorBoard
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage
import keys_control

import tensorflow as tf
import win32gui
import sys
import time
import numpy as np
import cv2

'''
决定使用迁移学习,懒得自己写模型
1.决定使用那种模型
2.处理数据,将图片处理成模型所需要的尺寸和相关的通道(比如RGB三个颜色)
3.引入模型
4.训练
5.使用校验集来校验
'''
MODEL_NAME = 'InceptionV3'
MODEL_FILE_PATH = ''
MODEL_HEIGHT = 299
MODEL_WIDTH = 299
MODEL_CHANNEL = 3


# 获取模型
def get_my_model():
    base_model = InceptionV3(input_shape=(MODEL_HEIGHT, MODEL_WIDTH, 3))

    my_model = models.Sequential()
    my_model.add(base_model)
    my_model.add(layers.Flatten())
    my_model.add(layers.Dense(100, activation='relu'))
    my_model.add(layers.Dropout(0.5))
    my_model.add(layers.Dense(9, activation='sigmoid'))
    base_model.trainable = False

    my_model.compile(
        optimizer=tf.keras.optimizers.RMSprop(lr=0.01),
        loss=tf.keras.losses.categorical_crossentropy,
        metrics=[tf.keras.metrics.binary_accuracy]
    )

    return my_model


def get_generator():
    # 数据源
    train_dagagen = ImageDataGenerator(
        rescale=1. / 255,
    )
    train_generator = train_dagagen.flow_from_directory(
        r'E:\gta5\collect_data',
        target_size=(299, 299),
        batch_size=16,
        class_mode='categorical',
        shuffle=True
    )
    return train_generator


def get_callbacks_list():
    monitor = 'val_loss'
    model_path = 'my_model\\my_best_weight.h5'
    log_path = 'my_model\\my_log'
    # LR衰减,如果在patience个epoch中看不到模型性能提升，则减少学习率
    reduce_lr = ReduceLROnPlateau(monitor=monitor, factor=0.1, patience=3, verbose=1)
    # 早听法，如果20轮val_loss还不下降就结束
    early_stopping = EarlyStopping(monitor=monitor, patience=20, verbose=1)
    # 保存最优模型
    checkpoint = ModelCheckpoint(model_path, monitor=monitor, save_best_only=True, verbose=1)
    # TensorBoard 可视化
    tensorboard = TensorBoard(log_dir=log_path)

    callbacks_list = [reduce_lr, early_stopping, checkpoint, tensorboard]
    return callbacks_list


def model_train():
    my_model = get_my_model()
    train_generator = get_generator()
    callbacks_list = get_callbacks_list()
    history = my_model.fit_generator(
        train_generator,
        epochs=100,
        steps_per_epoch=200,
        callbacks=callbacks_list,
        verbose=2
    )


# QPixmap => CvMat
# method from google/baidu
def qtpixmap_to_cvmat(qtpixmap):
    qimg = qtpixmap.toImage()
    temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
    temp_shape += (4,)
    ptr = qimg.bits()
    ptr.setsize(qimg.byteCount())
    result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
    result = result[..., :3]

    return result


# CvMat => QPixmap
# method from google/baidu
def cvmat_to_qtimg(cvimg):
    height, width, depth = cvimg.shape
    cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
    cvimg = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)

    return cvimg


def model_test(game_title, img_show=True):
    my_model = get_my_model()
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
        mat = qtpixmap_to_cvmat(q_pix_map)

        tmp = np.expand_dims(mat / 255, axis=0)
        prediction = my_model.predict(tmp)[0]
        index = np.argmax(prediction)
        key_choice = keys_control.index_to_key(index)
        t1 = time.time()
        cost = 1000 * (t1 - t0)
        if img_show:
            text = 'hwnd : {} , key_choice : {} ,cost : {:.6f} ms'.format(hwnd, key_choice, cost)
            # FIXME 图片颜色怪异,但如果不写下面代码,则cv2.putText会报错
            mat = cv2.cvtColor(mat, cv2.COLOR_RGB2BGR)
            cv2.putText(mat, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow('window', mat)
            cv2.waitKey(1)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    # 显存按需分配
    gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)

    # 训练模型 or 测试模型
    train_mode = False
    game_title = r'Grand Theft Auto V'
    if train_mode:
        model_train()
    else:
        model_test(game_title)
