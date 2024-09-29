'''
파이썬에서 MariaDB를 사용하기 위해서는 PyMySql을 설치해야한다. 
c:> pip install pymysql
'''
#모듈을 임포트 
import pymysql

#MariaDB에 접속한다. 이때 기본포트인 3306인 경우에는 port를 생략할 수 있다.
conn = pymysql.connect(host='localhost', user='sample_user',
        password='1234', db='sample_db', 
        charset='utf8', port=3307)
#커넥트 객체를 통해 커서를 생성.
curs = conn.cursor()

try:
    #board테이블의 모든 레코드를 인출하여 출력하는 쿼리문  
    sql = "SELECT * FROM board"
    #커서를 통해 쿼리를 실행 
    curs.execute(sql)

    #select한 모든 레코드를 인출 
    rows = curs.fetchall()
    print(rows)

    print('출력1', '-'*40)
    #인출한 레코드를 한 행씩 출력 
    for row in rows:
        #for문은 인출한 레코드를 순차적으로 한행씩 row로 넘겨준다.
        print(row)

    print('출력2', '-'*40)
    for row in rows:
        #행 단위로 출력하되 각 컬럼의 인덱스를 지정하여 출력한다. 
        print(row[0], row[1], row[2], end=" ")
        pdate = row[3]
        id = row[4]
        vcnt = row[5]
        print("%s, %s, %s" % (pdate, id, vcnt))
    
    #검색어를 통해 인출할 수 있는 like절을 사용한 쿼리문 
    print('출력3', '-'*40)
    sql = sql + " WHERE title like '%{0}%' ".format(input('검색어입력:'))
    #쿼리문을 실행한 후 조건에 맞는 모든 레코드를 인출한 후 출력 
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)
except Exception as e:
    print("쿼리 실행시 오류발생", e)

print('-'*40)
#DB작업 완료후에는 연결된 자원을 해제한다. 
conn.close()
print('자원반납')