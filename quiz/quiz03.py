'''
퀴즈] 1부터 n까지의 합을 구하는 함수를 정의하시오.
    함수명 : sum_to_n()
'''
def sum_to_n(n):
    sum = 0
    for x in range(1, n+1):
        sum = sum + x
    return sum

print("1~10까지:", sum_to_n(10))
print("1~100까지:", sum_to_n(100))
