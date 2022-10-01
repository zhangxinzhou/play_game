import os.path

import gym
import ray
from ray import air, tune
import ray.rllib.algorithms.ppo as ppo

from sqlalchemy import Column, BIGINT, NUMERIC, VARCHAR, TEXT, TIMESTAMP, Interval, create_engine
from sqlalchemy.sql.expression import text
from sqlalchemy import func
from sqlalchemy.orm import declarative_base, sessionmaker

from datetime import datetime
import uuid
import json
from pynput import keyboard

from src.utils import list_mutation
from src.utils import config_util

###############################################
# 常量相关定义
# 从
config = config_util.get_config()
# 模型,是训练还是测试
TRAIN_MODEL = False
# 框架
FRAMEWORK = "torch"
# 模型文件存放路径
MODEL_PATH = config['model']['root_dir']
# 数据库的连接串
DB_URL = config['postgres']['url']
# 游戏名称
ENV_NAME = "CartPole-v0"
# checkpoint文件存放文件夹
LOCAL_DIR = os.path.join(MODEL_PATH, ENV_NAME)
# 环境-最大承载量
ENV_CAPACITY = 100
# 模型全连接层
INIT_FCNET_HIDDENS = [10, 10]
# 训练迭代次数
TRAINING_ITERATION = 50
###############################################

Base = declarative_base()


class ModelIteration(Base):
    # 表信息
    __tablename__ = "model_iteration_0001"
    __table_args__ = ({"comment": "模型迭代表"})
    # 表字段信息
    model_id = Column(VARCHAR, primary_key=True, comment="模型id")
    model_parent_id = Column(VARCHAR, comment="父模型id")
    checkpoint_path = Column(VARCHAR, comment="存储路径")
    iteration_num = Column(BIGINT, comment="世代(第几代)")
    env_name = Column(VARCHAR, comment="环境名称")
    framework = Column(VARCHAR, comment="框架类型")
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
    error = Column(TEXT, comment="error")
    passed = Column(VARCHAR, comment="是否合格（Y或N）")
    reward = Column(NUMERIC, comment="评分，报酬")
    cost = Column(NUMERIC, comment="花费，成本")
    rank = Column(BIGINT, comment="当前世代，排名")
    created_by = Column(VARCHAR, comment="创建人", server_default="system")
    created_date = Column(TIMESTAMP, comment="创建时间", server_default=text("NOW()"))
    updated_by = Column(VARCHAR, comment="更新人", server_default="system")
    updated_date = Column(TIMESTAMP, comment="更新时间", server_default=text("NOW()"))

    def __str__(self):
        line0 = ""
        line1 = ""
        line2 = ""
        for key, val in self.__dict__.items():
            if not str(key).startswith("_"):
                tmp1 = str(key)
                tmp2 = str(val)
                len1 = len(tmp1)
                len2 = len(tmp2)
                diff = abs(len1 - len2)
                line0 += "-" * (max(len1, len2) + 1)
                if len1 > len2:
                    line1 += tmp1 + "|"
                    line2 += tmp2 + " " * diff + "|"
                else:
                    line1 += tmp1 + " " * diff + "|"
                    line2 += tmp2 + "|"
        return "\n".join([line0, line1, line2, line0])


def get_uuid():
    return uuid.uuid4().hex


engine = create_engine(url=DB_URL, encoding="utf-8", echo=True)
Base.metadata.create_all(engine)
# 建表
db_session = sessionmaker(bind=engine, autocommit=True)
session = db_session()

# 开关,控制,如果监听到esc按键被按下,整个程序就会停止
switch = True


def on_press(key):
    if key == keyboard.Key.f12:
        global switch
        switch = False
        print("*" * 50, f"监听到{key}按键被按下...", "*" * 50)
        print("*" * 50, "程序将在本次训练完毕后结束...", "*" * 50)
        return False


listener = keyboard.Listener(on_press=on_press)
listener.start()

