'''
class(클래스)
    : 파이썬에서 클래스는 데이터와 이를 조작하는 함수를 함께 
    묶어 정의한 사용자정의 데이터형식이다. 
    클래스를 통해 생성하는 변수를 인스턴스라고 표현한다. 
'''
#클래스 선언 
class FourCalculator:  
    '''변수를 생성하고 이를 초기화 하기 위한 목적의 함수. 클래스에
    정의되는 함수는 무조건 첫번째 매개변수로 self를 기술해야한다.'''
    def setdata(self, first, second):       
        ''' 인스턴스변수 선언 및 초기화. 매개변수로 전달된 2개의 값을
        통해 각 변수를 초기화한다. '''
        self.first = first
        self.second = second

    ''' 사칙연산을 수행하는 인스턴스 함수를 정의한다. 인스턴스 변수에
    접근하기 위해 첫번째 매개변수로 self를 반드시 기술해야한다. '''    
    def addition(self):
        result = self.first + self.second  
        return result
    def subtraction(self):
        result = self.first - self.second
        return result
    def multiplication(self):
        result = self.first * self.second
        return result
    def division(self):
        result = self.first / self.second
        return result

''' 인스턴스 변수 생성. 클래스명을 이용해서 변수를 생성한다. '''
a = FourCalculator()
b = FourCalculator()

'''
인스턴스 생성 후 변수를 초기화해주는 함수를 호출한다. 
첫번째 매개변수 self문은 클래스 안에서 함수를 생성할때 반드시 필요한
요소이므로 호출시에는 무시해야한다. 따라서 2개의 인자를 가지고 호출하면
된다. 
변수가 각각 4와2, 3과8로 초기화된다. 
'''
a.setdata(4, 2)
b.setdata(3, 8)

#각 인스턴스를 통해 함수를 호출하여 연산의 결과를 출력한다. 
print("객체a 덧셈", a.addition())
print("객체a 곱셈", a.multiplication())
print("객체b 뺄셈", b.subtraction())
print("객체b 나눗셈", b.division())
