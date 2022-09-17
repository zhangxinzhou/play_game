import random
import copy


def list_mutation_rearrange(list_old: list):
    # 随机重排,比如[1,2,3]排列成[2,1,3]
    arr_new = copy.deepcopy(list_old)
    random.shuffle(arr_new)
    return arr_new


def list_mutation_merge(list_old: list):
    # 合并,层数减少,如[1,2,3]=>[3,3]或[1,5]
    arr_new = copy.deepcopy(list_old)
    length = len(arr_new)
    if length <= 1:
        return arr_new
    index1, index2 = random.sample(range(0, length), 2)
    arr_new[index1] = arr_new[index1] + arr_new[index2]
    del arr_new[index2]
    return arr_new


def list_mutation_split(list_old: list):
    # 分裂,层数增加,如如[3,4]=>[1,3,3]或[2,2,3]等
    arr_new = copy.deepcopy(list_old)
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


def list_mutation_increase(list_old: list):
    arr_new = copy.deepcopy(list_old)

    length = len(arr_new)
    random_index = random.randint(0, length - 1)
    increase = int(arr_new[random_index] * 0.05)
    if increase == 0:
        increase = 1
    arr_new[random_index] = arr_new[random_index] + increase
    return arr_new


def list_mutation_decrease(list_old: list):
    arr_new = copy.deepcopy(list_old)

    length = len(arr_new)
    random_index = random.randint(0, length - 1)
    decrease = int(arr_new[random_index] * 0.05)
    if decrease == 0:
        decrease = 1
    arr_new[random_index] = arr_new[random_index] - decrease
    if arr_new[random_index] <= 0:
        arr_new[random_index] = 1
    return arr_new


def list_mutation(list_old: list):
    return [
        copy.deepcopy(list_old),
        list_mutation_rearrange(list_old),
        list_mutation_merge(list_old),
        list_mutation_split(list_old),
        list_mutation_increase(list_old),
        list_mutation_decrease(list_old)
    ]
