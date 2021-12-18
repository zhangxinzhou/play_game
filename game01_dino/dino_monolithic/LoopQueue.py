import numpy as np


class LoopQueue:
    def __init__(self, size):
        # 队列大小
        self.size = size
        # 队头
        self.head = 0
        # 队尾
        self.tail = 0
        # 队列内容
        self.queue = []

    def __str__(self):
        s = f"queue={self.queue}, size={self.size}, head={self.head}, tail={self.tail}"
        return s

    def is_full(self):
        return len(self.queue) >= self.size

    # 入队
    def add(self, element):
        if self.is_full():
            self.queue[self.tail] = element
            self.head = (self.head + 1) % self.size
            self.tail = (self.tail + 1) % self.size
        else:
            self.queue.append(element)
            self.head = len(self.queue) - 1

    # 出队
    # TODO 懒得搞
    def remove(self):
        pass

    def get_list(self):
        if self.is_full():
            return [self.queue[(self.tail + index) % self.size] for index in range(self.size)]
        else:
            return self.queue

    def get_numpy(self):
        return np.array(self.get_list())


# 测试
if __name__ == '__main__':
    q = LoopQueue(5)
    for i in range(100):
        image = np.random.randint(0, 255, size=(3, 3, 3))
        q.add(image)
        n = q.get_numpy()
        print("=" * 100)
        print(q)
        print(n.shape)
        print(n)
