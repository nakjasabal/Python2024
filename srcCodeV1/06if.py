'''
if문의 형식1
    if 조건 :
        조건이 참일때 실행문

if문의 형식2
    if 조건 :
        조건이 참일때 실행문
    else:
        조건이 거짓일때 실행문

if문의 형식3
    if 조건1 :
        조건1이 참일때 실행문
    elif 조건2 :
        조건2가 참일때 실행문
    else:
        위 모든 조건에 만족하지 않을때 실행문
'''
print("===비교연산자와 if문===")
a, b, c = 10, 20, 10

if a == c:
    print("a와 b는 같습니다.")

if a != b:
    print("a는 b와 같지 않습니다.")

if a >= c:
    print("a는 c보다 크거나 같습니다.")

if a < b:
    print("a는 b보다 작습니다.")

print("===논리연산자와 if문===")
#논리and는 둘다 True일때만 True를 반환한다. 하나라도 Fasle이면 False를 반환한다. 
if True and True:
    print("True 입니다.")

if True and False:
    print("True 입니다.")
else:
    print("False 입니다.")

if False and False:
    print("True 입니다.")
else:
    print("False 입니다.")

#논리or는 하나만 True라도 True를 반환한다. 둘다 Fasle일때만 False를 반환한다. 
print(True or True)
print(True or False)
print(False or False)

#논리연산자는 아래와 같이 2개이상의 비교연산에서 사용된다.
print(not 10 > 5)
print(10 == 10 and 10 != 5)
print(10 > 5 or 10 < 3)


age = 33
# 여러개의 print()를 사용할때 한줄로 출력하고 싶다면 end=''를 사용한다.
print(age, "살은 ", end="")
if age >= 35:
    print("중년입니다.")
elif age >= 30:
    print("중년의 시작입니다.")
else:
    print("청년입니다.")
print("==========================")

# 사용자로부터 입력값을 받을때 input()을 사용한다.
num1 = int(input("숫자 하나를 입력하세요 : "))
if num1%2==0:
    if num1%3==0:
        print("2와 3으로 나누어짐")
    else:
        print("2는 가능, 3은 불가")
else:
    if num1%3==0:
        print("2는 불가, 3은 가능")
    else:
        print("2와 3 모두 불가")
print("==========================")


'''
연습문제1] 국,영,수 점수를 입력받아 평균값을 구하고 이를 통해 학점을 출력하는 
    프로그램을 작성하시오. 
    90점 이상은 A학점 
    80점 이상은 B학점
    70점 이상은 C학점
    60점 이상은 D학점    
    60점 미만은 F학점으로 판단하여 출력합니다. 
'''

'''
연습문제2] 아이디를 먼저 입력받은 후 user_info 리스트에 등록되었다면 패스워드를 입력받아 
    일치하는지 확인하는 프로그램을 작성하시오. 여기서 패스워드는 1234로 가정합니다. 
'''
user_info = ['sung', 'kim', 'hong', 'park', 'lee']
my_id = input('아이디를 입력하세요')

