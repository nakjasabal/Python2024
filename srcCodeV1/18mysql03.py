import pymysql

conn = pymysql.connect(host='localhost', user='sample_user',
            password='1234', db='sample_db', charset='utf8')

curs = conn.cursor()

# 긴 문자열 처리시 인덱스를 활용하여 인파라미터를 설정한다. 
sql = """update board 
            set title='{1}', content='{2}'
            where num={0}
        """.format(input('수정할일련번호:'), input('제목:'), input('내용:'))
try:    
    curs.execute(sql)
    # DB에 변경사항을 적용한다.
    conn.commit()
    print("1개의 레코드가 수정됨")
except Exception as e:
    #오류가 발생하면 롤백한다.
    conn.rollback()
    print("쿼리 실행시 오류발생", e)


conn.close()