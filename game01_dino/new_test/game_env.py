from abc import abstractmethod


class GameEnv(object):

    @abstractmethod
    def step(self, action):
        # 下一步
        pass

    @abstractmethod
    def reset(self):
        # 环境充值
        pass

    @abstractmethod
    def render(self):
        # 渲染游戏截图
        pass

    @abstractmethod
    def close(self):
        # 环境关闭
        pass

    @abstractmethod
    def test_random_action(self):
        # 随机测试
        pass
