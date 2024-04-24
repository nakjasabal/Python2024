# -*- coding: utf-8 -*-
#셀레니움을 임포트 한다. 
from selenium import webdriver
#크롬 드라이버를 로드한다. 이때 웹브라우저가 실행된다. 
driver = webdriver.Chrome('./sdriver/chromedriver-win64/chromedriver.exe')
#만약 실행되지 않는다면 라이브러리 설치와 드라이버 경로를 확인해본다. 
