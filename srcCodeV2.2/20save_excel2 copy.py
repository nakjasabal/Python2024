#판다스 모듈 임포트 
import pandas as pd
#os모듈 임포트
import os

#엑셀에 저장할 데이터를 딕셔너리로 선언(Key와 Value를 가짐)     
data1 = {
    '이름' : [ '강백호', '서태웅', '채치수', '송태섭', '정대만'],
    '국어' : [ 100, 80, 90, 85, 95],
    '영어' : [ 80, 75, 60, 90, 80],
    '수학' : [ 90, 70, 55, 40, 80],
}

data2 = {
    '이름': ['알리스', '밥', '찰리', '데이비드', '이브'],
    '나이': [25, 30, 28, 35, 27],
    '취미': ['독서', '등산', '요리', '사진 촬영', '게임'],
    '특기': ['피아노', '프로그래밍', '그림', '기타', '체스'],
    '생년월일': ['1998-03-15', '1993-07-22', '1995-01-10', '1988-11-02', '1996-06-18']
}

#준비한 데이터를 '데이터프레임'으로 변환(엑셀과 같은 행렬형태의 데이터) 
df1 = pd.DataFrame(data1)
#이름 컬럼을 인덱스로 지정 
df1.set_index('이름', inplace=True)      
print(df1)
print('\n')

df2 = pd.DataFrame(data2)
df2.set_index('이름', inplace=True)        
print(df2)

#파일이 저장될 경로와 파일명 지정 
writer = pd.ExcelWriter("./saveFiles/sheetGubun.xlsx")
#각 시트별로 데이터를 저장한다. 
df1.to_excel(writer, sheet_name="sheet1")
df2.to_excel(writer, sheet_name="sheet2")
#엑셀 파일로 저장한다. 
writer._save()

#만약 폴더(디렉토리)를 동적으로 생성해야 한다면 os모듈을 사용한다. 
os.mkdir('./myFolder')