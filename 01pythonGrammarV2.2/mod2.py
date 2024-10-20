#곱셈, 나눗셈을 위한 함수 선언 
def mul(a, b):
    return a * b
def div(a, b): 
    return a / b

'''
__name__ 변수란?
    : 파이썬의 __name__은 내부적으로 사용하는 특별한 변수명이다.
    만약 콘솔에서 직접 mod2.py를 실행하면 해당 변수에 __main__이
    저장된다. 하지만 import하는 경우에는 모듈 이름인 mod2가 
    저장된다. 
    즉 해당 모듈이 직접 실행되는지 임포트되어 실행되는지 구분하기 
    위해 사용된다.
'''
#이 파일을 직접 실행하면 아래 부분이 출력된다. 
if __name__ == "__main__":
    print("==여긴 mod2.py==")
    print(mul(1, 4))
    print(div(4, 2))