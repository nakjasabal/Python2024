import pymysql

#MariaDB연결 및 커서생성 
conn = pymysql.connect(host='localhost', user='sample_user',
        password='1234', db='sample_db', 
        charset='utf8', port=3307)
curs = conn.cursor()

#update쿼리문 작성. format함수로 인덱스에 해당하는 파라미터 입력 
sql = """update board 
    set title='{1}', content='{2}'
    where num={0}
""".format(input('수정할일련번호:'), input('제목:'), input('내용:'))
try:   
    #쿼리문 실행 및 커밋  
    curs.execute(sql)
    conn.commit()
    print("1개의 레코드가 수정됨")
except Exception as e:
    conn.rollback()
    print("쿼리 실행시 오류발생", e)


conn.close()