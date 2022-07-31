import psycopg2
import uuid
import config_util

# 连接数据库需要提供相应的数据库名称、用户名、密码、地址、端口等信息
config = config_util.get_config()
db = config['postgres']['db']
host = config['postgres']['host']
port = config['postgres']['port']
user = config['postgres']['user']
pw = config['postgres']['pw']

conn = psycopg2.connect(database=db, host=host, port=port, user=user, password=pw)
curs = conn.cursor()


def generate_uuid():
    return uuid.uuid4().hex


def fetchone_to_dict(row, description: tuple) -> dict:
    if row is None or len(row) == 0:
        return None
    else:
        obj = {}
        for index, column in enumerate(description):
            column_name = column[0]
            obj[column_name] = row[index]
        return obj


def fetchall_to_list(rows, description: tuple) -> list:
    if rows is None or len(rows) == 0:
        return []
    else:
        obj_list = []
        for row in rows:
            obj = {}
            for index, column in enumerate(description):
                column_name = column[0]
                obj[column_name] = row[index]
            obj_list.append(obj)
        return obj_list


def query_one_by_sql(sql_: str) -> dict:
    curs.execute(sql_)
    row = curs.fetchone()
    description = curs.description
    return fetchone_to_dict(row, description)


def query_list_by_sql(sql_: str) -> list:
    curs.execute(sql_)
    rows = curs.fetchall()
    description = curs.description
    return fetchall_to_list(rows, description)


def add_model_era(model_era: dict) -> None:
    print("aaa")
    # 提交事务
    curs.execute("commit;")


def add_model_age(model_age_dict) -> None:
    print("aaa")
    # 提交事务
    curs.execute("commit;")


def get_model_era(env_name, input_shape, output_dim) -> dict:
    sql1 = fr"select count(*) total from model_era where env_name = '{env_name}'"
    obj1 = query_one_by_sql(sql1)
    model_count = obj1.get("total", 0)
    if model_count == 0:
        # 一个模型都没有,需要初始化一个模型
        sql2 = fr"INSERT INTO model_era (model_id, era_num, env_name, input_shape, output_dim, hidden_layer)" \
               fr"VALUES('{generate_uuid()}', 0, '{env_name}', {input_shape}, {output_dim}, '[10,10]')"
        curs.execute(sql2)

    # 查询模型
    curs.execute("commit;")
    return 0


if __name__ == '__main__':
    get_model_era('MyDev1', 10, 10)
