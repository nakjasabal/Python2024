'''
퀴즈] 정수의 사칙연산 문제를 랜덤하게 생성하여 맞추는 프로그램을 작성하시오.
-총 5회 반복한다.
-문제가 출제되면 정답을 입력한다. 
-오답인 경우에는 해답을 같이 출력한다. 
'''
import random

def make_question():
    n1 = random.randint(1, 40)
    n2 = random.randint(1, 40)
    o_arr = ['+', '-', '*', '/']
    o_str = o_arr[random.randint(0, 3)]

    quiz = str(n1) + o_str + str(n2)
    return quiz


# 정답과 오답횟수
sc1 = 0
sc2 = 0
for x in range(5):
    q = make_question()
    print("문제:" + q, end=" ")
    ans = input("답:")
    r = float(ans)

    if eval(q) == r:
        print("정답입니다.")
        sc1 = sc1 + 1
    else:
        print('오답입니다.')
        print(f'정답은:{eval(q)}')
        sc2 = sc2 + 1
    print()

print('정답:', sc1, "오답:", sc2)

if sc2 == 0:
    print("모든 문제를 맞췄습니다.");
