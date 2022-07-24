from demo06 import MyEnv1

import ray
from ray.rllib.agents import ppo

ray.init()
ppo_config = ppo.DEFAULT_CONFIG.copy()
ppo_config['model']['fcnet_hiddens'] = [10, 10]
trainer = ppo.PPOTrainer(env=MyEnv1, config=ppo_config)

for i in range(10):
    tmp = trainer.train()
    print(i)
    print(tmp)

    episode_reward = 0
    done = False
    test_env = MyEnv1()
    obs = test_env.reset()
    while not done:
        action = trainer.compute_single_action(obs)
        obs, reward, done, info = test_env.step(action)
        episode_reward += reward
    print(episode_reward)

print("*" * 100)
