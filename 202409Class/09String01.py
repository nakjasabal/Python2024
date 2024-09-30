'''
f-String
: 출력할 문자열 앞에 접두어 f를 붙이고 변수를 {}로 표현한다. 
형식]
    f'{문자열변수:<길이}'
        < : 좌측정렬
        ^ : 가운데정렬
        > : 우측정렬
        남은 부분은 공백으로 채워진다. 
'''
str = 'coffee'
num = 1
# 문자열 중간에 변수는 중괄호로 표현한다. 
result = f'{str}는 하루에 {num}잔만 마시는게 좋아요'
print(result)

'''
정해진 공간에서 문자열을 정렬하는 기능을 아래와 같이 사용할 수 있다. 
(예제에서 사용한 |는 서식이 아니라 단순히 확보된 공간을 확인하는 
용도로만 사용된다)
'''
s1 = '좌측정렬'
#전체 10칸의 공간을 확보한 후 문자열을 좌측으로 정렬해서 출력 
result1 = f'|{s1:<10}|' 
print(result1)

s2 = '센터정렬'
result2 = f'|{s2:^10}|'
print(result2)

s3 = '우측정렬'
result3 = f'|{s3:>10}|'
print(result3)

#f-String을 통해 딕셔너리 변수 출력. Key를 통해 Value를 출력한다. 
dics = {'name':'성유겸', 'gender':'남자', 'age':10}
result = f'{dics["name"]}은 {dics["gender"]}이고 나이는 {dics["age"]}살이다'
print(result)

#리스트의 경우 인덱스를 통해 접근한다. 
lists = [10, 20, 30]
print(f'리스트 : {lists[0]}, {lists[1]}, {lists[2]}') 
for v in lists:
    print(f'반복출력 : {v}')

