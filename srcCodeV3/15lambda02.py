'''
1. map 함수
map 함수는 주어진 함수와 컬렉션을 인자로 받아, 
컬렉션의 각 요소에 함수를 적용한 결과를 반환한다.
'''
'''
map함수
    : 전달된 데이터를 동일 함수에 반복적으로 적용시켜 주는
    역할을 한다. for문과 같은 반복문을 사용하지 않아도 지정한
    함수로 인자를 여러번 전달해서 그 결과를 List형태로 반환하는
    유용한 함수이다. 
    형식]
        map(람다식, 파라미터)
'''

# 함수 정의 : 매개변수에 2를 곱한 결과를 반환
def multiply_by_two(n):
    return n * 2
# 리스트 정의
numbers = [1, 2, 3, 4, 5]
# map(함수, 리스트)
result = map(multiply_by_two, numbers)
#결과출력1 : map object로 출력됨
print('결과1-1', result)
#결과출력2 : 리스트로 변환
print('결과1-2', list(result))
'''
각 요소에 2를 곱한 결과를 반환. 리스트의 크기는 동일함. 
결과: [2, 4, 6, 8, 10]
'''


'''
2. filter 함수
filter 함수는 주어진 함수로 각 요소를 검사하여, 
조건을 만족하는 요소만 남겨 반환한다.
'''
'''
filter함수
    : 반복가능한 객체에서 특정 조건에 맞는 요소만 가져오는데,
    지정된 람다식에서 true를 반환하는것만 해당 요소를 가져오게된다.
    형식은 map과 동일하다. 
'''

#짝수인 경우 True를 반환 
def is_even(x):
    return x % 2 == 0
# 리스트 정의
numbers = [1, 2, 3, 4, 5]
# filter 함수 사용
result = filter(is_even, numbers)
# 결과 출력
print('결과2', list(result))
'''
짝수만 리스트에 남고 홀수는 모두 제거됨
결과 : [2, 4]
'''


'''
3. reduce 함수
reduce 함수는 시퀀스의 모든 요소를 하나의 값으로 축소시킨다. 
이를 사용하기 위해서는 functools 모듈을 import 해야한다. 
'''
'''
reduce함수
    : 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤
    이전 결과와 누적해서 반환하는 함수이다. 
    파이썬3 부터는 내장함수가 아니므로 functools모듈을 import한후
    사용해야 한다. 
'''
from functools import reduce

# 두개의 매개변수를 합산한 결과를 반환
def add(x, y):
    return x + y
numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers)
print(result)
'''
reduce 함수는 리스트의 처음 두 개 요소를 함수에 전달하여 결과를 만들고, 
그 결과를 다시 다음 요소와 결합하는 식으로 전체 리스트를 처리한다.
add(1, 2) = 3
add(3, 3) = 6
add(6, 4) = 10
add(10, 5) = 15

reduce 함수에서 사용하는 함수는 두 개의 인자만 받을 수 있다.
따라서, 함수의 매개변수를 3개로 정의하면 에러가 발생한다. 
'''
