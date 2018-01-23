# coding: utf-8
# 功能:
# 数据清理
# 自动分组
# 计算均值
# pivot_table 统计分布数
# 独立样本t检验\相关样本t检验\方差分析及事后检验
# 做图

import pandas as pd
from scipy import stats #统计库
import numpy as np
import scikit_posthocs as sp # 事后分析库
from IPython.core.interactiveshell import InteractiveShell #设置jupyter notebook输出结果

InteractiveShell.ast_node_interactivity = "all" #以表格形式输出所有的datafame

#读取文件
df = pd.read_csv()

#分组依据,参看有哪些属性
df.columns.values
df.info()

#分组,手动录入
group = ['']


#统计量,手动录入
statistics = ['']


#分组统计,如何进行自动化的分组统计
def auto_group(x):
       g = df[].unique()
       args = []
       for i in list(g):
              args.append(df[df['海龄分类'] == i][statistics])

              
#方差分析及事后检验
f, p =stats.f_oneway(*args)
print(f, p)

x= [list(args[1]), list(args[2]), list(args[3])]
sp.posthoc_conover(x, group_col=x, val_col=statistics, p_adjust = 'holm')

#独立样本t检验

