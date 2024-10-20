'''
시나리오] 원의 넓이와 둘레를 계산할 수 있는 클래스를 작성한 후 
주어진 코드가 실행될 수 있도록 구현하시오.
circle1 = Circle(5)
print("원의넓이:", circle1.calArea())
print("원의둘레:", circle1.calRound())
'''
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    #넓이
    def calArea(self):
        return math.pi * (self.radius ** 2)
    #둘레
    def calRound(self):
        return 2 * math.pi * self.radius
    def __str__(self):
        return f'원의 반지름은 {self.radius} 입니다.'

circle1 = Circle(5)
print(circle1)
print("원의넓이:", circle1.calArea())
print("원의둘레:", circle1.calRound())

