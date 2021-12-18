import gym
import tensorflow as tf
from Deep_Q_Network import Deep_Q_Network

# tf2.x version  自适应显存占用
gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
for gpu in gpus:
    print(f"set gpu [{gpu}] memory growth")
    tf.config.experimental.set_memory_growth(gpu, True)


def main():
    step = 0
    for episode in range(1000):
        # initial observation
        observation = env.reset()
        reward_sum = 0;

        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(observation)

            # RL take action and get next observation and reward
            observation_, reward, done, info = env.step(action)
            reward_sum += reward

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
        print(f"episode {episode + 1}, reward_sum = {reward_sum}")
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
    print(f"n_actions={env.action_space.n}, n_features={env.observation_space.shape[0]}")
    RL = Deep_Q_Network(n_actions=env.action_space.n, n_features=env.observation_space.shape[0])
    main()
