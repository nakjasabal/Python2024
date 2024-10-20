class MyCalculator:
    calCount = 0 
    def __init__(self, first, second):
        MyCalculator.calCount = 1
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
        print("결과:", result)
        print("연산횟수:", MyCalculator.calCount)
    def __str__(self):
        str = f'계산기 클래스 입니다.' \
            f'first={self.first}, second={self.second}'
        return str


cal = MyCalculator(5, 9)
print(cal)
print('덧셈:', cal.calculate('+'))
print('곱셈:', cal.calculate('*'))

print('인스턴스변수:', cal.first, cal.second)

print('클래스변수:', cal.calCount, MyCalculator.calCount)

MyCalculator.otherNumMulti(cal, 10)

#인스턴스메서드는 클래스명으로 호출 불가
# MyCalculator.calculate('/')

