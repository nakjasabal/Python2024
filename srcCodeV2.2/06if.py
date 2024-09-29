'''
if문의 형식1
    if 조건식:
        조건이 참일때 실행문장

형식2
    if 조건식:
        참일때 실행문장
    else 
        거짓일때 실행문장
        
형식3
    if 조건식1:
        조건1이 참일때 실행문장
    elif 조건식2:
        조건2가 참일때 실행문장
    else:
        위 조건에 모두 만족하지 않을때 실행문장
※단 else에는 조건식이 들어가면 에러가 발생하니 주의해야한다. 
'''

age = 33
#print문 사용시 줄바꿈없이 출력하고 싶다면 end=''을 사용한다. 
print(age, "살은 ", end="")
if age >= 35: #조건이 False이므로 실행안됨
    print("중년입니다.")
elif age >= 30: #True이므로 여기 문장 실행됨
    print("중년의 시작입니다.")  
else: #위에서 이미 실행되었므로 if문을 탈출함 
    print("청년입니다.")
print("==========================")

'''
input() : 이 함수는 사용자로부터 새로운 입력값을 받을때 사용한다. 
    실행이 잠깐 중지되고, 입력을 받을때까지 대기한다.
int() : 특정 데이터를 정수로 변경하고 싶을때 사용한다. 
'''
num1 = int(input("숫자 하나를 입력하세요 : "))
#num1이 2의 배수라면(2로 나누어 떨어진다면) if문으로 진입한다. 
if num1%2==0:
    if num1%3==0:
        print("2와 3으로 나누어짐")
    else:
        print("2는 가능, 3은 불가")
#num1이 2의 배수가 아니라면 else문으로 진입한다.         
else:
    if num1%3==0:
        print("2는 불가, 3은 가능")
    else:
        print("2와 3 모두 불가")
print("==========================")


print('====논리연산자와 if문====')
'''
논리And는 두 조건이 모두 True일때만 True를 반환한다. 
만약 하나라도 False가 포함되면 False를 반환한다. 
'''
if True and True:
    print("모두 참 입니다");
if False and True:
    print("둘 중 하나가 False이므로 False입니다.");
if False and False:
    print("역시나 False입니다.");

'''
논리Or는 둘중 하나만 True이면 True를 반환한다. 
둘다 모두 False일때만 False를 반환한다. 
'''
print(True or True) #참
print(False or True) #참
print(False or False) #거짓 

#논리연산자는 아래와 같이 2개 이상의 비교연산에서 사용된다. 
print(not 10 > 5) #거짓
print(10==10 and 10!=5) #참
print(10>5 or 10<3) #참




'''
연습문제1] 국,영,수 점수를 입력받아 평균값을 구하고 이를 통해 학점을 출력하는 
    프로그램을 작성하시오. 
    90점 이상은 A학점 
    80점 이상은 B학점
    70점 이상은 C학점
    60점 이상은 D학점    
    60점 미만은 F학점으로 판단하여 출력합니다. 
'''
# 점수를 입력받음
kor = int(input('국어점수:'))
eng = int(input('영어점수:'))
math = int(input('수학점수:'))

# 평균값을 구함(세과목 점수의 합을 3으로 나눈다)
avg = (kor + eng + math) / 3
print('평균점수는:', avg)
#계산된 평균점수로 학점의 구간을 나눠준다. 
if avg>=90 :
    print("A학점입니다.")
elif avg>=80 :
    print("B학점입니다.")
elif avg>=70 :
    print("C학점입니다.")
elif avg>=60 :
    print("D학점입니다.")
else:
    print("F학점입니다. 학사경고ㅜㅜ")

print("잘못된 조건의 if문")
'''
학점의 구간을 아래와 같이 설정하면 높은 점수라도 모두 60점이상에는
만족하므로 잘못된 결과가 출력된다. 
따라서 다중 if문을 사용할때는 주의해야한다. 
'''
if avg>=60 :
    print("D학점입니다.")
elif avg>=70 :
    print("C학점입니다.")
elif avg>=80 :
    print("B학점입니다.")
elif avg>=90 :
    print("A학점입니다.")
else:
    print("F학점입니다. 학사경고ㅜㅜ")        