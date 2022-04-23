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


def get_insert_sql(table_name, row: dict):
    sql = f'insert into {table_name}'
    key_str = ""
    val_str = ""
    for index, (key, value) in enumerate(row.items()):
        prefix = "" if index == 0 else ","
        if isinstance(value, str):
            value = "'" + value + "'"
        key_str += prefix + key
        val_str += prefix + str(value)
    sql += " (" + key_str + ") values (" + val_str + ");"
    # print(sql)
    return sql


def insert_model_generation(data):
    if isinstance(data, dict):
        row = data
        sql = get_insert_sql(table_name="model_generation", row=row)
        curs.execute(sql)
    elif isinstance(data, list):
        for row in data:
            sql = get_insert_sql(table_name="model_generation", row=row)
            curs.execute(sql)
    # 提交事务
    curs.execute("commit;")


def insert_model_train_detail(data):
    if isinstance(data, dict):
        row = data
        sql = get_insert_sql(table_name="model_train_detail", row=row)
        curs.execute(sql)
    elif isinstance(data, list):
        for row in data:
            sql = get_insert_sql(table_name="model_train_detail", row=row)
            curs.execute(sql)
    # 提交事务
    curs.execute("commit;")


def query_one_model_generation_by_model_id(model_id):
    sql = f"select * from model_generation where model_id = '{model_id}'"
    curs.execute(sql)
    row = curs.fetchone()
    if row is None:
        return None

    description = curs.description
    result = {}
    for index, column in enumerate(description):
        column_name = column[0]
        result[column_name] = row[index]
    return result


def query_list_model_train_detail_by_model_id(model_id):
    sql = f"select * from model_train_detail where model_id = '{model_id}'"
    curs.execute(sql)
    rows = curs.fetchall()
    if rows is None or len(rows) == 0:
        return []
    description = curs.description
    result = []
    for row in rows:
        tmp = {}
        for index, column in enumerate(description):
            column_name = column[0]
            tmp[column_name] = row[index]
        # 将字典添加到list中
        result.append(tmp)
    return result


if __name__ == '__main__':
    model_id = generate_uuid()
    model_obj = {
        "model_id": model_id,
    }
    train_list = [
        {"model_id": model_id, "train_id": generate_uuid()},
        {"model_id": model_id, "train_id": generate_uuid()},
        {"model_id": model_id, "train_id": generate_uuid()}
    ]
    insert_model_generation(model_obj)
    insert_model_train_detail(train_list)
    oo: dict = query_one_model_generation_by_model_id(model_id)
    ll: list = query_list_model_train_detail_by_model_id(model_id)
    print(oo)
    for item in ll:
        print(item)
