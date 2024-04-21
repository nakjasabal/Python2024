'''
함수
    형식] def 함수명(매개변수1, 매개변수2):
            실행부
            return 결과1, 결과2
    return문은 경우에 따라 생략가능함.
'''
# 메뉴출력 및 선택용 함수
def menu():
    print('메뉴중 숫자를 선택하세요:')
    print('1.덧셈 2.뺄셈 3.곱셈 4.나눗셈')
    print('5.종료')
    return input('번호선택:')

# 사칙연산 용도의 함수
def add(a, b):
    print(a, "+", b, '=', a+b)
def sub(a, b):
    print(a, "-", b, '=', a-b)
def mul(a, b):
    print(a, "*", b, '=', a*b)
def div(a, b):
    print(a, "/", b, '=', a/b)


loop = 1
choice = 0
while loop==1: # 변수가 1일때 true이므로 반복됨
    choice = int(menu())
    if choice == 1:
        add(int(input("덧셈 a= ")), int(input("b=")))
    elif choice == 2:
        sub(int(input("뺄셈 a= ")), int(input("b=")))
    elif choice == 3:
        mul(int(input("곱셈 a= ")), int(input("b=")))
    elif choice == 4:
        div(int(input("나눗셈 a= ")), int(input("b=")))
    elif choice == 5:
        loop = 0
print("연산 종료!!")

#2개 이상의 반환값을 가진 함수
def min_max(num):
    sum = 0
    for val in num:
        sum += val
    #반환값이 2개 이상일때는 콤마로 구분하여 return한다.
    return sum, min(num), max(num)

# 인자로 사용할 튜플 정의
numbers = (8,7,6,8,4,9,5)
# 반환값의 갯수만큼 변수를 선언한 후 함수 호출
sumval, minval, maxval = min_max(numbers)
print("튜플의합, 최대값, 최소값:", sumval, minval, maxval)
    