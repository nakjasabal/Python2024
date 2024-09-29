#sqlite를 사용하기 위한 모듈 임포트 
import sqlite3
'''파일형태로 존재하는 dbase1에 연결한다. 최초 실행이라면 파일이
새롭게 생성된다. 이 파일이 데이터베이스의 역할을 하게된다. '''
conn = sqlite3.connect('dbase1')  
'''연결이 되었다면 DB작업을 위해 커서를 생성한다. 이를 통해 입력,
수정, 삭제와 같은 데이터베이스 작업을 수행할 수 있다. '''
curs = conn.cursor()  


'''
people 테이블을 새롭게 생성한다. 
형식] create table 테이블명 (컬럼명 자료형, ... )
'''
# tblcmd = 'create table people (name char, job char, pay int)'
# #쿼리문 실행 
# curs.execute(tblcmd)  

try:
    tblcmd = 'create table people (name char, job char, pay int)'
    curs.execute(tblcmd)  
except Exception as e:
    print("[예외발생]테이블은 이미 생성되었습니다.", e)

'''
레코드 삽입
방법1 : 한개의 레코드를 삽입한다. 튜플을 이용해서 인파라미터를 설정한다.
'insert into 테이블명 values (?,?,?)', (값1, 값2, 값3)
'''
curs.execute('insert into people values (?,?,?)', ('이순신','장군',500))

'''
방법2 : 2개 이상의 레코드를 삽입할때는 List를 사용한다. 
    List에 포함된 2개의 튜플이 순서대로 인파라미터를 설정한다. 
    여기서 사용하는 함수명은 executemany 이다. 
'''
curs.executemany('insert into people values (?,?,?)', 
		[('강감찬','장군',700), ('홍길동','의적',800)])

'''
방법3 : for문을 이용해서 반복적으로 삽입한다. 
'''
rows = [['곽재우','의병',1100],['유성룡','재상',1200],['임꺽정','의적',1500]]
#매회차 반복에서는 하나의 List가 반환된다. 
for row in rows :
    curs.execute('insert into people values (?,?,?)', row)

#데이터의 변화(입력 혹은 수정, 삭제)가 생기면 반드시 커밋해야한다.
conn.commit() 

'''
레코드 조회하기
조회1 : 조회된 레코드를 한꺼번에 출력한다. 
'''
curs.execute('select * from people')
print(curs.fetchall())
print('---------------------------------')

#조회2 : 조회된 결과를 한 행(row)씩 출력한다. 
curs.execute('select * from people')
for row in curs.fetchall():
    print(row)
print('---------------------------------')

#조회3 : 각 컬럼별로 출력한다. 
curs.execute('select * from people')
for(name, job, pay) in curs.fetchall():
    print(name, ':', job, ':', pay)



# '''
# 연습문제] 이름이 '강감찬'인 레코드의 급여를 9999로 변경하시오.
# '''
# #curs.execute("update people set pay=값 where name=값")
# curs.execute("update people set pay=? where name=?",
#              (9999, '강감찬'))

# '''
# 연습문제] 급여가 1200인 레코드를 삭제하시오.
# '''    
# curs.execute("delete from people where pay=?", (1200,))

# # 변경된 레코드가 있으면 반드시 커밋해서 테이블에 적용한다. 
# conn.commit() 