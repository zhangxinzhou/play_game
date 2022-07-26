from demo06 import MyEnv1

import ray
from ray.rllib.agents import ppo
from ray.tune.logger import pretty_print

ray.init()
ppo_config = ppo.DEFAULT_CONFIG.copy()
ppo_config['model']['fcnet_hiddens'] = [256, 256]
trainer = ppo.PPOTrainer(env=MyEnv1, config=ppo_config)
env = MyEnv1()
episode_reward_best = 0
checkpoint_dir = r'F:\models\dino'
for i in range(30):
    trainer_result = trainer.train()
    print("*" * 50, i, "*" * 50)
    print(pretty_print(trainer_result))

    episode_reward_max = trainer_result['episode_reward_max']
    episode_reward_min = trainer_result['episode_reward_min']
    episode_reward_mean = trainer_result['episode_reward_mean']
    agent_timesteps_total = trainer_result['agent_timesteps_total']

    if episode_reward_mean > episode_reward_best:
        episode_reward_best = episode_reward_mean
        print(trainer.save(checkpoint_dir))



