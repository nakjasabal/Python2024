'''
딕셔너리(Dictionary)
-List와 비슷하지만 고유키(Key)와 값(Value)으로 선언한다. 
-값은 변경할 수 있고 중괄호로 선언한다. 
-단, 순서는 보장되지 않는다. 
'''
#생성1 : dict() 함수를 통해 선언 
dic1 = dict(birth=1970, name="홍길동", size="100cm")
print(dic1)
#생성2 : 중괄호를 통해 딕셔너리 선언 
dic2 = {'one':1, 'two':2, 'three':'3'}
print(dic2)

fruits = {'apple':100, 'grapes':200, 'orange':300, 'peach':400}
print('for문을 이용한 출력')
#딕셔너리에 저장된 요소의 갯수만큼 반복하여 key를 인출한다.
for key in fruits: 
    #인출한 key를 통해 value를 얻어와서 변수에 저장 
    val = fruits[key]  
    #key는 문자열이므로 %s, value는 정수이므로 %d를 사용해서 출력
    #s => String, d => Decimal을 의미한다. 
    #특정 서식에 맞춰 출력에 도움을 주기때문에 '서식문자'라고 한다.
    print("%s : %d" % (key, val))

# len : 딕셔너리의 크기를 반환 
print("길이", len(fruits)) 
# key를 마치 인덱스처럼 사용하여 value를 인출한다. 
print("복숭아", fruits['peach']) #400출력

#기존에 key가 존재하는 경우에는 값이 변경(수정)된다. 
fruits['orange'] = 3500  
print("오렌지", fruits['orange'])

#삭제 : key에 해당하는 요소를 삭제한다. 
del fruits['peach'] 
print('fruits=', fruits)

#keys() : 딕셔너리의 키로 구성된 dict_keys 객체를 반환한다. 
get_keys = fruits.keys()
#key값을 반복해서 출력 
for k in get_keys:
    print(k) 

#values() : 딕셔너리의 값으로 구성된 dict_values 객체를 반환한다.
get_values = fruits.values()
#value만 반복해서 출력 
for v in get_values:
    print(v) 
