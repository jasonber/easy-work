# coding: utf-8
# 功能:
# 数据清理
# 自动分组
# 计算均值
# pivot_table 统计分布数
# 独立样本t检验\相关样本t检验\方差分析及事后检验
# 做图

import pandas as pd
from scipy import stats # 统计库
import numpy as np
import scikit_posthocs as sp # 事后分析库
from IPython.core.interactiveshell import InteractiveShell # 设置jupyter notebook输出结果

# pd输出格式
InteractiveShell.ast_node_interactivity = "all" # 以表格形式输出所有的datafame
pd.set_option("max_column", None)
pd.set_option("max_row",None)

# 读取文件
df = pd.read_csv()

# 分组依据,参看有哪些属性
df.columns.values
df.info()

# 建立分组信息
group = ['']
for i in group: # 建立新的values值列,为fenbu函数的values做准备
    k = i+'2'
    df[k]=df[i]
#清理空值 
for i in statistics:
    df[i].fillna(df.mean, inplace= True)

# 汇总统计信息
statistics = ['']

# 总体信息
df.describe()

# 各分组的统计结果
def group_mean(x):
    g_t = df.groupby(x)
    return g_t[statistics].agg('mean')

# 人口学信息的分布情况
def fenbu(x):
       y = x +"2"
       for c in group:
              if x != c:
                     return pd.pivot_table(df, index=x, columns=c ,values=y, aggfunc="count" )
for i in group:# 输出全部的分组信息
    fenbu(i)

#方差分析及事后检验
f, p =stats.f_oneway(*args)
print(f, p)

x= [list(args[1]), list(args[2]), list(args[3])]
sp.posthoc_conover(x, group_col=x, val_col=statistics, p_adjust = 'holm')

#独立样本t检验
ttest_group1=df[df['GHQ分2类（1-很好；2-较差）'] == 1]['GHQ总分']
ttest_group2=df[df['GHQ分2类（1-很好；2-较差）'] == 2]['GHQ总分']

group_mean = df.groupby('GHQ分2类（1-很好；2-较差）')
group_mean['GHQ总分.1'].agg("mean")

t, p = stats.ttest_ind(ttest_group1, ttest_group2)
print(t, p)

#事后检验
x = pd.DataFrame({"k":[1, 2 , 4, 5, 6], "j":[1, 3, 5, 7, 66],"m":[11, 222, 444, 5655, 777]}).T
sp.posthoc_conover(x, val_col=[0, 1, 2, 3, 4], group_col=["j","k","m"],p_adjust = 'holm') #why ?error

