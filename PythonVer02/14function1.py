'''
함수
    형식] def 함수명(매개변수1, 매개변수2):
            실행부
            return 결과1, 결과2
    return문은 경우에 따라 생략가능함.
'''
print(f'{'함수정의 및 호출':-^30}')
def sumTen():
    sum = 0
    for i in range(1,11):
        sum += i
    print('1~10까지의합:', sum)
sumTen()

print(f'{'함수정의 및 응용':-^30}')
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
# 사용자가 종료할때까지 무한 반복해서 함수 호출
choice = 0
while True: # 조건이 True이므로 무한루프
    choice = int(menu())
    if choice == 1:
        add(int(input("덧셈 a=")), int(input("b=")))
    elif choice == 2:
        sub(int(input("뺄셈 a=")), int(input("b=")))
    elif choice == 3:
        mul(int(input("곱셈 a=")), int(input("b=")))
    elif choice == 4:
        div(int(input("나눗셈 a=")), int(input("b=")))
    elif choice == 5:
        break #반복문에서 break를 만나면 탈출
print("연산 종료!!")    