# -*- coding: utf-8 -*-
import pandas as pd
import requests

df1 = pd.read_json('../resData/sample.json')  
print(df1)

print("="*30)

print(df1.index)
print("마지막데이터:", df1.loc['Paul','c++'])
print("첫번째컬럼:")
print( df1['algol'])
print("첫번째행:")
print(df1.loc['Jerry'])

print("="*30)

url = 'https://koreanjson.com/users'
response = requests.get(url)
if response.status_code==200: 
    jsonData = response.text
    df2 = pd.read_json(jsonData)  
    df2.set_index('id', inplace=True)
    print(df2)
else:
    print("API 연동 중 오류발생")
    print(response.status_code)



