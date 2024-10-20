#모듈 임포트
#판다스 : 데이터 시각화를 위해 데이터프레임을 만들때 주로 사용됨.
#   여기서는 데이터를 엑셀로 저장하기 위해 사용함. 
import pandas as pd
#크롤링을 위한 셀레니움, 뷰티플숩 임포트 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

#크롬 드라이버를 통해 지니챠트200 페이지로 진입 
driver = webdriver.Chrome()
url = 'https://www.genie.co.kr/chart/top200'
driver.get(url)

#크롬이 실행되면 페이지의 모든 내용을 읽어와서 Soup객체로 변환 
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#순위데이터를 저장하기 위해 List를 생성 
song_data = [] 
rank = 1
#range()함수로 1~4까지 4번 반복 
for page in range(1, 5):
    print("페이지", page)
    #각 페이지로 진입한 후 묵시적으로 2초간 대기 
    driver.implicitly_wait(2) 
    #챠트가 출력되는 부분의 table 태그를 선택 
    songs = soup.select('tbody > tr') 
    for song in songs: 
        #제목
        title = song.select('a.title')[0].text.strip()
        #가수
        singer = song.select('a.artist')[0].text 
        '''
        앞에서 생성한 List에 데이터를 추가한다. 이 데이터는 List로
        생성한다. 즉 List에 List를 추가하는 형태가 된다. 
        '''
        song_data.append(['Genie', rank, title, singer])
        rank += 1    
    if page < 4 :
        #각 페이지 하단의 버튼을 눌러 다음페이지로 이동한다. 
        #4페이지가 마지막 이므로 4미만의 조건이 걸려있다. 
        #f-String으로 페이지번호에 해당하는 부분만 변수로 처리한다.
        driver.find_element(
            By.XPATH, 
            f'//*[@id="body-content"]/div[7]/a[{page+1}]'
        ).click() 
    driver.implicitly_wait(5)

#컬럼명으로 사용할 List 생성     
columns = ['서비스','순위','타이틀','가수'] 
#크롤링한 List를 데이터프레임으로 만든다. 이때 최상단은 컬럼을 추가한다.
pd_data = pd.DataFrame(song_data, columns=columns)
#데이터프레임 최상단의 5개 행을 보여준다. 
print(pd_data.head())
#엑셀 파일로 저장한다. 
pd_data.to_excel('./saveFiles/genie_chart.xlsx', index=False)

