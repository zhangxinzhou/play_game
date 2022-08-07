import os
import ray
import shutil

from sqlalchemy import Column, BIGINT, NUMERIC, VARCHAR, TEXT, TIMESTAMP, Interval, create_engine
from sqlalchemy.sql.expression import text
from sqlalchemy import func
from sqlalchemy.orm import declarative_base, sessionmaker
from ray.rllib.agents import ppo

from datetime import datetime
import uuid
import time
import json
import game01_dino.new_test.game_utils as game_utils
from demo06 import MyEnv1

Base = declarative_base()


class ModelEra(Base):
    # 表信息
    __tablename__ = "model_era_test01"
    __table_args__ = ({"comment": "模型迭代表"})
    # 表字段信息
    model_id = Column(VARCHAR, primary_key=True, comment="模型id")
    model_parent_id = Column(VARCHAR, comment="父模型id")
    checkpoint_path = Column(VARCHAR, comment="存储路径")
    era_num = Column(BIGINT, comment="世代(第几代)")
    env_name = Column(VARCHAR, comment="环境名称")
    input_shape = Column(VARCHAR, comment="输入形状(游戏图像的形状)")
    output_shape = Column(VARCHAR, comment="输出维度(动作空间)")
    hidden_layer = Column(TEXT, comment="隐藏层(json),包含卷积层和全连接层")
    train_status = Column(VARCHAR, comment="todo(待处理),doing(处理中),done(处理完成)", server_default="todo")
    train_start_date = Column(TIMESTAMP, comment="训练开始时间")
    train_end_date = Column(TIMESTAMP, comment="训练结束时间")
    train_cost_time = Column(Interval, comment="训练花费时间")
    train_info = Column(TEXT, comment="训练信息(json字符串)")
    train_seq = Column(BIGINT, comment="顺序")
    best_age = Column(BIGINT, comment="表现最好的年龄")
    passed = Column(VARCHAR, comment="是否合格（Y或N）")
    reward = Column(NUMERIC, comment="当前世代，评分，报酬")
    cost = Column(NUMERIC, comment="当前世代，花费，成本")
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


class ModelAge(Base):
    # 表信息
    __tablename__ = "model_age_test01"
    __table_args__ = ({"comment": "模型年龄表(训练过程)"})
    # 表字段信息
    model_age_id = Column(VARCHAR, primary_key=True, comment="年龄id(训练迭代次数)")
    model_id = Column(VARCHAR, comment="模型id")
    checkpoint_path = Column(VARCHAR, comment="模型路径")
    era_num = Column(BIGINT, comment="世代")
    age_num = Column(BIGINT, comment="年龄")
    train_start_date = Column(TIMESTAMP, comment="训练开始时间")
    train_end_date = Column(TIMESTAMP, comment="训练结束时间")
    train_cost_time = Column(Interval, comment="训练花费时间")
    train_seq = Column(BIGINT, comment="顺序")
    episode_reward_max = Column(NUMERIC, comment="最大奖励")
    episode_reward_min = Column(NUMERIC, comment="最小奖励")
    episode_reward_mean = Column(NUMERIC, comment="平均奖励")
    agent_timesteps_total = Column(NUMERIC, comment="时间")
    created_by = Column(VARCHAR, comment="创建人", server_default="system")
    created_date = Column(TIMESTAMP, comment="创建时间", server_default=text("NOW()"))
    updated_by = Column(VARCHAR, comment="更新人", server_default="system")
    updated_date = Column(TIMESTAMP, comment="更新时间", server_default=text("NOW()"))


def get_uuid():
    return uuid.uuid4().hex


engine = create_engine(
    url="postgresql+psycopg2://postgres:postgres@localhost:5432/postgres",
    encoding="utf-8",
    echo=False
)
Base.metadata.create_all(engine)
# 建表
db_session = sessionmaker(bind=engine, autocommit=True)
session = db_session()

################ 定义常量 ################
# 环境-名称
env_name = "MyEnv1"
# 环境-最大承载量
env_capacity = 100
# 环境-年龄限制
age_limit = 30
# 环境-图像输入空间
input_shape = 1
# 环境-动作空间
output_shape = 1
# 模型初始的网络
init_hidden_layer = {
    "mutation_type": "init",
    "convolutional_layer": [],
    "fully_connected_layer": [100, 10]
}
################ 定义常量 ################


# 删除全部数据-方便从头开始
is_delete_all = False
if is_delete_all:
    session.query(ModelEra).delete()
    session.query(ModelAge).delete()
    session.commit()

