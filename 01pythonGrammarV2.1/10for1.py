for i in range(5):
    print("i=", i, end=" ") 

print()
print("="*30)

list1 = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in list1:
    sum += i
print("1부터 10까지의 합 = ", sum)

str1 = "파이썬이좋아요"
for ch in str1:
    print(ch, end=" ")

print()
print("="*30)

#구구단
for dan in range(2,10): 
    for su in range(1,10):  
        print("%2d * %2d = %2d" % (dan, su, su*dan), end=' ')
    print()

print()
print("="*30)

for i in range(3):
    print(i, end=" ")
else:
    print("for문 종료됨")

print()
print("="*30)

for i in range(3):
    print(i, end=" ")
    break
else:
    print("break를 통해 for문이 완료되지 않았으므로 출력되지 않음.")

print()
print("="*30)

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


