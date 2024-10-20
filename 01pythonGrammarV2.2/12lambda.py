'''
람다(lambda)식
    : def키워드를 사용하지 않고 식 형식으로 되어있다해서
    람다식 혹은 람다표현식이라 부른다. 이름이 없는 함수형식이므로
    익명함수라고 부르기도 한다. 
    lambda 키워드를 사용해서 간편하게 작성할 수 있고, 재사용되지
    않는 1회성 함수를 만들때 사용한다. 
'''

#두수의 합을 반환하는 일반적인 형태의 함수 정의 
def two_sum(x, y):
    return x + y
print("함수를 통한 두수의 합=", two_sum(10, 20))

'''
람다식 정의
형식]
    호출을위한변수 = lambda 매개변수1,2..N : 실행문장 
'''
# 앞에서 정의한 two_sum()을 람다식으로 표현하면 다음과같다.
sum = lambda arg1, arg2: arg1 + arg2
print("람다식을 통한 합=", sum(10, 20))

#매개변수로 전달된 인자를 제곱한 결과를 반환하는 람다식 
power = lambda num : num**2
print("5의 제곱은=", power(5))

'''
람다식 자체호출
    : 람다식을 변수에 할당하지않고, 소괄호를 이용해서 식 자체를
    즉시 호출할 수 있다. 
'''
print("람다식 자체호출=", (lambda x, y: x + y)(100, 200))





#람다식과 map, filter, reduce 함수 활용 
'''
map()함수
    : 전달된 데이터를 동일 함수에 반복 적용해주는 역할을한다.
    for문과 같은 반복문을 사용하지 않아도 지정한 함수로 인수를
    반복적으로 전달하여 그 결과를 List로 반환해준다. 
    형식]
        map(람다식, 매개변수)
'''
print("### 람다식과 map함수1 ###")
#매개변수로 전달된 값에 2를 곱한 결과를 반환하는 람다식 정의
multiLambda = lambda x: x*2 
#리스트 정의 
list_data = [1,2,3,4,-1,-2,-5,-10] 
''' 첫번째 인자로 람다식, 두번째 인자로 List를 전달해서 map을
호출한다. map에서 반환되는 값은 List로 만들어지게 된다. '''
result_list = list(map(multiLambda, list_data))
#각 인자에 2를 곱한 결과가 반환된다. 
print('result_list', result_list)

'''
람다식에서 조건부 표현식 사용하기
형식]
    실행문1 if 조건식 else 실행문2
    -조건문이 True일때 실행문1, False일때 실행문2가 실행된다.
    -람다식에서 조건부 표현식을 사용할때는 :을 붙이지 않는다.
    -if를 사용했다면 반드시 else가 있어야한다. 
    -elif는 사용할 수 없다. 따라서 2개 이상의 조건이라 할지라도
    if를 연속으로 사용해야한다. 
'''
print("### 람다식과 map함수2 ###")
list_data2 = [1,2,3,4,5,6,7,8,9,10] 
'''매개변수가 3의 배수인 경우에는 문자로 변환해서 반환하고, 아니면
숫자 그대로 반환하는 람다식 정의 '''
strNumLambda = lambda x: str(x) if x%3==0 else x
result_list2 = list(map(strNumLambda, list_data2))
#결과를 출력하면 3의배수만 '로 감싸져 있는것을 볼수있다. 
print('result_list2', result_list2)



'''
filter함수
    : 반복가능한 객체에서 특정 조건을 만족하는 인자만 반환한다. 
    지정된 람다식에서 True를 반환하는 원소만 찾아서 반환한다.
'''
print("### 람다식과 filter함수 ###")

#각 인자를 제곱한 결과를 반환하는 람다식 정의 후 실행 
powLambda = lambda y : y**2  
list_data3 = [1,4,9,16,25,46,64,81,100]
result_list3 = list(map(powLambda, list_data3))  
print('result_list2', result_list3)

'''50초과 100미만인 값만 추출해서 새로운 List로 반환한다. 
즉 filter()는 조건에 맞는 항목만 필터링해서 반환한다. '''
filter_result = list(filter(lambda z: z>50 and z<1000, 
                            result_list3)) 
print('filter_result', filter_result)  


'''
reduce함수
    : 반복 가능한 객체의 각 인자를 지정된 함수로 처리한 뒤 이전
    결과와 누적해서 반환하는 함수. 파이썬 3.x부터는 내장함수가 
    아니므로 functools 모듈을 임포트해서 사용해야한다. 

    형식] reduce(람다식, 반복가능객체)
        람다식은 2개의 매개변수를 사용한다. 
        첫번째는 누적할 변수
        두번째는 현재 반복에서 반환된 값을 저장할 변수
'''
print("### 람다식과 reduce함수 ###")
import functools, operator
 
#1부터 10까지의 누적합을 최종적으로 반환한다. 
#해당 회차에서 반환된 값은 다음 회차의 i로 할당된다. 
sum1 = functools.reduce(lambda i, j: i + j, range(1,11)) 
print("sum1=", sum1) #결과 : 55

#operator모듈의 add함수를 사용하여 위와 동일한 결과를 얻을수있다.
sum2 = functools.reduce(operator.add, range(1,11)) 
print("sum2=", sum2)
