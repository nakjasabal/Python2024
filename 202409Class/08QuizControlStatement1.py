'''
시나리오] 열번 찍어 안넘어가는 나무 없다라는 속담을 while문으로 작성하시오.
'''
# 직접 작성
treeHit = 0 
while treeHit<10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")

# ChatGPT 작성
#2개의 변수 생성 
tree_hits = 0
max_hits = 10
#생성한 변수를 통해 문제의 조건 작성 
while tree_hits < max_hits:
    #변수에 1씩 누적해서 더함 
    tree_hits += 1
    #f-String으로 횟수만큼의 출력 
    print(f"나무를 {tree_hits}번 찍었습니다.")
    #10번의 횟수가 확인되면 결과 출력 
    if tree_hits == max_hits:
        print("나무가 넘어갔습니다!")
        
print("="*30)

'''
시나리오] 하루에 판매할 수 있는 커피는 모두 10잔이다. 
    while문으로 무한루프를 만든 후 10잔의 커피가 모두 판매되었을때 반복문을
    탈출하는 프로그램을 while문으로 작성하시오. 단, break를 사용하시오.
'''
#직접 작성
coffee = 10
while True:
    print('커피 한잔을 판매합니다.')
    coffee -= 1
    print('남은 커피는 %d 입니다.' % coffee)
    if coffee == 0:
        print('커피 재고가 모두 소진되었습니다.(판매중지)')
        break


#ChatGPT 작성
#커피 재고 
coffee_sold = 0
#커피 최대 판매량 
max_coffee = 10
#무한 루프 생성 
while True:
    #커피 한잔 판매 표현 
    coffee_sold += 1
    print(f"커피 {coffee_sold}잔 판매되었습니다.")
    #모든 재고가 소진되면 판매 종료(while문 탈출)
    if coffee_sold == max_coffee:
        print("모든 커피가 판매되었습니다. 판매를 종료합니다.")
        break    

print("="*30)
'''
퀴즈] 로또 번호를 생성하는 프로그램을 while문으로 작성하시오. 1~45 사이에서 중복되지 않는 숫자 6개를 추출하면된다. 
'''
#모듈 임포트 
import random
#새로운 Set을 생성 
lottoNum = set() 
#반복횟수 카운트용 변수 
countNum = 0
#반복의 횟수가 명확하지 않으므로 while문으로 무한루프 구성
while True:
    countNum += 1
    #1~45사이의 난수 생성 
    rndNumber = random.randint(1, 45)
    #생성된 난수는 Set에 저장 
    lottoNum.add(rndNumber)
    #Set은 중복이 자동으로 제거되므로 6개의 숫자가 입력되었는지만
    #확인하면 된다. 확인되면 즉시 무한루프를 탈출한다. 
    if len(lottoNum)==6:
        break;
#번호를 오름차순 정렬하여 출력     
print("이번주 당첨번호:", sorted(lottoNum))
print("반복횟수", countNum)