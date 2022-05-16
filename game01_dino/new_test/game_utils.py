import os
import shutil
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


def create_model(input_shape, output_dim, hidden_layer: dict):
    convolutional_layer = hidden_layer.get("convolutional_layer")
    fully_connected_layer = hidden_layer.get("fully_connected_layer")
    # 创建模型
    model = Sequential()
    model.add(Flatten(input_shape=input_shape))

    if convolutional_layer is not None:
        # 待实现
        # 处理卷积层
        pass

    if fully_connected_layer is not None:
        # 处理全连接层
        for index, item in enumerate(fully_connected_layer):
            model.add(Dense(item, activation='relu'))
            model.add(Dropout(0.2))
        model.add(Dense(output_dim, activation='softmax'))

    return model


def model_mutation():
    # 模型变异-变异程度由低到高
    # 1.完全继承/复制-降低lr重训练
    # 2.完全继承/复制-并重训练
    # 3.数量不变,结构重排,并重训练
    # 4.降低5%结构,并重训练
    # 5.增加5%结构,并重训练
    pass


def arr_mutation_rearrange(arr_old: list):
    # 随机重排,比如[1,2,3]排列成[2,1,3]
    arr_new = copy.deepcopy(arr_old)
    random.shuffle(arr_new)
    return arr_new


def arr_mutation_merge(arr_old: list):
    # 合并,层数减少,如[1,2,3]=>[3,3]或[1,5]
    arr_new = copy.deepcopy(arr_old)
    length = len(arr_new)
    if length <= 1:
        return arr_new
    index1, index2 = random.sample(range(0, length), 2)
    arr_new[index1] = arr_new[index1] + arr_new[index2]
    del arr_new[index2]
    return arr_new


def arr_mutation_split(arr_old: list):
    # 分裂,层数增加,如如[3,4]=>[1,3,3]或[2,2,3]等
    arr_new = copy.deepcopy(arr_old)
    index_arr = []
    for i, val in enumerate(arr_new):
        if val > 1:
            index_arr.append(i)
    if len(index_arr) <= 0:
        # 数组中没有可以分裂的
        return arr_new
    index_random = random.sample(index_arr, 1)[0]
    val0 = arr_new[index_random]
    val1 = random.randint(1, val0 - 1)
    val2 = val0 - val1
    del arr_new[index_random]
    arr_new.insert(index_random, val2)
    arr_new.insert(index_random, val1)
    return arr_new


def arr_mutation_increase(arr_old: list):
    arr_new = copy.deepcopy(arr_old)

    length = len(arr_new)
    random_index = random.randint(0, length - 1)
    increase = int(arr_new[random_index] * 0.05)
    if increase == 0:
        increase = 1
    arr_new[random_index] = arr_new[random_index] + increase
    return arr_new


def arr_mutation_decrease(arr_old: list):
    arr_new = copy.deepcopy(arr_old)

    length = len(arr_new)
    random_index = random.randint(0, length - 1)
    decrease = int(arr_new[random_index] * 0.05)
    if decrease == 0:
        decrease = 1
    arr_new[random_index] = arr_new[random_index] - decrease
    if arr_new[random_index] <= 0:
        arr_new[random_index] = 1
    return arr_new


def hidden_layer_mutation(hidden_layer: dict):
    convolutional_layer = hidden_layer.get("convolutional_layer")
    fully_connected_layer = hidden_layer.get("fully_connected_layer")

    return [
        {
            "mutation_type": "origin",
            "convolutional_layer": convolutional_layer,
            "fully_connected_layer": copy.deepcopy(fully_connected_layer)
        },
        {
            "mutation_type": "mutations_rearrange",
            "convolutional_layer": convolutional_layer,
            "fully_connected_layer": arr_mutation_rearrange(fully_connected_layer)
        },
        {
            "mutation_type": "mutations_increase",
            "convolutional_layer": convolutional_layer,
            "fully_connected_layer": arr_mutation_increase(fully_connected_layer)
        },
        {
            "mutation_type": "mutations_decrease",
            "convolutional_layer": convolutional_layer,
            "fully_connected_layer": arr_mutation_decrease(fully_connected_layer)
        }
    ]


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


def create_folder(folder_path):
    # 删除模型
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def remove_folder(folder_path):
    # 删除模型
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)


if __name__ == '__main__':
    a = [100, 101, 102, 103, 104, 105, 106, 107, 108]
    a = [1, 2, 3]
    print(a)
    b = arr_mutation_merge(a)
    c = arr_mutation_split(a)
    print(b)
    print(c)
