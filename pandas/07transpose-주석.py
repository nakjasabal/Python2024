# -*- coding: utf-8 -*-
 
import pandas as pd
exam_data = {'이름' : [ '서준', '우현', '인아'],
             '국어' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print('\n')

# 데이터프레임 df를 함수를 통해 전치 
df = df.transpose() 
print(df)
print('\n')
 
# 클래스 속성을 활용해서 한번 더 전치
df = df.T
print(df)
