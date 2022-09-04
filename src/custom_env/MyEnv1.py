import random
import numpy as np
import gym
from gym.spaces import Discrete, Box


# import ray
# from ray.rllib.agents import ppo


class MyEnv1(gym.Env):
    def __init__(self, config: dict = None):
        self.action_space = Discrete(n=2)
        self.observation_space = Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32)
        self.count = 0
        self.correct_action = 0

    def reset(self):
        reset_value = 0
        observation: object = np.array([reset_value])
        self.count = 0
        self.correct_action = reset_value
        return observation

    def step(self, action):
        step_value = random.randint(0, 1)
        observation = np.array([float(step_value)])
        reward: float = 1.0 if action == self.correct_action else 0.0
        done: bool = self.count >= 100
        info: dict = {}
        self.count += 1
        self.correct_action = step_value
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
    env = MyEnv1()
    print(MyEnv1.__name__)
    for i in range(10):
        print("=" * 20, str(i), "=" * 20)
        prev_observation_ = env.reset()
        while True:
            action_ = random.randint(0, 1)
            observation_, reward_, done_, info_ = env.step(action=action_)
            print(f"observation_={observation_}, "
                  f"prev_observation_={prev_observation_}, "
                  f"action_={action_}, "
                  f"reward_={reward_} ")
            prev_observation_ = observation_
            if done_:
                break
