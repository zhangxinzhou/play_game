import random
import numpy as np
import gym, ray
from gym.spaces import Discrete, Box
from ray.rllib.agents import ppo


class MyEnv1(gym.Env):
    def __init__(self, config: dict):
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


ray.init()
trainer = ppo.PPOTrainer(
    env=MyEnv1,
    config={
        "env_config": {
            "corridor_length": 5
        }
    }
)

while True:
    print(trainer.train())
