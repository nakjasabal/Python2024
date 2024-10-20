'''
파일명 : 02List.py

파이썬에서는 2개 이상의 자료를 저장할 수 있는 컬렉션(집합자료형)에
List, Tuple, Dictionary, Set 4가지가 있다. 
 
List(리스트) 
    : 대괄호 [] 안에 콤마로 요소를 표현한다. 
    대입연산자로 항목을 변경할 수 있는 시퀀스(순서가 있는) 자료형.
    다른 자료형의 데이터로도 구성할 수 있다. 
    인덱싱, 슬라이싱, 연결, 반복 등이 가능하다. 
    Mutable 데이터 타입, 즉 변경이 가능한 데이터이다. 
'''
#정수형 리스트 선언 
list1 = [1,2,3,4,5]
#String(문자열)형 리스트 선언 
list2 = ['Java', 'HTML', 'Python']
#중첩된 리스트 선언 
list3 = [10, 20, ['Java', 'HTML', 'Python']]

#인덱스를 지정하지 않았으므로 리스트 전체를 출력한다. 
print('list1:', list1)  
#인덱스 2를 지정했으므로 'Python' 출력됨 
print('list2[2]:', list2[2])  
#인덱스 2를 지정했으므로 리스트안의 리스트를 출력함 
print('list3[2]:', list3[2])  

print("===슬라이싱", "="*30)
#1~3번 인덱스까지 슬라이싱 : 2,3,4 출력 
print('list1[1:4]:', list1[1:4]) 
#0~2번 인덱스까지 슬라이싱 : 1,2,3 출력 
print('list1[:3]:', list1[:3]) 
#1~마지막 인덱스 까지 : 2,3,4,5 출력 
print('list1[1:]:', list1[1:]) 

'''
'슬라이싱'의 경우 인덱스의 범위를 벗어나도 에러가 발생하지 않는다. 
리스트의 마지막 요소까지만 출력된다. 
하지만 '인덱싱'의 경우 인덱스를 벗어나면 에러가 발생한다. 
index out of range라는 오류가 발생하고 실행은 중단된다. 
'''
print('list2[:6]:', list2[:6])
#print('list2[6]:', list2[6]) <- 이부분은 에러이므로 주석처리 

 
print("===리스트 연결", "="*30)
#리스트내에 또다른 리스트를 삽입하여 연결하는 형태로 사용가능 
all_list = [list1, list2]
#2개의 리스트가 1개의 리스트로 합쳐진 중첩된 구조를 가짐 
print('all_list:', all_list)
#'Java' 가 출력됨 
print('all_list[1][0]:', all_list[1][0]) 


print("===list 관련 메소드", "="*30)
# 요소 추가 : 리스트의 마지막 부분에 요소를 추가한다. 
list1.append(6) 
print('append(6)=>', list1)

# 항목 전체 삭제
list1.clear()  
print('clear()=>', list1)

# 리스트 확장 : 인수로 주어진 데이터를 통해 확장한다.
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



'''
List Comprehension
    : 대괄호 안에 for문으로 반복적인 표현식을 실행해서 리스트 
    원소들을 초기화하는 방식이다. 
    형식]
        [표현식 for 원소 in 컬렉션 [if조건식]]
'''
print("===List Comprehension", "="*30)
'''
    표현식(n의제곱) 반복문(0~9까지반복) 조건식(3의배수)
    => 0~9까지의 정수 중 3의 배수인것만 찾아 제곱한 후 리스트를
    초기화한다. 
'''
list = [n ** 2 for n in range(10) if n%3==0]
print(list)
