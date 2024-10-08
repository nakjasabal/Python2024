# -*- coding: utf-8 -*-
import pandas as pd
 
exam_data = {'이름' : [ '유비', '관우', '장비'],
             '국어' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '수학' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data) 
print(df)
 
ndf = df.set_index(['이름'])
print(ndf)
 
ndf2 = ndf.set_index('체육')
print(ndf2)
 
ndf3 = ndf.set_index(['수학', '영어'])
print(ndf3)
