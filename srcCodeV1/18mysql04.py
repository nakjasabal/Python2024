import pymysql

conn = pymysql.connect(host='localhost', user='sample_user',
            password='1234', db='sample_db', charset='utf8')

curs = conn.cursor()

# 긴 문자열 중간에 변수를 삽입할때 f를 접두어로 붙히고, {}를 사용한다.
sql = f"""delete from board where num='{input('삭제할일련번호:')}'"""

try:    
    curs.execute(sql)
    # DB에 변경사항을 적용한다.
    conn.commit()
    print("1개의 레코드가 삭제됨")
except Exception as e:
    #오류가 발생하면 롤백한다.
    conn.rollback()
    print("쿼리 실행시 오류발생", e)

conn.close()