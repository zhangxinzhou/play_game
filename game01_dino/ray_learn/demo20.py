import os.path

import ray
from ray import tune
from ray.rllib.agents import ppo

from sqlalchemy import Column, BIGINT, NUMERIC, VARCHAR, TEXT, TIMESTAMP, Interval, create_engine
from sqlalchemy.sql.expression import text
from sqlalchemy import func
from sqlalchemy.orm import declarative_base, sessionmaker

from datetime import datetime
import uuid
import json
import gc

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


def get_uuid():
    return uuid.uuid4().hex


engine = create_engine(
    url="postgresql+psycopg2://postgres:postgres@localhost:5432/postgres",
    encoding="utf-8",
    echo=True
)
Base.metadata.create_all(engine)
# 建表
db_session = sessionmaker(bind=engine, autocommit=True)
session = db_session()

################ 定义常量 ################
# 模型文件存放路径
model_path = r"F:\models"
# 游戏名称
env_name = "MyEnv1"
# checkpoint文件存放文件夹
local_dir = os.path.join(model_path, env_name)
# 环境-最大承载量
env_capacity = 100
# 模型全连接层
init_fcnet_hiddens = [10, 10]
# 训练迭代次数
training_iteration = 20
################ 定义常量 ################

# 删除全部数据-方便从头开始
is_delete_all = False
if is_delete_all:
    session.query(ModelIteration).delete()
    session.commit()

while True:
    gc.collect()
    model_count = session.query(func.count(ModelIteration.model_id)).scalar()
    # 如果era一条数据都没有，则初始化一个模型
    if model_count == 0:
        model_init_obj = ModelIteration(model_id=get_uuid(), train_seq=0, iteration_num=0,
                                        fcnet_hiddens=json.dumps(init_fcnet_hiddens),
                                        env_name=env_name, train_status="todo")
        session.add(model_init_obj)

    # 取出待训练的模型
    model_todo: ModelIteration = session.query(ModelIteration).filter_by(train_status="todo").first()
    if model_todo is not None:
        start_time = datetime.now()
        # 模型名称
        model_name = model_todo.model_id
        fcnet_hiddens = json.loads(model_todo.fcnet_hiddens)
        train_seq = session.query(func.max(ModelIteration.train_seq)).scalar() + 1
        ray.init()
        analysis = tune.run(
            # 与ray.agent.ppo.PPOTrainer，同样效果，只支持内置的算法
            run_or_experiment=ppo.PPOTrainer,
            # 保存路径
            local_dir=local_dir,
            # 名字
            name=model_name,
            # 停止条件
            stop={
                "training_iteration": training_iteration
            },
            config={
                "env": MyEnv1,
                "num_gpus": 0,
                "num_workers": 1,
                "model": {
                    "fcnet_hiddens": fcnet_hiddens
                },
                # "lr": tune.grid_search([0.01, 0.001, 0.0001])
            },
            # 同时运行两个实验
            num_samples=1,
            # 在训练结束后存储模型
            checkpoint_at_end=True
        )
        ray.shutdown()

        analysis.default_metric = "episode_reward_mean"
        analysis.default_mode = "max"
        best_checkpoint = analysis.best_checkpoint.local_path
        best_result = analysis.best_result

        episode_reward_max = best_result.get("episode_reward_max")
        episode_reward_min = best_result.get("episode_reward_min")
        episode_reward_mean = best_result.get("episode_reward_mean")
        episode_len_mean = best_result.get("episode_len_mean")
        episode_reward_rate = episode_reward_mean / episode_len_mean

        end_time = datetime.now()
        era_cost = end_time - start_time
        model_todo.checkpoint_path = best_checkpoint
        model_todo.train_start_date = start_time
        model_todo.train_end_date = end_time
        model_todo.train_cost_time = era_cost
        model_todo.train_status = "done"
        model_todo.train_info = '{}'
        model_todo.train_seq = train_seq
        model_todo.training_iteration = training_iteration
        model_todo.episode_reward_max = episode_reward_max
        model_todo.episode_reward_min = episode_reward_min
        model_todo.episode_reward_mean = episode_reward_mean
        model_todo.episode_len_mean = episode_len_mean
        model_todo.passed = 'Y' if episode_reward_rate > 0.9 else 'N'
        model_todo.reward = episode_reward_mean
        cost = 1
        for num in fcnet_hiddens:
            cost * num
        model_todo.cost = cost
    else:
        # 所有待训练的模型已经训练完毕,因此繁衍下一代模型
        iteration_max = session.query(func.max(ModelIteration.iteration_num)).filter_by(train_status="done").scalar()
        iteration_next_num = iteration_max + 1
        # 取出最近一代已训练完成的全部模型的
        iteration_list = session.query(ModelIteration).filter_by(iteration_num=iteration_max).order_by(
            ModelIteration.reward.desc(), ModelIteration.cost.asc()).all()
        for index, model_tmp in enumerate(iteration_list):
            # 更新最近一代模型的排名
            model_tmp.rank = index + 1
        # 优先获取合格的(passed=Y)模型,如果没有合格的,则获取全部的模型,排个序,优秀的模型繁衍下一代
        iteration_list = session.query(ModelIteration).filter_by(iteration_num=iteration_max, passed='Y').order_by(
            ModelIteration.rank.desc()).all()
        if len(iteration_list) == 0:
            iteration_list = session.query(ModelIteration).filter_by(iteration_num=iteration_max).order_by(
                ModelIteration.rank.desc()).all()

        for index, model_tmp in enumerate(iteration_list):
            fcnet_hiddens_old = json.loads(model_tmp.fcnet_hiddens)
            fcnet_hiddens_new_list = list_mutation.list_mutation(fcnet_hiddens_old)
            for fcnet_hiddens_new in fcnet_hiddens_new_list:
                model_next_obj = ModelIteration(model_id=get_uuid(), model_parent_id=model_tmp.model_id,
                                                iteration_num=iteration_next_num,
                                                fcnet_hiddens=json.dumps(fcnet_hiddens_new), env_name=env_name,
                                                train_status="todo")
                session.add(model_next_obj)
            # 环境承载能力,下一代最多有一百个
            model_next_count = session.query(func.count(ModelIteration.model_id)).filter_by(
                iteration_num=iteration_next_num).scalar()
            if model_next_count >= env_capacity:
                break
