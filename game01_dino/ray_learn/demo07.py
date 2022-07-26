import os
import ray
import shutil

from demo06 import MyEnv1
from ray.rllib.agents import ppo
from ray.tune.logger import pretty_print

ray.init()
ppo_config = ppo.DEFAULT_CONFIG.copy()
ppo_config['model']['fcnet_hiddens'] = [256, 256]
trainer = ppo.PPOTrainer(env=MyEnv1, config=ppo_config)
env = MyEnv1()
episode_reward_best = 0
model_name = 'aaa'
checkpoint_dir = fr'F:\models\dino\{model_name}'
not_increase = 0
for age in range(30):
    trainer_result = trainer.train()
    episode_reward_max = trainer_result['episode_reward_max']
    episode_reward_min = trainer_result['episode_reward_min']
    episode_reward_mean = trainer_result['episode_reward_mean']
    agent_timesteps_total = trainer_result['agent_timesteps_total']

    # 保存模型
    if episode_reward_mean > episode_reward_best:
        not_increase = 0
        if checkpoint_path is not None and os.path.exists(checkpoint_path):
            shutil.rmtree(os.path.dirname(checkpoint_path))
        checkpoint_path = trainer.save(checkpoint_dir)

# 保存数据,进行下一个模型结构的迭代
# model_save
