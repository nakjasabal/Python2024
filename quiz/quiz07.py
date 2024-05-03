'''
퀴즈] 속으로 10초를 세어 맞히는 프로그램을 작성하시오.
'''
import time

input("엔터를 누르고 10초를 셉니다.")
start = time.time()
input("10초후 다시 엔터를 눌러주세요.")
end = time.time()
result = end - start
print("실제시간:%d초" % result)
print("차이:%d초" % (result-10))