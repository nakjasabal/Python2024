# -*- coding: utf-8 -*-
#셀레니움 모듈과 드라이버를 로드한다.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# driver.implicitly_wait(3) #암묵적 3초간 대기
# time.sleep(3) #로딩과 상관없이 3초간 대기
 
#네이버에 접속
url = 'https://www.naver.com/'
driver.get(url)

#로그인 버튼을 클릭
driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click()
time.sleep(2)

#로그인 페이지로 이동 후 아이디/비번 입력
#send_keys() : input태그에 지정한 값을 입력한다. 
#아이디 입력
driver.find_element(By.NAME, 'id').send_keys('nakjasabal')
time.sleep(2) 
#패스워드 입력
driver.find_element(By.NAME, 'pw').send_keys('7578120403!')
time.sleep(2)

# xpath로 지정한 엘리먼트를 클릭한다. 즉 로그인 버튼을 누른다.
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
#셀레니움 로그인을 감지하므로 캡챠화면을 뜨게된다. 
time.sleep(30)

#메인화면으로 돌아오면 검색어를 입력한다. 
driver.find_element(By.NAME, 'query').send_keys('비트코인')
time.sleep(2)

#검색 버튼을 눌러서 결과를 확인한다. 
driver.find_element(By.CLASS_NAME, 'btn_search').click()
time.sleep(10)