'''
집합(Set)
    : 객체를 참조하기 위한 순서가 없는 collection으로 요소를 
    쉽게 추가/삭제 할수있다.
    딕셔너리에서 value를 제거하고 key만 남은 상태와 동일하다. 
'''
# set() 메소드로 새로운 set을 생성한다. 
empty_set = set()
print(empty_set)

# set()의 인자로 리스트를 전달하여 set으로 변환한다. 
even_set = set([0,2,4,6,8])
print(even_set)

# 생성과 동시에 초기화한다. 이때 중복값은 제거된다. 
# 딕셔너리와 같이 중괄호를 사용한다. 단 value가 없다. 
odd_set = {1,3,5,7,9,7,5,3,1}
print('중복제거:', odd_set)
print('크기:', len(odd_set))

#set에서 추가 및 삭제를 위한 메소드 사용 
myset = {1, 3, 5} # 초기화

myset.add(7) # 인자 추가
print("myset1=", myset)

myset.update({4, 6, 8}) # 여러개의 인자 추가
print("myset2=", myset)

myset.remove(1) # 삭제. 단 여러개 삭제할 수 없음.
print("myset3=", myset)
 
myset.clear() # 인자 한꺼번에 삭제
print("myset4=", myset)

# 집합연산
set_a = {1, 3, 5, 7, 9}
set_b = {1, 2, 5}
print("합집합", set_a | set_b) #{1, 2, 3, 5, 7, 9}
print("교집합", set_a & set_b) #{1, 5}
print("차집합", set_a - set_b) #{9, 3, 7}

