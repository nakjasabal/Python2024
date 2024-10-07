class Computer:
    def __init__(self, name, passwd):
        self.name = name
        self.__passwd = passwd
    def hitKeyboard(self):
        return f'{self.name}로 키보드 작업을 합니다.'
    def clickMouse(self):
        print(f'{self.name}에서 마우스로 클릭합니다.')        
    def getPasswd(self):
        return self.__passwd
    def setPasswd(self, passwd):
        self.__passwd = passwd

myCom = Computer('LG Gram', 'qwer1234')
 
print(myCom.hitKeyboard())
myCom.clickMouse()

print("컴퓨터이름", myCom.name)

# private 이므로 접근할 수 없어 에러 발생
# print("패스워드", myCom.__passwd)

# getter 메서드를 통해 접근해야 함
print('패스워드', myCom.getPasswd())

# setter 메서드를 통해 값을 변경한 후 재출력
myCom.setPasswd('abcd9876')
print('패스워드 변경후1', myCom.getPasswd())

#직접 사용 불가
myCom.__passwd = "xxxxXXXX"
print('패스워드 변경후2', myCom.getPasswd())

# private 멤버는 Python의 이름 맹글링(name mangling) 규칙에 의해 다음과같이 변경된다. 
# 이렇게 사용할 수 있으나 권장되지 않는 방법이다. 
# print("맹글링규칙", myCom._Computer__passwd)