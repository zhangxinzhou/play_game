import gym, ray
from ray.rllib.agents import ppo


class MyEnv(gym.Env):
    def __init__(self, env_config):
        self.action_space = gym.Space()
        self.observation_space = gym.Space()

    def reset(self):
        return 1

    def step(self, action):
        return 1, 1, False, {}


ray.init()
trainer = ppo.PPOTrainer(
    env='CartPole-v0',
    config={
        "env_config": {}
    }
)

while True:
    print(trainer.train())
    
    print('abc')
