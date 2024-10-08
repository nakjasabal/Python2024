# -*- coding: utf-8 -*-
import pandas as pd

# 데이터프레임 정의
exam_data = {'이름' : [ '유비', '관우', '장비'],
             '국어' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '수학' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)

# 컬럼 추가 
print(f"{'역사 열 추가':-^30}") 
df['역사'] = 80
print(df)

# 행 추가. 인덱스 지정이 없으므로 숫자형
print(f"{'3행 추가':-^30}") 
# 전체 0으로 초기화
df.loc[3] = 0
print(df)

# 4행으로 추가됨
print(f"{'제갈량 행 추가':-^30}")  
df.loc[4] = ['제갈량', 90, 80, 70, 60, 50]
print(df)

#5번째 행으로 추가됨. 단 숫자형 아닌 문자형으로 지정됨.
print(f"{'5행 추가':-^30}")  
df.loc['행5'] = df.loc[2]
print(df)


