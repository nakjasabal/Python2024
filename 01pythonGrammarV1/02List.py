'''
파일명 : 02List.py

파이썬에는 연속된 collection데이터 구조에
list, tuple, dictionary, set 이 있다. 

리스트(list)
    : 대괄호[] 안에 콤마로 항목을 구분하며, 대입연산자로 항목을 변경할수 있는
    시퀀스 자료형(Mutable 데이타 타입). 서로 다른 자료형의 항목으로 구성할수 있음.
    인덱싱, 슬라이싱, 연결, 반복 등 가능함.
'''
#기본적인 선언과 사용법은 배열과 동일함.
#선언
list1 = [1,2,3,4,5]
list2 = ['Java', 'HTML', 'Python']
list3 = [10, 20, ['Java', 'HTML', 'Python']]
#출력
print('list1:', list1)  #배열전체가 출력됨.
print('list2[2]:', list2[2])  
print('list3[2]:', list3[2]) #리스트내의 리스트가 출력됨. 

#슬라이싱 
print("===슬라이싱", "="*30)
print('list1[1:4];', list1[1:4]) #인덱스 1~3까지 출력
print('list1[:3];', list1[:3]) #0~2까지 출력
print('list1[1:];', list1[1:]) #1~마지막까지 출력

#list간의 연결이 가능함. 리스트내에 또다른 리스트를 삽입함. 
print("===리스트 연결", "="*30)
all_list = [list1, list2]
print('all_list:', all_list)
print('all_list[1][0]:', all_list[1][0]) #Java출력됨.


#list 관련 메소드
print("===list 관련 메소드", "="*30)
list1.append(6) #추가
print('append(6)=>', list1)

list1.clear() #항목 전체 삭제
print('clear()=>', list1)

list1.extend([10, 20, 30, 40, 50]) #리스트 확장
print('extend=>', list1)
list1.insert(1, 99) #지정된 인덱스에 요소 삽입
print('insert=>', list1)

print(list1.pop()) #리스트의 마지막 항목 반환 및 삭제
print('pop()=>', list1)

list1.remove(99) #처음 나오는 항목 99 삭제
print('remove=>', list1)

list1.reverse() #리스트를 뒤집을때 사용
print('reverse()=>', list1)

'''
List Comprehension
    : 대괄호 안에 for루프로 반복적인 표현식을 실행해서
    리스트 요소들을 초기화 하는 방법
    형식]
        [표현식 for 요소 in 컬렉션 [if조건식]]
'''
print("===List Comprehension", "="*30)
#0~9까지의 정수중 3의배수의 제곱으로 이루어진 리스트 초기화
list = [n ** 2 for n in range(10) if n%3==0]
print(list)
