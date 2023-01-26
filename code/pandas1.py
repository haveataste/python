import pandas as pd
import numpy as np

#读json文件
df = pd.read_json('a.json')
print(df)
print()

#通过传递一个list对象来创建一个Series，pandas会默认创建整型索引
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
print()

#通过传递一个能够被转换成类似序列结构的字典对象来创建一个DataFrame
df = pd.DataFrame({
  'A':1.,
  'B':pd.Timestamp('20171231'),
  'C':pd.Series(1,index=list(range(4)),dtype='float32'),
  'D':np.array([3]*4,dtype='int32'),
  'E':pd.Categorical(['test','train','test','train']),
  'F':'foo'
  })
print(df)
print()
#查看不同列的数据类型
print(df.dtypes)
print()

#通过传递一个numpy array，时间索引以及列标签来创建一个DataFrame
dates = pd.date_range('20180101',periods=10)
df = pd.DataFrame(np.random.randn(10,4),index=dates,columns=list('ABCD'))
print(df)
print()
#查看数据，查看frame中头部和尾部的行
print(df.head(), df.tail(3),  df.index, df.columns, df.values, df.T, df.describe(), df.sort_index(axis=1,ascending=False), sep='\n\n')
#df.sort(columns='B'), sep='\n\n')
