'''
파일명 : 03Tuple.py

튜플(Tuple)
    : 소괄호() 안에 콤마로 구분된 항목들이 나열되어 표현되는 시퀀스 자료형.
    서로다른 자료형으로 구성할수 있지만, 대입연산자로 튜플의 항목을
    변경할 수 없는 Immutable 데이타 타입.
'''
tu1 = tuple()  #빈 튜플 생성
tu2 = (1, 2, 3, 4, 5) 
#1개의 항목을 갖는 튜플생성. 뒤에 컴마가 없으면 단순한 변수생성.
tu3 = 1,  # 즉, 소괄호 생략가능.
tu4 = (98, 99, 100)
print(tu1, tu2, tu3)

#인덱싱, 슬라이싱
print(f"{'인덱싱/슬라이싱':-^30}")
print("tu2[0]", tu2[0]) 
print("tu2[-1]", tu2[-1]) #마지막 항목을 출력함.
print("tu2[1:3]", tu2[1:3]) #인덱스1~2까지 출력됨.

#해당 요소가 포함되었는지 확인
print(f"{'포함여부확인':-^30}")
print("4 in tu2", 4 in tu2) # 4가 포함되었으므로 true
print("99 not in tu2", 99 not in tu2) # 99가 포함되지 않았으므로 true

#튜플을 반복해서 출력
print(f"{'반복출력':-^30}")
print("tu2 * 3", tu2 * 3) 

#튜플 병합 : 2개의 튜플을 하나로 합침.
print(f"{'병합':-^30}")
new_tu = tu2 + tu4
print("new_tu", new_tu)

#tuple과 list간 변환할때 사용.
print(f"{'튜플과 리스트 변환':-^30}")
my_list = [1, 2, 3]
my_tuple = ('x', 'y', 'z')
print(tuple(my_list))
print(list(my_tuple))