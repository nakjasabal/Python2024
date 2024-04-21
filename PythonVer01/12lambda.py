'''
람다(lambda) 함수
    :  def 키워드를 사용하지 않고 식 형식으로 되어있다해서
    람다식이라고 부른다. 이름이 없으므로 익명함수로 부르기도 한다.
    lambda 키워드를 사용하여 간편하게 작성할 수 있고, 재사용되지
    않는 1회성 함수를 만들때 사용한다. 
'''
# 두 수의 합
def two_sum(x, y):
    return x + y
print("함수를 통합 두수의 합=", two_sum(10, 20))

'''
형식]
    람다식 이름 = lambda 매개변수1, 매개변수2 : 실행문장
'''
sum = lambda arg1, arg2: arg1 + arg2
print("람다식을 통한 합=", sum(10, 20))

# 인자를 제곱해서 반환하는 람다식
power = lambda num : num**2
print("5의 제곱은=", power(5))

'''
람다식 자체호출
    : 람다식을 변수에 할당하지 않고, 괄호를 이용해서 
    식 자체를 바로 호출할 수 있다.
'''
print("람다식 자체호출=", (lambda x, y: x + y)(100, 200))



# 람다식과 map, filter, reduce 함수 활용
'''
map함수
    : 전달된 데이터를 동일 함수에 반복적으로 적용시켜 주는
    역할을 한다. for문과 같은 반복문을 사용하지 않아도 지정한
    함수로 인자를 여러번 전달해서 그 결과를 List형태로 반환하는
    유용한 함수이다. 
    형식]
        map(람다식, 파라미터)
'''
print("### 람다식과 map함수1 ###")
multiLambda = lambda x: x*2 #인자에 2를 곱한결과를 반환하는 람다식
list_data = [1,2,3,4,-1,-2,-5,-10]
# list_data의 인자갯수만큼 람다식을 호출하여 얻어진 결과를 리스트로 반환한다.
result_list = list(map(multiLambda, list_data))
# 리스트의 전체 인자를 2로 곱한 결과값이 출력된다. 
print('result_list', result_list)

'''
람다식에서 조건부 표현식 사용하기
형식]
    식1 if 조건식 else 식2
    - 조건식이 참일때 식1, 거짓일때 식2를 사용한다 
    - 람다식에서 조건부 표현식을 사용할때는 : 를 붙히지 않는다.
    - if를 사용했다면 반드시 else를 사용해야 한다. 
    - elif는 사용할 수 없다. 따라서 2개 이상의 조건도 if를 연속으로 사용한다.
'''
print("### 람다식과 map함수2 ###")
list_data2 = [1,2,3,4,5,6,7,8,9,10] 
# 인자가 3으로 나누어지는 경우 문자형태로 반환하고, 아니면 숫자의형태로 반환한다.
strNumLambda = lambda x: str(x) if x%3==0 else x
result_list2 = list(map(strNumLambda, list_data2))
print('result_list2', result_list2)
# 출력결과 : 3의 배수는 문자열로, 나머지는 숫자로 출력된다. 



'''
filter함수
    : 반복가능한 객체에서 특정 조건에 맞는 요소만 가져오는데,
    지정된 람다식에서 true를 반환하는것만 해당 요소를 가져오게된다.
    형식은 map과 동일하다. 
'''
print("### 람다식과 filter함수 ###")
powLambda = lambda y : y**2 #각 인자의 제곱의 결과를 반환하는 람다식
list_data3 = [1,4,9,16,25,46,64,81,100]
result_list3 = list(map(powLambda, list_data3)) #map을 통해 리스트 항목의 제곱을 구함
print('result_list2', result_list3)
# 50초과 & 1000미만인 요소일때만 true를 반환함.(해당 값만 필터링한다) 
filter_result = list(filter(lambda z: z>50 and z<1000, result_list3)) 
print('filter_result', filter_result) #실행결과 : 81, 256, 625


'''
reduce함수
    : 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤
    이전 결과와 누적해서 반환하는 함수이다. 
    파이썬3 부터는 내장함수가 아니므로 functools모듈을 import한후
    사용해야 한다. 
'''
print("### 람다식과 reduce함수 ###")
import functools, operator
'''
    1~10까지의 합을 반환하게 된다. 람다식이 두 요소를 더해서
    반환하도록 정의되었으므로, 처음엔 1과2가 인자로 주어져 
    더해지고, 그 결과에 3을 더하는 구조를 가지게 된다. 
'''
sum1 = functools.reduce(lambda i, j: i + j, range(1,11)) 
print("sum1=", sum1)
# operator 모듈의 add함수를 사용한다. 결과는 위와 동일하다. 
sum2 = functools.reduce(operator.add, range(1,11)) 
print("sum2=", sum2)
