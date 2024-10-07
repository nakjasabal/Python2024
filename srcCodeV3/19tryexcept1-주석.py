'''
예외처리
    : 에러를 핸들링하기 위해 사용된다. 
    파이썬에서는 try~except를 사용한다. 
    그리고 else절을 사용할 수 있다. 
'''
def calc(val):
    sum = None
    try: #예외발생 예상 지점을 try로 묶음
        sum = val[0] + val[1] + val[2]
        if val[0]==100:
            print(no_var)
        elif val[0]==55:
            result = val[0] / 0
            print("결과", result)
    #예외명을 명시하여 특정 예외만 처리한다.
    except IndexError:
        print('리스트의 인덱스에 에러가 있습니다')
    #예외발생시의 에러메세지를 변수로 받아서 출력한다. 
    except NameError as err:         
        print('선언되지 않은 변수를 사용하였습니다', str(err)) 
    #예외명을 명시하지 않으면 모든 예외를 처리할수있는 블럭이된다. 
    except:         
        print('예외가 발생하였습니다')
    else: #예외가 발생하지 않았을때 실행되는 블럭
        print('에러없음^^') 
    finally: #예외발생과 상관없이 무조건 실행되는 블럭
        print('sum', sum) 
print('실행1')
calc([1, 2, 3]) #정상실행
print('실행2')
calc([10, 20]) #인덱스 에러
print('실행3')
calc([100,101,102,103]) #NameError 발생
print('실행4')
calc([55,56,57]) #ZeroDivisionError가 발생되어 except: 에서 처리됨


#중첩된 예외처리
print('실행5')
try:    
    #파일 읽기 
    fp = open("./saveFiles/애국가.txt", mode="rt", encoding='utf-8') 
    #파일을 읽기전용으로 오픈
    try:
        while True:
            lines = fp.readlines()
            if not lines: break
            print(lines)
    finally:
        print("예외]더 이상 읽을 내용이 없습니다")
        fp.close()
except IOError: #현재 파일이 없으므로 예외발생됨
    print('예외]파일이 없습니다')
