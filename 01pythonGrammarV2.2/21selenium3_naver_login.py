#셀레니움 모듈과 드라이버를 로드 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#셀레니움 크롬 드라이버 로드 
driver = webdriver.Chrome()
 
#네이버 접속  
url = 'https://www.naver.com/'
driver.get(url)

#메인화면에서 로그인 버튼을 Xpath로 찾은 후 클릭 
driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click()
#페이지 로딩과 상관없이 무조건 2초간 대기
time.sleep(2)

#<input> 태그의 name속성을 통해 엘리먼트를 찾음
#찾았다면 입력상자에 아이디와 비번을 입력
driver.find_element(By.NAME, 'id').send_keys('nakjasabal')
time.sleep(2) 
driver.find_element(By.NAME, 'pw').send_keys('7578120403!')
time.sleep(2)
#입력을 마친 후 로그인 버튼을 클릭
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
#네이버는 셀레니움으로 로그인 하는것을 인식하므로 캡챠화면이 
#뜨게되므로 30초 대기시간동안 사람이 직접 입력해야한다. 
time.sleep(30)

#로그인이 완료되면 메인화면으로 이동한다. 검색창에 검색어를 입력한다.
driver.find_element(By.NAME, 'query').send_keys('비트코인')
time.sleep(2)

#검색 버튼을 눌러 검색결과를 확인한다. 
driver.find_element(By.CLASS_NAME, 'btn_search').click()
time.sleep(10)