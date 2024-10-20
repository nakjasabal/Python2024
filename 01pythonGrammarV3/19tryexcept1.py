def calc(val):
    sum = None
    try:  
        sum = val[0] + val[1] + val[2]
        if val[0]==100:
            print(no_var)
        elif val[0]==55:
            result = val[0] / 0
            print("결과", result)
    except IndexError:
        print('리스트의 인덱스에 에러가 있습니다')
    except NameError as err:         
        print('선언되지 않은 변수를 사용하였습니다', str(err)) 
    except:         
        print('예외가 발생하였습니다')
    else: 
        print('에러없음^^') 
    finally: 
        print('sum', sum) 
print('실행1')
calc([1, 2, 3]) #정상실행
print('실행2')
calc([10, 20]) #인덱스 에러
print('실행3')
calc([100,101,102,103]) #NameError 발생
print('실행4')
calc([55,56,57]) #ZeroDivisionError


#중첩된 예외처리
print('실행5')
try:    
    fp = open("./saveFiles/애국가.txt", mode="rt", encoding='utf-8') 
    try:
        while True:
            lines = fp.readlines()
            if not lines: break
            print(lines)
    finally:
        print("예외]더 이상 읽을 내용이 없습니다")
        fp.close()
except IOError: 
    print('예외]파일이 없습니다')
