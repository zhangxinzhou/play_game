import ray
import uuid
import shutil
from ray.rllib.agents import ppo
from pynput import keyboard

from src.custom_env.MyEnv2 import MyEnv2

# ====================常量=====================

# 迭代轮数
TRAINING_ITERATION = 3
# 迭代轮数
EPISODE_ITERATION = 3
# 框架
FRAMEWORK = "torch"
# 环境
ENV_CLASS = MyEnv2
# 游戏名称
ENV_NAME = ENV_CLASS.__name__
# 训练开关,控制,如果监听到xxx按键被按下,就会改变TRAIN_SWITCH的值
TRAIN_SWITCH = True


# ====================常量=====================


def on_press(key):
    if key == keyboard.Key.f12:
        global TRAIN_SWITCH
        TRAIN_SWITCH = False
        print("*" * 50, f"监听到{key}按键被按下...", "*" * 50)
        print("*" * 50, "程序将在本次训练完毕后结束...", "*" * 50)
        return False


listener = keyboard.Listener(on_press=on_press)
listener.start()


def get_trainer():
    config = ppo.DEFAULT_CONFIG.copy()
    config['model']['post_fcnet_hiddens'] = [1024, 100]
    trainer = ppo.PPOTrainer(env=ENV_CLASS, config=config)
    return trainer


def train():
    ray.shutdown()
    ray.init()
    tmp_list = []
    for train_index in range(TRAINING_ITERATION):
        model_id = uuid.uuid4().hex
        checkpoint_dir = fr'F:\models\{ENV_NAME}\{model_id}'
        # trainer
        trainer = get_trainer()
        # 打印模型的结构
        # trainer.get_policy().model.base_model.summary()
        for episode_index in range(EPISODE_ITERATION):
            trainer_result = trainer.train()
            episode_reward_max = trainer_result['episode_reward_max']
            episode_reward_min = trainer_result['episode_reward_min']
            episode_reward_mean = trainer_result['episode_reward_mean']
            # 保存模型
            checkpoint_path = trainer.save(checkpoint_dir)
            tmp_obj = {
                "train_index": train_index,
                "episode_index": episode_index,
                "episode_reward_max": episode_reward_max,
                "episode_reward_min": episode_reward_min,
                "episode_reward_mean": episode_reward_mean,
                "checkpoint_path": checkpoint_path
            }
            print(tmp_obj)
            tmp_list.append(tmp_obj)
        trainer.stop()

    sort_list = sorted(tmp_list, key=lambda item: item['episode_reward_mean'], reverse=True)
    print("*" * 100)
    for index, obj in enumerate(sort_list):
        print(obj)
        if index != 0:
            shutil.rmtree(obj['checkpoint_path'])

    best_obj = sort_list[0]
    best_checkpoint_path = best_obj.get("checkpoint_path")
    best_agent = get_trainer()
    best_agent.restore(checkpoint_path=best_checkpoint_path)

    # test
    env = ENV_CLASS()
    for i in range(10):
        episode_reward = 0
        done = False
        obs = env.reset()
        while not done:
            action = best_agent.compute_single_action(obs)
            obs, reward, done, info = env.step(action)
            episode_reward += reward

        print(f"NO.{i},episode_reward={episode_reward}")


if __name__ == '__main__':
    train()
