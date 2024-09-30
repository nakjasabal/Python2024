'''
시나리오] 1부터 20까지의 숫자중 홀수만 출력하는 프로그램을 while문으로 작성하시오.
    단 continue를 사용하시오.
'''
a = 1
#변수 a를 통해 20번 반복하는 반복문 생성 
while a<=20:
    if a % 2 == 0:
        #짝수인 경우 1증가 후 출력없이 반복문의 처음으로 돌아감
        a += 1
        continue
    else:
        #홀수인 경우 a를 출력 
        print(a, end=' ')
    a += 1

print()
print("#"*30)
    
'''
퀴즈] 다음과 같은 메트릭스를 출력하는 프로그램을 for문으로 작성하시오.

1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
'''
for x in range(1,5):
    for y in range(1,5):
        if x == y:
            #행과 열이 동일할때 1을 출력
            print("1", end=' ')
        else:
            #다를때 0을 출력한다. 
            print("0", end=' ')
    #한 행을 모두 출력하면 줄바꿈 한다. 
    print()


'''
시나리오] 다음과 같은 피라미드를 출력하는 프로그램을 for문으로 작성하시오.

*
**
***
****
*****
'''
for i in range(5):
    for j in range(5):
        if i >= j:
            print("*", end=" ")
    print()
 