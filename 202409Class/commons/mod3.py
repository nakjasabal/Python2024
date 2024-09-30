'''
1~10까지의 합의 결과를 출력하는 함수 정의 
단, commons 패키지 내부에 정의되어있다. 
'''
def sum1To10():
	sum = 0
	for i in range(1,11):
		sum += i
	print("1부터 10까지의 합 = ", sum)