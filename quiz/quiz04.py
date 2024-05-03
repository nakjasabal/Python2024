'''
퀴즈] 1~10사이의 난수를 2개 생성해서 덧셈 문제를 출력하면 사용자가 정답을 맞추는 프로그램을 작성하시오.
    사용자가 종료할때까지 실행을 유지해야 한다. 
'''
from random import randint

while True:
    a = randint(1, 10)
    b = randint(1, 10)
    print(f'{a}+{b}의 정답은?')
    ans = int(input())
    if a+b == ans:
        print('정답입니다.')
    else:
        print('틀렸습니다.')
    
    print('계속할까요?(N:종료, 아무키나 누르면 계속)')
    if input() == 'N':
        print('종료합니다.')
        break
    else:
        print('계속합니다.')
