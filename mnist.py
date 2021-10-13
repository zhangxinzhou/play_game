import os
import tensorflow as tf
import time

# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

t0 = time.time()
model.fit(x_train, y_train, epochs=10)
model.evaluate(x_test, y_test)
t1 = time.time()
print("cost {} ms".format(1000 * (t1 - t0)))
