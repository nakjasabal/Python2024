import pandas as pd

'''
CSV(Comma-separated values)
  : 텍스트 파일의 일종으로 쉼표(,)로 열을 구분하고 엔터로 행을 구분한다. 엑셀을 통해 주로 생성한다. 
'''
csvFilePath1 = 'resData/csv-sample.csv'

'''
read_csv() 
  : CSV파일을 데이터프레임으로 변환한다. 별도의 옵션이 없으면 첫번째행은 제목으로 간주한다. 
'''
print(f'{"출력1":-^50}')
df1 = pd.read_csv(csvFilePath1)
print(df1)

'''
header 
  : 열의 이름으로 사용될 행의 번호를 지정한다. 기본값은 0이다. 만약 첫행부터 데이터가 있다면 None으로 지정하면된다.
''' 
print(f'{"출력2":-^50}')
df2 = pd.read_csv(csvFilePath1, header=None)
print(df2)

'''
index_col 
  : 행의 인덱스로 사용할 열의 번호를 지정한다. 아래는 None이므로 단순히 정수형 인덱스로 지정된다.
''' 
print(f'{"출력3":-^50}')
df3 = pd.read_csv(csvFilePath1, index_col=None)
print(df3)
print('-'*10)
print(df3['이름'][1],'의',df3['과목1'][0],'점수',df3['과목1'][1])

# '이름' 컬럼을 인덱스로 지정한다.  
print(f'{"출력4":-^50}')
df4 = pd.read_csv(csvFilePath1, index_col='이름')
print(df4)
print('-'*10)
print(df4['과목1'])
print('-'*10)
print('과목2:', df4['과목2']['name'])
print('Jerry의 과목2 학점:', df4['과목2']['Jerry'])

#skiprows : 처음 몇줄을 건너뛴후(skip) 데이터프레임으로 변환할지 설정
print(f'{"출력5":-^50}')
df5 = pd.read_csv(csvFilePath1, header=0, skiprows=2)
print(df5)