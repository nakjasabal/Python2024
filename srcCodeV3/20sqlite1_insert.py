import sqlite3
import random 

conn = sqlite3.connect('./saveFiles/biography.db')  
curs = conn.cursor()  
rnd = random.randint(0,100);

#테이블생성. 
try:
    tblcmd = 'create table people (name char, job char, pay int)'
    curs.execute(tblcmd)  
except Exception as e:
    print("[예외발생]테이블은 이미 생성되었습니다.", e)

#레코드 1개 삽입. 
curs.execute('insert into people values (?,?,?)', (f'이순신{rnd}','장군',500))

#레코드 2개이상 삽입
curs.executemany('insert into people values (?,?,?)', 
		[(f'강감찬{rnd}','장군',700), (f'홍길동{rnd}','의적',800)])

#for문을 이용한 삽입
rows = [[f'곽재우{rnd}','의병',1100], [f'유성룡{rnd}','재상',1200], [f'임꺽정{rnd}','의적',1500]]
for row in rows :
    curs.execute('insert into people values (?,?,?)', row)

conn.commit()
print('레코드 insert 및 commit 완료')

