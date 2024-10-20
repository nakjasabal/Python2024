# -*- coding: utf-8 -*-
import pandas as pd
file_path = '../resData/sample.csv'

df1 = pd.read_csv(file_path)
print(df1)
print('마지막 데이터', df1.loc[2, 'c3'])
print("="*30)

df2 = pd.read_csv(file_path, header=None)
print(df2)
print('마지막 데이터', df2.iloc[3, 3])
print("="*30)

df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print('마지막 데이터', df3.loc[2, 'c3'])
print("="*30)

df4 = pd.read_csv(file_path, index_col='c0')
print(df4)
print('마지막 데이터', df4.loc[2, 'c3'])
print("="*30)

df5 = pd.read_csv(file_path, names=['삼장법사','손오공','저팔계','사오정'])
print(df5)
print('마지막 데이터', df5.loc[3, '사오정'])
print("="*30)

df6 = pd.read_csv(file_path, names=['유비','관우','장비'])
print(df6)
print('마지막 데이터', df6.loc['2', '장비'])
print("="*30)

df7 = pd.read_csv(file_path, skiprows=2)
print(df7)
print('마지막 데이터1', df7.iloc[0, 3])
print('마지막 데이터2', df7.loc[0, '8'])


