'''
인스턴스변수 : 메소드 안에 정의되는 변수
-클래스 내부에서는 self.변수명 형태로 접근한다.
-클래스 외부에서는 객체변수.인스턴스변수 형태로 접근한다. 

인스턴스 메소드는 인스턴스 변수에 항상 엑세스할수 있도록
메소드의 첫번째 파라미터에 항상 객체 자신을 의미하는
self라는 파라미터를 선언해야한다.
'''
class FourCalculator:
    # setter()메소드 (초기화담당)
    def setdata(self, first, second):
        self.first = first
        self.second = second
    # 사칙연산을 수행하는 인스턴스메소드. 첫번째 인자로 self를 사용한다.
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
#객체생성(new를 사용하지 않는다.)
a = FourCalculator()
b = FourCalculator()

#setter()를 통해 초기값 설정
a.setdata(4, 2)
b.setdata(3, 8)

#인스턴스 메소드 호출. 인스턴스 변수를 통해 접근한다. 
print("객체a 덧셈", a.addition())
print("객체a 곱셈", a.multiplication())
print("객체b 뺄셈", b.subtraction())
print("객체b 나눗셈", b.division())

'''
생성자(initializer) : 클래스로부터 객체를 만들때 인스턴스 변수를
    초기화한다. init양쪽에 언더바 2개를 붙여 정의한다. 
정적메소드 : 클래스명으로 바로 접근할 수 있는 메소드를 말한다.
클래스메소드 : 정적메소드와 비슷한데, 객체 인스턴스를 의미하는 
    self대신 cls라는 클래스를 의미하는 파라미터를 전달받는다. 
    cls를 통해 클래스변수에 엑세스할 수 있다. 
'''
class CalculatorInit:
    count = 0 #클래스 변수(클래스 전체에서 접근가능한 전역변수)

    ''' Java처럼 생성자 오버로딩은 지원하지 않는다. 
    def __init__(self):
        self.first = 1
        self.second = 2'''
    #생성자메소드 정의. self를 첫번째 매개변수로 선언해야함. 
    def __init__(self, first, second):
        self.first = first  
        self.second = second
        CalculatorInit.count += 1
    #일반적인 인스턴스 메소드
    def addition(self):
        result = self.first + self.second
        return result
    #정적메소드로 정의한 메소드
    @staticmethod  
    def staticArea(pFirst, pSecond):
        result = pFirst * pSecond 
        print("static메소드", result)
    #클래스 메소드로 정의
    @classmethod     
    def showInfo(cls): #cls를 통해 클래스변수에 접근할수 있다. 
        print('class메소드', cls.count)    
 
#fCal = FourCalculatorInit() -> 에러발생(해당 생성자는 정의되지 않음)
#인자를 전달하여 생성자를 통해 객체를 생성한다. 
fCal = CalculatorInit(2010, 43) 
print(fCal.addition())
fCal.showInfo() #클래스메소드 호출
CalculatorInit.staticArea(5, 8) #정적메소드 호출

# 상속 : 파이썬에서는 별도의 키워드 없이 클래스 정의시 매개변수 형태로 상속한다.
class moreCalculator(CalculatorInit):    
    # 확장한 메소드
    def pow(self):
        result = self.first ** self.second
        return result    
    #오버라이딩 : 부모의 기능을 재정의함
    def addition(self):
        return (self.first + self.second) * 2

#자식객체 생성 및 호출
moreCal = moreCalculator(4, 3) #4의 3승의 결과출력
print("상속후", moreCal.pow())

#부모 및 자식 클래스를 통한 객체생성 
p1 = CalculatorInit(100, 200)
p2 = moreCalculator(100, 200)
#오버라이딩 결과 확인하기
print("부모객체로호출", p1.addition()) #결과 : 300
print("자식객체로호출", p2.addition()) #결과 : 600

#정보은닉 : 인스턴스 변수를 비공개속성(private)으로 만들수있다.
class Person:
    def __init__(self, n, a, pw):
        self.name = n
        self.age = a
        # private멤버로 만들기 위해 변수앞에 언더바를 2개 붙여준다.
        self.__passwd = pw
    def secret_info(self):
        return self.__passwd

p1 = Person('my', 22, 'qwer1234')
print("이름", p1.name)
print("나이", p1.age)
#private 변수이므로 클래스외부에서는 접근불가함. 에러발생됨.
#print("비밀번호1", p1.__passwd)
#print("비밀번호2", p1.passwd) 
#private 변수는 메소드를 통해 간접적으로 접근한다.
print("비밀번호", p1.secret_info())

