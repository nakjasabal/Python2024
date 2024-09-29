import pymysql

conn = pymysql.connect(host='localhost', user='sample_user',
        password='1234', db='sample_db', 
        charset='utf8', port=3307)
curs = conn.cursor()

#f-String으로 쿼리문의 파라미터 설정 
sql = f"""delete from board where num='{input('삭제할일련번호:')}'"""

try:
    #쿼리문 실행 및 커밋     
    curs.execute(sql)
    conn.commit()
    print("1개의 레코드가 삭제됨")
except Exception as e:
    conn.rollback()
    print("쿼리 실행시 오류발생", e)

conn.close()