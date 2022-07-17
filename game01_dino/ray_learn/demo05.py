import random

import numpy as np
import gym, ray
from gym.spaces import Discrete, Box
from ray.rllib.env.env_context import EnvContext
from ray.rllib.agents import ppo


class MyEnv(gym.Env):

    def __init__(self, env_config: EnvContext):
        self.end_pos = env_config['corridor_length']
        self.cur_pos = 0
        self.action_space = Discrete(2)
        self.observation_space = Box(0.0, self.end_pos, shape=(1,), dtype=np.float32)
        # set the seed, This is only used for the final (reach goal) reward.

    def reset(self):
        self.cur_pos = 0
        return [self.cur_pos]

    def step(self, action):
        assert action in [0, 1], action
        if action == 0 and self.cur_pos > 0:
            self.cur_pos = 1;
        elif action == 1:
            self.cur_pos += 1
        done = self.cur_pos >= self.end_pos
        # Produce a random reward when we reach the goal
        print("aaa")
        return [self.cur_pos], random.random() * 2 if done else -0.1, done, {}


ray.init()
trainer = ppo.PPOTrainer(
    env=MyEnv,
    config={
        "env_config": {
            "corridor_length": 5
        }
    }
)

while True:
    print(trainer.train())
    
    print('abc')
