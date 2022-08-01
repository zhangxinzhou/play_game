from sqlalchemy import Column, Integer, VARCHAR, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users1'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(256), nullable=False)
    age = Column(Integer)
    place = Column(VARCHAR(256), nullable=False)

    def __init__(self, id, name, age, place):
        self.id = id
        self.name = name
        self.age = age
        self.place = place


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


def add_user(user):
    session = get_session()
    session.add(user)
    session.commit()
    session.close()


def query_user():
    session = get_session()
    users = session.query(User).all()
    session.close()
    return users


def print_all(users):
    names = [user.name for user in users]
    print(names)


def update_user():
    session = get_session()
    session.query(User).filter(User.name == 'zhangsan').update({"place": "Shanghai"})
    session.commit()
    session.close()


def delete_user(user_id):
    session = get_session()
    session.query(User).filter(User.id == user_id).delete()
    session.commit()
    session.close()


if __name__ == '__main__':
    init_db()
    zhangsan = User(1, 'zhangsan', 18, 'Chengdu')
    lisi = User(2, 'lisi', 19, 'Beijing')
    add_user(lisi)
    users = query_user()
    print_all(users)
    update_user()
    delete_user(1)
