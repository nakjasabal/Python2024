# 타자 게임
import random, time

word = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda',
        'flog', 'snake', 'wolf', 'lion']
n = 1
print('[타자게임] 준비되면 엔터')
input()
start = time.time()
quiz = random.choice(word)
while n <= 5:
    print("문제", n)
    print(quiz)
    answer = input()
    if quiz == answer:
        print('통과')
        n = n + 1
        quiz = random.choice(word)
    else:
        print('오타. 다시 입력.')
end = time.time()
et = end - start
et = format(et, '.2f')

print("타자시간:", et, "초")
