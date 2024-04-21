'''
Built-in Function(내장함수)
    : 내장함수는 외부모듈과 달리 import가 필요하지 않기 때문에
    아무런 설정없이 바로 사용할수 있다. 
    int(), print(), max(), input()과 같은 함수가 있다.
'''
print("="*5, "min() or max()", "="*20)
data1 = list(range(1,11)) 
print(data1)
print('len=', len(data1)) 
print('sum=', sum(data1))
print('max=', max(data1)) 
print('min=', min(data1))


'''
enumerate()
    : 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력받아 
    인덱스 값을 포함하는 enumerate객체를 반환한다. 
'''
print("="*5, "enumerate()", "="*20)

print('리스트출력')
for i, v in enumerate(data1):
    print(i, v)

print('딕셔너리출력')
data2 = dict(birth=1970, name="홍길동", size="100cm")
for i, v in enumerate(data2): #해당 객체의 인덱스와 값을 반환한다. 
    print(i, v, data2[v])

