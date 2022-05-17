-- public.model_generation definition

-- Drop table

-- DROP TABLE public.model_generation;

CREATE TABLE public.model_generation (
	model_id varchar NULL, -- 模型id
	model_parent_id varchar NULL, -- 父模型id
	model_path varchar NULL, -- 模型路径
	generation_num int8 NULL, -- 世代(第几代)
	best_age int8 NULL, -- 表现最好的年龄
	best_score numeric NULL, -- 分数中位数
	input_shape varchar NULL, -- 输入形状(游戏图像的形状)
	output_dim varchar NULL, -- 输出维度(动作空间)
	hidden_layer varchar NULL, -- 隐藏层(json),包含卷积层和全连接层
	game_name varchar NULL, -- 游戏名
	training_status varchar NULL DEFAULT 'started'::character varying, -- init(初始化),training(训练中),finished(训练完成)
	training_start_date timestamp NULL, -- 训练开始时间
	training_end_date timestamp NULL, -- 训练结束时间
	training_cost_time interval NULL, -- 训练花费时间
	created_by varchar NULL DEFAULT 'system'::character varying, -- 创建人
	created_date timestamp NULL DEFAULT now(), -- 创建时间
	updated_by varchar NULL DEFAULT 'system'::character varying, -- 更新人
	updated_date timestamp NULL DEFAULT now(), -- 更新时间
	train_info varchar NULL -- 训练信息(json字符串)
);
COMMENT ON TABLE public.model_generation IS '模型世代表';

-- Column comments

COMMENT ON COLUMN public.model_generation.model_id IS '模型id';
COMMENT ON COLUMN public.model_generation.model_parent_id IS '父模型id';
COMMENT ON COLUMN public.model_generation.model_path IS '模型路径';
COMMENT ON COLUMN public.model_generation.generation_num IS '世代(第几代)';
COMMENT ON COLUMN public.model_generation.best_age IS '表现最好的年龄';
COMMENT ON COLUMN public.model_generation.best_score IS '分数中位数';
COMMENT ON COLUMN public.model_generation.input_shape IS '输入形状(游戏图像的形状)';
COMMENT ON COLUMN public.model_generation.output_dim IS '输出维度(动作空间)';
COMMENT ON COLUMN public.model_generation.hidden_layer IS '隐藏层(json),包含卷积层和全连接层';
COMMENT ON COLUMN public.model_generation.game_name IS '游戏名';
COMMENT ON COLUMN public.model_generation.training_status IS 'init(初始化),training(训练中),finished(训练完成)';
COMMENT ON COLUMN public.model_generation.training_start_date IS '训练开始时间';
COMMENT ON COLUMN public.model_generation.training_end_date IS '训练结束时间';
COMMENT ON COLUMN public.model_generation.training_cost_time IS '训练花费时间';
COMMENT ON COLUMN public.model_generation.created_by IS '创建人';
COMMENT ON COLUMN public.model_generation.created_date IS '创建时间';
COMMENT ON COLUMN public.model_generation.updated_by IS '更新人';
COMMENT ON COLUMN public.model_generation.updated_date IS '更新时间';
COMMENT ON COLUMN public.model_generation.train_info IS '训练信息(json字符串)';


-- public.model_train_detail definition

-- Drop table

-- DROP TABLE public.model_train_detail;

CREATE TABLE public.model_train_detail (
	train_id varchar NULL, -- 训练id
	model_id varchar NULL, -- 模型id
	model_parent_id varchar NULL, -- 夫模型id
	model_path varchar NULL, -- 模型路径
	generation_num int8 NULL, -- 世代
	age_num int8 NULL, -- 年数
	input_shape varchar NULL, -- 输入形状(游戏图像的形状)
	output_dim varchar NULL, -- 输出维度(动作空间)
	hidden_layer varchar NULL, -- 隐藏层(json),包含卷积层和全连接层
	game_name varchar NULL, -- 游戏名称
	score_total varchar NULL, -- 一局游戏分数
	training_start_date timestamp NULL, -- 训练开始时间
	training_end_date timestamp NULL, -- 训练结束时间
	training_cost_time interval NULL, -- 训练花费时间
	created_by varchar NULL DEFAULT 'system'::character varying, -- 创建人
	created_date timestamp NULL DEFAULT now(), -- 创建时间
	updated_by varchar NULL DEFAULT 'system'::character varying, -- 更新人
	updated_date timestamp NULL DEFAULT now() -- 更新时间
);
COMMENT ON TABLE public.model_train_detail IS '模型训练明细表';

-- Column comments

COMMENT ON COLUMN public.model_train_detail.train_id IS '训练id';
COMMENT ON COLUMN public.model_train_detail.model_id IS '模型id';
COMMENT ON COLUMN public.model_train_detail.model_parent_id IS '夫模型id';
COMMENT ON COLUMN public.model_train_detail.model_path IS '模型路径';
COMMENT ON COLUMN public.model_train_detail.generation_num IS '世代';
COMMENT ON COLUMN public.model_train_detail.age_num IS '年数';
COMMENT ON COLUMN public.model_train_detail.input_shape IS '输入形状(游戏图像的形状)';
COMMENT ON COLUMN public.model_train_detail.output_dim IS '输出维度(动作空间)';
COMMENT ON COLUMN public.model_train_detail.hidden_layer IS '隐藏层(json),包含卷积层和全连接层';
COMMENT ON COLUMN public.model_train_detail.game_name IS '游戏名称';
COMMENT ON COLUMN public.model_train_detail.score_total IS '一局游戏分数';
COMMENT ON COLUMN public.model_train_detail.training_start_date IS '训练开始时间';
COMMENT ON COLUMN public.model_train_detail.training_end_date IS '训练结束时间';
COMMENT ON COLUMN public.model_train_detail.training_cost_time IS '训练花费时间';
COMMENT ON COLUMN public.model_train_detail.created_by IS '创建人';
COMMENT ON COLUMN public.model_train_detail.created_date IS '创建时间';
COMMENT ON COLUMN public.model_train_detail.updated_by IS '更新人';
COMMENT ON COLUMN public.model_train_detail.updated_date IS '更新时间';