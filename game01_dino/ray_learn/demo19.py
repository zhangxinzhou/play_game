import ray
from ray import tune
from ray.rllib.agents import ppo
from ray.tune.logger import pretty_print

from demo06 import MyEnv1

ray.init()
analysis = tune.run(
    # 与ray.agent.ppo.PPOTrainer，同样效果，只支持内置的算法
    run_or_experiment=ppo.PPOTrainer,
    # 保存路径
    local_dir=r"F:\models\aaa",
    # 名字
    name="my_name",
    # 停止条件
    stop={
        "training_iteration": 10
    },
    config={
        "env": MyEnv1,
        "num_gpus": 0,
        "num_workers": 1,
        # "lr": tune.grid_search([0.01, 0.001, 0.0001])
    },
    # 同时运行两个实验
    num_samples=1,
    # 在训练结束后存储模型
    checkpoint_at_end=True
)

best_checkpoint = analysis.get_best_checkpoint(
    trial=analysis.get_best_trial("episode_reward_mean", mode="max"),
    metric="episode_reward_mean",
    mode="max")

print("=" * 100)
print("best_checkpoint")
print(best_checkpoint)

agent = ppo.PPOTrainer(config={}, env=MyEnv1)
agent.restore(checkpoint_path=best_checkpoint)

env = MyEnv1()
# run until episode ends
episode_reward = 0
done = False
obs = env.reset()
while not done:
    # 设置full_fetch=True可以获得除了action外的其他辅助信息，
    # 包括action的logits，及obs的value等
    action = agent.compute_action(obs)
    obs, reward, done, info = env.step(action)
    episode_reward += reward

print("=" * 100)
print("episode_reward")
print(episode_reward)
