'''
집합(Set)
  : 객체를 참조하기 위한 순서가 없는 컬렉션으로 인자를
  쉽게 추가, 삭제할 수 있다. 
  딕셔너리에서 value를 제거하고 key만 남은 상태와 같다. 
  따라서 중괄호로 표현한다. 
  List는 순서를 보장하지만, Set은 순서를 보장하지 않는다. 
'''
#set() 함수를 통해 새로운 set을 생성한다. 
empty_set = set()
print(empty_set)

#set() 인자로 List를 전달하면 set으로 변환할 수 있다.
even_set = set([0,2,4,6,8])
print(even_set)

'''
set은 집합의 특성을 가지므로 순서를 보장하지 않고, 
중복을 허용하지 않는다. 따라서 아래와 같이 동일한 자료가 
있다면 자동으로 중복이 제거된다. 
'''
odd_set = {1,3,5,7,9,7,5,3,1}
print(odd_set)

#새로운 set 생성 후 초기화 
myset = {1, 3, 5}  
#추가 : 새로운 인자 1개를 추가한다. 
myset.add(7)  
print("myset1=", myset)
#추가 : 여러개의 인자를 추가할때 사용한다. 
myset.update({4, 6, 8})  
print("myset2=", myset)
#삭제 : 인자 1개를 삭제한다. 여러개를 삭제할 수 없다. 
myset.remove(1)  
print("myset3=", myset)
#삭제 : set의 전체 인자를 한꺼번에 삭제한다. 
myset.clear() 
print("myset4=", myset)

#집합 연산이 가능하다. 
set_a = {1, 3, 5, 7, 9}
set_b = {1, 2, 5}
print("합집합", set_a | set_b)  
print("교집합", set_a & set_b) 
print("차집합", set_a - set_b) 

