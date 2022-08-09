import ray
from ray import tune
from demo06 import MyEnv1

ray.init()
tune.run(
    # 与ray.agent.ppo.PPOTrainer，同样效果，只支持内置的算法
    "PPO",
    # 停止条件
    stop={"episode_reward_mean": 100},
    config={
        "env": MyEnv1,
        "num_gpus": 0,
        "num_workers": 1,
        "lr": tune.grid_search([0.01, 0.001, 0.0001])
    },
    # 同时运行两个实验
    num_samples=2
)
