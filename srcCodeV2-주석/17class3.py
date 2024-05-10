'''
퀴즈1] 원의 넓이와 둘레를 계산할 수 있는 클래스를 작성한 후 
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
#반지름이 5인 인스턴스 생성
circle1 = Circle(5)
print(circle1)
print("원의넓이:", circle1.calArea())
print("원의둘레:", circle1.calRound())


'''
퀴즈2] 그래프상에서 원을 표시하려면 중심점의 좌표값과 반지름이 있으면 된다. 이를 상속으로 구현하시오. 
-부모클래스 : x, y(좌표값)를 멤버로 가진 Point 클래스
-자식클래스 : rad(반지름)을 멤버로 가진 GraphCircle 클래스
인스턴스 생성은 다음과 같이 한다. 
graphCircle1 = GraphCircle(3,4,10)
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'x,y좌표값:({self.x},{self.y})'

class GraphCircle(Point):
    def __init__(self, x, y, rad):
        super().__init__(x, y)
        self.rad = rad
    def __str__(self):        
        return f'{super().__str__()}, 반지름:{self.rad}'

graphCircle1 = GraphCircle(3,4,10)
graphCircle2 = GraphCircle(6,9,15)
print("첫번째원", graphCircle1)
print("두번째원", graphCircle2)