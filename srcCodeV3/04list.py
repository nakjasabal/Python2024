import random
rndNum = random.randint(6,10) 

#선언
list1 = [1,2,3,4,5,rndNum] 
list2 = ['Java', 'HTML', 'Python']
list3 = [10, 20, ['Java', 'HTML', 'Python']]

#출력
print('list1', list1) 
print('list2[2]', list2[2])  
print('list3[2]', list3[2]) 

#슬라이싱 
print(f"{'슬라이싱':-^30}")
print('list1[1:4]', list1[1:4])  
print('list1[:3]', list1[:3]) 
print('list1[1:]', list1[1:]) 

print(f"{'리스트 연결':-^30}")
all_list = [list1, list2]
print('all_list', all_list)
print('all_list[1][0]', all_list[1][0])

#list 관련 메소드
print(f"{'list 관련 메소드':-^30}")
rndNum = random.randint(11,20)
list1.append(rndNum)
print(f'append({rndNum})', list1)

list1.clear()
print('clear()', list1)

list1.extend([10, 20, 30, 40, 50])
print('extend()', list1)
list1.insert(1, 99)
print('insert()', list1)

print(list1.pop()) 
print('pop()', list1)

list1.remove(99) 
print('remove()', list1)

list1.reverse() 
print('reverse()', list1)

del list1[0]
print('0번항목삭제후', list1)



