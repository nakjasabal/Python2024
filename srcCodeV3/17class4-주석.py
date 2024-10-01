class MyCalculator:
    #클래스 변수 : 클래스 전체에서 공유됨. 딱 하나만 생성됨.
    calCount = 0
    #생성자 
    def __init__(self, first, second):
        #인스턴스 변수 : 생성된 인스턴스마다 존재함 
        self.first = first  
        self.second = second
    #인스턴스 함수 정의 
    def calculate(self, symbol):
        MyCalculator.calCount += 1
        if symbol=='+':
            result = self.first + self.second
        elif symbol=='-':
            result = self.first - self.second
        elif symbol=='*':
            result = self.first * self.second
        elif symbol=='/':
            result = self.first / self.second
        return result
    #정적함수 정의 
    @staticmethod  
    def otherNumMulti(refCls, otherNum):
        result = (refCls.first + refCls.second) * otherNum
        MyCalculator.calCount += 1
        print("결과:", result)
        print("연산횟수:", MyCalculator.calCount)
    #참조변수 자체를 사용해서 인스턴스의 내용을 출력할 수 있는 함수 
    #print(참조변수) 와 같이 작성하면 이 함수가 자동으로 호출되어 작성된 내용이 반환됨 
    def __str__(self):
        str = f'계산기 클래스 입니다.' \
            f'first={self.first}, second={self.second}'
        return str

#참조변수 생성(계산기1, 2를 생성했다고 가정) 
cal1 = MyCalculator(5, 9)
cal2 = MyCalculator(3, 4)

#계산기1을 통해 연산
print('덧셈(cal1):', cal1.calculate('+'))
print('곱셈(cal1):', cal1.calculate('*'))

#계산기2을 통해 연산
print('뺄셈(cal2):', cal1.calculate('-'))
print('나눗셈(cal2):', cal1.calculate('/'))

#클래스변수는 딱 하나만 생성되므로 4가 출력됨 
print("계산횟수", MyCalculator.calCount)

#정적함수는 참조변수가 아니라 클래스명으로 직접 호출할 수 있다. 
#즉 함수 호출을 위해 참조변수를 생성할 필요가 없다. 
MyCalculator.otherNumMulti(cal1, 10)
MyCalculator.otherNumMulti(cal2, 10)

#인스턴스메서드는 클래스명으로 호출할 수 없다. 
#반드시 참조변수 생성 후 호출해야한다. 
# MyCalculator.calculate('/')
