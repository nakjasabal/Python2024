# -*- coding: utf-8 -*-
'''
lxml 라이브러리가 설치되야 함. 

'''
import pandas as pd

'''HTML파일의 경로 혹은 웹URL을 통해 읽어온 웹페이지의 표(table)을
가져와서 데이터프레임으로 변환한다. '''
url ='../resData/sample.html'
tables = pd.read_html(url)

#테이블의 갯수를 확인한다. 
print('테이블갯수:', len(tables))

#테이블의 갯수만큼 반복하여 출력한다. 
for i in range(len(tables)):
    print("## tables[%s] ##" % i)
    print(tables[i])
    print("="*30)

#두번째 테이블을 변수에 저장한다. 
df = tables[1] 
#name 컬럼을 인덱스로 지정하고 기존 데이터프레임에 적용한다.     
df.set_index(['name'], inplace=True)
print(df)
print("="*30)

#웹URL을 지정
url ='https://pann.nate.com/talk/c20023?page=1'
tables = pd.read_html(url)
print('테이블갯수:', len(tables))
print("="*30)

#이 페이지에는 테이블이 하나만 있으므로 0번인덱스로 가져온다.
boardTable = tables[0]
''' 데이터프레임으로 변환된 테이블의 내용이 출력된다. 컬럼명은 Unnamed과 같이 출력된다. '''
print(boardTable)

''' 데이터프레임에 columns 속성을 이용해서 컬럼명을 지정한다. '''
print("="*30)
boardTable.columns = ['제목','작성자','조회수','작성일']
print(boardTable)
