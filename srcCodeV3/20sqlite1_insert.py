import sqlite3
import random 

conn = sqlite3.connect('./saveFiles/biography.db') #sqlite 연결
curs = conn.cursor() #커서생성
rnd = random.randint(0,100);

#테이블생성. 이미 생성된 경우에는 오류발생됨.
#따라서 두번째 실행에서는 예외처리를 하지않으면 실행중지됨.
try:
    tblcmd = 'create table people (name char, job char, pay int)'
    curs.execute(tblcmd) #쿼리실행
except Exception as e:
    print("[예외발생]테이블은 이미 생성되었습니다.", e)

#레코드 1개 삽입. 튜플을 사용하여 인파라미터를 설정한다.
curs.execute('insert into people values (?,?,?)', (f'이순신{rnd}','장군',500))

#레코드 2개 이상을 삽입할때는 list를 사용한다. 
curs.executemany('insert into people values (?,?,?)', 
		[(f'강감찬{rnd}','장군',700), (f'홍길동{rnd}','의적',800)])

#for문을 이용한 삽입
rows = [[f'곽재우{rnd}','의병',1100], [f'유성룡{rnd}','재상',1200], [f'임꺽정{rnd}','의적',1500]]
for row in rows :
    curs.execute('insert into people values (?,?,?)', row)

conn.commit() #커밋
print('레코드 insert 및 commit 완료')
