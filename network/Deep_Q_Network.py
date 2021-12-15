import tensorflow as tf
import numpy as np
from Q_Network import Q_Network


class Deep_Q_Network:

    def __init__(
            self,
            n_actions,
            n_features,
            learning_rate=0.01,
            reward_decay=0.9,
            e_greedy=0.9,
            replace_target_iter=300,
            memory_size=500,
            batch_size=32,
            e_greedy_increment=None
    ):
        """

        :param n_actions: 动作种类个数
        :param n_features: 观察向量的维度
        :param learning_rate: 学习率
        :param reward_decay: 奖励衰减系数
        :param e_greedy: 贪心策略的epsilon
        :param replace_target_iter: 多少步替换依次权重
        :param memory_size: 内存表的大小
        :param batch_size: 神经网络训练的批次
        :param e_greedy_increment: 贪心选择策略中的epsilon的衰减
        """
        self.memory_counter = 0
        self.n_actions = n_actions
        self.n_features = n_features
        self.learning_rate = learning_rate
        self.gamma = reward_decay
        self.epsilon_max = e_greedy
        self.replace_target_iter = replace_target_iter
        self.memory_size = memory_size
        self.batch_size = batch_size
        self.epsilon_increment = e_greedy_increment
        self.epsilon = 0 if e_greedy_increment is not None else self.epsilon_max

        # total learning step
        self.learn_step_counter = 0

        # initialize zero memory [s, a, r, s_]
        self.memory = np.zeros((self.memory_size, n_features * 2 + 3))

        self.q_target = Q_Network(observation_n=self.n_features, action_n=self.n_actions).target_model
        self.q_eval = Q_Network(observation_n=self.n_features, action_n=self.n_actions).eval_model
        self.optimizer = tf.keras.optimizers.Adam(learning_rate=self.learning_rate)
        self.loss = tf.losses.MeanSquaredError()

    def choose_action(self, state, eps=0.1):
        state = tf.Variable(state, dtype=tf.float32)
        if len(tf.shape(state)) == 1:
            state = tf.expand_dims(state, axis=0)
        if np.random.uniform() > eps:
            action_value = self.q_eval.predict(state)
            return np.argmax(action_value)
        else:
            return np.random.choice(np.arange(self.n_actions))

    def learn(self):
        if self.learn_step_counter % self.replace_target_iter == 0:
            self.soft_update(1)

        # sample batch memory from all memory
        if self.memory_counter > self.memory_size:
            sample_index = np.random.choice(self.memory_size, size=self.batch_size)
        else:
            sample_index = np.random.choice(self.memory_counter, size=self.batch_size)

        experience = self.memory[sample_index, :]
        states = np.array([e[:self.n_features] for e in experience]).astype("float32")
        actions = np.array([e[self.n_features] for e in experience]).astype("int32")
        rewards = np.array([e[self.n_features + 1] for e in experience]).astype("float32")
        next_states = np.array([e[-self.n_features:] for e in experience]).astype("float32")
        dones = np.array([e[self.n_features + 2] for e in experience])

        q_target_values = self.q_target.predict(next_states)
        q_target_values = tf.reduce_max(q_target_values, axis=-1, keepdims=True)
        q_target_values = rewards + self.gamma * (1 - dones) * tf.squeeze(q_target_values)
        with tf.GradientTape() as tape:
            q_values = self.q_eval(states, training=True)
            enum_actions = list(enumerate(actions))
            q_values = tf.gather_nd(params=q_values, indices=enum_actions)
            loss = self.loss(q_values, q_target_values)

        grads = tape.gradient(loss, self.q_eval.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.q_eval.trainable_variables))
        print("梯度更新")
        self.memory_counter += 1

    def store_transition(self, s, a, r, done, s_):
        transition = np.hstack((s, [a, r, done], s_))
        # replace the old memory with new memory
        index = self.memory_counter % self.memory_size
        self.memory[index, :] = transition
        self.memory_counter += 1

    def soft_update(self, tau):
        for target_param, local_param in zip(self.q_target.weights, self.q_eval.weights):
            tf.compat.v1.assign(target_param, tau * local_param + (1. - tau) * target_param)
