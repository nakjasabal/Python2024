#지역변수/전역변수
total = 0 # 전역변수로 선언
def sum(arg1, arg2):
    total = arg1 + arg2 #지역변수로 선언
    print("지역변수 total=", total)
    return total 

print("전역변수 total=", total) # 초기값 0이 그대로 출력됨
print("sum(10, 20)호출후 반환값=", sum(10, 20)) #10+20의 결과값 출력
print("===========================")

#내부함수
'''
    : 파이썬은 함수내부에 또다른 함수를 선언할 수 있다. 
    형식]
        def 함수명1():
            실행문
            def 함수명2():
                실행문
'''
def commander(saying):
    def inner(quote): # 내부함수 정의
        return "조선의 위대한 장군 = '%s'" % quote
    return inner(saying) #2차호출
print(commander("이순신")) # 1차호출
print("===========================")

## 매개변수의 종류는 아래 4가지가 있다. 
#순서매개변수 : 함수에서 사용하는 일반적인 매개변수. 작성순서대로 적용됨.
def printme(str1, str2):
    print(str1, str2)
    return
cont = "은 매우 좋은 프로그램입니다."
printme("Python", cont)
print("===========================")

#키워드매개변수 : 순서와 상관없이 매개변수명에 따라 전달됨.
def printinfo(name, age):
    print("이름:", name)
    print("나이:", age)
    return
printinfo(age=50, name='홍길동')
print("===========================")

#기본매개변수 : 매개변수가 주어지지 않았을때 디폴트로 지정되는 매개변수를 말함.
def defaultArgs(lan="Java"):
    print("내가 좋아하는 언어는 ", lan, "입니다")
    return
defaultArgs() # Java가 출력
defaultArgs("C++") # C++이 출력

#가변매개변수
'''
    : 여러개의 매개변수를 전달해야할때 사용하는 매개변수로
    Java의 가변인자와 비슷하다. 
    *를 이용해서 매개변수값을 튜플로 그룹화한다.
    **를 이용해서 매개변수를 딕셔너리로 사용할 수 있다. 
'''
def product(*args):
    print("*args=>", args) # 튜플 형태로 출력됨.
    result = 1
    for a in args: # 튜플이므로 반복문 사용가능
        result *= a # 누적해서 곱함
    return result
print("product(1,2,3,4) =", product(1,2,3,4))


def famousMan(**man):
    print('**man', man) #딕셔너리로 형태로 출력됨
    for key in man: # 딕셔너리이므로 key와 value로 출력가능
        print(key, "=>", man[key])
famousMan(의인='홍길동', 장군='이순신', 임금='세종대왕')

