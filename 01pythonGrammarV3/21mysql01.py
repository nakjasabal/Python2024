import pymysql 

conn = pymysql.connect(host='localhost', user='sample_user',
            password='1234', db='sample_db', charset='utf8')
curs = conn.cursor()

try:
    sql = "SELECT * FROM board"
    curs.execute(sql)

    rows = curs.fetchall()
    print('단순인출', rows)

    print(f"{'인출1':-^30}")
    for row in rows:
        print(row)

    print(f"{'인출2':-^30}")
    for row in rows:        
        print(row[0], row[1], row[2], end=" ")
        pdate = row[3]
        id = row[4]
        vcnt = row[5]
        print("%s, %s, %s" % (pdate, id, vcnt))
    
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


