'''
퀴즈] 올해 크리스마스까지 몇일이 남았는지 계산하는 프로그램을 작성하시오.
-현재날짜가 크리스마스가 지난 시점이라면 내년 크리스마스까지의 날짜를 계산해야한다.
-함수로 정의하시오. 
-함수명 : days_until_christmas()
'''
from datetime import datetime

def days_until_christmas():
    # 현재 날짜와 년도를 얻음
    today = datetime.today()
    current_year = today.year
    
    # 올해 크리스마스 날짜를 생성
    christmas_date = datetime(current_year, 12, 25)
    
    # 오늘 날짜와 올해 크리스마스 날짜를 비교하여 크리스마스가 지나지 않았다면
    if today > christmas_date:
        # 올해 크리스마스가 이미 지났으면 내년 크리스마스까지의 날짜를 계산
        christmas_date = datetime(current_year + 1, 12, 25)
    
    # 크리스마스까지 남은 날짜를 계산
    days_left = (christmas_date - today).days
    
    return days_left

# 크리스마스까지 남은 날짜 계산
days_left = days_until_christmas()
print(f"올해 크리스마스까지 남은 날짜: {days_left}일")

