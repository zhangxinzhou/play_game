import random

from sqlalchemy import Column, BIGINT, NUMERIC, VARCHAR, TEXT, TIMESTAMP, Interval, create_engine
from sqlalchemy.sql.expression import text
from sqlalchemy import func
from sqlalchemy.orm import declarative_base, sessionmaker

from datetime import datetime
import uuid
import time
import json
import game01_dino.new_test.game_utils as game_utils

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
    model_parent_id = Column(VARCHAR, comment="父模型id")
    checkpoint_path = Column(VARCHAR, comment="模型路径")
    era_num = Column(BIGINT, comment="世代")
    age_num = Column(BIGINT, comment="年龄")
    input_shape = Column(VARCHAR, comment="输入形状(游戏图像的形状)")
    output_shape = Column(VARCHAR, comment="输出维度(动作空间)")
    hidden_layer = Column(TEXT, comment="隐藏层(json),包含卷积层和全连接层")
    env_name = Column(VARCHAR, comment="环境名称")
    train_start_date = Column(TIMESTAMP, comment="训练开始时间")
    train_end_date = Column(TIMESTAMP, comment="训练结束时间")
    train_cost_time = Column(Interval, comment="训练花费时间")
    train_seq = Column(BIGINT, comment="顺序")
    created_by = Column(VARCHAR, comment="创建人", server_default="system")
    created_date = Column(TIMESTAMP, comment="创建时间", server_default=text("NOW()"))
    updated_by = Column(VARCHAR, comment="更新人", server_default="system")
    updated_date = Column(TIMESTAMP, comment="更新时间", server_default=text("NOW()"))


def get_engine():
    return create_engine(
        url="postgresql+psycopg2://postgres:postgres@localhost:5432/postgres",
        encoding="utf-8",
        echo=True
    )


def init_db():
    engine = get_engine()
    Base.metadata.create_all(engine)
    print('Create table successfully!')


def get_session() -> sessionmaker:
    engine = get_engine()
    db_session = sessionmaker(bind=engine)
    return db_session()


def get_connect():
    engine = get_engine()
    return engine.connect()


def get_uuid():
    return uuid.uuid4().hex


def db_test():
    init_db()

    start = datetime.now()
    time.sleep(1)
    end = datetime.now()
    cost = end - start
    print("=" * 100)
    print(cost)
    print(type(cost))
    m1 = ModelEra(model_id=get_uuid(), train_start_date=start, train_end_date=end, train_cost_time=cost)
    session = get_session()
    session.add(m1)

    count = session.query(func.count(ModelEra.model_id)).scalar()
    print(f"count={count}")

    con = get_connect()
    results = con.execute('select now();')
    for result in results:
        print(result)
        print(type(result))

    # 释放资源
    session.commit()
    session.close()


if __name__ == '__main__':
    # 建表
    init_db()
    # 常量定义
    env_name = "env_name"
    input_shape = 1
    output_shape = 1
    # 环境最大承载量
    env_capacity = 100
    session = get_session()

    init_hidden_layer = {
        "mutation_type": "init",
        "convolutional_layer": [],
        "fully_connected_layer": [100, 10]
    }

    # 删除数据
    session.query(ModelEra).delete()
    session.query(ModelAge).delete()
    for i in range(100):
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
            train_seq = session.query(func.max(ModelEra.train_seq)).scalar() + 1
            era_start = datetime.now()
            # 训练
            for age in range(1, 3):
                age_start = datetime.now()
                time.sleep(0.1)
                age_end = datetime.now()
                age_cost = age_end - age_start
                age_obj = ModelAge(model_age_id=get_uuid(), model_id=era_todo.model_id, train_seq=train_seq,
                                   train_start_date=age_start, train_end_date=age_end,
                                   train_cost_time=age_cost)
                session.add(age_obj)

            reward = random.randint(0, 100)
            era_end = datetime.now()
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
            era_todo.cost = random.randint(0, 100)
            session.commit()

        else:
            # 所有待训练的模型已经训练完毕,因此繁衍下一代模型
            era_max = session.query(func.max(ModelEra.era_num)).filter_by(train_status="done").scalar()
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

            era_next_count = 0
            for index, era_tmp in enumerate(era_list):
                hidden_layer = json.loads(era_tmp.hidden_layer)
                hidden_layer_mutation_list = game_utils.hidden_layer_mutation(hidden_layer)
                for hidden_layer_mutation in hidden_layer_mutation_list:
                    era_next_obj = ModelEra(model_id=get_uuid(), model_parent_id=era_tmp.model_id,
                                            era_num=era_max + 1, input_shape=input_shape, output_shape=output_shape,
                                            hidden_layer=json.dumps(hidden_layer_mutation), env_name=env_name,
                                            train_status="todo")
                    session.add(era_next_obj)
                    era_next_count += 1
                # 环境承载能力,下一代最多有一百个
                if era_next_count >= env_capacity:
                    break

    # 提交事务
    session.commit()
