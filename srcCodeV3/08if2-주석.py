print(f"{'중첩된 if문':-^30}")
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


print(f"{'삼항연산자':-^30}")
#삼항연산자
#if~else 문을 하나의 문장으로 표현할 수 있는 장점이 있다.
number = 99
result = "100보다 크다" if number>100 else "100보다 작다"
print(result)

#삼항연산자에서 즉시 출력도 가능하다.
print("3의배수") if number%3==0 else print("3의배수아님")


print(f"{'if~in문':-^30}")
countryList = ["세부","보라카이","파타야","나트랑","코타키나발루","푸켓"]
journey = input("여행할 나라를 입력하세요:")
if journey in countryList :
    print("{}는(은) 여행지 목록에 있습니다.".format(journey))
else :
    print("{}는(은) 여행지 목록에 없습니다.".format(journey))
