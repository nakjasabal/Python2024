'''
파일명 : 01HelloPython.py

싱글쿼테이션 3개를 연결하면 블럭단위 주석이 된다. 
'''
print("Hello Python")
print("한줄에 "); print("여러줄 쓰려면 "); print("세미콜론이 필요함")

#라인단위 주석은 샵(#)으로...



print("================================")
print("여러 변수 선언")
print("================================") 
#변수와 할당연산자 부분을 구분하여 선언 및 초기화한다.
r, g, b = "Red", "Green", "Blue"
#여러개의 변수를 출력할때는 콤마를 통해 구분한다. 
print(r, g, b)


print("================================")
print("정수형")
print("================================")
x = 2
y = 4
z = 8

print("x / y", x / y) #나누기. 항상 float형 결과를 반환함.
print("x // y", x // y) #나누기. 소수부분을 제거하여 항상 int형의 결과를 반환함.
print("x * y", x * y) #곱하기
print("x ** y", x ** y) #2의 4승. 지수승을 표현함.
print("pow(x, y)", pow(x, y)) #2의 4승을 함수로 표현함. 
print("pow(x, y, z)", pow(x, y, z)) #2의 4승을 8로 나눈 나머지값을 출력
print("divmod(x, y)", divmod(x, y)) #x와 y를 나눈 몫과 나머지를 튜플로 반환함.

#import는 모듈을 불러올때 사용하는 명령으로 math모듈을 사용한다는 의미
import math
print("math.factorial(5)", math.factorial(5))


print("================================")
print("String형")
print("================================")
str = """아래와같이 
여러줄에 걸쳐 문자열을 작성하고 싶으면
이와같이 더블쿼테이션을 3개 작성한다.
"""
print(str)

head = "나는 헤더 "
bottom = " 나는 보텀"
print(head + bottom) #문자열 더하기(문자열 연결)
print(head * 3) #문자열 곱하기(동일 문자열 반복)

#문자열 슬라이싱
engStr = "Hello Python Good"
print(engStr[0]) #0번 인덱스 : H
print(engStr[:3]) #0~3까지의 범위에서 3앞까지 가져온다. 
print(engStr[1:3]) #1~2까지만 가져온다. 
print(engStr[1:]) #1~마지막까지 가져온다.

korStr = "안녕하세요? 파이썬입니다."
print(korStr[0]) #안
print(korStr[:2]) #안녕
print(korStr[0:6]) #안녕하세요?

'''
format()
    : 문자열의 format함수를 사용하면 좀 더 발전된
    스타일로 문자열 포맷을 지정할 수 있다. 
''' 
# 인덱스를 사용하는 방법
print("{0}는 중복되지않는 숫자 {1}개로 구성된다".format("Lotto", 6)) 
print("{1}는 중복되지않는 숫자 {0}개로 구성된다".format("Lotto", 6)) 

# 인덱스 대신 변수를 사용하는 방법. 단 default값을 지정할때는
# name=value형태로 기술한다. 
menu1 = "치킨"
menu2 = "맥주"
print("오늘 {str}은 {0}과 {1}로 정했다".format(menu1, menu2, str="저녁"))
 
