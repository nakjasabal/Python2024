# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

#엑셀을 데이터프레임으로 변환한다. 
df = pd.read_excel('../resData/남북한_발전_전력량.xlsx', engine='openpyxl')  

'''
데이터프레임으로 변환시 header옵션이 없으므로 첫행은 컬럼명
으로 인식한다. 따라서 두번째행부터 가져오게된다. 
[0,5] => 엑셀의 2행과 7행을 의미한다. 
3: => D열부터 마지막을 의미하므로 1991년부터 끝까지 선택
해서 변수에 저장한다. 
''' 
df_ns = df.iloc[[0, 5], 3:]
#남북한 데이터에 인덱스를 부여한다.             
df_ns.index = ['South','North'] 
#열 이름의 자료형을 정수형으로 변경한다.       
df_ns.columns = df_ns.columns.map(int)
# 처음 5개 데이터 확인하기
print(df_ns.head())
print(df_ns.T.head())

#선 그래프1(원본 데이터프레임)
df_ns.plot()
plt.show()

#선 그래프2(전치한 데이터프레임)
df_ns.T.plot()
plt.show()

#막대 그래프1(원본 데이터프레임)
df_ns.plot(kind='bar')
plt.show()

#막대 그래프1(전치한 데이터프레임)
df_ns.T.plot(kind='bar')
plt.show()

#히스토그램(전치한 데이터프레임)
df_ns = df_ns.apply(pd.to_numeric, errors='coerce')
df_ns.T.plot(kind='hist')
plt.show()
'''
X축: 발전량(억㎾h)의 값들이 위치한 범위.
Y축: 각 발전량 범위에 속하는 연도의 개수 (Frequency).
남한과 북한의 막대: 각 구간에 속하는 남한과 북한의 연도별 
발전량 빈도를 나타내며, 이를 통해 두 지역의 전력 발전량 분포를 
비교할 수 있습니다.
'''





