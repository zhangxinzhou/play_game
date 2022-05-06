import time
import random
import db_utils

# 环境容量-一代模型最大数量
env_capacity = 100
# 年龄限制,就是训练多少轮数
age_limit = 60
# 训练次数
train_episodes = 200
# 评估次数
test_episodes = 12


# 模型演化主流程
def model_evolution():
    a = 0
    while a < 10:
        a += 1
        # 判断是否有模型,如果没有,那就是第一次执行,需要初始化一个最初的模型,这就是初代模型
        is_init = db_utils.count_model_generation() == 0
        if is_init:
            # 初始化一个最初模型,存入数据库
            init_model_obj = {
                "model_id": db_utils.generate_uuid(),
                "generation_num": 0,
                "training_status": "init"
            }
            db_utils.insert_model_generation(init_model_obj)

        # 开始训练模型
        training_model_obj = db_utils.query_one_training_model_generation()
        if training_model_obj is not None:
            # 开始训练模型
            model_id = training_model_obj.get("model_id")
            # 模型表更新状态为训练中,更新模型开始训练时间
            db_utils.update_model_generation_start_time(model_id)
            # 查询待训练模型当前最大年龄
            age_max = db_utils.query_max_age_by_model_id(model_id)
            age_next = age_max + 1
            for age in range(age_next, age_limit + 1):
                # 一岁训练一次模型,一次模型训练需要执行train_episodes次游戏来更新参数,一次模型训练需要评估test_episodes次,来计算得分
                train_obj = {
                    "train_id": db_utils.generate_uuid(),
                    "model_id": model_id,
                    "score_total": random.randint(1, 100),
                    "age_num": age
                }
                db_utils.insert_model_train_detail(train_obj)

            # 模型训练完成
            # 取出模型的全部训练数据,并排序
            train_list = db_utils.query_list_model_train_detail_by_model_id(model_id)
            train_list.sort(key=lambda item: (item.get('score_total', 0)), reverse=True)
            train_obj_best = train_list[0]
            best_age = train_obj_best.get("age_num")
            best_score = train_obj_best.get("score_total")
            # 模型表更新状态为已完成,更新训练花费时间
            db_utils.update_model_generation_end_time(model_id, best_age, best_score)

        else:
            # 待训练模型,训练完毕
            # 说明最新一代的模型全部训练完毕
            # 1.首先取出最新一世代的全部模型
            last_generation_num = db_utils.query_max_generation_num()
            next_generation_num = last_generation_num + 1
            finished_model_list: list = db_utils.query_list_model_generation_by_generation_num(last_generation_num)
            # 2.将最新一世代的训练完成的模型,按照优秀程度来排序,最优秀的越排最前面
            finished_model_list.sort(key=lambda item: (item.get('best_score', 0)), reverse=True)
            # 3.优秀的模型开始获得繁衍下一代的权力
            for finished_model_obj in finished_model_list:
                next_generation_count = db_utils.count_model_generation_by_generation_num(next_generation_num)
                if next_generation_count <= env_capacity:
                    # 如果下一代的模型数量达到了环境容量,则繁衍结束
                    # 模型变异,并将模型变异的数据插入数据库
                    son_model_list = [
                        {
                            "model_id": db_utils.generate_uuid(),
                            "generation_num": next_generation_num,
                            "training_status": "init"
                        },
                        {
                            "model_id": db_utils.generate_uuid(),
                            "generation_num": next_generation_num,
                            "training_status": "init"
                        },
                        {
                            "model_id": db_utils.generate_uuid(),
                            "generation_num": next_generation_num,
                            "training_status": "init"
                        }
                    ]
                    db_utils.insert_model_generation(son_model_list)


if __name__ == '__main__':
    model_evolution()
