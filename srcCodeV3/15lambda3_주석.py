# 람다식과 map, filter, reduce 함수 활용

print(f"{'람다식과 map함수1':-^30}")
#인자에 2를 곱한결과를 반환하는 람다식
multiLambda = lambda x: x*2 
list_data = [1,2,3,4,-1,-2,-5,-10]
# list_data의 인자갯수만큼 람다식을 호출하여 얻어진 결과를 리스트로 반환한다.
result = list(map(multiLambda, list_data))
# 리스트의 전체 인자를 2로 곱한 결과값이 출력된다. 
print('결과1', result)



'''
람다식에서 조건부 표현식 사용하기
형식]
    식1 if 조건식 else 식2
    - 조건식이 참일때 식1, 거짓일때 식2를 사용한다 
    - 람다식에서 조건부 표현식을 사용할때는 : 를 붙히지 않는다.
    - if를 사용했다면 반드시 else를 사용해야 한다. 
    - elif는 사용할 수 없다. 따라서 2개 이상의 조건도 if를 연속으로 사용한다.
'''
print(f"{'람다식과 map함수2':-^30}")
list_data2 = [1,2,3,4,5,6,7,8,9,10] 
# 인자가 3으로 나누어지는 경우 '3X'를 반환하고, 아니면 숫자를 그대로 반환한다.
strNumLambda = lambda x: '3X' if x%3==0 else x
result = list(map(strNumLambda, list_data2))
print('결과2', result)
# 출력결과 : 3의 배수는 문자열로, 나머지는 숫자로 출력된다. 


print(f"{'람다식과 filter함수':-^30}")
list_data3 = [1,4,9,16,25,46,64,81,100]
# 5초과 80미만인 요소일때만 true를 반환함.(해당 값만 필터링한다) 
result = list(filter(lambda z: z>5 and z<80, list_data3)) 
print('결과3', result) 
#실행결과 : 9~64까지의 인자만 리스트에 남는다. 



print(f"{'람다식과 reduce함수':-^30}")
import functools, operator
'''
    1~10까지의 합을 반환하게 된다. 람다식이 두 요소를 더해서
    반환하도록 정의되었으므로, 처음엔 1과2가 인자로 주어져 
    더해지고, 그 결과에 3을 더하는 구조를 가지게 된다. 
'''
sum1 = functools.reduce(lambda i, j: i + j, range(1,11)) 
print("결과4-1", sum1)

# operator 모듈의 add함수를 사용한다. 결과는 위와 동일하다. 
sum2 = functools.reduce(operator.add, range(1,11)) 
print("결과4-2", sum2)
