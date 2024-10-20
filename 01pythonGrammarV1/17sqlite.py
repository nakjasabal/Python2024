import sqlite3

conn = sqlite3.connect('./saveFiles/myPeoples.db')
curs = conn.cursor()

try:
    tblcmd = 'create table people (name char, job char, pay int)'
    curs.execute(tblcmd)  
except Exception as e:
    print("[예외발생]테이블은 이미 생성되었습니다.", e)

#레코드 삽입
curs.execute('insert into people values (?,?,?)', ('이순신','장군',500))

curs.executemany('insert into people values (?,?,?)', 
		[('강감찬','장군',700), ('홍길동','의적',800)])

rows = [
    ['곽재우','의병',1100],
    ['유성룡','재상',1200],
    ['임꺽정','의적',1500]
]
for row in rows :
    curs.execute('insert into people values (?,?,?)', row)

conn.commit() 

##레코드 조회
curs.execute('select * from people')
print(curs.fetchall())
print('---------------------------------')

curs.execute('select * from people')
for row in curs.fetchall():
    print(row)
print('---------------------------------')

curs.execute('select * from people')
for(name, job, pay) in curs.fetchall():
    print(name, ':', job, ':', pay)
print('---------------------------------')

'''
퀴즈] 이름이 '강감찬'인 레코드의 급여를 9999로 변경하시오.
'''
#curs.execute("update people set pay=값 where name=값")
curs.execute("update people set pay=? where name=?",
             (9999, '강감찬'))

'''
퀴즈] 급여가 1200인 레코드를 삭제하시오.
'''    
curs.execute("delete from people where pay=?", (1200,))

conn.commit()

##레코드 조회
curs.execute('select * from people')
print(curs.fetchall())

