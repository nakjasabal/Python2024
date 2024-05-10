#변수선언 및 출력
i, j, k = 7, 8, 9
print(i, j, k)
print(i, j, k, sep='-')
print(i, end=', ')
print(j, end=', ')
print(k)

#format 함수
print("원주율 =", format(3.14159, "8.3f")) 
print('맥주 =', format(5000, "10d")) 
print('노트북 =', format(1580000, "3,d"))

#서식문자
name = "성유겸" 
age = 13 
price = 123.456 
print("이름 : %s, 나이 : %d, 용돈 : %.2f" % (name, age, price))

menu1 = "치킨"
menu2 = "맥주"
print("오늘 {str}은 {0}과 {1}로 정했다".format(menu1, menu2, str="저녁"))
print("오늘은 {}과 {}로 {str}을 시작하겠다".format(menu1, menu2, str="아침"))

#입력
num = input('숫자를 입력하세요 : ')
print('입력한 숫자는', num, '이고, 타입은', type(num))

# result_error = num + 10
result1 = int(num) + 10
print('덧셈결과', result1)

result2 = int(input('숫자1 : ')) * int(input('숫자2 : '))
print('곱셈결과', result2)

result3 = float(input('원주율 : ')) * (float(input('원의반지름 : ')) ** 2)
print("원의넓이", result3) 

