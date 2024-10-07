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
print(head + bottom)  
print(head * 3) 

#문자열 슬라이싱
engStr = "Hello Python Good"
print(engStr[0])
print(engStr[:3])
print(engStr[1:3])
print(engStr[1:])

korStr = "안녕하세요? 파이썬입니다."
print(korStr[0])
print(korStr[:2])
print(korStr[0:6])

#TypeError: can only concatenate str (not "int") to str
print(engStr + 100)

