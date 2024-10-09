# -*- coding: utf-8 -*-
import pandas as pd

exam_data = {'국어' : [ 90, 80, 70], 
             '영어' : [ 98, 89, 95],
             '수학' : [ 85, 95, 100], 
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data, index=['유비', '관우', '장비'])
print(f"{'df전체출력':-^30}")
print(df, '\n')

#행 선택
print(f"{'유비':-^30}")
label1 = df.loc['유비'] 
print(label1, '\n')
print(f"{'인덱스1':-^30}")
position1 = df.iloc[1]  
print(position1, '\n')

#2개이상 선택
print(f"{'유비,장비':-^30}")
label2 = df.loc[['유비', '장비']]
print(label2, '\n')
print(f"{'인덱스 0,2':-^30}")
position2 = df.iloc[[0, 2]]
print(position2, '\n')

#범위선택
print(f"{'유비:장비':-^30}")
label3 = df.loc['유비':'장비']
print(label3, '\n')
print(f"{'0:2':-^30}")  
position3 = df.iloc[0:2]
print(position3, '\n')  

#열 선택
print(f"{'수학 열':-^30}")
math1 = df['수학'] 
print(math1, '\n')

print(f"{'영어 열':-^30}")
english = df.영어 
print(english, '\n')
print(type(english), '\n')  

print(f"{'국어, 체육 열':-^30}")
column1 = df[['국어', '체육']]
print(column1, '\n')
print(type(column1), '\n')  

print(f"{'수학 열':-^30}")
math2 = df[['수학']]
print(math2, '\n')
print(type(math2), '\n')






