import gym

env = gym.make('CartPole-v0')
print(env.action_space)  # Discrete(2)
observation = env.reset()
print(observation)  # [-0.0390601  -0.04725411  0.0466889   0.02129675]
