'''
문자에서 사용되는 연산자
'''

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

#한글인 경우에도 동일하게 적용된다. 
korStr = "안녕하세요? 파이썬입니다."
print(korStr[0]) #안
print(korStr[:2]) #안녕
print(korStr[0:6]) #안녕하세요?

#TypeError: can only concatenate str (not "int") to str
print(engStr + 100)