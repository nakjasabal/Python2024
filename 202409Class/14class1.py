'''
클래스는 변수와 함수로 구성되어 있다. class 키워드를 통해
생성하면되고, 이를 통해 생성된 변수를 인스턴스 변수라고 한다. 
'''
class MyCalculator:
    #클래스변수 : 클래스 전체에서 사용할 수 있는 전역변수 
    calCount = 0 
    #생성자 : 클래스로부터 인스턴스를 생성할 때 변수를 초기화하는
    #   역할을 한다. 첫번째 매개변수 self는 필수사항이다. 
    def __init__(self, first, second):
        #클래스변수에 접근할때는 클래스명을 사용한다. 
        MyCalculator.calCount = 1
        #인스턴스 변수 선언 및 초기화 
        self.first = first  
        self.second = second
    #인스턴스 함수 
    def calculate(self, symbol):
        #클래스변수에 접근하여 1을 증가시킨다. 
        MyCalculator.calCount += 1
        #심볼을 확인하여 사칙연산을 수행한다. 
        #인스턴스 변수에 접근시에는 self를 사용한다. 
        if symbol=='+':
            result = self.first + self.second
        elif symbol=='-':
            result = self.first - self.second
        elif symbol=='*':
            result = self.first * self.second
        elif symbol=='/':
            result = self.first / self.second
        #사칙연산의 결과를 반환한다. 
        return result
    
    '''
    정적함수를 생성하기 위한 어노테이션이 부착한다. 어노테이션은
    함수의 역할을 지정하는 키워드 정도로 생각하면된다. 
    정적함수는 클래스를 통해 인스턴스를 생성하지 않고도, 클래스명
    으로 직접 호출할 수 있는 함수를 말한다. 
    '''
    @staticmethod  
    def otherNumMulti(refCls, otherNum):
        '''정적함수에서는 인스턴스 변수에 직접 접근할 수 없으므로
        인스턴스 변수를 매개변수를 통해 받은 후 접근해야한다.'''
        result = (refCls.first + refCls.second) * otherNum
        print("결과:", result)
        print("연산횟수:", MyCalculator.calCount)
    #인스턴스 변수를 출력할때 도움을 주는 함수로 지정된 문자열을
    #반환한다. 
    def __str__(self):
        str = f'계산기 클래스 입니다.' \
            f'first={self.first}, second={self.second}'
        return str

#클래스를 통해 인스턴스 변수 생성 
#이 문장을 통해 생성자를 호출하여 인스턴스 변수를 초기화한다.
cal = MyCalculator(5, 9)
# __str__() 함수를 통해 지정된 문자열이 출력된다. 
print(cal)

#덧셈과 곱셈 연산이 수행된다. 
print('덧셈:', cal.calculate('+')) #5+9의 결과
print('곱셈:', cal.calculate('*')) #5*9의 결과 

#인스턴스 변수 출력 
print('인스턴스변수:', cal.first, cal.second)

#클래스 변수 출력 
print('클래스변수:', cal.calCount, MyCalculator.calCount)

#정적함수 호출은 클래스명을 통해 할 수 있다. 
MyCalculator.otherNumMulti(cal, 10)

#인스턴스 함수는 클래스명으로 호출 불가
# MyCalculator.calculate('/')
