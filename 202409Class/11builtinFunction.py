'''
Built-in function(내장함수)
: 내장함수는 외부모듈과 달리 import가 필요하지 않기 때문에
아무런 설정없이 바로 사용할 수 있다. 
파이썬의 버전에 따라 import가 필요한 경우도 있다. 
int(), print(), max(), input()과 같은 함수가 있다. 
'''
print(f"{'기본 내장 함수':-^30}")
''' range() 함수는 인수의 범위에 해당하는 숫자를 자동으로 반환하여
list() 함수에 의해 리스트로 생성된다. '''
data1 = list(range(1,11)) 
#1~10까지의 인자를 가진 리스트가 출력된다. 
print(data1)
print('len=', len(data1)) #크기를 반환
print('sum=', sum(data1)) #합계
print('max=', max(data1)) #최대값
print('min=', min(data1)) #최소값

'''
순서가 있는 자료형(리스트, 튜플, 문자열)을 입력받아 인덱스 값을
포함하는 enumerate객체를 반환한다. 
'''
print(f"{'enumerate()':-^30}") 
for i, v in enumerate(data1):
    #리스트의 인덱스와 값을 출력 
    print(i, v, end=', ')
print()

#딕셔너리도 리스트와 동일한 방식으로 출력된다. 
data2 = dict(birth=1970, name="홍길동", size="100cm")
#딕셔너리는 별도의 설정이 없다면 Key가 반환된다. 
for i, v in enumerate(data2):  
    #Key를 통해 Value를 출력할 수 있다. 
    print(i, v, data2[v], end=', ')
print()

'''
실행가능한 문자열을 입력받아 실행한 결과값을 반환한다. 
'''
print(f"{'eval()':-^30}") 
print(eval('1+2')) # 합의 결과 3 반환
print(eval("'hi' + 'a'")) # 문자열이 연결되어 반환 

#입력값을 정렬한 후 리스트로 반환한다. 
print(f"{'sorted()':-^30}") 
#튜플 생성 및 초기화 
numbers = (8,7,6,8,4,9,7,5,3,2,7,4,9,8,2,6,5)
#리스트로 반환됨 
print(sorted(numbers))

'''
값을 차례대로 꺼낼 수 있는 객체(Object)이다. 
for i in range(100): 와 같이 작성하면 파이썬은 0~99까지의 
값을 차례대로 꺼낼 수 있는 이터레이터를 통해 숫자를 생성하게된다. 
iter() : 반복을 끝낼 값(Sentinel)을 지정하면 특정 값이 나올때
반복을 종료한다. 
'''
print(f"{'이터레이터(iterator)':-^30}")
#이터레이터 생성 
it = iter([1,2,3,4,5,99]) 
while it:
    #next()가 호출되면 다음 인자로 넘어간다. 
    row = next(it)
    #99가 인출되면 반복문을 탈출한다. 
    if row == 99:
        break
    #출력시 줄바꿈 없이 콤마로 구분한다. 
    print(row, end=", ")
print()

#랜덤함수를 사용하기 위한 모듈 
import random  
count = 0
#0~10까지의 난수를 생성하다 2가 나오면 실행이 종료된다. 
for i in iter(lambda : random.randint(0,10), 2):
    print(i, end=', ')
    count += 1
else:
    print('\n난수 2가 생성되어 종료')
print(f'반복횟수:{count}')




