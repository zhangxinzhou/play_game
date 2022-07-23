from demo06 import MyEnv1

import ray
from ray.rllib.agents import ppo

ray.init()
trainer = ppo.PPOTrainer(
    env=MyEnv1,
    config={
        "env_config": {
            "corridor_length": 5
        }
    }
)

for i in range(10):
    tmp = trainer.train()
    print(i)
    print(tmp)

print("*" * 100)
ray.shutdown()
