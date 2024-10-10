# -*- coding: utf-8 -*-
import pandas as pd 

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 
             'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(f"{'최초 출력':-^30}")
print(df)

new_index1 = ['r0', 'r1', 'r2', 'r3', 'r4'] 
new_df2 = df.reindex(new_index1)
print(f"{'인덱스 재지정 후 출력':-^30}")
print(new_df2)

new_index2 = ['kor', 'eng', 'math', 'music', 'physical'] 
subject_df = df.reindex(new_index2)
print(f"{'과목 인덱스 재지정 후 출력':-^30}")
print(subject_df)

new_df3 = df.reindex(new_index1, fill_value=0)
print(f"{'fill_value 사용 후 출력':-^30}")
print(new_df3)
 
new_df4 = df.reset_index()
print(f"{'인덱스 초기화 후 출력':-^30}")
print(new_df4)
 
new_df5 = df.set_index('c0')
print(f"{'c0를 인덱스로 지정':-^30}")
print(new_df5)

new_df6 = new_df5.reset_index()
print(f"{'인덱스 초기화 후 출력':-^30}")
print(new_df6) 

sort_df1 = new_df3.sort_index(ascending=False)
print(f"{'인덱스를 내림차순 정렬':-^30}")
print(sort_df1) 

sort_df2 = new_df3.sort_values(by='c4', ascending=True)
print(f"{'c4컬럼을 오름차순 정렬':-^30}")
print(sort_df2)


