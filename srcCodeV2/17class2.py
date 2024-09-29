class Person:
    def __init__(self, name, age, passwd):
        self.name = name
        self.age = age
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
print('이름:', p1.name)
#접근할 수 없어 에러 발생
# print('패스워드:', p1.__passwd)
print('패스워드:', p1.getPasswd())


class Teacher(Person):
    def __init__(self, name, age, passwd, subject):
        super().__init__(name, age, passwd)
        self.subject = subject
    def teaching(self):
        print(f'{self.name} 쌤이 {self.subject} 를 강의합니다')
        print(f'나이는 {self.age} 입니다')
    def showPasswd(self):
        #에러발생됨
        #print(f'선생님의 비밀번호는 {self.__passwd} 일까요?')
        print(f'선생님의 비밀번호는 {self.getPasswd()} 입니다')

p2 = Teacher('낙자', 40, '9876', 'Python')
p2.teaching()
p2.showPasswd()

