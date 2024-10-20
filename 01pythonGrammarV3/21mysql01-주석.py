''''
파일명 : 18mysql01.py

파이썬에서 MySQL(or MariaDB)를 사용하기 위해서는
PyMySQL을 설치해야 한다. 

c:\> pip3 install pymysql
'''
import pymysql #모듈 임포트

#DB연결
conn = pymysql.connect(host='localhost', user='sample_user',
            password='1234', db='sample_db', charset='utf8')
'''
레코드를 인출할때 cursorclass부분을 주석처리하면 튜플로 
인출된다. 아래와같이 설정하면 딕셔너리로 인출된다. 
, cursorclass=pymysql.cursors.DictCursor
'''
#커서생성
curs = conn.cursor()

try:
    sql = "SELECT * FROM board"
    curs.execute(sql)

    #select한 모든 레코드 인출
    rows = curs.fetchall()
    print('단순인출', rows)

    print(f"{'인출1':-^30}")
    #행 단위로 인출한다. 
    for row in rows:
        print(row)

    print(f"{'인출2':-^30}")
    for row in rows:
        #행 단위로 인출하되 각 컬럼의 인덱스를 지정하여 인출한다. 
        print(row[0], row[1], row[2], end=" ")
        pdate = row[3]
        id = row[4]
        vcnt = row[5]
        print("%s, %s, %s" % (pdate, id, vcnt))
    
    #검색어를 통한 검색처리
    print(f"{'인출3':-^30}")
    sql = sql + " WHERE title like '%{0}%' ".format(input('검색어입력:'))
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)
except Exception as e:
    print("쿼리 실행시 오류발생", e)

print('-'*40)
conn.close()
print('자원반납')
