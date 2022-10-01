import ray
import gym
from ray import air, tune
import ray.rllib.algorithms.ppo as ppo

from src.custom_env.MyEnv2 import MyEnv2

ENV_CLASS = MyEnv2
ENV_NAME = ENV_CLASS.__name__
TRAINING_ITERATION = 3
FRAMEWORK = "tf"
FCNET_HIDDENS_LIST = [
    [10, 10],
    [20, 20],
    [30, 30],
    [64, 64]
]

for fcnet_hiddens in FCNET_HIDDENS_LIST:
    ray.init()
    print("*" * 100)
    print(fcnet_hiddens)
    tuner = tune.Tuner(
        "PPO",
        param_space={
            "env": ENV_CLASS,
            "framework": FRAMEWORK,
            "model": {
                "fcnet_hiddens": fcnet_hiddens
            },
            "num_gpus": 1,
            "num_workers": 10,
        },
        tune_config=ray.tune.tune_config.TuneConfig(
            metric="episode_reward_mean",
            mode="max"
        ),
        run_config=air.RunConfig(
            # 保存路径
            local_dir=r"F:\models\models\aaaa",
            # 名字
            name="name",
            # 停止条件
            stop={"training_iteration": TRAINING_ITERATION},
            # verbose
            verbose=2,
            # checkpoint_config
            checkpoint_config=air.CheckpointConfig(
                checkpoint_at_end=True
            )
        ),
    )
    results = tuner.fit()

    best_result = results.get_best_result(metric="episode_reward_mean", mode="max")
    best_result_config = best_result.config
    best_result_metrics = best_result.metrics
    best_checkpoint = best_result.checkpoint._local_path
    episode_reward_max = best_result_metrics.get('episode_reward_max')
    episode_reward_min = best_result_metrics.get('episode_reward_min')
    episode_reward_mean = best_result_metrics.get('episode_reward_mean')
    episode_len_mean = best_result_metrics.get('episode_len_mean')
    error = best_result.error.__str__()
    print(
        f"best_checkpoint={best_checkpoint},episode_reward_max={episode_reward_max},episode_reward_min={episode_reward_min},episode_reward_mean={episode_reward_mean},episode_len_mean={episode_len_mean}")

    # 开始测试
    print("*" * 50, "测试开始...", "*" * 50)
    best_agent = ppo.PPO(config={
        "framework": best_result_config.get("framework"),
        "model": {
            "fcnet_hiddens": fcnet_hiddens
        }
    }, env=ENV_CLASS)
    best_agent.restore(checkpoint_path=best_checkpoint)
    env = ENV_CLASS()
    for i in range(10):
        episode_reward = 0
        done = False
        obs = env.reset()
        while not done:
            action = best_agent.compute_action(obs)
            obs, reward, done, info = env.step(action)
            episode_reward += reward

        print(f"NO.{i},episode_reward={episode_reward}")
    print("*" * 50, "测试结束...", "*" * 50)

    ray.shutdown()
