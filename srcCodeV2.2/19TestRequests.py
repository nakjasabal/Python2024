#s_content > div.section > ul > li:nth-child(1) > dl > dt > a

import requests
response = requests.get('http://nakja.co.kr/APIs/html/Crawling.html')

print(response.status_code) # 응답코드를 출력
print(response.text) # HTML 코드를 출력

https://kin.naver.com/search/list.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC