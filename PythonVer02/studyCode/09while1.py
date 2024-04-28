'''
반복문 
    : 파이썬에서의 반복문은 while문과 for문만 있다.
    do~while문은 없다. 
    형식]
        초기값;
        while 조건문:
            수행할문장;
            증감식;
'''

'''
시나리오] 열번 찍어 안넘어가는 나무 없다라는 속담을 while문으로 구현하시오.
'''
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")

print("="*30)

str = 'python'
# str이 공백이 될때까지 반복한다. 공백이 아니면 true
while str: 
    # 출력문 끝에 공백을 추가하여 줄바꿈없이 출력한다.
    print(str, end=' ')
    '''
    문자열에서 첫글자를 제거한 후 대입한다. 
    인덱스 1부터 끝까지 슬라이싱 한다. 
    '''
    str = str[1:] 

print()
print("="*30)

# 시나리오] 1~10까지의 합을 구하시오.
'''
python에서는 while문에 else를 추가할수 있다. 
while문의 조건에 위배되어 탈출하면 else구문이 실행된다.
'''
sum = 0
i = 1
while i<=10 :
    sum += i
    if i<10:
        print(i, end=" + ")
    else:
        print(i, end=" = ")
    i += 1
else:
    #while문을 벗어나면 실행됨
    print(sum)

print()
print("="*30)

'''
시나리오] 하루에 판매할 수 있는 커피는 모두 10잔이다. 
    while문으로 무한루프를 만든 후 10잔의 커피가 모두 판매되었을때 반복문을
    탈출하는 프로그램을 작성하시오. 단, break를 사용하시오.
'''
coffee = 10
while True:
    print("커피 한잔을 판매합니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
