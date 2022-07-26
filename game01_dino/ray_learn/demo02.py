import os
import shutil

import ray
import ray.rllib.agents.ppo as ppo
from ray.tune.logger import pretty_print

ray.init()
config = ppo.DEFAULT_CONFIG.copy()
config["num_gpus"] = 0
config["num_workers"] = 1
trainer = ppo.PPOTrainer(config=config, env="CartPole-v0")

# Can optionally call trainer.restore(path) to load a checkpoint.
checkpoint_dir = r"F:\models\dino"
checkpoint_path = None
for i in range(5):
    # Perform one iteration of training the policy with PPO
    result = trainer.train()
    print("*" * 100, i, "*" * 100)
    print(pretty_print(result))

    if checkpoint_path is not None and os.path.exists(checkpoint_path):
        shutil.rmtree(os.path.dirname(checkpoint_path))
    checkpoint_path = trainer.save(checkpoint_dir)
    print("checkpoint saved at", checkpoint_path)

# Also, in case you have trained a model outside of ray/RLlib and have created
# an h5-file with weight values in it, e.g.
# my_keras_model_trained_outside_rllib.save_weights("model.h5")
# (see: https://keras.io/models/about-keras-models/)

# ... you can load the h5-weights into your Trainer's Policy's ModelV2
# (tf or torch) by doing:
trainer.load_checkpoint(checkpoint_path)
# NOTE: In order for this to work, your (custom) model needs to implement
# the `import_from_h5` method.
# See https://github.com/ray-project/ray/blob/master/rllib/tests/test_model_imports.py
# for detailed examples for tf- and torch trainers/models.
