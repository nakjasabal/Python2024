# 업다운 게임

import random

while True:
    print("1~100사이의 숫자를 6회안에 맞추시오")
    comNum = random.randint(1,100)
    print(comNum)
    for i in range(0,7):
        userNum = int(input("숫자를 입력하세요:"))

        if comNum < userNum:
            print(userNum, "=>이보다 작은 숫자입니다.")
        elif comNum > userNum:
            print(userNum, "=>이보다 큰 숫자입니다.")
        elif comNum == userNum:
            print(userNum, "=>정답입니다.")
            break

        if i>=5:
            print("모든 기회를 다 사용했습니다.")
            break
        else:
            print("%d회 시도했습니다." % (i+1))

    str = input("한게임 더 하시겠습니까?(y / n)")
    if str!='y':
        print("안녕히 가세요")
        break

