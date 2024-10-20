# 일반 함수 정의
def two_sum(x, y):
    return x + y
print("함수를 통한 두수의 합=", two_sum(10, 20))

# 람다식 정의
sum = lambda arg1, arg2: arg1 + arg2
print("람다식을 통한 합=", sum(10, 20))

# 인자를 제곱해서 반환하는 람다식
power = lambda num : num**2
print("5의 제곱은=", power(5))

#람다식 자체호출
print("람다식 자체호출=", (lambda x, y: x + y)(100, 200))

