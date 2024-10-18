# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# df = pd.read_csv('../resData/auto-mpg.csv', header=None)
df = pd.read_csv('../resData/auto-mpg.csv', header=None, na_values='?')

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

'''
통계함수 : 데이터프레임의 기술 통계 정보를 확인하는 함수들로
    평균, 표준편차, 최대, 최소, 중간값 등을 표현한다. 
    count() : 데이터의 갯수
    mean() : 평균값
    max(), min() : 최대, 최소값 
    std() : 표준편차
        ※표준편차란 평균에 대한 오차를 뜻한다. 실제 데이터 값이 평균을
        기준으로 얼만큼 기복이 있는지를 나타내는 지표이다. 
        -집단1 : 172 174 176 178 180
        -집단2 : 176 176 176 176 176 
        위 두집단의 평균은 둘다 176이지만 표준편차는 각각 2.823, 0이
        된다. 즉 집단2가 좀더 신뢰성이 높은 데이터라 할수있다. 
'''

# 문자형 데이터가 포함되어 있으므로 에러 발생됨
# print(df.mean()) #에러발생

print("수치형 열만 선택 후 평균 출력", "="*30)
numeric_df = df.select_dtypes(include=[np.number])
print(numeric_df.mean())

print("연비의 평균 출력", "="*30)
print(df['mpg'].mean())
# print(df['name'].mean()) #에러발생. String은 수치데이터가 아님.

print("연비와 무게 평균 출력", "="*30)
print(df[['mpg','weight']].mean()) #2개 이상의 평균값

print("중간값", "="*30)
# print(df.median()) #에러발생. String은 수치데이터가 아님.
print("연비", df['mpg'].median())
print("제조국가", df['origin'].median())

# 최대값
'''
horsepower(마력) 컬럼의 경우 문자열이므로 아스키코드로 변환후 비교한다. 
하지만 중간에 ?가 포함되어있어 다른 숫자까지 문자열로 인식하여 결과가
제대로 나오지 않는다.
'''
print("최대값", "="*30)
print(df.max())  # 전체 데이터의 최대값
print("연비", df['mpg'].max())  # 연비의 최대값
print("마력", df['horsepower'].max())  # 마력의 최대값

# 최소값
print("최소값", "="*30)
print(df.min())
print(df['mpg'].min())

# 표준편차
print("표준편차", "="*30)
# print(df.std()) # 에러발생
print(df['mpg'].std())

# 상관계수
'''
두 변수가 얼마나 서로 관련을 맺고 있는지를 수치화한것으로 
-1 ~ 1 사이에서 표현된다. 
0인경우 : 서로 관련이 없다.
1혹은 -1인 경우 : 양의관계(정비례) 이거나 음의관계(반비례)가 있다. 
'''
print("상관계수", "="*30)
# print(df.corr()) # 에러발생
print(df[['mpg', 'weight']].corr())