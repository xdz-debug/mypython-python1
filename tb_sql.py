'''
调用create_tb中的建表函数
传入表名和建表字段
'''

#用户表
"create table tb_user(\
id int primary key auto_increment COMMENT '编号',\
user_name varchar(18)  NOT NULL unique COMMENT '用户名',\
mima varchar(15) COMMENT '密码',\
mail varchar(15) COMMENT '邮箱',\
name varchar(15) COMMENT '姓名',\
phone varchar(15) COMMENT '联系电话',\
miaoshu varchar(15) COMMENT '说明'\
)"

#属性表
"create table tb_suxing(\
id int primary key  COMMENT '编号',\
gj int  not null default 10 COMMENT '攻击',\
fy int not null default 10 COMMENT '防御',\
sm int not null default 100 COMMENT '生命值',\
shan int not null default 0 COMMENT '闪避',\
mz int not null default 10 COMMENT '命中',\
ren int not null default 10 COMMENT '韧性',\
bjl int not null default 0 COMMENT '暴击率',\
dj int not null default 1 COMMENT '等级'\
)"


"insert into tb_suxing(id,gj,fy,sm,shan,mz,ren,bjl) values(1001,100,2,100,0,0,0,0)"
"insert into tb_suxing(id,gj,fy,sm,shan,mz,ren,bjl) values(1002,10,2,100,0,0,0,0)"
"insert into tb_suxing(id,gj,fy,sm,shan,mz,ren,bjl) values(1003,10,2,100,0,0,0,0)"
