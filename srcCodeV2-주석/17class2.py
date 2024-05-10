class Person:
    def __init__(self, name, age, passwd):
        #public으로 선언되어 외부에서 접근 가능
        self.name = name
        self.age = age
        #private으로 선언되어 외부에서 접근 불가능
        self.__passwd = passwd
    def doEat(self):
        return f'{self.name}님이 식사를 합니다.'
    def doAge(self):
        print(f'나이는 {self.age}살 입니다.')
    def getPasswd(self):
        return self.__passwd
    def setPasswd(self, passwd):
        self.__passwd = passwd
p1 = Person('정우성', 39, 'qwer1234')
print(p1.doEat())
p1.doAge()
#접근 가능하므로 정상 출력
print('이름:', p1.name)
#접근할 수 없어 에러 발생
# print('패스워드:', p1.__passwd)
#함수를 통해 간접적으로 접근해야 함
print('패스워드:', p1.getPasswd())


#자식클래스 선언 
class Teacher(Person):
    #자식의 생성자에서는 부모의 멤버변수까지 초기화해야된다. 
    def __init__(self, name, age, passwd, subject):
        super().__init__(name, age, passwd)
        self.subject = subject
    #자식의 인스턴스 메서드에서 부모의 인스턴스 변수에 접근할 수 있다.
    def teaching(self):
        print(f'{self.name} 쌤이 {self.subject} 를 강의합니다')
        print(f'나이는 {self.age} 입니다')
    #private 멤버는 자식에서도 접근할 수 없다. 
    def showPasswd(self):
        #에러발생됨
        #print(f'선생님의 비밀번호는 {self.__passwd} 일까요?')
        #getter메서드를 통해 접근해야한다. 
        print(f'선생님의 비밀번호는 {self.getPasswd()} 입니다')

p2 = Teacher('낙자', 40, '9876', 'Python')
p2.teaching()
p2.showPasswd()

