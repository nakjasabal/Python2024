'''
퀴즈] 구구단을 출력하는 프로그램을 주어진 조건에 따라 작성하시오.
    조건1 : 순수 print문을 사용
    조건2 : %d와 같은 서식문자를 사용
    조건3 : f-String을 사용
    조건4 : format 함수를 사용
'''
# 조건1(순수 print 문)
for i in range(2, 9+1):
    for j in range(1, 9+1):
        print(i, '*', j, '=', i * j, end=" ")
    print("")

print("="*30)

# 조건2(서식문자)
for i in range(2, 9+1):
    for j in range(1, 9+1):
        print("%d*%d=%2d" % (i, j, i*j), end=" ")
    print("")

print("="*30)

# 조건3(f-string 사용하기)
for i in range(2, 9+1):
    for j in range(1, 9+1):
        print(f'{i}*{j}={i*j}', end=' ')
    print("")

print("="*30)

# 조건4(format 함수)
for i in range(2, 9+1):
    for j in range(1, 9+1):
        print('{}*{}={}'.format(i, j, i*j), end=' ')
    print("")
