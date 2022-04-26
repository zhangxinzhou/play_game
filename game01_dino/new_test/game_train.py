import db_utils


# 演化主流程
def model_evolution():
    # 环境容量-一代模型最大数量
    env_capacity = 100

    while True:
        # 判断是否有模型,如果没有,那就是第一次执行,需要初始化一个最初的模型,这就是初代模型
        is_init = db_utils.count_model_generation() == 0
        if is_init:
            # 初始化一个最初模型,存入数据库
            init_model_obj = {}
            db_utils.insert_model_generation(init_model_obj)

        # 开始训练模型
        training_model_obj = db_utils.query_one_training_model_generation()
        if training_model_obj is not None:
            # 训练模型
            pass
        else:
            # 待训练模型,训练完毕
            # 说明最新一代的模型全部训练完毕
            # 1.首先取出最新一世代的全部模型
            last_generation_num = db_utils.query_max_generation_num()
            next_generation_num = last_generation_num + 1
            finished_model_list = db_utils.query_list_model_generation_by_generation_num(last_generation_num)
            # 2.将最新一世代的训练完成的模型,按照优秀程度来排序,最优秀的越排最前面
            finished_model_list = []  # 按优秀程度排序,最优秀的越排最前面
            # 3.优秀的模型开始获得繁衍下一代的权力
            for finished_model_obj in finished_model_list:
                next_generation_count = db_utils.count_model_generation_by_generation_num(next_generation_num)
                if next_generation_count >= env_capacity:
                    # 如果下一代的模型数量达到了环境容量,则繁衍结束
                    break

                # 模型变异,并将模型变异的数据插入数据库
                son_model_list = []
                db_utils.insert_model_generation(son_model_list)
            continue
