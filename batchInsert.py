import os

import pandas as pd
import numpy as np
import pymysql
from odps import df

# 当前脚本的位置
current_folder_path = os.path.dirname(__file__)

# 你的文件的位置
your_file_path1 = os.path.join(current_folder_path, "文件的名字1")
your_file_path2 = os.path.join(current_folder_path, "文件的名字2")

# 我这里是以读取csv文件为例, delimiter为我们内部约定的列之间的分割符
# df1 = pd.read_csv(your_file_path1, dtype={"column1": str, "column2": str}, delimiter="/t")
# df2 = pd.read_csv(your_file_path2, dtype={"column1": str, "column2": str}, delimiter="/t")


# pymysql的接口获取链接
def mysql_conn(host, user, password, db, port=6030, charset="utf8"):
    # 传参版本
    conn = pymysql.connect(host=host, user=user, password=password, database=db, port=port, charset=charset)
    return conn


# 先创建cursor负责操作conn接口
conn = mysql_conn("192.168.132.117", "contract_helper", "tMprAowx0ni#nCR9", "contract_helper")
cursor = conn.cursor()
# 开启事务
conn.begin()


# # 先构造需要的或是和数据库相匹配的列
# columns = list(df.columns)
# # 可以删除不要的列或者数据库没有的列名
# columns.remove("列名")
# # 重新构造df,用上面的columns,到这里你要保证你所有列都要准备往数据库写入了
# new_df = df[columns].copy()
#
# # 构造符合sql语句的列，因为sql语句是带有逗号分隔的,(这个对应上面的sql语句的(column1, column2, column3))
# columns = ','.join(list(new_df.columns))
#
# # 构造每个列对应的数据，对应于上面的((value1, value2, value3))
# data_list = [tuple(i) for i in gdsord_df.values]  # 每个元组都是一条数据，根据df行数生成多少元组数据
#
# # 计算一行有多少value值需要用字符串占位
# s_count = len(data_list[0]) * "%s,"

# 构造sql语句
insert_sql = "insert into " + "数据库表名" + " (" + columns + ") values (" + s_count[:-1] + ")"
