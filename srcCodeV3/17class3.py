class Computer:
    def __init__(self, name, passwd):
        self.name = name
        self.__passwd = passwd
    def doKeyboard(self):
        return f'{self.name}로 키보드 작업을 합니다.'
    def doMouse(self):
        print(f'{self.name}에서 마우스로 클릭합니다.')        
    def getPasswd(self):
        return self.__passwd
    def setPasswd(self, passwd):
        self.__passwd = passwd

myCom = Computer('LG Gram', 'qwer1234')
 
print(myCom.doKeyboard())
myCom.doMouse()

# private 이므로 접근할 수 없어 에러 발생
# print('패스워드:', myCom.__passwd)
print('패스워드:', myCom.getPasswd())