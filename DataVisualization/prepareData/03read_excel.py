# -*- coding: utf-8 -*-
import pandas as pd

df1 = pd.read_excel('../resData/남북한_발전_전력량.xlsx', 
                    engine='openpyxl')
print(df1)
print("="*30)

df2 = pd.read_excel('../resData/남북한_발전_전력량.xlsx', 
                    engine='openpyxl', header=1)  
# print(df2)
print("="*30)

df3 = pd.read_excel('../resData/남북한_발전_전력량.xlsx', 
                    engine='openpyxl', header=None)  
print(df3)
print("="*30)

df4 = pd.read_excel('../resData/남북한_발전_전력량.xlsx', 
                    engine='openpyxl')
print(df4)
print("="*30)

# 데이터프레임 변경 시작 
new_df = df4.drop(df4.index[5:9]);
print(new_df)
print("="*30)

new_df = new_df.drop(['전력량 (억㎾h)'], axis=1)
print(new_df)
print("="*30)

new_df = new_df.rename({'발전 전력별':'전력구분'}, axis=1)
print(new_df)
print("="*30)

new_df.set_index('전력구분', inplace=True) 
print(new_df)

new_df.to_excel("../saveFiles/남한전력량.xlsx")


