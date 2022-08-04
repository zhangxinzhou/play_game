from sqlalchemy import Column, BIGINT, NUMERIC, VARCHAR, TEXT, TIMESTAMP, Interval, create_engine
from sqlalchemy.sql.expression import text
from sqlalchemy import func
from sqlalchemy.orm import declarative_base, sessionmaker

from datetime import datetime
import uuid
import time
import json

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
    training_status = Column(VARCHAR, comment="todo(待处理),doing(处理中),done(处理完成)", server_default="todo")
    training_start_date = Column(TIMESTAMP, comment="训练开始时间")
    training_end_date = Column(TIMESTAMP, comment="训练结束时间")
    training_cost_time = Column(Interval, comment="训练花费时间")
    train_info = Column(TEXT, comment="训练信息(json字符串)")
    best_age = Column(BIGINT, comment="表现最好的年龄")
    passed = Column(VARCHAR, comment="是否合格（Y或N）")
    reward = Column(VARCHAR, comment="当前世代，评分，报酬")
    cost = Column(VARCHAR, comment="当前世代，花费，成本")
    rank = Column(VARCHAR, comment="当前世代，排名")
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
    training_start_date = Column(TIMESTAMP, comment="训练开始时间")
    training_end_date = Column(TIMESTAMP, comment="训练结束时间")
    training_cost_time = Column(Interval, comment="训练花费时间")
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


def get_model_era():
    session = get_session()


def db_test():
    init_db()

    start = datetime.now()
    time.sleep(1)
    end = datetime.now()
    cost = end - start
    print("=" * 100)
    print(cost)
    print(type(cost))
    m1 = ModelEra(model_id=get_uuid(), training_start_date=start, training_end_date=end, training_cost_time=cost)
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
    session = get_session()
    for i in range(100):
        era_count = session.query(func.count(ModelEra.model_id)).scalar()
        # 如果era一条数据都没有，则初始化一个模型
        if era_count == 0:
            era_init_obj = ModelEra(model_id=get_uuid(), era_num=0, input_shape=input_shape, output_shape=output_shape,
                                    hidden_layer="[10,10]", env_name=env_name, training_status="todo")
            session.add(era_init_obj)

        # 取出待训练的模型
        era_todo = session.query(ModelEra).filter_by(training_status="todo").one()
        print(era_todo)

    session.commit()
    session.close()
