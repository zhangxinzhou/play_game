from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation

model = Sequential()  # 顺序模型

# 输入层
model.add(Dense(7, input_shape=(4,)))  # Dense就是常用的全连接层
model.add(Activation('sigmoid'))  # 激活函数

# 隐层
model.add(Dense(13))  # Dense就是常用的全连接层
model.add(Activation('sigmoid'))  # 激活函数

# 输出层
model.add(Dense(5))
model.add(Activation('softmax'))

# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])

tmp = model.summary()
print("0" * 100)
print(tmp)
