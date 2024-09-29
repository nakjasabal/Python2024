'''
예외처리
  : 파이썬 구문에 대한 에러가 아닌 실행상의 에러가 발생되었을때
  프로그램의 흐름이 중단되지 않도록 처리하는것을 말한다. 
  예외가 발생할 수 있는 코드를 try~except로 감싼후 처리한다. 
형식]
  try:
    예외발생 가능성이 있는 실행구문
  except:
    예외가 발생하면 처리
  else:
    예외가 발생하지 않으면 실행되는 구문
  finally:
    예외발생과 상관없이 try문으로 진입하면 항상 실행되는 구문
'''

#함수선언 
def calc(val):    
    sum = None
    #예외발생이 예상되는 지점을 try로 묶어준다. 
    try:
        #3개 이상의 인자를 가진 List의 경우 문제없이 실행
        sum = val[0] + val[1] + val[2]
        
        #List의 0번 인자에 따라 각 블록이 실행
        if val[0]==100:
            #선언하지 않은 변수를 출력하므로 예외발생
            print(no_var) 
        elif val[0]==55:
            #정수를 0으로 나누면 무한대가 되므로 연산불능 예외발생 
            result = val[0] / 0 
            print("결과", result)
    #예외명을 명시하여 특정 예외만 처리
    except IndexError:
        #인덱스 사용을 잘못한 경우 발생되는 예외 
        print('리스트의 인덱스에 에러가 있습니다')  
    except NameError as err:
        #예외발생시 에러메세지를 변수로 받아서 출력할때 as를 사용
        print('선언되지 않은 변수를 사용하였습니다', str(err)) 
    #예외명을 명시하지 않았으므로 모든 예외를 처리할 수 있는 블럭이 됨
    except:         
        print('예외가 발생하였습니다')
    #try블럭에서 예외가 발생하지 않았을때 실행(필요없다면 생략가능)
    else:  
        print('에러없음^^') 
    # try블럭으로 진입했을때 예외발생과 상관없이 무조건 실행해야
    # 하는 코드가 있다면 finally절에 기술하면 된다.(필요없다면 생략가능)
    finally:
        print('sum', sum)


#List의 크기가 3이므로 정상적으로 실행된다. 
print('실행1')
calc([1, 2, 3]) 

#인자가 2개밖에 없으므로 IndexError가 발생된다. 
print('실행2')
calc([10, 20]) 

#no_var라는 변수는 선언한적이 없으므로 NameError가 발생된다. 
print('실행3')
calc([100,101,102,103])

#0으로 나누기 때문에 연산불능 예외가 발생된다. 
print('실행4')
calc([55,56,57])


'''
파일을 r(Read모드)로 오픈할때 파일이 없으면 에러가 발생된다. 
파일이 있을때와 없을때 각각 실행해본다. 
'''
print('실행5')
try:   
    fp = open("test.txt", "r", encoding='utf-8') 
    try:
        #내용을 한줄 읽어온다. 
        lines = fp.readlines()
        print(lines)
    finally:
        #예외와 상관없이 파일 객체를 닫아준다. 
        print("파일 객체를 닫습니다")
        fp.close()
except IOError: 
    #현재 경로에는 해당 파일이 없으므로 예외가 발생된다. 
    print('파일에러발생')


#개발자가 직접 예외 발생시키기 
print('실행6')
try:
    x = int(input('3의 배수를 입력하세요: '))
    #입력한 수가 3의 배수가 아니면 예외를 직접 발생시킨다.
    if x % 3 != 0: 
        #예외를 발생시킬때는 raise 키워드를 사용해서 Exception
        #인스턴스를 생성해주면 된다. 
        raise Exception('[예외메세지] 3의 배수가 아님')
    print(x)
except Exception as e:    
    print('예외가 발생했습니다.', e)


'''
개발자 정의 예외클래스 생성
: 예외클래스 생성시 Exception 클래스를 상속하고 생성자에서 
예외발생시 출력할 메세지를 정의한다. 
'''
print('실행7')
class GugudanRangeExcept(Exception):
    #생성자 함수 
    def __init__(self):
        super().__init__('구구단의 범위를 벗어났습니다')
    
def print_gugudan(end_num):
    try:
        ''' 입력한 단수가 9를 초과하는 경우 예외객체를 생성하여 raise
        해준다. 그러면 파이썬이 예외를 발생시키는것과 동일한 상태가
        된다. '''
        if end_num > 9:            
            raise GugudanRangeExcept
        end_dan = end_num + 1        
        for dan in range(2,end_dan):
            for su in range(1,10):
                print("%2d * %2d = %2d" % (dan, su, dan*su), 
                      end=' ')
            print()
        print()    
    except Exception as e:
        '''예외객체 새성시 생성자를 통해 지정했던 예외메세지가
        출력된다. '''
        print('예외발생', e)

print_gugudan(int(input("출력할 단 수를 입력하세요:")))    