if TRAIN_MODEL:
    # 训练开始
    print("*" * 50, "训练开始...", "*" * 50)
    while switch:
        model_count = session.query(func.count(ModelIteration.model_id)).scalar()
        # 如果era一条数据都没有，则初始化一个模型
        if model_count == 0:
            model_init_obj = ModelIteration(model_id=get_uuid(), train_seq=0, iteration_num=0,
                                            fcnet_hiddens=json.dumps(INIT_FCNET_HIDDENS),
                                            env_name=ENV_NAME, train_status="todo")
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
            tuner = tune.Tuner(
                ppo.PPO,
                param_space={
                    "env": ENV_NAME,
                    "framework": FRAMEWORK,
                    "model": {
                        "fcnet_hiddens": fcnet_hiddens
                    },
                    "num_gpus": 1,
                    "num_workers": 10,
                    # "lr": tune.grid_search([0.01, 0.001, 0.0001]),
                },
                tune_config=ray.tune.tune_config.TuneConfig(
                    metric="episode_reward_mean",
                    mode="max"
                ),
                run_config=air.RunConfig(
                    # 保存路径
                    local_dir=LOCAL_DIR,
                    # 名字
                    name=model_name,
                    # 停止条件
                    stop={"training_iteration": TRAINING_ITERATION},
                    # verbose
                    verbose=2,
                    # checkpoint_config
                    checkpoint_config=air.CheckpointConfig(
                        checkpoint_at_end=True
                    )
                ),
            )
            results = tuner.fit()
            ray.shutdown()

            # 取出训练信息
            best_result = results.get_best_result(metric="episode_reward_mean", mode="max")
            best_result_config = best_result.config
            best_result_metrics = best_result.metrics
            best_checkpoint = best_result.checkpoint._local_path
            episode_reward_max = best_result_metrics.get('episode_reward_max')
            episode_reward_min = best_result_metrics.get('episode_reward_min')
            episode_reward_mean = best_result_metrics.get('episode_reward_mean')
            episode_len_mean = best_result_metrics.get('episode_len_mean')
            episode_reward_rate = episode_reward_mean / episode_len_mean
            error = best_result.error.__str__()

            # 更新数据库
            end_time = datetime.now()
            era_cost = end_time - start_time
            model_todo.framework = best_result_config.get("framework")
            model_todo.checkpoint_path = best_checkpoint
            model_todo.train_start_date = start_time
            model_todo.train_end_date = end_time
            model_todo.train_cost_time = era_cost
            model_todo.train_status = "done"
            model_todo.train_info = '{}'
            model_todo.train_seq = train_seq
            model_todo.training_iteration = TRAINING_ITERATION
            model_todo.episode_reward_max = episode_reward_max
            model_todo.episode_reward_min = episode_reward_min
            model_todo.episode_reward_mean = episode_reward_mean
            model_todo.episode_len_mean = episode_len_mean
            model_todo.error = error
            model_todo.passed = 'Y' if episode_reward_rate > 0.9 else 'N'
            model_todo.reward = episode_reward_mean
            cost = 1
            for num in fcnet_hiddens:
                cost = cost * num
            model_todo.cost = cost
            model_todo.updated_date = datetime.now()
        else:
            # 所有待训练的模型已经训练完毕,因此繁衍下一代模型
            iteration_max = session.query(func.max(ModelIteration.iteration_num)).filter_by(
                train_status="done").scalar()
            iteration_next_num = iteration_max + 1
            # 取出最近一代已训练完成的全部模型的
            iteration_list = session.query(ModelIteration).filter_by(iteration_num=iteration_max).order_by(
                ModelIteration.reward.desc(), ModelIteration.cost.asc()).all()
            for index, model_tmp in enumerate(iteration_list):
                # 更新最近一代模型的排名(评分高,成本低)
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
                                                    fcnet_hiddens=json.dumps(fcnet_hiddens_new), env_name=ENV_NAME,
                                                    train_status="todo")
                    session.add(model_next_obj)
                # 环境承载能力,下一代最多有一百个
                model_next_count = session.query(func.count(ModelIteration.model_id)).filter_by(
                    iteration_num=iteration_next_num).scalar()
                if model_next_count >= ENV_CAPACITY:
                    break
    # 训练结束
    print("*" * 50, "训练结束...", "*" * 50)
else:
    # 测试开始
    print("*" * 50, "测试开始...", "*" * 50)
    best_model: ModelIteration = session.query(ModelIteration).filter_by(train_status='done').order_by(
        ModelIteration.reward.desc(),
        ModelIteration.cost.asc()).first()
    best_agent = ppo.PPO(config={
        "framework": best_model.framework,
        "model": {
            "fcnet_hiddens": json.loads(best_model.fcnet_hiddens)
        }
    }, env=best_model.env_name)
    best_agent.restore(checkpoint_path=best_model.checkpoint_path)
    env = gym.make(best_model.env_name)
    print(best_model)
    for i in range(10):
        episode_reward = 0
        done = False
        obs = env.reset()
        while not done:
            action = best_agent.compute_action(obs)
            obs, reward, done, info = env.step(action)
            episode_reward += reward

        print(f"NO.{i},episode_reward={episode_reward}")

    # 测试结束
    print("*" * 50, "测试结束...", "*" * 50)
