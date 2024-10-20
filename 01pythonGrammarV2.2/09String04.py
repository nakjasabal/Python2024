'''
replace(바꿀문자열, 새문자열)
  : 특정 문자열을 찾아서 변경한다. 만약 찾는 문자열이 없다면
  변경되지 않는다. 
''' 
print("="*5, "replace()", "="*20)
print('Hello, world!'.replace('world', 'Python'))

#변수에 적용한다.  
s = 'Hello, world!'
s = s.replace('world!', 'Python')
print(s)

'''
문자바꾸기
  translate() : 문자열 내의 문자를 다른 문자로 변경한다.
  maketrans(바꿀문자, 새문자) : 변환테이블을 만든 후 적용한다. 
'''
print("="*5, "maketrans()/translate()", "="*20)
str1 = "apple"
'''
a e i o u
1 2 3 4 5 ==> 이와같이 변환테이블을 생성해서 a는 1로, e는 2로 
            변경하는 방식을 취한다. 
'''
table = str1.maketrans('aeiou', '12345')
print(str1.translate(table)) #결과 : 1ppl2

str2 = "한글은 아름다운 언어"
table = str2.maketrans('한아언', 'XYZ')
print(str2.translate(table)) 

'''
'구분자'.join(합칠문자열)
    : 합칠문자열을 구분자를 통해 합쳐서 반환한다. 
''' 
print("="*5, "join()", "="*20)
print('-'.join(['010', '7906', '3600']))

'''
공백삭제 혹은 특정문자삭제
    : lstrip(왼쪽), rstrip(오른쪽), strip(양쪽)의 문자를 
    제거한다. 별도의 인자가 없다면 공백을 삭제한다. 
''' 
print("="*5, "strip()", "="*20)
str = "#^%오늘은 @@ 파이썬 @@ 공부하는날#^%"
print(str.lstrip('#')) #좌측의 #을 제거 
print(str.rstrip('%')) #우측의 %를 제거
#메서드체인을 통해 2개이상의 함수를 연결해서 사용할 수 있다. 
print(str.rstrip('%').lstrip('#').replace('@', ''))
 
'''
문자열의 위치 찾기
    : find(왼쪽부터찾기), rfind(오른쪽부터찾기)
''' 
print("="*5, "find()", "="*20)
print('apple pineapple'.find('pl'))
print('apple pineapple'.rfind('pl'))

