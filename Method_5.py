# -*- coding:utf-8 -*-
"""
作者: mq_wang
日期: 2022年04月13日
"""
"""
The fifth method is similar to the fourth method but fills unpaired missing values with 0.
"""
import numpy as np
import pandas as pd
DATA = pd.read_table(r'path')
DATA = pd.DataFrame(DATA)
n = len(DATA.iloc[:,0])
result = np.zeros([n, n])
name = np.array(DATA.loc[:, :])

def method_5(dataframe):
    data = pd.DataFrame(dataframe)
    n = len(data.iloc[:,0])
    result = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            A = [data.iloc[i,:], data.iloc[j,:]]
            A1 = np.array(A)
            k = 0
            temp = []
            while k <= len(A1[0])-1:
                  if np.all(A1[:, k] == 0) == True:
                    temp.append(k)
                  k = k + 1
            A = np.delete(A, temp, axis=1)
            temp.clear()
            A2 = list(A)
            AA = pd.DataFrame({'0': A2[0][1:], '1': A2[1][1:]})
            AA = AA.apply(lambda x: x.astype(float))
            if AA.empty:
                corr = pd.DataFrame({'0': [99,99], '1': [99,99]})
            else:
                corr = AA.corr(method="spearman")
            result[i, j] = corr.iloc[0:1,1:2].values[0][0]
            result[j, i] = corr.iloc[0:1,1:2].values[0][0]
            temp.clear()
    RT = pd.DataFrame(result)
    RT.columns = name[:, 0]
    RT.index = name[:, 0]
    RT.to_csv(r"path", sep=',')
method_5_spearman = method_5(DATA)
method_5_spearman