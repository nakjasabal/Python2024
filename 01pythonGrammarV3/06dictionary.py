dic1 = dict(birth=1970, name="홍길동", size="100cm")
print(dic1)
dic2 = {'one':1, 'two':2, 'three':'3'}
print(dic2)

fruits = {'apple':100, 'grapes':200, 'orange':300, 'peach':400}
print('for문을 이용한 출력')
for key in fruits:
    val = fruits[key]
    print("%s : %d" % (key, val))

print("길이", len(fruits))
print("복숭아", fruits['peach'])

fruits['orange'] = 3500
print("오렌지", fruits['orange'])

del fruits['peach']
print('복숭아삭제', fruits)

#keys()
get_keys = fruits.keys()
for k in get_keys:
    print(k)
    
#values()
get_values = fruits.values()
for v in get_values:
    print(v)

