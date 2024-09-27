'''
반복문1
    : 반복의 횟수가 명확하지 않은 경우 주로 사용하는 반복문으로
    반복을 위한 초기값, 조건식, 증감식이 분리되어있는 형태이다. 
    다른 언어와 다른 2가지 특징이 있는데  
        첫째 do~while문이 없다는것과
        둘째 else를 사용할 수 있다는것이다. 
''' 

'''
str이 공백이 될때까지 반복한다. 파이썬에서는 문자열을 List와
같이 인덱스로 접근할 수 있으므로 아래의 조건은 True가된다. 
'''
str = 'python'
#문자열의 길이만큼 반복 
while str: 
    #출력문 끝에 스페이스를 추가하여 출바꿈없이 출력 
    print(str, end=' ')
    '''슬라이싱을 통해 1번 인덱스부터 마지막까지를 잘라낸다. 
    즉, 첫번째 문자를 하나씩 제거한다. '''
    str = str[1:] 
#python부터 마지막 n까지 출력한 후 while문을 탈출한다.     
print()
print("=========================="*3)

# 시나리오] 1~10까지의 합을 구하시오.
#누적해서 1부터 덧셈을 위한 변수 
sum = 0
#while문의 조건식에 사용할 변수 
i = 1
#변수 i를 통해 조건을 확인한 후 while문으로 진입 
while i<=10 :
    '''복합대입 연산자를 사용하면 좌우측항의 변수를 연산한 후 
    좌측항으로 결과를 대입한다. 즉 좌측항의 변수에 모든 연산결과가
    누적해서 대입된다. '''
    sum += i
    '''1부터 10까지의 합산 과정을 보여주기 위해 i가 10미만일때는
    +기로를 출력하고 마지막에 =을 출력한다. '''  
    if i<10:
        print(i, end=" + ")
    else:
        print(i, end=" = ")
    #i값을 증가시켜 10보다 큰 조건이 되어야 while문을 탈출할 수 있다. 
    i += 1 
else:
    #while문을 탈출하면 else로 진입해서 결과를 출력한다. 
    print(sum)
'''
if문과 마찬가지로 else구문은 필수사항은 아니다. 따라서 필요한 
경우에만 추가해주면 된다. 
'''    
    


print("=========================="*3)
# 시나리오] 구구단을 출력하되 짝수단만 출력하시오
#단에 해당하는 변수는 2~9단까지 증가 
dan = 2
while dan<=9 : #9단까지 반복    
    if dan%2 == 1: 
        '''dan을 2로 나눈 나머지가 1이라면 홀수를 의미하므로 1을 
        더한 후 반복문의 처음으로 돌아간다. 
        반복문 안에서 continue를 만나면 실행이 중지된 후 반복문의 
        처음으로 돌아가게된다. '''
        dan += 1
        continue
    else:
        '''dan이 짝수라면 출력을 위해 su를 1로 초기화한 후 9까지
        반복해서 출력한다. '''
        su = 1
        while su<=9: 
            '''서식문자 %d는 정수를 출력할때 사용한다. 사이에 숫자를
            추가하면 공간을 미리 확보한 후 우측정렬해서 출력한다. '''
            print("%d*%d=%d" % (dan, su, su*dan), end=' ')
            su += 1  
    dan += 1 
    #하나의 단을 모두 출력한 후 다음 단 출력을 위해 줄바꿈한다. 
    print()  
print()

'''
퀴즈] 1~100까지의 정수 중 짝수의 합을 계산해서 출력할 수 있는 
프로그램을 while문으로 작성하시오. 
'''
x = 1 
total = 0
while x<=100:
    #print(x)
    if x%2==0: #x가 2의배수 즉 짝수일때만 누적해서 더한다. 
        total += x #증가하는 x를 누적해서 더해준다. 
    x += 1
print("1~100까지의 짝수 합", total)