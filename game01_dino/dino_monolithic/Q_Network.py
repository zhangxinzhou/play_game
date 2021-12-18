import tensorflow as tf


class Q_Network:
    def __init__(self, observation_n, action_n):
        self.observation_n = observation_n
        self.action_n = action_n
        self._build_model()

    def create_model(self, model_name):
        model = tf.keras.models.Sequential(
            layers=[
                # tf.keras.layers.Flatten(input_shape=self.observation_n),
                tf.keras.layers.Dense(1024, activation='relu', input_shape=(None, self.observation_n)),
                tf.keras.layers.Dropout(0.5),
                tf.keras.layers.Dense(64, activation='relu'),
                tf.keras.layers.Dropout(0.5),
                tf.keras.layers.Dense(self.action_n)
            ],
            name=model_name
        )
        return model

    def _build_model(self):
        # ------------------ build eval network -------------------------
        self.eval_model = self.create_model(model_name="eval_network")
        # print(self.eval_model.summary())

        # ------------------ build target network ---------------------
        self.target_model = self.create_model(model_name="target_network")
        # print(self.target_model.summary())
