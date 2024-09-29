import random

# 게임 초기화
target_number = random.randint(1, 50)
attempts_left = 7

print("1부터 50까지의 숫자 중 하나를 맞춰보세요.")
print("기회는 7번 주어집니다.")

# 메인 게임 루프
while attempts_left > 0:
    guess = int(input("추측한 숫자를 입력하세요: "))

    if guess == target_number:
        print("축하합니다! 숫자를 맞추셨습니다.")
        break
    elif guess < target_number:
        print("업! 더 큰 숫자를 입력하세요.")
    else:
        print("다운! 더 작은 숫자를 입력하세요.")

    attempts_left -= 1
    print("남은 기회:", attempts_left)

if attempts_left == 0:
    print("게임 오버! 정답은", target_number, "입니다.")
