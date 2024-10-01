### 테스트1
import requests
response1 = requests.get('https://www.naver.com/')
# print(response1.status_code) # 응답코드를 출력
# print(response1.text) # HTML 코드를 출력


### 테스트2
'''
https://section.blog.naver.com/Search/Post.naver?
pageNo=1&
rangeType=ALL&
orderBy=sim&
keyword=웹크롤링
'''
paramJson = {
    'pageNo' : 1,
    'rangeType' : 'ALL',
    'orderBy' : 'sim',
    'keyword' : '파이썬 웹크롤링'
}
response2 = requests.get('https://section.blog.naver.com/Search/Post.nhn', params=paramJson)
# print(response2.status_code) # 응답코드를 출력
# print(response2.text) # HTML 코드를 출력


### 테스트3
import requests
from bs4 import BeautifulSoup

url = 'http://daum.net/'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
else : 
    print(response.status_code)
