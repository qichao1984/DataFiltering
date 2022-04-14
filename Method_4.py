# -*- coding:utf-8 -*-
"""
作者: mq_wang
日期: 2022年04月13日
"""
"""
The fourth method is to exclude the samples from correlation calculation in which pairwise missing values are detected and fill the unpaired missing values with 0.01.
"""
import numpy as np
import pandas as pd
DATA = pd.read_table(r'path')
DATA = pd.DataFrame(DATA)
n = len(DATA.iloc[:,0])
result = np.zeros([n, n])
name = np.array(DATA.loc[:, :])

def method_4(dataframe):
    data = pd.DataFrame(dataframe)
    n = len(data.iloc[:,0])
    result = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            A = [data.iloc[i,:], data.iloc[j,:]]
            A1 = np.array(A)
            temp = []
            idx = np.argwhere(np.all(A1[:, :] == 0, axis=0))
            AA = np.delete(A1, idx, axis=1)
            AA = pd.DataFrame(AA)
            AAA = AA.apply(lambda x: x.replace(0, 0.01))
            AAA = AAA.iloc[:, 1:]
            AAA = AAA.apply(lambda x: x.astype(float))
            AAA = pd.DataFrame(AAA.T)
            corr = AAA.corr(method="spearman")
            result[i, j] = corr.iloc[0:1,1:2].values[0][0]
            result[j, i] = corr.iloc[0:1,1:2].values[0][0]
            temp.clear()
    RT = pd.DataFrame(result)
    RT.columns = name[:, 0]
    RT.index = name[:, 0]
    RT.to_csv(r"path", sep=',')
method_4_spearman = method_4(DATA)
method_4_spearman