################ 初始化ray ################
ray.init()
ppo_config = ppo.DEFAULT_CONFIG.copy()
################ 初始化ray ################
while True:
    era_count = session.query(func.count(ModelEra.model_id)).scalar()
    # 如果era一条数据都没有，则初始化一个模型
    if era_count == 0:
        era_init_obj = ModelEra(model_id=get_uuid(), train_seq=0, era_num=0, input_shape=input_shape,
                                output_shape=output_shape, hidden_layer=json.dumps(init_hidden_layer),
                                env_name=env_name, train_status="todo")
        session.add(era_init_obj)

    # 取出待训练的模型
    era_todo: ModelEra = session.query(ModelEra).filter_by(train_status="todo").first()
    if era_todo is not None:
        era_start = datetime.now()
        fully_connected_layer = json.loads(era_todo.hidden_layer)["fully_connected_layer"]
        ppo_config['model']['fcnet_hiddens'] = fully_connected_layer
        trainer = ppo.PPOTrainer(env=MyEnv1, config=ppo_config)
        model_id = era_todo.model_id
        checkpoint_dir = fr'F:\models\{env_name}\{model_id}'
        episode_reward_mean_best = 0
        checkpoint_path_best = None
        train_seq = session.query(func.max(ModelEra.train_seq)).scalar() + 1
        # 训练
        for age in range(1, age_limit + 1):
            age_start = datetime.now()
            # 模型开始第age次迭代(迭代参数)
            trainer_result = trainer.train()
            episode_reward_max = trainer_result['episode_reward_max']
            episode_reward_min = trainer_result['episode_reward_min']
            episode_reward_mean = trainer_result['episode_reward_mean']
            agent_timesteps_total = trainer_result['agent_timesteps_total']
            # 保存模型
            checkpoint_path = trainer.save(checkpoint_dir)
            if episode_reward_mean_best < episode_reward_mean:
                episode_reward_mean_best = episode_reward_mean
                checkpoint_path_best = checkpoint_path
            age_end = datetime.now()
            age_cost = age_end - age_start
            age_obj = ModelAge(model_age_id=get_uuid(), model_id=era_todo.model_id, checkpoint_path=checkpoint_path,
                               train_seq=train_seq, era_num=era_todo.era_num, age_num=age,
                               train_start_date=age_start, train_end_date=age_end, train_cost_time=age_cost,
                               episode_reward_max=episode_reward_max, episode_reward_min=episode_reward_min,
                               episode_reward_mean=episode_reward_mean, agent_timesteps_total=agent_timesteps_total)
            session.add(age_obj)

        reward = episode_reward_mean
        era_end = datetime.now()
        era_todo.checkpoint_path = checkpoint_path_best
        era_cost = era_end - era_start
        era_todo.train_start_date = era_start
        era_todo.train_end_date = era_start
        era_todo.train_cost_time = era_cost
        era_todo.train_status = "done"
        era_todo.train_info = '{}'
        era_todo.train_seq = train_seq
        era_todo.best_age = 1
        era_todo.passed = 'Y' if reward > 50 else 'N'
        era_todo.reward = reward
        era_todo.cost = sum(fully_connected_layer)

        # 结束训练
        trainer.stop()
        # 删除不是最优的checkpoint的数据，只保留最优的checkpoint数据
        folder_list = os.listdir(checkpoint_dir)
        for folder in folder_list:
            path_tmp = os.path.join(checkpoint_dir, folder)
            if os.path.exists(path_tmp):
                path_best = os.path.dirname(checkpoint_path_best)
                if path_best != path_tmp:
                    shutil.rmtree(path_tmp)

    else:
        # 所有待训练的模型已经训练完毕,因此繁衍下一代模型
        era_max = session.query(func.max(ModelEra.era_num)).filter_by(train_status="done").scalar()
        era_next_num = era_max + 1
        # 取出最近一代已训练完成的全部模型的
        era_list = session.query(ModelEra).filter_by(era_num=era_max).order_by(ModelEra.reward.desc()).all()
        for index, era_tmp in enumerate(era_list):
            # 更新最近一代模型的排名
            era_tmp.rank = index + 1
        # 优先获取合格的(passed=Y)模型,如果没有合格的,则获取全部的模型,排个序,优秀的模型繁衍下一代
        era_list = session.query(ModelEra).filter_by(era_num=era_max, passed='Y').order_by(
            ModelEra.rank.desc()).all()
        if len(era_list) == 0:
            era_list = session.query(ModelEra).filter_by(era_num=era_max).order_by(
                ModelEra.rank.desc()).all()

        for index, era_tmp in enumerate(era_list):
            hidden_layer = json.loads(era_tmp.hidden_layer)
            hidden_layer_mutation_list = game_utils.hidden_layer_mutation(hidden_layer)
            for hidden_layer_mutation in hidden_layer_mutation_list:
                era_next_obj = ModelEra(model_id=get_uuid(), model_parent_id=era_tmp.model_id,
                                        era_num=era_next_num, input_shape=input_shape, output_shape=output_shape,
                                        hidden_layer=json.dumps(hidden_layer_mutation), env_name=env_name,
                                        train_status="todo")
                session.add(era_next_obj)
            # 环境承载能力,下一代最多有一百个
            era_next_count = session.query(func.count(ModelEra.model_id)).filter_by(era_num=era_next_num).scalar()
            if era_next_count >= env_capacity:
                break
