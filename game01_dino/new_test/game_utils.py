import os
import numpy as np
import cv2
import random
import copy

from keras.models import Sequential
from keras.layers.core import Dense, Flatten, Dropout
import tensorflow as tf


def qpixmap_to_array(qtpixmap):
    # qpixmap转换成array
    img = qtpixmap.toImage()
    temp_shape = (img.height(), img.bytesPerLine() * 8 // img.depth())
    temp_shape += (4,)
    ptr = img.bits()
    ptr.setsize(img.byteCount())
    result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
    result = result[..., :3]

    return result


def img_to_candy(img):
    # 图片转换成灰色,灰色图片转换为轮廓
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_candy = cv2.Canny(img_gray, 100, 200)
    return img_candy


def model_mutation():
    # 模型变异-变异程度由低到高
    # 1.完全继承/复制-降低lr重训练
    # 2.完全继承/复制-并重训练
    # 3.数量不变,结构重排,并重训练
    # 4.降低5%结构,并重训练
    # 5.增加5%结构,并重训练
    pass


def create_model(input_shape, output_dim, hidden_layer: dict):
    convolutional_layer = hidden_layer.get("convolutional_layer")
    fully_connected_layer = hidden_layer.get("fully_connected_layer")
    # 创建模型
    model = Sequential()
    model.add(Flatten(input_shape=input_shape))

    if convolutional_layer is not None:
        # 处理卷积层
        pass

    if fully_connected_layer is not None:
        # 处理全连接层
        for index, item in enumerate(fully_connected_layer):
            model.add(Dense(item, activation='relu'))
            model.add(Dropout(0.2))
        model.add(Dense(output_dim, activation='softmax'))

    return model


def arr_mutations(arr_old):
    arr_new = copy.deepcopy(arr_old)

    length = len(arr_new)
    random_index = random.randint(0, length - 1)
    increase = int(arr_new[random_index] * 0.05)
    if increase == 0:
        increase = 1
    arr_new[random_index] = arr_new[random_index] + increase
    return arr_new


def get_model_path(root_path, game_name, model_id):
    # 拼接model路径
    full_path = os.path.join(root_path, game_name, model_id)
    return full_path


def model_save(model, model_path):
    # 模型保存
    if not os.path.exists(model_path):
        os.makedirs(model_path)
    tf.saved_model.save(model, model_path)


def model_load(model_path):
    # 模型加载
    if not os.path.exists(model_path):
        print(f"[{model_path}] is not exists ,exit")
        exit(-1)
    model = tf.saved_model.load(model_path)
    return model
