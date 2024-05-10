'''
채우기와 정렬
    형식]
        '{인덱스:<길이}'.format(값)
    
    < : 좌측정렬
    > : 우측정렬
    ^ : 센터정렬
    남은 공간은 공백으로 채운다. 
'''

str = 'coffee'
num = 1
# f를 제일앞에 붙히고, 표현할 변수를 중괄호를 이용해서 삽입한다. 
result = f'{str}는 하루에 {num}잔만 마시는게 좋아요'
print(result)

# 출력 범위 지정후 정렬
str = '문자열처리'
result1 = f'{str:<10}' 
print(result1)
result2 = f'{str:^10}'
print(result2)
result3 = f'{str:>10}'
print(result3)

# 출력 범위내 정렬 및 문자채우기
result4 = f'{str:-^50}'
print(result4)

# 딕셔너리 사용
dics = {'name':'성유겸', 'gender':'남자', 'age':10}
result = f'{dics["name"]}은 {dics["gender"]}이고 나이는 {dics["age"]}살이다'
print(result)

# 리스트 사용
lists = [10, 20, 30]
print(f'리스트 : {lists[0]}, {lists[1]}, {lists[2]}') 
for v in lists:
    print(f'반복출력 : {v}')



