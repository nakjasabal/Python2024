import pandas as pd

'''
?로 표현된 결측치 때문인지 여기서는 mean()부터 에러가 발생됨.
아나콘다 환경에서는 문제가 없었던것 같은데, 이유는 아직 발견하지 못함. 
'''
csvFilePath2 = 'resData/auto-mpg.csv'
df = pd.read_csv(csvFilePath2, header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 처음 5개의 행
print(df.head())
# 마지막 5개의 행
print(df.tail())

# df의 모양과 크기 확인 
print(df.shape)
#내용 확인
print(df.info())
#자료형 확인 
print(df.dtypes)
print(df.mpg.dtypes) 
print(df.cylinders.dtypes)

#데이터 출력
print(df.describe()) 
print(df.describe(include='all')) 

#유효한 원소의 갯수 
print(df.count())
print(type(df.count()))  

#특정 열의 고유값
unique_values = df['origin'].value_counts() 
print(unique_values)
  
# 평균값 
print(df.mean())  
print(df['mpg'].mean())  
print(df.mpg.mean())
print(df[['mpg','weight']].mean()) 

# 중간값 
print(df.median())
print(df['mpg'].median())
print(df['origin'].median())
 
# 최대값 
print(df.max()) 
print(df['mpg'].max()) 
print(df['horsepower'].max())  
 
# 최소값 
print(df.min())
print(df['mpg'].min())
 
# 표준편차 
print(df.std())
print(df['mpg'].std())

# 상관계수 
print(df.corr())
print(df[['mpg','weight']].corr())


