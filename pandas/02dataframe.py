# -*- coding: utf-8 -*-
import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 
             'c2':[7,8,9], 'c3':[10,11,12], 
             'c4':[13,14,15]}
df = pd.DataFrame(dict_data)
print('타입', type(df))
print('데이터프레임1\n', df)

print("="*30)

df = pd.DataFrame([[20, '남', '부산'], [17, '여', '서울']], 
                  index=['철수', '영희'], 
                  columns=['나이', '성별', '지역'])
print('데이터프레임2\n',df)     
print('index\n', df.index) 
print('columns\n', df.columns) 

print("="*30)

#변경1
df.index=['학생1', '학생2']
df.columns=['연령', '남녀', '거주']
print('변경1\n', df)    

#변경2
df.rename(columns={'연령':'No', '남녀':'Gender', '거주':'City'}, 
          inplace=True)
df.rename(index={'학생1':'Student1', '학생2':'Student2'}, 
          inplace=True)
print('변경2\n', df)

print("="*30)

#요소에 접근
stu1 = df.loc['Student1'] 
stu2 = df.iloc[1] 
print('stu1과 stu2 \n', stu1, stu2)

print("="*30)

#삭제
df.drop('Student1', inplace=True)
print('삭제후1\n', df)

#Gender라는 행이 없으므로 오류가 발생된다. 
#df.drop('Gender')

df.drop('Gender', axis=1) 
df.drop('Gender', axis=1, inplace=True) 
print('삭제후2\n',df)








