import random
import numpy as np
import gym, ray
from gym.spaces import Discrete, Box
from ray.rllib.agents import ppo


class MyEnv1(gym.Env):
    def __init__(self, config: dict):
        self.action_space = Discrete(n=2)
        self.observation_space = Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32)
        self.prev_observation = np.array([0])
        self.count = 0

    def reset(self):
        observation: object = np.array([0])
        self.prev_observation = observation
        self.count = 0
        return observation

    def step(self, action):
        observation = np.array([float(random.randint(0, 1))])
        reward: float = 1.0 if action == int(sum(self.prev_observation)) else 0.0
        done: bool = self.count >= 100
        info: dict = {}
        self.prev_observation = observation
        self.count += 1
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
