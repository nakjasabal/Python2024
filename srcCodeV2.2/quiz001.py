#교제 2장 연습문제
'''
1번 : 다음 조건에 맞게 수량과 단가변수를 만들어서 금액을 출력하시오.
'''
su = 5
dan = 800
total = su * dan
print('수량', su)
print("단가", dan)
print('합계금액', su * dan)


'''
2번 : 2차방정식을 파이썬 수식으로 코딩하고 y의 결과를 확인
'''
x = 2
y = 2.5 * x**2 + 3.3 * x + 6
print('2차방정식 결과', y)


'''
3번 : 지방, 탄수화물, 단백질 칼로리의 합계를 계산하는 프로그램 작성
'''
print('지방, 탄수화물, 단백질을 순서대로 입력하세요')
'''input() 함수를 통해 입력받는 값은 문자열로 인식하므로 산술연산을
위해서는 반드시 정수형으로 변환해야한다. '''
fat = int(input('지방:'))
carb = int(input('탄수화물:'))
prot = int(input('단백질:'))
result = fat*9 + carb*4 + prot*4
print('총 칼로리:', result)


'''
4번 : 3개의 단어를 키보드로 입력받아서 첫글자를 추출하여 단어의 
약자를 출력하시오.
'''
word1 = input('첫번째단어:')
word2 = input('두번째단어:')
word3 = input('세번째단어:')
myStr = f'{word1[0]}{word2[0]}{word3[0]}'
print('첫글자추출', myStr)



