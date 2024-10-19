# -*- coding: utf-8 -*-
#모듈 임포트
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

#폰트설정
font_path = "../resData/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

#서울->경기 데이터를 Excel로부터 추출
df = pd.read_excel('../resData/시도별_전출입_인구수.xlsx', engine= 'openpyxl',
                   header=0)
df = df.fillna(method='ffill')
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시') 
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

#연도를 지정한 후 각 4개의 도를 선택하여 데이터를 추출한다. 
col_years = list(map(str, range(1970, 2018)))
df4 = df_seoul.loc[['충청남도','경상북도', '강원도', '전라남도'], 
                   col_years]
#그래프 사이즈를 지정한 후 4개의 Axe객체를 생성한다. 
fig = plt.figure(figsize=(20,10))
#2행 2열에서 1부터 순서대로 그래프를 그린다. 
axe1 = fig.add_subplot(2,2,1)
axe2 = fig.add_subplot(2,2,2)
axe3 = fig.add_subplot(2,2,3)
axe4 = fig.add_subplot(2,2,4)

#Axe객체에 plot함수로 그래프를 출력한다. 
axe1.plot(col_years, df4.loc['충청남도',:], marker='o', markerfacecolor='green'
          ,markersize=10, color='olive', linewidth=2, label='서울->충남')
axe2.plot(col_years, df4.loc['경상북도',:], marker='o', markerfacecolor='blue'
          ,markersize=10, color='skyblue', linewidth=2, label='서울->경북')
axe3.plot(col_years, df4.loc['강원도',:], marker='o', markerfacecolor='red'
          ,markersize=10, color='magenta', linewidth=2, label='서울->강원')
axe4.plot(col_years, df4.loc['전라남도',:], marker='o', markerfacecolor='orange'
          ,markersize=10, color='yellow', linewidth=2, label='서울->전남')          

#범례 표시
axe1.legend(loc='best')          
axe2.legend(loc='best')          
axe3.legend(loc='best')          
axe4.legend(loc='best')          

#타이틀 표시
axe1.set_title('서울 -> 충남 인구 이동', size=15)
axe2.set_title('서울 -> 경북 인구 이동', size=15)
axe3.set_title('서울 -> 강원 인구 이동', size=15)
axe4.set_title('서울 -> 전남 인구 이동', size=15)

#축 라벨 지정 및 회전
axe1.set_xticklabels(col_years, rotation=90)
axe2.set_xticklabels(col_years, rotation=90)
axe3.set_xticklabels(col_years, rotation=90)
axe4.set_xticklabels(col_years, rotation=90)

plt.show()

 










