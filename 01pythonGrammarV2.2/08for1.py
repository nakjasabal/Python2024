'''
for문 
    : 반복의 횟수가 명확한 경우에 주로 사용하는 반복문
    파이썬에서는 주로 range() 함수와 같이 사용한다. 
'''

#0~4까지 반복해서 i값을 출력 
for i in range(5):
    print("i=", i, end=" ") 
print()

#for문에 List를 사용해서 요소의 갯수만큼 반복 
list1 = [1,2,3,4,5,6,7,8,9,10]
sum = 0
#list1에 있는 요소를 순서대로 하나씩 꺼내서 i에 대입 
for i in list1:    
    #sum에 i를 누적해서 더해줌 
    sum += i
print("1부터 10까지의 합 = ", sum)

#문자열의 길이만큼 반복해서 출력한다.
str1 = "파이썬이좋아요"
for ch in str1:
    #ch에는 한 문자씩 할당된다. 
    print(ch, end=" ")
print()

#구구단 구현 
#단 :  2~9까지 반복 
for dan in range(2,10): 
    #수 : 1~9까지 반복 
    for su in range(1,10): 
        #서식문자로 공간을 확보한 후 구구단을 출력한다.  
        print("%2d*%2d=%2d" % (dan, su, su*dan), end=' ')        
    print()
print()

'''
for문도 else 구문을 사용할 수 있다. 단, for문이 정상적으로 
종료되었을때만 실행된다. 
'''
for i in range(3):    
    print(i, end=" ")
else:
    print("for문 종료됨")

#for문이 딱 한번만 실행된 후 즉시 탈출하게되므로 else는 실행되지 않는다.
for i in range(3):
    print(i, end=" ")
    #반복문 내에서 break을 만나면 즉시 반복문을 탈출한다.
    break
else:
    print("break를 통해 for문이 완료되지 않았으므로 출력되지 않음.")



'''
List Comprehension
    : 대괄호 안에 for문으로 반복적인 표현식을 실행해서 리스트 
    원소들을 초기화하는 방식이다. 
    형식]
        [표현식 for 원소 in 컬렉션 [if조건식]]
'''
print("===List Comprehension", "="*30)
'''
    표현식(n의제곱) 반복문(0~9까지반복) 조건식(3의배수)
    => 0~9까지의 정수 중 3의 배수인것만 찾아 제곱한 후 리스트를
    초기화한다. 
'''
list = [n ** 2 for n in range(10) if n%3==0]
print(list)
