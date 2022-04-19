from abc import abstractmethod


class GameAgent(object):

    @abstractmethod
    def model_create(self):
        # 模型创建
        pass

    @abstractmethod
    def model_mutation(self):
        # 模型变异-变异程度由低到高
        # 1.完全继承/复制-降低lr重训练
        # 2.完全继承/复制-并重训练
        # 3.数量不变,结构重排,并重训练
        # 4.降低5%结构,并重训练
        # 5.增加5%结构,并重训练
        pass

    @abstractmethod
    def model_save(self):
        # 模型保存
        pass

    @abstractmethod
    def model_load(self):
        # 模型加载
        pass
