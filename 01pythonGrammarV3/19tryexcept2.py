print('실행6')
try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:  
        raise Exception('[예외메세지] 3의 배수가 아님')
    print(x)
except Exception as e:    
    print('예외가 발생했습니다.', e)
    
print('실행7')
class GugudanRangeExcept(Exception):
    def __init__(self):
        super().__init__('구구단의 범위를 벗어났습니다')
    
def print_gugudan(end_num):
    try:
        if end_num > 9:            
            raise GugudanRangeExcept
        end_su = end_num + 1        
        for dan in range(2,end_su):
            for su in range(1,10):
                print("%d * %d = %2d" % (dan, su, dan*su), end=' ')
            print()
        print()    
    except Exception as e:
        print('예외발생', e)

print_gugudan(int(input("출력할 단 수를 입력하세요:")))    


