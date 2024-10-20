print(f"{'비교연산자와 if문':-^30}")
a, b, c = 10, 20, 30

if a == c:
    print("a와 b는 같습니다.")

if a != b:
    print("a는 b와 같지 않습니다.")

if a >= c:
    print("a는 c보다 크거나 같습니다.")

if a < b:
    print("a는 b보다 작습니다.")

print(f"{'논리연산자 - 논리And':-^30}")
print(True and True)
print(True and False)
print(False and False)

print(f"{'논리연산자 - 논리Or':-^30}")
print(True or True)
print(True or False)
print(False or False)

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


print(f"{'if~else문':-^30}")
age = 33
print(age, "살은 ", end="")
if age >= 35:
    print("중년입니다.")
elif age >= 30:
    print("중년의 시작입니다.")
else:
    print("청년입니다.")
print("==========================")


print(f"{'중첩된 if문':-^30}")
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


print(f"{'삼항연산자':-^30}")
number = 99
result = "100보다 크다" if number>100 else "100보다 작다"
print(result)

print("3의배수") if number%3==0 else print("3의배수아님")


print(f"{'if~in문':-^30}")
countryList = ["태국","필리핀","괌","사이판","코타키나발루","발리","베트남"]
journey = input("여행할 나라를 입력하세요:")
if journey in countryList :
    print("{}는(은) 여행지 목록에 있습니다.".format(journey))
else :
    print("{}는(은) 여행지 목록에 없습니다.".format(journey))

