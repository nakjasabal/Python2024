'''
Built-in Function(내장함수)
: 내장함수는 외부모듈과 달리 import가 필요하지 않기 때문에 아무런
설정없이 바로 사용할 수 있다.
int(), min(), print()와 같은 함수가 있다. 
''' 

'''
enumerate()
: 순서가 있는 자료형(리스트, 튜플, 문자열 등)을 입력받아 인덱스를 
포함한 객체를 반환한다. 
'''
print("="*5, "enumerate()", "="*20)
# 리스트 선언
data = ['Naver', 'Kakao', 'Google'] 
# 반복시 인덱스를 포함한 값을 반환한다. 
for i, v in enumerate(data):
    # 인덱스와 같은 값을 출력하기 위해 별도의 변수를 선언하지 않아도된다.
    print(i, v)


'''
eval()
: 실행가능한 문자열을 입력받아 실행한 결과를 반환한다. 
즉 문자열 좌우의 쿼테이션을 이발하듯 잘라낸 후 내부의 코드를 실행한다. 
'''
print("="*5, "eval()", "="*20)
print(eval('1+2'))  
print(eval("'hi' + 'a'"))  

'''
sorted()
: 입력값을 정렬한 후 리스트로 반환한다. 
'''
print("="*5, "sorted()", "="*20)
#정렬전의 데이터는 튜플로 전달한다. 
numbers = (8,7,6,8,4,9,7,5,3,2,7,4,9,8,2,6,5)  
#정렬된 결과는 리스트로 반환된다. 
print(sorted(numbers)) # 오름차순(디폴트)
print(sorted(numbers, reverse=True)) # 내림차순 








