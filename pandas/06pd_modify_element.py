# -*- coding: utf-8 -*-
import pandas as pd
 
exam_data = {'이름' : [ '유비', '관우', '장비'],
             '국어' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '수학' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
 
df.set_index('이름', inplace=True)
print(df)
 
df.iloc[0][3] = 80
print(df)

df.loc['유비']['체육'] = 90
print(df)

df.loc['유비', '체육'] = 100
print(df)


df.loc['관우', ['영어', '체육']] = 50
print(df)
df.loc['관우', ['영어', '체육']] = 100, 50
print(df)

