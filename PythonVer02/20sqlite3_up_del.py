import sqlite3

conn = sqlite3.connect('biography.db') #sqlite 연결
curs = conn.cursor() #커서생성

'''
시나리오] 이름이 '곽재우xx'인 레코드의 급여를 9999로 변경(update)하시오.
'''
#curs.execute("update people set pay=값 where name=값")
curs.execute("update people set pay=? where name=?",
    (9999, '곽재우95'))

'''
시나리오] 급여가 1200인 레코드를 삭제(delete)하시오.
'''    
curs.execute("delete from people where pay=?", (1200,))

# 변경된 레코드가 있으면 반드시 커밋해서 테이블에 적용한다. 
conn.commit() 
print('레코드 update/delete 및 commit 완료')