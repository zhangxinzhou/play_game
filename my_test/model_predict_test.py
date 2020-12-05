import tensorflow as tf
import numpy as np
import time

from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras import models
from tensorflow.keras import layers


# 获取模型
def get_my_model():
    base_model = InceptionV3(input_shape=(299, 299, 3))

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


# 测试模型需要的数据维度,测试模型预测花费的时间
def model_test():
    my_model = get_my_model()
    shape = (299, 299, 3)
    data = np.random.random(shape)
    data = np.expand_dims(data, axis=0)
    print(data.shape)
    for i in range(100):
        t0 = time.time()
        predict = my_model.predict(data)
        t1 = time.time()
        cost = t1 - t0
        print('*' * 100)
        print('cost : {:.4f} s '.format(cost))
        print(data.shape)
        print(predict)


if __name__ == '__main__':
    model_test()
