'''
연산자
'''

#산술연산자
x = 2
y = 4
z = 8

print("x + y", x + y)
print("x - y", x - y)
#곱하기
print("x * y", x * y) 
#나누기. 항상 float형 결과를 반환.
print("x / y", x / y) 
#나눈 결과에서 소수부분을 제거하여 항상 int형의 결과를 반환.
print("x // y", x // y) 
#2의 4승. 지수승을 표현.
print("x ** y", x ** y) 
#2의 4승을 함수로 표현.
print("pow(x, y)", pow(x, y)) 
#2의 4승을 8로 나눈 나머지값을 출력.
print("pow(x, y, z)", pow(x, y, z)) 
#x와 y를 나눈 몫과 나머지를 튜플로 반환.
print("divmod(x, y)", divmod(x, y)) 


#import는 모듈을 불러올때 사용하는 명령으로 math모듈을 사용한다는 의미
import math
print("math.factorial(5)", math.factorial(5))