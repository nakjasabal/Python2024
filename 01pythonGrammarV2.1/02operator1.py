#변수선언
x = 2
y = 4
z = 8

#산술연산자
print("x + y", x + y)
print("x - y", x - y)
print("x * y", x * y) 
print("x / y", x / y) 
print("x // y", x // y) 
print("x ** y", x ** y) 
#함수사용
print("pow(x, y)", pow(x, y)) 
print("pow(x, y, z)", pow(x, y, z)) 
print("divmod(x, y)", divmod(x, y)) 

#관계연산자
num1, num2 = 5, 8
result = num1 == num2
print("같은지 비교", result)

result = num1 != num2
print("다른지 비교", result)

result = num1 >= num2
print("큰지 비교", result)

result = num1 < num2
print("작은지 비교", result)

result = not (num1 > num2)
print("관계식 판단의 부정", result)

#모듈사용
import math
print("math.factorial(5)", math.factorial(5))

