'''
파일명 : 04Dictionary.py
 
딕셔너리(Dicionary)
    : List와 비슷하지만 고유키(Key)와 값(Value)로 선언한다.
    값은 변경할 수 있고, 중괄호로 선언한다. 
    단, 순서는 보장되지 않는다. 
'''
#생성1 : dict() 함수를 통해 선언 
dic1 = dict(birth=1970, name="홍길동", size="100cm")
print(dic1)
#생성2 : 중괄호로 선언 
dic2 = {'one':1, 'two':2, 'three':'3'}
print(dic2)

fruits = {'apple':100, 'grapes':200, 'orange':300, 'peach':400}
print('for문을 이용한 출력')
#딕셔너리에 저장된 요소의 갯수만큼 반복하여 Key를 인출한다.
for key in fruits: 
    #인출한 key를 통해 value을 얻어와서 출력한다. 
    val = fruits[key]  
    #Key는 문자열이므로 %s, Value는 정수이므로 %d를 사용
    #s => String, d => Decimal을 뜻한다. 
    print("%s : %d" % (key, val))

#len() : 딕셔너리의 크기를 반환 
print("길이", len(fruits)) 
#Key를 마치 인덱스처럼 사용하여 Value를 인출 
print("복숭아", fruits['peach']) #400출력

#Key가 존재하는 경우에는 기존의 값이 변경된다. 
fruits['orange'] = 3500  
print("오렌지", fruits['orange'])

#삭제 : Key에 해당하는 요소를 삭제한다. 
del fruits['peach'] 
print('fruits=', fruits)

#keys() : 딕셔너리의 키로 구성된 dict_keys 객체를 반환한다. 
get_keys = fruits.keys()
for k in get_keys:
    #Key값을 출력한다. 
    print(k) 

#values() : 딕셔너리의 값으로 구성된 dict_values 객체를 반환한다. 
get_values = fruits.values()
for v in get_values:
    #Value값만 출력한다. 
    print(v) 
