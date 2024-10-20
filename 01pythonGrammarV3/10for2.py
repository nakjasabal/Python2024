'''
시나리오]1~100사이의 정수 중 3의 배수의 합을 구하시오.
'''
total = 0
for i in range(1, 101):
    if i % 3 == 0:
        total += i
        print(i, end='+')        
print('\b', '=', total)

print()
print("="*30)

'''
List Comprehension
'''
list = [n ** 2 for n in range(10) if n%3==0]
print(list)

print()
print("="*30)

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

print()
print("="*30)

'''
퀴즈] 다음과 같은 피라미드를 출력하는 프로그램을 for문으로 작성하시오.

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
