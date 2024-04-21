'''
for문
    형식] for 반복변수 in 목록형:
        실행문

range()
    : 반복문과 직접적인 연관은 없지만 흔히 반복문과
    연동해서 많이 사용하는 메소드
    형식]
        range(10) : 0~9까지
        range(2,10) : 2~9까지
        range(2,10,2) : 2부터 2씩 증가
'''

#0~4까지 반복됨
for i in range(5):
    print("i=", i, end=" ") 
print()

#for문에 리스트를 사용해서 인자의 갯수만큼 반복
list1 = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in list1:
    sum += i
print("1부터 10까지의 합 = ", sum)

#문자열의 크기만큼 반복. 
str1 = "파이썬이좋아요"
for ch in str1:
    print(ch, end=" ")
print()


#구구단
for dan in range(2,10): #단은 2~9까지 반복
    for su in range(1,10): #수는 1~9까지 반복
        print("%2d * %2d = %2d" % (dan, su, su*dan), end=' ')
    print()
print()


'''
for문도 else구문을 사용할수 있다.
단, for문이 정상적으로 종료되었을때만 실행된다. 
'''
for i in range(3):
    print(i, end=" ")
else:
    print("for문 종료됨")

#for문이 딱 한번만 실행된후 탈출하게되므로 else는 실행되지 않는다. 
for i in range(3):
    print(i, end=" ")
    break
else:
    print("break를 통해 for문이 완료되지 않았으므로 출력되지 않음.")















'''
시나리오] 연월일을 입력해서 요일 구하는 프로그램을 작성하시오.
#윤년추가규칙 : 지구의 공전주기가 365.2422 이므로 이를 보정하기위한 수식이다.
-4로 나누어 떨어지는 해는 윤년, 그 밖의 해는 평년으로 한다.
-4로 나누어 떨어지지만 100으로도 나누어 떨어지는 해는 평년으로 한다.
-단, 400으로 나누어 떨어지는 해는 윤년으로 한다.(예: 2000년, 2400년)
'''
#숫자형으로 년/월/일을 입력받는다.
year = int(input("년도를 입력하시오:"))
month = int(input("월을 입력하시오:"))
day = int(input("일을 입력하시오:"))

#전체 누적 날짜수
total_days = 0
#월별 날짜수를 리스트로 정의
year_month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
 
for d in range(1,year):
    if d % 400 == 0: #400으로 나누어 떨어지면 윤년
        total_days = total_days + 366
    elif d % 100 == 0: #100으로 나눠지면 평년 
        total_days = total_days + 365
    elif d % 4 == 0: #4로 나눠지면 윤년
        total_days = total_days + 366
    else: #그외는 무조건 365일로 계산
        total_days = total_days + 365  

#입력년도의 각 달의 날수를 누적해서 더함. 
for m in range(1, month):
    total_days = total_days + year_month_days[m]

'''
입력월이 3이상이고, 입력년도가 윤년일경우 1을 더한다. 
윤년은 2월이 29일까지 있기 때문임.
'''
if month >= 3:
    if year % 400 == 0:
        total_days = total_days + 1
    elif year % 100 == 0:
        total_days = total_days + 0
    elif year % 4 == 0:
        total_days = total_days + 1
    else:
        total_days = total_days + 0

#총 누적된 일수에 현재년도의 일수를 더해준다. 
total_days += day
print()
print("total_days :", total_days)
remainder = total_days % 7 # 7로 나눈 나머지를 구한다. 

#요일은 항상 일요일부터 시작이므로 나머지가 0이면 일요일이다.
if remainder == 0:
    print("일요일입니다.")
if remainder == 1:
    print("월요일입니다.")
if remainder == 2:
    print("화요일입니다.")
if remainder == 3:
    print("수요일입니다.")
if remainder == 4:
    print("목요일입니다.")
if remainder == 5:
    print("금요일입니다.")
if remainder == 6:
    print("토요일입니다.")

