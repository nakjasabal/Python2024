'''
파이썬에서는 2개 이상의 자료를 저장할 수 있는 컬렉션(집합자료형)에
List, Tuple, Dictionary, Set 4가지가 있다. 

List(리스트)
-대괄호 [] 안에 콤마로 요소를 표현
-대입연산자로 항목을 변경할 수 있는 시퀀스(순서가있는) 자료형
-서로 다른 자료형의 데이터로도 구성 가능
-인덱싱, 슬라이싱, 연결, 반복 등의 연산 가능 
-Mutable 데이터 타입. 즉 변경 가능한 데이터이다. 
'''
#정수형 리스트 선언
list1 = [1,2,3,4,5]
#문자형(String) 리스트 선언 
list2 = ['Java', 'HTML', 'Python']
#중첩된 리스트 선언 
list3 = [10, 20, ['Java', 'HTML', 'Python']]

#인덱스 지정이 없으므로 리스트 전체를 출력 
print('list1:', list1)  
#2번 인덱스이므로 'Python' 출력
print('list2[2]:', list2[2])  
#2번 인덱스이므로 리스트 내부의 리스트를 출력 
print('list3[2]:', list3[2])  

'''
"슬라이싱"의 경우 인덱스의 범위를 벗어나도 에러가 발생하지 않는다. 
리스트의 마지막 요소까지만 출력된다. 
하지만 "인덱싱"의 경우 인덱스를 벗어나면 에러가 발생한다. 
'''
print('list2[:6]:', list2[:6]) 
#print('list2[6]:', list2[6]) <- 이 부분은 에러이므로 주석처리 


print("===슬라이싱", "="*30)
#1~3번 인덱스까지 슬라이싱 : 2,3,4 출력
print('list1[1:4]:', list1[1:4]) 
#0~2까지
print('list1[:3]:', list1[:3]) 
#1~마지막까지 
print('list1[1:]:', list1[1:]) 
 

print("===리스트 연결", "="*30)
#리스트내에 또다른 리스트를 삽입하여 연결하는 형태로 사용 가능 
all_list = [list1, list2]
#2개의 리스트가 1개의 리스트로 합쳐진 중첩된 구조를 가짐 
print('all_list:', all_list)
#'java' 출력됨 
print('all_list[1][0]:', all_list[1][0]) 


print("===list 관련 메소드", "="*30)
#요소 추가 : 리스트의 마지막 부분에 요소 추가 
list1.append(6) 
print('append(6)=>', list1)

#항목 전체 삭제
list1.clear()  
print('clear()=>', list1)

#리스트 확장 : 인수로 주어진 데이터를 통해 확장한다. 
list1.extend([10, 20, 30, 40, 50])  
print('extend=>', list1)

#삽입 : 1번 인덱스에 99를 삽입한다. 
list1.insert(1, 99)  
print('insert=>', list1)

#삭제 및 반환 : 리스트의 마지막 요소를 삭제한 후 반환한다. 
print(list1.pop())  
print('pop()=>', list1)

#삭제 : 처음 나오는 요소 99를 삭제한다. 
list1.remove(99)  
print('remove=>', list1)

#리스트 뒤집기 
list1.reverse()  
print('reverse()=>', list1)

