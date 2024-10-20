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

print('패스워드', myCom.getPasswd())

myCom.setPasswd('abcd9876')
print('패스워드 변경후1', myCom.getPasswd())

myCom.__passwd = "xxxxXXXX"
print('패스워드 변경후2', myCom.getPasswd())

# 권장되지 않음 
# print("맹글링규칙", myCom._Computer__passwd)