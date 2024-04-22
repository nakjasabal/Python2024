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
print("="*5, '비교연산자와 if문')
a, b, c = 10, 20, 30

if a == c:
    print("a와 b는 같습니다.")

if a != b:
    print("a는 b와 같지 않습니다.")

if a >= c:
    print("a는 c보다 크거나 같습니다.")

if a < b:
    print("a는 b보다 작습니다.")

'''
논리and(곱)는 둘다 True(1)일때만 True를 반환한다. 하나라도 Fasle(0)이면 False를 반환한다. 
1*1*0 = 0 즉 0이 하나만 곱해져도 결과는 0이된다. 
'''
print("="*5, '논리연산자 - 논리And')
print(True and True)
print(True and False)
print(False and False)

'''
논리or(합)는 하나만 True라도 True를 반환한다. 둘다 Fasle일때만 False를 반환한다. 
0+0+1 = 1 즉 1이 하나만 더해져도 결과는 1이된다. 
'''
print("="*5, '논리연산자 - 논리Or')
print(True or True)
print(True or False)
print(False or False)

#논리연산자는 아래와 같이 2개이상의 비교연산에서 사용된다.
if not a > b:
    print('a는 b보다 크지 않습니다.')
else:
    print('a는 b보다 큽니다.')

if a == b and b != c:
    print('모든 조건을 만족합니다.')
else:
    print('조건중 False가 있습니다.')

if a > b or b < c:
    print('조건중 True가 있습니다.')
else:
    print('모든 조건에 만족하지 않습니다.')


print("="*5, 'if~else문')
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

print("="*5, '중첩된 if문')
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


print("="*5, '삼항연산자')
#삼항연산자
#if~else 문을 하나의 문장으로 표현할 수 있는 장점이 있다.
number = 99
result = "100보다 크다" if number>100 else "100보다 작다"
print(result)

#삼항연산자에서 즉시 출력도 가능하다.
print("3의배수") if number%3==0 else print("3의배수아님")


print("="*5, 'if~in문')
countryList = ["태국","필리핀","괌","사이판","코타키나발루","발리","베트남"]
journey = input("여행할 나라를 입력하세요:")
if journey in countryList :
    print("{}는(은) 여행지 목록에 있습니다.".format(journey))
else :
    print("{}는(은) 여행지 목록에 없습니다.".format(journey))
