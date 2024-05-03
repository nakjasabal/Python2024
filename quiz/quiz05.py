'''
퀴즈] 업다운 게임을 다음 조건에 맞게 구현하시오.
    -컴퓨터는 1~50사이의 난수를 생성한다. 
    -기회는 7번이 주어진다. 
    -횟수내 맞추면 승리, 틀리면 패배로 판단한다. 
    -게임이 종료되면 재시작할지 물어본다. 
    -y는 재시작, n은 프로그램종료
'''
import random

while True:
    print("1~50사이의 숫자를 7회안에 맞추시오")
    comNum = random.randint(1,50)
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

        if i>=6:
            print("모든 기회를 다 사용했습니다.")
            break
        else:
            print("%d회 시도했습니다." % (i+1))

    str = input("한게임 더 하시겠습니까?(y / n)")
    if str!='y':
        print("안녕히 가세요")
        break

