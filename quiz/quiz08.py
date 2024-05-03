# 계산 문제를 맞히는 프로그램
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
    r = int(ans)

    if eval(q) == r:
        print("정답입니다.")
        sc1 = sc1 + 1
    else:
        print('오답입니다.')
        sc2 = sc2 + 1
    print()

print('정답:', sc1, "오답:", sc2)

if sc2 == 0:
    print("모든 문제를 맞췄습니다.");
