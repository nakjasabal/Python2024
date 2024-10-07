#대입 연산자
a = tot = 10

#복합 대입 연산자
a += 1
tot += a
print(a, tot)

v1, v2 = 100, 200
v2, v1 = v1, v2
print('변수교체', v1, v2)

mylist = [1,2,3,4,5]
x1, *x2 = mylist
print('패킹연산자1', x1, x2)

*y1, y2 = mylist
print('패킹연산자2', y1, y2)


