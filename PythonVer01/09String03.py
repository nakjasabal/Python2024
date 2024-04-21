'''
format() 사용하기
    : 문자열 포매팅(string formatting)은 서식문자보다 더 간단히 표현할 수 있다. 
    { }(중괄호) 안에 포매팅을 지정하고 format 메서드로 값을 삽입한다.
    형식]
        '{인덱스}'.format(값)
'''

# 직접 대입하기
str1 = 'name : {0}'.format('홍길동')
print(str1) 
 
# 변수로 대입 하기
age = 55
str2 = 'age : {0}'.format(age)
print(str2)
 
# 변수명으로 대입하기
str3 = 'name : {name}, age : {age}'.format(name='홍길동', age=33)
print(str3)

# 인덱스를 입력하지 않으면 인자의 순서대로 매칭된다.
str4 = '이름 : {}, 나이 : {}'.format('이순신', 44)
print(str4)
 
# 인덱스 순서를 바꿀수도 있다. 
str5 = '나이 : {1}, 이름 : {0}'.format('이성계', 55)
print(str5)
 
# 인덱스를 중복해서 입력할수도 있다.
str6 = '항목1 : {0}, 항목2 : {1}, 항목3 : {0}'.format('서울','부산')
print(str6)

# 정수 N자리
str7 = '정수3자리 : {0:03d}, {1:03d}'.format(12345, 12)
print(str7)

# 소수점 N자리
str8 = '소수점 아래 2자리 : {0:0.2f}, 소수점 아래 5자리 : {1:0.5f}'.format(123.1234567, 3.14)
print(str8)

#드물기는 하지만 {} 자체를 출력해야 할때는 {{ }} 처럼 두번붙여서 사용한다.
str9 = '{{ {0} }}'.format('Python 중괄호 표현')
print("str9=", str9)

# 세자리마다 콤마 찍기
str10 = 1592000
print(format(str10, ','))

