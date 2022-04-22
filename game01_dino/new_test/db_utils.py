import psycopg2
import uuid

# 连接数据库需要提供相应的数据库名称、用户名、密码、地址、端口等信息

db = 'zxz'
user = 'postgres'
pw = 'admin'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(database=db, user=user, password=pw, host=host, port=port)
curs = conn.cursor()


def generate_uuid():
    return uuid.uuid4().hex


def conn_close():
    curs.close()
    conn.close()


def insert_model_generation(model_id):
    sql = f"insert into model_generation (model_id) values('{model_id}')"
    curs.execute(sql)
    # 提交事务
    curs.execute("commit;")


def insert_model_train_detail(model_id):
    sql = f"insert into model_train_detail (model_id) values('{model_id}')"
    curs.execute(sql)
    # 提交事务
    curs.execute("commit;")


def query_model_generation_by_model_id(model_id):
    sql = f"select * from model_generation where model_id = '{model_id}'"
    curs.execute(sql)
    return curs.fetchall()


def query_model_train_detail_by_model_id(model_id):
    sql = f"select * from model_train_detail where model_id = '{model_id}'"
    curs.execute(sql)
    return curs.fetchall()


if __name__ == '__main__':
    model_id = generate_uuid()
    insert_model_generation(model_id)
    insert_model_train_detail(model_id)
    d1 = query_model_generation_by_model_id(model_id)
    d2 = query_model_train_detail_by_model_id(model_id)
    print(d1)
    print(d2)
