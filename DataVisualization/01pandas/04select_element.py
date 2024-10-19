# -*- coding: utf-8 -*-
import pandas as pd

exam_data = {'이름' : [ '유비', '관우', '장비'],
             '국어' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '수학' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(f"{'생성 후 df전체출력':-^30}")
print(df)

#a = df.loc['유비', '수학'] #오류발생
a = df.loc[0, '수학']  
print(f"{'0, 수학':-^30}")
print(a)  

df.set_index('이름', inplace=True)
print(f"{'index설정 후 출력':-^30}")
print(df)

a = df.loc['유비', '수학']  
print(f"{'유비, 수학 출력':-^30}")
print(a)
print(f"{'0, 2 출력':-^30}")
b = df.iloc[0, 2]  
print(b)  

print(f"{'유비의 영어와 체육 출력':-^30}")
c = df.loc['유비', ['영어', '체육']] 
print(c)
d = df.iloc[0, [1, 3]]  
print(d)

print(f"{'유비의 영어~체육까지 출력':-^30}")
e = df.loc['유비', '영어':'체육']
print(e)
f = df.iloc[0, 1:]
print(f)

print(f"{'개별 선택 출력':-^30}")
g = df.loc[['유비', '관우'], ['영어', '체육']]
print(g)
h = df.iloc[[0, 1], [1, 3]]
print(h)

print(f"{'범위 지정 출력':-^30}")
i = df.loc['유비':'관우', '영어':'체육']
print(i)
j = df.iloc[0:2, 1:]
print(j)






