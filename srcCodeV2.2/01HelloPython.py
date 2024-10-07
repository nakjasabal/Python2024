# 한줄(라인단위) 주석은 샵# 을 사용합니다. 
'''
블럭단위 주석은 싱글쿼테이션 3개를 연결해서 만들 수 있다. 
주석에 들어간 모든 내용은 실행에서 제외된다. 
''' 

'''문장을 적당히 쓰세요. 그리고 주석설정을 해봅시다. 
블럭으로 감싼후 싱글퀘테이션을 3번 입력해주세요. '''

# 파이썬은 문장의 끝에 ;(세미콜론)을 사용하지 않는다. 
print("Hello Python")

#한줄에 여러 명령을 입력하는 경우에는 세미콜론으로 구분해야 한다.  
print("한줄에 "); print("여러줄 쓰려면 "); print("세미콜론이 필요함")

#문자열은 아래와 같이 *를 이용해서 여러번 반복할 수 있다. 
print("="*30)
print("여러 변수 선언")
print("================================")
'''
좌측항은 변수, 우측항은 할당할 값으로 구분하여 선언 및 초기화한다.
또한 자료형은 별도로 기술하지 않는다. 값이 초기화될때 파이썬이 
판단하여 자료형을 결정해준다. 
''' 
r, g, b = "Red", "Green", "Blue"
# 여러개의 변수를 출력할때 콤마로 구분하면 된다.  
print(r, g, b)


print("================================")
print("정수형")
print("================================")
# 순수한 숫자를 입력할때는 " 을 붙이지 않는다.  
x = 2
y = 4
z = 8
#나누기 연산. 결과는 항상 실수(float)형으로 반환한다.  
print("x / y", x / y) 
print("z / y", z / y)  
#몫을 구하는 나누기 연산. 결과는 항상 정수(int)형으로 반환한다. 
print("x // y", x // y) 

# *는 곱셈연산. 결과는 8
print("x * y", x * y)   
# **는 거듭제곱이므로 2의 4승. 결과는 16
print("x ** y", x ** y)  
# pow()는 파이썬에서 제공하는 기본 함수로 거듭제곱의 결과를 반환
print("pow(x, y)", pow(x, y)) 
# x(2)의 y(4)승의 결과를 z(8)로 나눈 나머지가 반환된다.
print("pow(x, y, z)", pow(x, y, z)) 
# x를 y로 나눈 몫과 나머지를 Tuple(튜플)로 반환한다. 
print("divmod(x, y)", divmod(x, y))

'''
수학관련 여러가지 함수를 가지고 있는 
math 모듈을 현재 문서에 import(수입)한 후 팩토리얼 함수를 호출
'''
import math
print('math.factorial(5)', math.factorial(5))



print("================================")
print("String형")
print("================================")
str = """아래와같이 
여러줄에 걸쳐 문자열을 작성하고 싶으면
이와같이 더블쿼테이션을 3개 작성한다.
"""
print(str)

# 문자열 변수 생성 
head = "나는 헤더 "
bottom = " 나는 보텀"
# 문자열의 덧셈은 '합치기'의 결과가 출력됨
print(head + bottom) 
# 문자열의 곱셈은 '반복'의 결과가 출력됨 
print(head * 3) 

'''
파이썬에서 문자열은 인덱스를 통해 접근할 수 있다. 
인덱스는 0부터 시작이고, 콜론을 사용하면 범위를 지정할 수 있다. 
범위 사용시 0:10 으로 입력했다면 0~9까지를 의미한다. 
'''
engStr = "Hello Python Good"
#0번 인덱스 : H
print(engStr[0])
#시작인덱스가 없으면 처음부터 시작한다. 따라서 0~2까지 : Hel 
print(engStr[:3])
#1~2까지만 슬라이싱 한다 : el 
print(engStr[1:3])
#종료인덱스가 없으면 끝까지를 지정한다 : 1~마지막 
print(engStr[1:]) 

# 파이썬에서는 영어와 한글을 동일한 인덱스로 접근할 수 있다. 
korStr = "안녕하세요? 파이썬입니다."
# 0번인덱스 : 안
print(korStr[0])
#0~1 까지 : 안녕 
print(korStr[:2])
#0~5까지 : 안녕하세요? 
print(korStr[0:6])


'''
format()
  : 문자열을 format()함수를 사용하면 좀 더 발전된 스타일로 문자열
  서식을 지정할 수 있다. 
  형식] format(0번인덱스, 1번인덱스, .... N)
    사용시에는 {인덱스} 와 같이 사용한다. 
'''
print("{0}는 중복되지않는 숫자 {1}개로 구성된다".format("Lotto", 6)) 
print("{1}는 중복되지않는 숫자 {0}개로 구성된다".format("Lotto", 6)) 

'''
인덱스 대신 변수를 사용하는 방법으로 default값을 지정하는 경우
"변수명=값"으로 사용할 수 있다. 
'''
menu1 = "치킨"
menu2 = "맥주"
print("오늘 {str}은 {0}과 {1}로 정했다".format(menu1, menu2, str="저녁"))