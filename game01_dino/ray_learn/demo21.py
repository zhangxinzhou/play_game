import os.path

import ray
from ray import tune
from ray.rllib.agents import ppo

from sqlalchemy import Column, BIGINT, NUMERIC, VARCHAR, TEXT, TIMESTAMP, Interval, create_engine
from sqlalchemy.sql.expression import text
from sqlalchemy import func
from sqlalchemy.orm import declarative_base, sessionmaker

from datetime import datetime
import json

from demo06 import MyEnv1
import list_mutation

Base = declarative_base()


class ModelIteration(Base):
    # 表信息
    __tablename__ = "model_iteration_test02"
    __table_args__ = ({"comment": "模型迭代表"})
    # 表字段信息
    model_id = Column(VARCHAR, primary_key=True, comment="模型id")
    model_parent_id = Column(VARCHAR, comment="父模型id")
    checkpoint_path = Column(VARCHAR, comment="存储路径")
    iteration_num = Column(BIGINT, comment="世代(第几代)")
    env_name = Column(VARCHAR, comment="环境名称")
    fcnet_hiddens = Column(TEXT, comment="模型全连接层")
    train_status = Column(VARCHAR, comment="todo(待处理),doing(处理中),done(处理完成)", server_default="todo")
    train_start_date = Column(TIMESTAMP, comment="训练开始时间")
    train_end_date = Column(TIMESTAMP, comment="训练结束时间")
    train_cost_time = Column(Interval, comment="训练花费时间")
    train_info = Column(TEXT, comment="训练信息(json字符串)")
    train_seq = Column(BIGINT, comment="顺序")
    training_iteration = Column(BIGINT, comment="episode_reward_max")
    episode_reward_max = Column(NUMERIC, comment="episode_reward_max")
    episode_reward_min = Column(NUMERIC, comment="episode_reward_min")
    episode_reward_mean = Column(NUMERIC, comment="episode_reward_mean")
    episode_len_mean = Column(NUMERIC, comment="episode_len_mean")
    passed = Column(VARCHAR, comment="是否合格（Y或N）")
    reward = Column(NUMERIC, comment="评分，报酬")
    cost = Column(NUMERIC, comment="花费，成本")
    rank = Column(BIGINT, comment="当前世代，排名")
    created_by = Column(VARCHAR, comment="创建人", server_default="system")
    created_date = Column(TIMESTAMP, comment="创建时间", server_default=text("NOW()"))
    updated_by = Column(VARCHAR, comment="更新人", server_default="system")
    updated_date = Column(TIMESTAMP, comment="更新时间", server_default=text("NOW()"))


engine = create_engine(
    url="postgresql+psycopg2://postgres:postgres@localhost:5432/postgres",
    encoding="utf-8",
    echo=True
)
# 建表
db_session = sessionmaker(bind=engine, autocommit=True)
session = db_session()

best_model: ModelIteration = session.query(ModelIteration).filter_by(train_status="done").order_by(
    ModelIteration.episode_reward_mean.desc()).first()
fcnet_hiddens = json.loads(best_model.fcnet_hiddens)
checkpoint_path = best_model.checkpoint_path
# 最好的模型
agent = ppo.PPOTrainer(config={
    "model": {
        "fcnet_hiddens": fcnet_hiddens
    }
}, env=MyEnv1)
agent.restore(checkpoint_path=checkpoint_path)
print(rf"fcnet_hiddens={fcnet_hiddens}")
print(rf"checkpoint_path={checkpoint_path}")
print("=" * 100)
env = MyEnv1()
# run until episode ends
for i in range(10):
    episode_reward = 0
    done = False
    obs = env.reset()
    while not done:
        # 设置full_fetch=True可以获得除了action外的其他辅助信息，
        # 包括action的logits，及obs的value等
        action = agent.compute_action(obs)
        obs, reward, done, info = env.step(action)
        episode_reward += reward

    print(f"NO.{i},episode_reward={episode_reward}")
