import requests
import pandas as pd

# 특정 회차의 로또 번호를 가져오는 함수
def get_lotto_numbers(draw_number):
    # 동행복권 API에서 특정 회차의 로또 정보를 가져옴
    url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={draw_number}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['returnValue'] == 'success':
            # 당첨 번호와 보너스 번호
            lotto_numbers = [
                data['drwtNo1'], data['drwtNo2'], data['drwtNo3'], 
                data['drwtNo4'], data['drwtNo5'], data['drwtNo6']
            ]
            bonus_number = data['bnusNo']
            return lotto_numbers, bonus_number
        else:
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

# 여러 회차의 로또 번호를 가져와서 엑셀에 저장하는 함수
def get_multiple_lotto_numbers_to_excel(start_draw, end_draw, file_name):
    # 데이터를 저장할 리스트
    all_lotto_data = []
    
    for draw_number in range(start_draw, end_draw + 1):
        result = get_lotto_numbers(draw_number)
        if result:
            lotto_numbers, bonus_number = result
            print(f"회차 {draw_number}: {lotto_numbers} + 보너스 {bonus_number}")
            
            # 회차 정보와 당첨 번호를 리스트에 추가
            all_lotto_data.append([draw_number] + lotto_numbers + [bonus_number])
        else:
            print(f"회차 {draw_number}에 대한 정보를 가져올 수 없습니다.")
    
    # 데이터를 DataFrame으로 변환
    df = pd.DataFrame(all_lotto_data, columns=[
        '회차', '번호1', '번호2', '번호3', '번호4', '번호5', '번호6', '보너스 번호'
    ])
    
    # DataFrame을 엑셀 파일로 저장
    df.to_excel(file_name, index=False)
    print(f"엑셀 파일로 저장되었습니다: {file_name}")

# 사용 예시
# start_draw = 1  # 시작 회차
# end_draw = 1140   # 끝 회차
# file_name = "lotto_numbers.xlsx"  # 저장할 엑셀 파일 이름
# get_multiple_lotto_numbers_to_excel(start_draw, end_draw, file_name)

#특정 회차 하나만 가져옴
start_draw = 1141  # 선택회차
result = get_lotto_numbers(start_draw)
print(result[0], result[1])

# 오라클 연동 후 입력
import oracledb
connection = oracledb.connect(
    user="musthave",         # Oracle DB 사용자 이름
    password="1234",     # 사용자 패스워드
    dsn="localhost/xe"  # 데이터베이스의 호스트 이름과 서비스 이름
)
# 커서 생성
cursor = connection.cursor()

# 쿼리문 작성
sql = f"insert into lotto values ('{start_draw}','{result[0][0]}','{result[0][1]}','{result[0][2]}','{result[0][3]}','{result[0][4]}','{result[0][5]}','{result[1]}')"
print('쿼리문', sql)

# 쿼리 실행
cursor.execute(sql)
connection.commit()

# 영향을 받은 행 수 확인
affected_rows = cursor.rowcount
print(f"{affected_rows} 행이 삽입되었습니다.")

# # 결과 출력
# for row in cursor:
#     print(row)

# 커서와 연결 닫기
cursor.close()
connection.close()