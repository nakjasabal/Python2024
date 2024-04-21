'''
문자열 바꾸기
    replace('바꿀문자열', '새문자열')
'''
print("="*5, "replace()")
print('Hello, world!'.replace('world', 'Python'))

s = 'Hello, world!'
s = s.replace('Hello', '안녕')
print(s)


'''
문자 바꾸기
    translate()는 문자열 안의 문자를 다른 문자로 변경한다. 
    maketrans('바꿀문자', '새문자')로 변환 테이블을 만든 후 적용한다. 
    아래 테이블은 a는 1, u는 5로 변경된다.
'''
print("="*5, "maketrans()/translate()", "="*20)
str1 = "apple"
table = str1.maketrans('aeiou', '12345')
print(str1.translate(table))

str2 = "한글은 아름다운 언어"
table = str2.maketrans('한아언', 'XYZ')
print(str2.translate(table))


'''
구분자과 문자열 리스트 연결하기
'''
print("="*5, "join()")
print('-'.join(['010', '7906', '3600']))


'''
공백삭제 혹은 특정 문자 삭제
    lstrip(왼쪽), rstrip(오른쪽), strip(양쪽)
    인자가 없으면 공백이 삭제된다. 
'''
print("="*5, "strip()")
str = "#^%오늘은 @@ 파이썬 @@ 공부하는날#^%"
print(str.lstrip('#'))
print(str.rstrip('%'))
print(str.rstrip('%').lstrip('#').replace('@', ''))


'''
열 위치 찾기
   find(왼쪽에서부터), rfind(오른쪽에서부터)
'''
print("="*5, "find()")
print('apple pineapple'.find('pl'))
print('apple pineapple'.rfind('pl'))
