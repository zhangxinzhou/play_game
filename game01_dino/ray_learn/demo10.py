from demo06 import MyEnv1
from ray.rllib.agents import ppo

env = MyEnv1()
checkpoint_path = r"F:\models\dino\checkpoint_000030\checkpoint-30"
trainer = ppo.PPOTrainer(env=MyEnv1)
trainer.load_checkpoint(checkpoint_path)
episode_reward = 0
done = False
obs = env.reset()
while not done:
    action = trainer.compute_single_action(obs)
    obs, reward, done, info = env.step(action)
    print(reward)
    episode_reward += reward
print("=" * 100)
print(episode_reward)
