#셀레니움의 웹드라이버를 페이지에 임포트 
from selenium import webdriver
#크롬 드라이버를 로드한다. 이때 웹브라우저가 실행된다. 
driver = webdriver.Chrome()
#만약 실행되지 않는다면 패키지를 삭제 및 재설치를 진행해본다. 

'''
셀레니움은 웹브라우저를 이용해서 크롤링한 페이지를 띄운 후 데이터를
가져온다. 이때 비동기통신(Ajax)을 통해 데이터를 로드하는 경우에는 
조금 늦게 로딩되는 경우가 있으므로 '암묵적대기'가 필요한 경우가있다. 
이런경우를 대비해서 최대 5초간 대기한다. 만약 로딩이 빨리된다면
즉시 크롤링을 시작한다. 
'''
driver.implicitly_wait(5)

'''
time모듈을 사용하면 로딩과 상관없이 무조건 5초를 대기한다. 
이 함수는 반드시 필요한 경우에만 사용할것을 권장한다. 
'''
# import time
# time.sleep(5)

#멜론 실시간 챠트 페이지에 접속하여 정보(HTML소스)를 읽어온다. 
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)
html = driver.page_source

#셀레니움을 통해 읽어온 데이터를 뷰티플숩 객체로 변환한다. 
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

#파싱한 정보를 저장하기 위한 리스트를 생성한다. 
song_data = [] 
rank = 1
#챠트 테이블이 있는 엘리먼트의 셀렉터를 통해 반복되는 항목을 얻어온다.
songs = soup.select('tbody > tr') 
for song in songs: 
    #노래제목
    title = song.select('div.ellipsis.rank01 > span > a')[0].text 
    #가수
    singer = song.select('div.ellipsis.rank02 > a')[0].text 
    #좋아요 갯수
    favo = song.select('td:nth-child(8) > div > button > span.cnt')[0].text 
    
    print(title, singer, favo, sep="|")
    #파싱한 정보를 리스트에 추가한다. 
    song_data.append(['Melon', rank, title, singer, favo])
    #순위에 1을 더해준다. 
    rank += 1

#리스트에 저장된 내용을 엑셀로 저장하기위해 데이터프레임으로 변환한다.
import pandas as pd
#컬럼으로 사용할 리스트를 생성
columns = ['서비스','순위','타이틀','가수','좋아요'] 
#데이터프레임으로 변환시 컬럼을 추가 
pd_data = pd.DataFrame(song_data, columns=columns)
print(pd_data.head())
#엑셀 파일로 저장 
pd_data.to_excel('./saveFiles/melon_chart.xlsx', index=False)