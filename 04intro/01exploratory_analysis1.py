# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('../resData/auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 데이터프레임의 일부 데이터 확인
print("처음 5개 행", "="*30)
print(df.head())
print("마지막 5개 행", "="*30)
print(df.tail())

# 행의 갯수, 열의 갯수를 튜플로 반환
print("데이터프레임의 모양과 크기", "="*30)
print(df.shape)

# 클래스유형, 행 인덱스, 열의 이름과 갯수, 자료형 등을 출력
print("내용 확인", "="*30)
print(df.info())

print("자료형 확인1", "="*30)
print(df.dtypes)

print("자료형 확인2 - 컬럼 지정", "="*30)
print(df.mpg.dtypes) 
print(df.cylinders.dtypes)

print("기술 통계 정보 확인1", "="*30)
print(df.describe())

print("기술 통계 정보 확인2 - include 옵션 추가", "="*30)
print(df.describe(include='all'))

print("자료의 갯수", "="*30)
print(df.count())
print(type(df.count()))

print("고유값 확인", "="*30)
unique_values = df['origin'].value_counts()
print(unique_values)

