# -*- coding: utf-8 -*-
import pandas as pd

'''
read_excel() 메서드로 데이터프레임 변환. 첫행은 타이틀로 인식한다. 
즉 header=0을 디폴트로 사용한다. 
'''
df1 = pd.read_excel('../resData/남북한_발전_전력량.xlsx', engine='openpyxl')
print(df1)
print("="*30)


'''
header=1은 인덱스 1을 타이틀로 간주하겠다는 의미이므로 2행이 타이틀로
인식되어 데이터프레임으로 변환된다. 
'''
df2 = pd.read_excel('../resData/남북한_발전_전력량.xlsx', engine='openpyxl', header=1)  
# print(df2)
print("="*30)


'''
데이터를 가져오는것은 df1과 동일하지만 타이틀이 없는것으로 간주하여
정수형 컬럼명이 타이틀로 추가된다. 
'''
df3 = pd.read_excel('../resData/남북한_발전_전력량.xlsx', engine='openpyxl', header=None)  
print(df3)
print("="*30)

#header옵션이 없으므로 0으로 지정되어 첫번째행이 컬럼이 된다. 
df4 = pd.read_excel('../resData/남북한_발전_전력량.xlsx', engine='openpyxl')
print(df4)
print("="*30)

# 남한의 데이터만 남기고 북한의 데이터를 삭제한다. 
new_df = df4.drop(df4.index[5:9]);
print(new_df)
print("="*30)


# 전력량 컬럼 삭제 : 축 옵션을 부여하여 컬럼을 삭제한다. 만약 옵션이 없으면 행이 삭제된다. 
new_df = new_df.drop(['전력량 (억㎾h)'], axis=1)
print(new_df)
print("="*30)

# 컬럼명 변경 : 축 옵션을 부여해야 컬럼명이 변경된다. 
new_df = new_df.rename({'발전 전력별':'전력구분'}, axis=1)
print(new_df)
print("="*30)

# '전력구분' 컬럼을 인덱스로 지정한다. 이때 inplace 옵션으로 원본을 변경한다. 앞에서는 원본은 변하지 않고, 복사본이 반환된다. 
new_df.set_index('전력구분', inplace=True) 
print(new_df)

# 남한 데이터만 남긴 상태로 저장한다. 
new_df.to_excel("../saveFiles/남한전력량.xlsx")