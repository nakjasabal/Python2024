import pandas as pd

#딕셔너리 생성
data = {
    '이름' : [ '강백호', '서태웅', '채치수', '송태섭', '정대만'],
    '국어' : [ 100, 80, 90, 85, 95],
    '영어' : [ 80, 75, 60, 90, 80],
    '수학' : [ 90, 70, 55, 40, 80],
}

#데이터프레임으로 변환
df = pd.DataFrame(data)
#이름 컬럼을 인덱스로 지정
df.set_index('이름', inplace=True)   
print(df)
#엑셀로 저장
df.to_excel("./saveFiles/slamDunk.xlsx")
