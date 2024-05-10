'''
시나리오] 연월일을 입력해서 요일 구하는 프로그램을 작성하시오.
#윤년추가규칙 : 지구의 공전주기가 365.2422 이므로 이를 보정하기위한 수식이다.
-4로 나누어 떨어지는 해는 윤년, 그 밖의 해는 평년으로 한다.
-4로 나누어 떨어지지만 100으로도 나누어 떨어지는 해는 평년으로 한다.
-단, 400으로 나누어 떨어지는 해는 윤년으로 한다.(예: 2000년, 2400년)
'''
year = int(input("년도를 입력하시오:"))
month = int(input("월을 입력하시오:"))
day = int(input("일을 입력하시오:"))

total_days = 0
year_month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

#서기1년 ~ 입력 연도까지 날짜 합계 
for d in range(1,year):
    if d % 400 == 0:  
        total_days = total_days + 366
    elif d % 100 == 0: 
        total_days = total_days + 365
    elif d % 4 == 0:  
        total_days = total_days + 366
    else:  
        total_days = total_days + 365  

#입력 연도의 이전 월까지의 날짜 합계
for m in range(1, month):
    total_days = total_days + year_month_days[m]

#입력 월이 3월 이후라면 2월이 29일까지 있는지 확인해서 1 더함 
if month >= 3:
    if year % 400 == 0:
        total_days = total_days + 1
    elif year % 100 == 0:
        total_days = total_days + 0
    elif year % 4 == 0:
        total_days = total_days + 1
    else:
        total_days = total_days + 0

#마지막에 입력한 일을 더함 
total_days += day
print()
print("total_days :", total_days)
remainder = total_days % 7  

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

