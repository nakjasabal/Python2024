# -*- coding: utf-8 -*-
import pandas as pd
import requests

# JSON파일을 데이터프레임으로 변환한다. 
df1 = pd.read_json('../resData/sample.json')  
print(df1)

print("="*30)

#인덱스만 출력한다. 
print(df1.index)
print("마지막데이터:", df1.loc['Paul','c++'])
#컬럼 전체를 출력할때는 데이터프레임명만 사용한다. 
print("첫번째컬럼:")
print( df1['algol'])
#행 전체를 출력할때는 loc속성을 사용한다. 
print("첫번째행:")
print(df1.loc['Jerry'])

print("="*30)

url = 'https://koreanjson.com/users'
response = requests.get(url)
if response.status_code==200: 
    jsonData = response.text
    # print(jsonData)
    df2 = pd.read_json(jsonData)  
    # print(df2)
    df2.set_index('id', inplace=True)
    print(df2)
else:
    print("API 연동 중 오류발생")
    print(response.status_code)