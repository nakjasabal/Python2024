import pandas as pd

data = {
    '이름' : [ '강백호', '서태웅', '채치수', '송태섭', '정대만'],
    '국어' : [ 100, 80, 90, 85, 95],
    '영어' : [ 80, 75, 60, 90, 80],
    '수학' : [ 90, 70, 55, 40, 80],
}

df = pd.DataFrame(data)
df.set_index('이름', inplace=True)   
print(df)
df.to_excel("./saveFiles/slamDunk.xlsx")
