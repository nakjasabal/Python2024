num1 = float(input("첫번째 숫자를 입력하세요:"))
num2 = float(input("두번째 숫자를 입력하세요:"))

#관계연산자
result1 = num1 == num2
print("같은지 비교", result1)

result2 = num1 != num2
print("다른지 비교", result2)

result3 = num1 >= num2
print("큰지 비교", result3)

result4 = num1 < num2
print("작은지 비교", result4)

result5 = not (num1 > num2)
print("관계식 판단의 부정", result5)


#논리연산자 
logical1 = result1 and result2
logical2 = result3 or result4
logical3 = not (result3 or result4)

print('logical1', logical1)
print('logical2', logical2)
print('logical3', logical3)


