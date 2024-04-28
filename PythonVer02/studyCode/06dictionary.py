'''
파일명 : 04Dictionary.py

딕셔너리(dictionary)
    : list와 비슷하며, 순서는 중요하지 않으나 :(콜론) 문자로 구분되는
    고유키(Key)와 값(Value)으로 지정되고 값은 변경 가능하다.  
    중괄호{} 안에 선언한다.
'''
#생성1 : dict() 메소드를 이용한 딕셔너리 생성
dic1 = dict(birth=1970, name="홍길동", size="100cm")
print(dic1)
#생성2 : 중괄호를 이용한 생성
dic2 = {'one':1, 'two':2, 'three':'3'}
print(dic2)

#반복문을 이용한 딕셔너리 출력
fruits = {'apple':100, 'grapes':200, 'orange':300, 'peach':400}
print('for문을 이용한 출력')
for key in fruits: # key값을 얻어옴
    val = fruits[key] # 얻어온 key값을 통해 출력
    print("%s : %d" % (key, val))

print("길이", len(fruits)) #딕셔너리 크기 반환
print("복숭아", fruits['peach'])

fruits['orange'] = 3500 # 값을 변경함.
print("오렌지", fruits['orange'])

del fruits['peach'] #peach 키값을 삭제
print('fruits=', fruits)

#keys() : 딕셔너리의 키로 된 dict_keys 객체를 리턴한다.
get_keys = fruits.keys()
for k in get_keys:
    print(k)
#values() : 딕셔너리의 값들로 된 dict_values 객체를 리턴한다.
get_values = fruits.values()
for v in get_values:
    print(v)
