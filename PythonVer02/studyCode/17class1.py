'''
생성자(initializer) 
    : 클래스로부터 객체를 만들때 인스턴스 변수를 초기화한다. init양쪽에 언더바 2개를 붙여 정의한다. 
정적메소드 
    : 클래스명으로 바로 접근할 수 있는 메소드를 말한다.
'''
class MyCalculator:
    #클래스 변수 : 클래스 전체에서 접근가능한 전역변수
    calCount = 0 
    #생성자
    def __init__(self, first, second):
        #클래스변수 접근시에는 클래스명을 사용
        MyCalculator.calCount = 1
        #인스턴스변수 선언 및 초기화
        self.first = first  
        self.second = second
    #인스턴스 메서드
    def calculate(self, symbol):
        #클래스변수에 접근시 클래스명을 사용 
        MyCalculator.calCount += 1
        #인스턴스변수에 접근시 self를 사용
        if symbol=='+':
            result = self.first + self.second
        elif symbol=='-':
            result = self.first - self.second
        elif symbol=='*':
            result = self.first * self.second
        elif symbol=='/':
            result = self.first / self.second
        return result
    #정적메소드로 정의한 메소드
    @staticmethod  
    def otherNumMulti(refCls, otherNum):
        #정적메서드에서는 인스턴스변수에 직접 접근할 수 없으므로 
        #인스턴스 변수를 받은 후 접근해야한다. 
        result = (refCls.first + refCls.second) * otherNum
        print("결과:", result)
        print("연산횟수:", MyCalculator.calCount)
    #출력을 도와주는 메서드
    def __str__(self):
        str = f'계산기 클래스 입니다.' \
            f'first={self.first}, second={self.second}'
        return str


#인스턴스 변수 생성
cal = MyCalculator(5, 9)
print(cal)
print('덧셈:', cal.calculate('+'))
print('곱셈:', cal.calculate('*'))

#인스턴스 변수 접근
print('인스턴스변수:', cal.first, cal.second)

#클래스 변수 접근
print('클래스변수:', cal.calCount, MyCalculator.calCount)

#정적메서드 호출
MyCalculator.otherNumMulti(cal, 10)

#인스턴스메서드는 클래스명으로 호출 불가
# MyCalculator.calculate('/')

