empty_set = set()
print(empty_set)

even_set = set([0,2,4,6,8])
print(even_set)

odd_set = {1,3,5,7,9,7,5,3,1}
print('중복제거', odd_set)
print('크기', len(odd_set))

myset = {1, 3, 5}

myset.add(7)
print("myset1", myset)

myset.update({4, 6, 8})
print("myset2", myset)

myset.remove(1)
print("myset3", myset)
 
myset.clear()
print("myset4", myset)

# 집합연산
set_a = {1, 3, 5, 7, 9}
set_b = {1, 2, 5}
print("합집합", set_a | set_b) #{1, 2, 3, 5, 7, 9}
print("교집합", set_a & set_b) #{1, 5}
print("차집합", set_a - set_b) #{9, 3, 7}

