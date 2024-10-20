class MyCalculator:
    #클래스 변수 : 클래스 전체에서 공유됨. 딱 하나만 생성됨.
    calCount = 0
    def __init__(self, first, second):
        #인스턴스 변수 : 생성된 인스턴스마다 존재함 
        self.first = first  
        self.second = second
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
    @staticmethod  
    def otherNumMulti(refCls, otherNum):
        result = (refCls.first + refCls.second) * otherNum
        MyCalculator.calCount += 1
        print("결과:", result)
        print("연산횟수:", MyCalculator.calCount)
    def __str__(self):
        str = f'계산기 클래스 입니다.' \
            f'first={self.first}, second={self.second}'
        return str

cal1 = MyCalculator(5, 9)
cal2 = MyCalculator(3, 4)

print('덧셈(cal1):', cal1.calculate('+'))
print('곱셈(cal1):', cal1.calculate('*'))

print('뺄셈(cal2):', cal1.calculate('-'))
print('나눗셈(cal2):', cal1.calculate('/'))

print("계산횟수", MyCalculator.calCount)

MyCalculator.otherNumMulti(cal1, 10)
MyCalculator.otherNumMulti(cal2, 10)

#인스턴스메서드는 클래스명으로 호출 불가
# MyCalculator.calculate('/')
