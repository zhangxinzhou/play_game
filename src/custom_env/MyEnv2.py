import random
import numpy as np
import gym
from gym.spaces import Discrete, Box


def get_frame():
    frame = np.random.randint(low=0, high=256, size=(10, 10))
    frame = frame / 255
    return frame


def get_expect_action(frame):
    mean = np.mean(frame)
    action = 0 if mean < 0.5 else 1
    return action


class MyEnv2(gym.Env):
    def __init__(self, config: dict = None):
        self.action_space = Discrete(n=2)
        self.observation_space = Box(low=0.0, high=1.0, shape=(10, 10), dtype=np.float32)
        self.count = 0
        self.expect_action = 0

    def reset(self):
        observation = get_frame()
        self.count = 0
        self.expect_action = get_expect_action(observation)
        return observation

    def step(self, action):
        observation = get_frame()
        reward: float = 1.0 if action == self.expect_action else 0.0
        done: bool = self.count >= 99
        info: dict = {}
        self.count += 1
        self.expect_action = get_expect_action(observation)
        return observation, reward, done, info

    def render(self, mode="human"):
        # if mode == 'rgb_array':
        #     # return RGB frame suitable for video
        #     return np.array(...)
        # elif mode == 'human':
        #     # pop up a window and render
        #     ...
        pass


if __name__ == '__main__':
    env = MyEnv2()
    for i in range(10):
        print("=" * 20, str(i), "=" * 20)
        prev_observation_ = env.reset()
        while True:
            action_ = random.randint(0, 1)
            observation_, reward_, done_, info_ = env.step(action=action_)
            print(f"observation_={get_expect_action(observation_)}, "
                  f"prev_observation_={get_expect_action(prev_observation_)}, "
                  f"action_={action_}, "
                  f"reward_={reward_} ")
            prev_observation_ = observation_
            if done_:
                break
