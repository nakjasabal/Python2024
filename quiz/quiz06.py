# 날짜와 시간 형식 데이터 다루기
# https://docs.google.com/document/d/1LNBf1Lwl4j05WwN3OuHJl9eFT604NtGSmS6-hqXaC7Y/edit?usp=sharing
import time
from datetime import date, datetime, timedelta

today = date.today()
# 2022-12-01 / 2022 / 12 / 1
print(today, today.year, today.month, today.day)

print("="*30)

dtime = datetime.now()
# 2022-12-01 21:47:49.449218
print(dtime)
# 2022 12 1
print(dtime.year, dtime.month, dtime.day)
# 21 47 49 449218
print(dtime.hour, dtime.minute, dtime.second, dtime.microsecond)

print("="*30)

one_day = timedelta(days=1)

yesterday = today - one_day
tomorrow = today + one_day
print("어제와오늘", yesterday, tomorrow)

date_diff = today - yesterday
print("날짜차이", date_diff)

date_str = today.strftime('%Y-%m-%d')
print("형식지정", date_str)

date1 = '2022-12-25'
date2 = datetime.strptime(date1, '%Y-%m-%d')
date3 = datetime.date(date2)
# <class 'str'> <class 'datetime.datetime'> <class 'datetime.date'>
print(type(date1), type(date2), type(date3))
# 2022-12-25 2022-12-25 00:00:00 2022-12-25
print(date1, date2, date3)

date_diff = date3 - today
print("크리스마스까지", date_diff)

# 속으로 10초를 세어 맞히는 프로그램
input("엔터를 누르고 10초를 셉니다.")
start = time.time()
input("10초후 다시 엔터를 눌러주세요.")
end = time.time()
result = end - start
print("실제시간:%d초" % result)
print("차이:%d초" % (result-10))