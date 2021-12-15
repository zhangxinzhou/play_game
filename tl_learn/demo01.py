import gym

env = gym.make('CartPole-v1')
env.reset()
for _ in range(1000):
    env.render()
    observation, reward, done, info = env.step(env.action_space.sample())  # take a random action
    print(f"observation={observation}, reward={reward}, done={done}, info={info}")
env.close()
