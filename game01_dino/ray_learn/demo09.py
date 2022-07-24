import os

os.environ["CUDA_VISIBLE_DEVICES"] = '3'
import ray
import ray.rllib.agents.ppo as ppo
from ray.tune.logger import pretty_print
import gym

ray.init()
config = ppo.DEFAULT_CONFIG.copy()
config["num_gpus"] = 0
config["num_workers"] = 1
config["framework"] = 'tf2'
config['model']['fcnet_hiddens'] = [10, 10]
agent = ppo.PPOTrainer(config=config, env="CartPole-v0")

print("config start")
for k, v in config.items():
    print(k, ":", v)
print("=" * 100)
for k, v in config['model'].items():
    print(k, ":", v)
print("config end")

# instantiate env class
env = gym.make("CartPole-v0")

# run until episode ends
episode_reward = 0
done = False
obs = env.reset()
while not done:
    action = agent.compute_single_action(obs)
    obs, reward, done, info = env.step(action)
    episode_reward += reward
    print(reward)
print(episode_reward)
