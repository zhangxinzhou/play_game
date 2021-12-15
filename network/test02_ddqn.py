import gym
from Double_Deep_Q_Network import Double_Deep_Q_Network


def main():
    step = 0
    for episode in range(300):
        # initial observation
        observation = env.reset()

        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(observation)

            # RL take action and get next observation and reward
            observation_, reward, done, info = env.step(action)

            RL.store_transition(observation, action, reward, done, observation_)

            if (step > 200) and (step % 5 == 0):
                RL.learn()
                RL.soft_update(1)

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break
            step += 1
        print("episode %d" % (episode + 1))
    # end of game
    print('game over')
    env.close()


def transformer_state(state):
    """将 position, velocity 通过线性转换映射到 [0, 40] 范围内"""
    pos, v = state
    pos_low, v_low = env.observation_space.low
    pos_high, v_high = env.observation_space.high
    pos = 40 * (pos - pos_low) / (pos_high - pos_low)
    v = 40 * (v - v_low) / (v_high - v_low)
    return int(pos), int(v)


if __name__ == "__main__":
    env = gym.make("CartPole-v1")
    RL = Double_Deep_Q_Network(n_actions=env.action_space.n, n_features=env.observation_space.shape[0])
    main()
