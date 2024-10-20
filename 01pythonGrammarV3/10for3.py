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

'''
4로 나누어 떨어지지만 100으로도 나누어 떨어지는 숫자는 100, 200 .. 2000이다. 
이 숫자들은 100으로 나눠서 떨어지게 되므로 두번째 조건으로 사용하고, 
세번째 조건에서 4로만 나눠지는 값을 찾게된다. 
''' 
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

