import os
import ray
import time
import shutil

from demo06 import MyEnv1
from ray.rllib.agents import ppo
from ray.tune.logger import pretty_print

ray.init()
ppo_config = ppo.DEFAULT_CONFIG.copy()
env_name = 'MyEnv1'
for i in range(3):
    era_time_start = time.time()
    ppo_config['model']['fcnet_hiddens'] = [256, 256]
    trainer = ppo.PPOTrainer(env=MyEnv1, config=ppo_config)
    model_name = 'aaa' + str(i)
    checkpoint_dir = fr'F:\models\{env_name}\{model_name}'
    episode_reward_mean_best = 0
    checkpoint_path_best = None
    for age in range(10):
        # age开始时间
        age_time_start = time.time()
        # age训练
        trainer_result = trainer.train()
        episode_reward_max = trainer_result['episode_reward_max']
        episode_reward_min = trainer_result['episode_reward_min']
        episode_reward_mean = trainer_result['episode_reward_mean']
        agent_timesteps_total = trainer_result['agent_timesteps_total']
        # 保存模型
        checkpoint_path = trainer.save(checkpoint_dir)
        if episode_reward_mean_best < episode_reward_mean:
            episode_reward_mean_best = episode_reward_mean
            checkpoint_path_best = checkpoint_path
        # age结束时间
        age_time_end = time.time()
        age_time_cost = age_time_end - age_time_start
        # age数据保存
        # save_model_age

    # 结束训练
    trainer.stop()
    # 删除不是最优的checkpoint的数据，只保留最优的checkpoint数据
    folder_list = os.listdir(checkpoint_dir)
    for folder in folder_list:
        path_tmp = os.path.join(checkpoint_dir, folder)
        if os.path.exists(path_tmp):
            path_best = os.path.dirname(checkpoint_path_best)
            if path_best != path_tmp:
                shutil.rmtree(path_tmp)

    # 保存数据,进行下一个模型结构的迭代
    # model_save
    era_time_end = time.time()
    era_time_cost = era_time_end - era_time_start
    pass
