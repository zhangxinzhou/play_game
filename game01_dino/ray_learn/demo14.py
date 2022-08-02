from sqlalchemy import Column, BIGINT, NUMERIC, VARCHAR, TEXT, TIMESTAMP, create_engine
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class ModelEra(Base):
    # 表信息
    __tablename__ = "model_era1"
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
    training_cost_time = Column(NUMERIC, comment="训练花费时间")
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


class ModelAge(Base):
    # 表信息
    __tablename__ = "model_age1"
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
    training_cost_time = Column(VARCHAR, comment="训练花费时间")
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


def get_session():
    engine = get_engine()
    db_session = sessionmaker(bind=engine)
    return db_session()


def get_connect():
    engine = get_engine()
    return engine.connect()


if __name__ == '__main__':
    init_db()
    m1 = ModelEra(model_id='ccc')
    session = get_session()
    session.add(m1)

    con = get_connect()
    results = con.execute('select now();')
    for result in results:
        print(result)

    # 释放资源
    session.commit()
    session.close()
