# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('../resData/auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print("처음 5개 행", "="*30)
print(df.head())

print("마지막 5개 행", "="*30)
print(df.tail())

print("데이터프레임의 모양과 크기", "="*30)
print(df.shape)

print("내용 확인", "="*30)
print(df.info())

print("자료형 확인", "="*30)
print(df.dtypes) #데이터프레임 전체의 자료형 확인

print("특정 컬럼의 자료형 확인", "="*30)
print(df.mpg.dtypes) #특정 컬럼의 자료형 확인
print(df.cylinders.dtypes)

print("기술 통계 정보 확인1", "="*30)
print(df.describe())

print("include 옵션 추가", "="*30)
print(df.describe(include='all'))

print("자료의 갯수", "="*30)
print(df.count())
print(type(df.count()))

print("고유값 확인", "="*30)
unique_values = df['origin'].value_counts()
print(unique_values)

