from keras.models import Sequential
from keras.layers.core import Dense, Flatten, Dropout

import random
import copy


def create_model(input_shape, output_dim, model_struct):
    model = Sequential()
    model.add(Flatten(input_shape=input_shape))
    for index, item in enumerate(model_struct):
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


if __name__ == '__main__':
    input_shape = (100, 100)
    output_dim = 10
    arr_old = [100, 20, 5]
    for i in range(100):
        print("*" * 100)
        arr_new = arr_mutations(arr_old)
        print(arr_new)
        arr_old = arr_new
        tmp_model = create_model(input_shape, output_dim, arr_old)
        tmp_model.summary()
