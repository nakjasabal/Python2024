import sqlite3

conn = sqlite3.connect('biography.db') #sqlite 연결
curs = conn.cursor() #커서생성

#조회1 : 조회된 레코드를 한꺼번에 출력한다.
print(f"{'조회1':-^30}")
curs.execute('select * from people')
print(curs.fetchall())


#조회2 : 조회된 결과를 한 행(row)씩 출력한다. 
print(f"{'조회2':-^30}")
curs.execute('select * from people')
for row in curs.fetchall():
    print(row)


#조회3 : 각 컬럼별로 출력한다.
print(f"{'조회3':-^30}")
curs.execute('select * from people')
for(name, job, pay) in curs.fetchall():
    print(name, ':', job, ':', pay)

