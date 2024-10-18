# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

df = pd.read_csv('../resData/auto-mpg.csv', header=None, na_values='?')
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# print(df.mean()) #에러발생.

print("수치형 열만 선택 후 평균 출력", "="*30)
numeric_df = df.select_dtypes(include=[np.number])
print(numeric_df.mean())

print("연비의 평균 출력", "="*30)
print(df['mpg'].mean())
# print(df['name'].mean()) #에러발생. String은 수치데이터가 아님.

print("연비와 무게 평균 출력", "="*30)
print(df[['mpg','weight']].mean()) #2개 이상의 평균값