#표준 입출력 장치

i, j, k = 7, 8, 9
#출력값 사이에 스페이스가 하나씩 추가된다.
print(i, j, k)
#출력값 사이에 구분자를 추가할 수 있다.
print(i, j, k, sep='-')
#값을 줄바꿈 없이 출력할 수 있다.
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

# 인덱스 대신 변수를 사용하는 방법. 단 default값을 지정할때는
# name=value형태로 기술한다. 
menu1 = "치킨"
menu2 = "맥주"
print("오늘 {str}은 {0}과 {1}로 정했다".format(menu1, menu2, str="저녁"))
print("오늘은 {}과 {}로 {str}을 시작하겠다".format(menu1, menu2, str="아침"))


#키보드를 통해 입력받는 값은 항상 '문자형'이 된다. 
num = input('숫자를 입력하세요 : ')
print('입력한 숫자는', num, '이고, 타입은', type(num))

#문자형 + 정수형 이므로 에러가 발생된다. 
# result_error = num + 10
#따라서 정수형으로 변환 후 연산해야 한다. 
result1 = int(num) + 10
print('덧셈결과', result1)

#입력과 동시에 정수형으로 변환할 수 있다. 
result2 = int(input('숫자1 : ')) * int(input('숫자2 : '))
print('곱셈결과', result2)

#실수형이라면 float로 변환한다. 
result3 = float(input('원주율 : ')) * (float(input('원의반지름 : ')) ** 2)
print("원의넓이", result3) 
