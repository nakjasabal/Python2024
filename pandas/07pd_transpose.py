# -*- coding: utf-8 -*-
 
import pandas as pd
exam_data = {'이름' : [ '유비', '관우', '장비'],
             '국어' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '수학' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
 
df = df.transpose() 
print(df)
 
df = df.T
print(df)
