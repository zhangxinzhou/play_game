from keras import layers, models


class Q_Network:
    def __init__(self, observation_n, action_n):
        self.observation_n = observation_n
        self.action_n = action_n
        self._build_model()

    def _build_model(self):
        # ------------------ build eval network -------------------------
        self.eval_model = models.Sequential(name="eval_network")
        self.eval_model.add(layers.Dense(64, activation="relu", input_shape=(None, self.observation_n)))
        self.eval_model.add(layers.Dense(64, activation="relu"))
        self.eval_model.add(layers.Dense(self.action_n))

        # print(self.eval_model.summary())

        # ------------------ build target network ---------------------
        self.target_model = models.Sequential(name="target_network")
        self.target_model.add(layers.Dense(64, activation="relu", input_shape=(None, self.observation_n)))
        self.target_model.add(layers.Dense(64, activation="relu"))
        self.target_model.add(layers.Dense(self.action_n))

        # print(self.target_model.summary())
