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


def get_model_era() -> dict:
    return 0


def add_model_era(model_era: dict) -> None:
    print("aaa")
    # 提交事务
    curs.execute("commit;")


def add_model_age(model_age_dict) -> None:
    print("aaa")
    # 提交事务
    curs.execute("commit;")


if __name__ == '__main__':
    sql = "select count(*) total from model_era"
    obj = query_one_by_sql(sql)
    total = obj.get("total", 0)
    print(total)
