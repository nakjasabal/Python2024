#셀레니움 모듈과 드라이버를 로드한다.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'https://www.naver.com/'
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click()
time.sleep(2)

driver.find_element(By.NAME, 'id').send_keys('nakjasabal')
time.sleep(2) 
driver.find_element(By.NAME, 'pw').send_keys('본인의패스워드입력')
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
time.sleep(30)

driver.find_element(By.NAME, 'query').send_keys('셀레니움')
time.sleep(2)

driver.find_element(By.CLASS_NAME, 'btn_search').click()
time.sleep(10)


