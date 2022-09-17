import ray
from ray import air, tune

TRAINING_ITERATION = 5
FCNET_HIDDENS_LIST = [
    [10, 10],
    [20, 20],
    [30, 30],
    [64, 64]
]
ray.init()
for fcnet_hiddens in FCNET_HIDDENS_LIST:
    print(fcnet_hiddens)
    tuner = tune.Tuner(
        "PPO",
        run_config=air.RunConfig(
            # 保存路径
            local_dir=r"F:\models\models\aaaa",
            # 名字
            name="name",
            # 停止条件
            stop={"training_iteration": TRAINING_ITERATION},
            # verbose
            verbose=1,
            # checkpoint_config
            checkpoint_config=air.CheckpointConfig(
                checkpoint_at_end=True
            )
        ),
        param_space={
            "env": "CartPole-v0",
            "model": {
                "fcnet_hiddens": fcnet_hiddens
            },
        },
    )
    results = tuner.fit()
    best_result = results.get_best_result(metric="episode_reward_mean", mode="max")
    best_checkpoint = best_result.log_dir.__str__()
    episode_reward_max = best_result.metrics.get('episode_reward_max')
    episode_reward_min = best_result.metrics.get('episode_reward_min')
    episode_reward_mean = best_result.metrics.get('episode_reward_mean')
    episode_len_mean = best_result.metrics.get('episode_len_mean')
    print(
        f"best_checkpoint={best_checkpoint},episode_reward_max={episode_reward_max},episode_reward_min={episode_reward_min},episode_reward_mean={episode_reward_mean},episode_len_mean={episode_len_mean}")

ray.shutdown()
