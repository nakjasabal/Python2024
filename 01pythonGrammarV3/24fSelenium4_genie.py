import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://www.genie.co.kr/chart/top200'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

song_data = [] 
rank = 1
for page in range(1, 5):
    print("페이지", page)
    driver.implicitly_wait(2) 
    songs = soup.select('tbody > tr') 
    for song in songs: 
        #제목
        title = song.select('a.title')[0].text.strip()
        #가수
        singer = song.select('a.artist')[0].text 
        song_data.append(['Genie', rank, title, singer])
        rank += 1    
    if page < 4 :
        driver.find_element(
            By.XPATH, 
            f'//*[@id="body-content"]/div[7]/a[{page+1}]'
        ).click() 
    driver.implicitly_wait(5)
    # 1~4페이지까지 페이지번호 링크를 누르면서 순차적으로 크롤링
    
columns = ['서비스','순위','타이틀','가수'] 
pd_data = pd.DataFrame(song_data, columns=columns)
print(pd_data.head())
pd_data.to_excel('./saveFiles/genie_chart.xlsx', index=False)

