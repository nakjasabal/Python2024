'''
변수 선언, 초기화
변수의 타입, 참조값 
'''

'''
싱글쿼테이션 3개를 연결하면 블럭단위 주석이 된다. 
'''

#라인단위 주석은 샵(#)을 사용한다. 

#문자열 변수 선언
a = "Hello Python"
#변수에 할당된 값과 메모리 참조값을 출력
print(a, id(a))
print("한줄에 "); print("여러줄 쓰려면 "); print("세미콜론이 필요함")

#새로운 값을 할당하면 참조값도 변경됨
a = 100
print(a, id(a))

#파이썬의 기본 자료형
#정수형
i = 200 
print(i, type(i))

#실수형
i = 3.14
print(i, type(i))

#Bool형
i = True
print(i, type(i))

#문자형
i = "안녕"
print(i, type(i))

#2개 이상의 변수선언 및 초기화
r, g, b = "Red", "Green", "Blue"
#여러개의 변수를 출력할때는 콤마를 통해 구분한다. 
print(r, g, b)
