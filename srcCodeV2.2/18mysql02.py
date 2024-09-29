import pymysql

conn = pymysql.connect(host='localhost', user='sample_user',
        password='1234', db='sample_db', 
        charset='utf8', port=3307)

curs = conn.cursor()
#f-String으로 입력값이 들어가는 부분에 input함수를 사용
sql = f"""INSERT INTO board (title, content, id)
	VALUES ('{input('제목:')}', '{input('내용:')}', '{input(' 아이디:')}')"""
try:    
    #insert 쿼리문 실행 
    curs.execute(sql)
    #행의 변화가 생기는 쿼리문을 실행한 후 반드시 커밋을 실행해야함.
    conn.commit()
    print("1개의 레코드가 입력됨")
except Exception as e:
    #만약 쿼리 실행시 예외가 발생되면 모든 작업을 취소하기 위해
    #롤백을 실행한다. 
    conn.rollback()
    print("쿼리 실행시 오류발생", e)


conn.close()