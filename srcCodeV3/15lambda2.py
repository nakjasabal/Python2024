# 1.map()
# 함수 정의
def multiply_by_two(n):
    return n * 2
# 리스트 정의
numbers = [1, 2, 3, 4, 5]
result = map(multiply_by_two, numbers)
print('결과1-1', result)
print('결과1-2', list(result))


# 2.filter 함수
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5]
result = filter(is_even, numbers)
print('결과2', list(result))


# 3.reduce 함수
from functools import reduce

def add(x, y):
    return x + y
numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers)
print(result)

