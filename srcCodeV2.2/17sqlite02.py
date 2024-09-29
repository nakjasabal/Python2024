import sqlite3
conn = sqlite3.connect('dbase1')  
curs = conn.cursor()  

'''
레코드 수정하기
형식] update 테이블명 set 수정할컬럼=값, ... where 조건 
'''
sql01 = "update people set job='가수' where name='홍길동'"
curs.execute(sql01)

sql02 = "update people set name='이정후^^' where job='장군'"
curs.execute(sql02)

#레코드 조회하기 
curs.execute('select * from people')
for row in curs.fetchall():
    print(row)
print('---------------------------------')


'''
레코드 삭제하기
형식] delete from 테이블명 where 조건
'''
sql03 = "delete from people where job='의적'"
curs.execute(sql03)

sql04 = "delete from people where pay=1100"
curs.execute(sql04)

#레코드 조회하기 
curs.execute('select * from people')
for row in curs.fetchall():
    print(row)
print('---------------------------------')

# 변경된 레코드가 있으면 반드시 커밋해서 테이블에 적용한다. 
conn.commit() 