#0~4까지 반복됨
for i in range(5):
    print("i=", i, end=" ") 

print()
print("="*30)

#for문에 리스트를 사용
list1 = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in list1:
    sum += i
print("1부터 10까지의 합 = ", sum)

print()
print("="*30)

#문자열의 크기만큼 반복. 
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



