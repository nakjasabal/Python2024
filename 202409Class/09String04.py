'''
replace(찾을문자열, 변경할문자열)
: 특정 문자열을 찾아서 변경한다. 만약 찾는 문자열이 없다면
변경되지 않는다. 
''' 
print("="*5, "replace()", "="*20)
#문자열을 그대로 적용
print('Hello, world!'.replace('world', 'Python'))

#변수를 통해 함수 호출 
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
1 2 3 4 5 ==> 이와 같이 변환테이블을 생성해서 a는 1로, e는 2로
            변경한다. 
'''
table = str1.maketrans('aeiou', '12345')
print(str1.translate(table)) #결과 : 1ppl2

str2 = "한글은 아름다운 언어"
table = str2.maketrans('한아언', 'XYZ')
print(str2.translate(table)) 

'''
호출에 사용한 구분자를 통해 합쳐서 문자열을 반환한다. 
''' 
print("="*5, "join()", "="*20)
print('-'.join(['010', '7906', '3600']))

'''
공백삭제 혹은 특정문자삭제
  : l은 왼쪽, r은 오른쪽의 문자를 제거한다. strip()은 
  양쪽의 문자를 모두 제거한다. 별도의 인자가 없다면 공백을 삭제한다.
''' 
print("="*5, "strip()", "="*20)
str = "#^%오늘은 @@ 파이썬 @@ 공부하는날#^%"
print(str.lstrip('#')) # 좌측의 #을 제거 
print(str.rstrip('%')) # 우측의 %를 제거
#함수를 2개 이상 체인처럼 연결하는것을 '메서드체이닝' 이라고 한다. 
print(str.rstrip('%').lstrip('#').replace('@', ''))

'''
문자열의 위치 찾기 
  : find=>왼쪽부터 찾기, rfind=>오른쪽부터 찾기 
  찾는 문자열이 있다면 인덱스를 반환한다. 
''' 
print("="*5, "find()", "="*20)
print('apple pineapple'.find('pl'))
print('apple pineapple'.rfind('pl'))

