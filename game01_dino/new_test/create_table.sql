-- public.model_generation definition

-- Drop table

-- DROP TABLE public.model_generation;

CREATE TABLE public.model_generation (
	model_id varchar NULL, -- 模型id
	model_parent_id varchar NULL, -- 父模型id
	model_path varchar NULL, -- 模型路径
	generation_num int8 NULL, -- 世代(第几代)
	input_shape varchar NULL, -- 输入形状(游戏图像的形状)
	output_dim varchar NULL, -- 输出维度(动作空间)
	convolutional_layer varchar NULL, -- 卷积层
	fully_connected_layer varchar NULL, -- 全连接层
	game_name varchar NULL, -- 游戏名
	score_min numeric NULL, -- 最低分
	score_max numeric NULL, -- 最高分
	score_average numeric NULL, -- 平均分
	score_median numeric NULL, -- 分数中位数
	created_by varchar NULL DEFAULT 'system'::character varying, -- 创建人
	created_date timestamp NULL DEFAULT now(), -- 创建时间
	updated_by varchar NULL DEFAULT 'system'::character varying, -- 更新人
	updated_date timestamp NULL DEFAULT now() -- 更新时间
);
COMMENT ON TABLE public.model_generation IS '模型世代表';

-- Column comments

COMMENT ON COLUMN public.model_generation.model_id IS '模型id';
COMMENT ON COLUMN public.model_generation.model_parent_id IS '父模型id';
COMMENT ON COLUMN public.model_generation.model_path IS '模型路径';
COMMENT ON COLUMN public.model_generation.generation_num IS '世代(第几代)';
COMMENT ON COLUMN public.model_generation.input_shape IS '输入形状(游戏图像的形状)';
COMMENT ON COLUMN public.model_generation.output_dim IS '输出维度(动作空间)';
COMMENT ON COLUMN public.model_generation.convolutional_layer IS '卷积层';
COMMENT ON COLUMN public.model_generation.fully_connected_layer IS '全连接层';
COMMENT ON COLUMN public.model_generation.game_name IS '游戏名';
COMMENT ON COLUMN public.model_generation.score_min IS '最低分';
COMMENT ON COLUMN public.model_generation.score_max IS '最高分';
COMMENT ON COLUMN public.model_generation.score_average IS '平均分';
COMMENT ON COLUMN public.model_generation.score_median IS '分数中位数';
COMMENT ON COLUMN public.model_generation.created_by IS '创建人';
COMMENT ON COLUMN public.model_generation.created_date IS '创建时间';
COMMENT ON COLUMN public.model_generation.updated_by IS '更新人';
COMMENT ON COLUMN public.model_generation.updated_date IS '更新时间';

-- Permissions

ALTER TABLE public.model_generation OWNER TO postgres;
GRANT ALL ON TABLE public.model_generation TO postgres;


-- public.model_train_detail definition

-- Drop table

-- DROP TABLE public.model_train_detail;

CREATE TABLE public.model_train_detail (
	train_id varchar NULL, -- 训练id
	model_id varchar NULL, -- 模型id
	model_parent_id varchar NULL, -- 夫模型id
	model_path varchar NULL, -- 模型路径
	generation_num int8 NULL, -- 世代
	input_shape varchar NULL, -- 输入形状(游戏图像的形状)
	output_dim varchar NULL, -- 输出维度(动作空间)
	convolutional_layer varchar NULL, -- 卷积层
	fully_connected_layer varchar NULL, -- 全连接层
	age_num int8 NULL, -- 年龄
	day_num int8 NULL, -- 天数
	train_times_num int8 NULL, -- 训练次数
	game_name varchar NULL, -- 游戏名称
	score_total varchar NULL, -- 一局游戏分数
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
COMMENT ON COLUMN public.model_train_detail.input_shape IS '输入形状(游戏图像的形状)';
COMMENT ON COLUMN public.model_train_detail.output_dim IS '输出维度(动作空间)';
COMMENT ON COLUMN public.model_train_detail.convolutional_layer IS '卷积层';
COMMENT ON COLUMN public.model_train_detail.fully_connected_layer IS '全连接层';
COMMENT ON COLUMN public.model_train_detail.age_num IS '年龄';
COMMENT ON COLUMN public.model_train_detail.day_num IS '天数';
COMMENT ON COLUMN public.model_train_detail.train_times_num IS '训练次数';
COMMENT ON COLUMN public.model_train_detail.game_name IS '游戏名称';
COMMENT ON COLUMN public.model_train_detail.score_total IS '一局游戏分数';
COMMENT ON COLUMN public.model_train_detail.created_by IS '创建人';
COMMENT ON COLUMN public.model_train_detail.created_date IS '创建时间';
COMMENT ON COLUMN public.model_train_detail.updated_by IS '更新人';
COMMENT ON COLUMN public.model_train_detail.updated_date IS '更新时间';

-- Permissions

ALTER TABLE public.model_train_detail OWNER TO postgres;
GRANT ALL ON TABLE public.model_train_detail TO postgres;