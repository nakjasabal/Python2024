# -*- coding: utf-8 -*-
import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '국어' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
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

print(f"{'서준, 체육 요소 수정후':-^30}") 
# df.loc['서준']['체육'] = 66 #경고 발생
df.loc['서준', '체육'] = 66
print(df)

print(f"{'우현 수정후':-^30}") 
df.loc['우현', ['영어', '체육']] = 55
print(df)
print(f"{'인아 수정후':-^30}") 
df.loc['인아', ['국어', '음악']] = 44, 33
print(df)

print(f"{'체육을 index로 수정':-^30}") 
new_df1 = df.set_index('체육')
print(new_df1)
print('66, 국어 => ', new_df1.loc[66, '국어'])
 
print(f"{'음악과 영어를 index로 수정':-^30}") 
new_df2 = new_df1.set_index(['음악', '영어'])
print(new_df2)
print('(85,98), 국어 => ', new_df2.loc[(85,98), '국어'])
print('(33,95), 국어 => ', new_df2.loc[(33,95), '국어'])


