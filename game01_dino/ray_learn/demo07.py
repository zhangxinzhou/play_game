from demo06 import MyEnv1

import ray
from ray.rllib.agents import ppo

ray.init()
ppo_config = ppo.DEFAULT_CONFIG.copy()
env = MyEnv1()
for i in range(10):
    ppo_config['model']['fcnet_hiddens'] = [1]
    trainer = ppo.PPOTrainer(env=MyEnv1, config=ppo_config)
    trainer_result = trainer.train()
    print("*" * 50, i, "*" * 50)

    episode_reward = 0
    done = False
    obs = env.reset()
    while not done:
        action = trainer.compute_single_action(obs)
        obs, reward, done, info = env.step(action)
        episode_reward += reward
    print(episode_reward)
