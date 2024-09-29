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
    except:
        print('ddddd')
    finally:
        print('aaaaaa')
    

    
    