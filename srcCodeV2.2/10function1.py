'''
함수
    형식] def 함수명(매개변수1, 매개변수2):
            실행부
            return 결과1, 결과2
    -return문은 경우에 따라 생략할 수 있다. 
    -2개 이상의 결과를 콤마로 구분하여 반환할 수 있다.
    -이 경우 2개 이상의 변수를 통해 반환값을 받거나
    -만약 1개의 변수로 받고 싶다면 튜플로 받을 수 있다. 
''' 
#메뉴출력 및 선택용 함수 정의 
def menu():
    print('메뉴중 숫자를 선택하세요:')
    print('1.덧셈 2.뺄셈 3.곱셈 4.나눗셈')
    print('5.종료')
    #여기서 입력한 값은 호출한 지점으로 반환된다. 
    return input('번호선택:')  

'''
사칙연산 용도의 함수를 정의. 반환값이 없는 함수이므로 return은
생략한다. return이 없더라도 함수의 실행이 종료되면 항상 호출한
지점으로 돌아간다.
'''
def add(a, b):
    print(a, "+", b, '=', a+b)
def sub(a, b):
    print(a, "-", b, '=', a-b)
def mul(a, b):
    print(a, "*", b, '=', a*b)
def div(a, b):
    print(a, "/", b, '=', a/b)

#변수 선언 및 초기화 
loop = 1
choice = 0
#loop가 1일때 반복할 수 있는 while문을 정의
while loop==1:
    '''메뉴 출력을 위해 menu()함수를 호출한다. 함수내에서
    입력된 값은 이 위치로 반환되어 choice에 할당된다. '''
    choice = int(menu()) 

    '''사칙연산을 위해 2개의 숫자를 입력받은 후 각 함수를 
    호출한다. 앞에서 입력받은 choice에 의해 호출하는 함수를
    구분한다. '''
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


#2개 이상의 반환값을 가진 함수를 정의 
def min_max(num): #매개변수 num은 튜플을 전달받게된다.
    sum = 0 
    for val in num:
        sum += val  
    return sum, min(num), max(num)

numbers = (1,2,3,4,5,6,7,8,9,10) 
sumval, minval, maxval = min_max(numbers) 
print("튜플의합, 최소값, 최대값:", sumval, minval, maxval) 