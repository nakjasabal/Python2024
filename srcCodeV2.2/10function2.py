'''
지역변수와 전역변수
: 2개의 변수가 동일한 이름으로 사용되는 경우 지역변수가 
항상 높은 우선순위를 가진다.  
''' 
# 전역변수로 선언함. 해당 프로그램 전체에서 사용할수 있음. 
total = 0  

# 함수를 선언함. 
def sum(arg1, arg2):   
    #두개의 값을 합산하여 지역변수 total에 할당한다. 
    total = arg1 + arg2
    #지역변수 total은 해당 함수내에서만 사용할수있다. 
    print("지역변수 total=", total)
    #값을 반환한다. 
    return total  

#전역변수 total이 출력되므로 초기값인 0이 출력된다. 
print("전역변수 total=", total)  
 
#함수내에서 합산한 결과를 반환하므로 30이 출력된다.  
print("sum(10, 20)호출후 반환값=", sum(10, 20))  
print("===========================")

'''
내부함수
:  파이썬은 함수내부에 또 다른 함수를 정의할 수 있다. 
형식]
    def 함수1():
        실행문
        def 함수2():
            실행문
''' 
#함수 정의 
def commander(saying):  
    #내부함수정의 
    def inner(quote):
        #매개변수로 전달된 값을 아래와 같이 문자열로 반환한다. 
        return "조선의 위대한 장군 = '%s'" % quote  
    #내부함수인 inner()를 호출한 후 반환되는 값을 다시 반환한다. 
    return inner(saying) 
 
print(commander("이순신"))  
print("===========================")

'''
파이썬에서는 매개변수를 전달하는 4가지 방법이 있다. 
1.순서 매개변수 : 함수에서 사용하는 가장 일반적인 방식으로 작성 순서대로
    전달한다. 
'''  
def printme(str1, str2):
    print(str1, str2)
    #반환되는 값 없이 함수를 종료한다. 
    return 
cont = "은 매우 좋은 프로그램입니다."
#2개의 문자열을 전달하여 출력한 후 종료된다. 
printme("Python", cont)
print("===========================")

'''
2.키워드 매개변수 : 매개변수의 순서와 상관없이 매개변수명을 지정하여
    값을 전달한다. 
''' 
def printinfo(name, age):
    print("이름:", name)
    print("나이:", age)
    return
printinfo(age=50, name='홍길동')
print("===========================")

'''
3.기본(디폴트) 매개변수 : 인수가 전달되지 않는 경우 디폴트로 지정되는
    값을 말한다. 그러므로 매개변수의 갯수가 틀려도 호출할 수 있다. 
''' 
def defaultArgs(lan="Java"):
    print("내가 좋아하는 언어는 ", lan, "입니다")
    return  
# 이와 같이 인수가 전달되지 않는 경우 'Java'가 함수에서 사용된다.
defaultArgs() #만약 디폴트값이 없는 상태라면 여기에서 에러가 발생된다. 
# 전달되는 경우에는 'c++'을 함수에서 사용한다. 
defaultArgs("C++")  


'''
4. 가변 매개변수
    : 여러개의 매개변수를 전달하는 경우 그 갯수가 매번 달라질 수 있는경우에
    사용하는 방식으로
        *를 이용해서 매개변수의 값을 튜플로 받는다.
        **를 이용해서 매개변수의 값을 딕셔너리로 받아서 사용할 수 있다. 
''' 
def product(*args):
    #전달되는 인수를 튜플로 받아서 출력한다. 
    print("*args=>", args)  
    result = 1     
    #튜플의 갯수만큼 반복할 수 있다. 
    for a in args:
        result *= a #원소의 갯수만큼 누적곱을 계산해서 result에 저장한다.    
    #계산된 결과를 호출한 지점으로 반환한다.
    return result
#4개의 인수를 전달하여 함수를 호출한다.  
print("product(1,2,3,4) =", product(1,2,3,4))

# 2개의 *를 통해 딕셔너리로 인수를 받을수있다. 
def famousMan(**man):  
    print('**man', man)      
    '''딕서너리는 key를 통해 value를 출력한다. 즉 반복시 얻어온
    key를 통해 해당 값을 출력할수 있다. '''
    for key in man:  
        print(key, "=>", man[key])
#인수를 딕셔너리로 전달한다.     
famousMan(의인='홍길동', 장군='이순신', 임금='세종대왕')
