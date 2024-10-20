# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# df = pd.read_csv('../resData/auto-mpg.csv', header=None)
df = pd.read_csv('../resData/auto-mpg.csv', header=None, na_values='?')

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 문자형 데이터가 포함되어 있으므로 에러 발생됨
# print(df.mean()) 

print("수치형 열만 선택 후 평균 출력", "="*30)
numeric_df = df.select_dtypes(include=[np.number])
print(numeric_df.mean())

print("연비의 평균 출력", "="*30)
print(df['mpg'].mean())
# print(df['name'].mean()) #에러발생. String은 수치데이터가 아님.

print("연비와 무게 평균 출력", "="*30)
print(df[['mpg','weight']].mean())  

print("중간값", "="*30)
# print(df.median()) #에러발생. String은 수치데이터가 아님.
print("연비", df['mpg'].median())
print("제조국가", df['origin'].median())

# 최대값
print("최대값", "="*30)
print(df.max())   
print("연비", df['mpg'].max())  
print("마력", df['horsepower'].max()) 

# 최소값
print("최소값", "="*30)
print(df.min())
print(df['mpg'].min())

# 표준편차
print("표준편차", "="*30)
# print(df.std()) # 에러발생
print(df['mpg'].std())

print("상관계수", "="*30)
# print(df.corr()) # 에러발생
print(df[['mpg', 'weight']].corr())



