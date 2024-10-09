# -*- coding: utf-8 -*-
import pandas as pd

exam_data = {'이름' : [ '유비', '관우', '장비'],
             '국어' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '수학' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

print(f"{'최초 출력':-^30}") 
print(df)

print(f"{'이름을 index로 지정 후 출력':-^30}") 
df.set_index('이름', inplace=True)
print(df)

print(f"{'0,3 요소 수정후':-^30}") 
# df.iloc[0][3] = 77 #경고 발생
df.iloc[0, 3] = 77
print(df)

print(f"{'유비, 체육 요소 수정후':-^30}") 
# df.loc['유비']['체육'] = 66 #경고 발생
df.loc['유비', '체육'] = 66
print(df)

print(f"{'관우 수정후':-^30}") 
df.loc['관우', ['영어', '체육']] = 55
print(df)
print(f"{'장비 수정후':-^30}") 
df.loc['장비', ['국어', '수학']] = 44, 33
print(df)

print(f"{'체육을 index로 수정':-^30}") 
new_df1 = df.set_index('체육')
print(new_df1)
print('66, 국어 => ', new_df1.loc[66, '국어'])
 
print(f"{'수학과 영어를 index로 수정':-^30}") 
new_df2 = new_df1.set_index(['수학', '영어'])
print(new_df2)
print('(85,98), 국어 => ', new_df2.loc[(85,98), '국어'])
print('(33,95), 국어 => ', new_df2.loc[(33,95), '국어'])


