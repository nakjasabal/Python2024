#개발자가 직접 예외 발생시키기
print('실행6')
try:
    x = int(input('3의 배수를 입력하세요: '))
    #사용자가 입력한 숫자가 3의배수가 아니면 예외를 발생시킴
    if x % 3 != 0: #예외발생시 throw대신 raise를 사용함
        raise Exception('[예외메세지] 3의 배수가 아님')
    print(x)
except Exception as e:    
    print('예외가 발생했습니다.', e)
    
#사용자정의 예외클래스 만들기
'''
    예외 클래스 정의시 Exception객체를 상속하고
    생성자에서 예외발생시 출력할 메세지를 정의한다. 
'''
print('실행7')
class GugudanRangeExcept(Exception):
    def __init__(self):
        super().__init__('구구단의 범위를 벗어났습니다')
    
def print_gugudan(end_num):
    try:
        #예외를 발생시킬 조건에서 해당 클래스를 raise한다. 
        if end_num > 9:            
            raise GugudanRangeExcept
        end_su = end_num + 1        
        for su in range(2,end_su):
            for dan in range(1,10):
                print("%2d * %2d = %2d" % (su, dan, su*dan), end=' ')
            print()
        print()    
    except Exception as e:
        print('예외발생', e)

print_gugudan(int(input("출력할 단 수를 입력하세요:")))    
