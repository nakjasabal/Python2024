# -*- coding: utf-8 -*-
import pandas as pd

'''
auto-mpg.csv
: 자동차 연비를 데이터셋으로 구성한 파일이다. 
연비, 실린더수, 배기량 등의 데이터로 구성되어있다. 
'''

''' CSV 파일을 데이터프레임으로 변환한다. 타이틀 없이 모든 데이터를 사용할 
것이므로 header=none으로 지정한다. '''
df = pd.read_csv('../resData/auto-mpg.csv', header=None)
# 연비, 실린더 ... 제조국가, 모델명으로 컬럼명 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 데이터프레임의 일부 데이터를 확인할때 사용
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

'''
int64 : 정수형
float64 : 실수형
object : 문자형
datetime64, timedelta64 : 날짜 및 시간
'''
print("자료형 확인", "="*30)
print(df.dtypes) #데이터프레임 전체의 자료형 확인

print("특정 컬럼의 자료형 확인", "="*30)
print(df.mpg.dtypes) #특정 컬럼의 자료형 확인
print(df.cylinders.dtypes)

# 산술 데이터를 갖는 열에 대한 평균, 표준편차 등을 출력
print("기술 통계 정보 확인1", "="*30)
print(df.describe())

# 산술데이터가 아닌 열에 대한 정보를 포함하여 출력. NaN이 나올수 있음.
print("include 옵션 추가", "="*30)
print(df.describe(include='all'))

# 각 열이 가지고 있는 원소의 갯수 표시
print("자료의 갯수", "="*30)
print(df.count())
print(type(df.count()))

'''
origin 열은 제조국가 데이터를 표현한다. 
1 : 미국(USA)
2 : 유럽(EU)
3 : 일본(JPN)
'''
print("고유값 확인", "="*30)
unique_values = df['origin'].value_counts()
print(unique_values)

