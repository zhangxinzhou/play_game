from directkeys import *


# no key
def key_():
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(S)
    ReleaseKey(D)


def key_w():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(S)
    ReleaseKey(D)


def key_s():
    ReleaseKey(W)
    ReleaseKey(A)
    PressKey(S)
    ReleaseKey(D)


def key_a():
    ReleaseKey(W)
    PressKey(A)
    ReleaseKey(S)
    ReleaseKey(D)


def key_d():
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(S)
    PressKey(D)


def key_wa():
    PressKey(W)
    PressKey(A)
    ReleaseKey(S)
    ReleaseKey(D)


def key_wd():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(S)
    PressKey(D)


def key_sa():
    ReleaseKey(W)
    PressKey(A)
    PressKey(S)
    ReleaseKey(D)


def key_sd():
    ReleaseKey(W)
    ReleaseKey(A)
    PressKey(S)
    PressKey(D)


key_to_index_dict = {
    'key_': 0,
    'key_w': 1,
    'key_s': 2,
    'key_a': 3,
    'key_d': 4,
    'key_wa': 5,
    'key_wd': 6,
    'key_sa': 7,
    'key_sd': 8
}

index_to_key_dict = {v: k for k, v in key_to_index_dict.items()}


def key_to_index(key):
    index = key_to_index_dict.get(key, 0)
    return index


def index_to_key(index):
    method_name = index_to_key_dict.get(index)
    eval(method_name)()
    return method_name


if __name__ == '__main__':
    for i in range(5):
        method_name = index_to_key(i)
        print(method_name)
