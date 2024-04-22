'''
Built-in Function(내장함수)
    : 내장함수는 외부모듈과 달리 import가 필요하지 않기 때문에
    아무런 설정없이 바로 사용할수 있다. 
    int(), print(), max(), input()과 같은 함수가 있다.
'''
print(f'{'기본 내장 함수':-^30}')
data1 = list(range(1,11)) 
print(data1)
print('len=', len(data1)) 
print('sum=', sum(data1))
print('max=', max(data1)) 
print('min=', min(data1))


print(f'{'enumerate()':-^30}')
'''
순서가 있는 자료형(리스트, 튜플, 문자열)을 입력받아 인덱스 값을 포함하는 enumerate객체를 반환한다. 
'''
#리스트출력
for i, v in enumerate(data1):
    print(i, v, end=', ')
print()

#딕셔너리출력
data2 = dict(birth=1970, name="홍길동", size="100cm")
for i, v in enumerate(data2): #해당 객체의 인덱스와 값을 반환한다. 
    print(i, v, data2[v], end=', ')
print()


print(f'{'eval()':-^30}')
'''
실행가능한 문자열을 입력받아 실행한 결과값을 반환한다. 
'''
print(eval('1+2')) # 합의 결과 3 반환
print(eval("'hi' + 'a'")) # 문자열이 연결되어 반환


print(f'{'sorted()':-^30}')
'''
입력값을 정렬한 후 리스트로 반환한다. 
'''
numbers = (8,7,6,8,4,9,7,5,3,2,7,4,9,8,2,6,5)
print(sorted(numbers))


print(f'{'이터레이터(iterator)':-^30}')
'''
값을 차례대로 꺼낼 수 있는 객체(object)이다. 
for i in range(100): 와 같이 작성하면 파이썬은 0부터 99까지의 값을 
차례대로 꺼낼 수 있는 이터레이터를 생성하여 숫자를 생성하게된다. 

iter() : 반복을 끝낼 값(sentinel)을 지정하면 특정 값이 나올 때 반복을 종료한다.
형식]
    iter(반복가능한객체, 반복을끝낼값)
'''
it = iter([1,2,3,4,5,99]) #이터레이터 생성
while it:
    row = next(it)
    if row == 99:
        break
    print(row, end=", ")
#더 이상 출력할 항목이 없을때 next()를 호출하면 예외가 발생된다.
#이 부분은 예외처리에서 학습할 예정이다.     
print()


import random # 랜덤함수를 사용하기 위한 모듈
#0~10까지 난수를 생성하다 2가 나오면 실행종료
count = 0;
for i in iter(lambda : random.randint(0,10), 2):
    print(i, end=', ')
    count += 1
else:
    print('\n난수 2가 생성되어 종료')
print(f'반복횟수:{count}')




