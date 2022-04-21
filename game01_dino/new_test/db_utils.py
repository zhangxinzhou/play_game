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

uid = uuid.uuid4()
# insert_sql = f"INSERT INTO zxz1(id, name) VALUES('{uid}', '{uid}')"
# curs.execute(insert_sql)
# curs.execute('commit')

select_sql = "select * from model_generation"  # 从表格table中读取全表内容
curs.execute(select_sql)  # 执行该sql语句
data = curs.fetchall()  # 获取数据


def generate_uuid():
    uid = uuid.uuid4().hex
    return uid


if __name__ == '__main__':
    uid = generate_uuid()
    print(uid)

curs.close()
conn.close()
