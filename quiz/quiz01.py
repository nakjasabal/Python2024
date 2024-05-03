'''
퀴즈] 1부터 10까지 숫자의 합을 구하는 프로그램을 while과 for문으로 작성하세요.
'''
sum = 0
i = 1
while i<=10:
    sum = sum + i
    print("i:", i, "sum:", sum)
    i = i + 1
print("결과1:", sum)

total = 0
for j in range(1, 10+1):
    total = total + j
print("결과2:", total)