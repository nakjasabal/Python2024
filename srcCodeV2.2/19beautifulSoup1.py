'''
뷰티플숩으로 웹크롤링을 하기 위해 2개의 패키지 설치가 필요
c:\> pip install requests
c:\> pip install beautifulsoup4
''' 
# 모듈 임포트 
import requests
from bs4 import BeautifulSoup

#크롤링할URL : 네이버 지식인에서 '파이썬'을 검색한 결과페이지
#한글인 경우 서버로 전송시 깨짐방지를 위해 인코딩 처리가 자동으로된다.  
url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
#get함수로 해당 페이지의 모든 출력 내용을 읽어온다. 
response = requests.get(url)

#응답코드가 200이면 통신에 성공한것으로 판단 
if response.status_code==200:  
    #페이지의 HTML코드를 텍스트형식으로 받아온다. 
    html = response.text  
    #데이터를 파싱하기 위해 HTML형식의 Soup객체로 변환한다. 
    soup = BeautifulSoup(html, 'html.parser') 
    
    # 검색결과에서 첫번째 제목을 선택 후 Selector 복사 
    title1_1 = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt > a')
    # print("추출1_1:", title1_1)
    
    # 셀렉터로 추출(파이어폭스)
    # title1_2 = soup.select_one('.basic1 > li:nth-child(1) > dl:nth-child(2) > dt:nth-child(1)')
    # print("추출1_2:", title1_2)

    # get_text() : 엘리먼트의 모든 태그를 제거한 후 텍스트만 추출
    text = title1_1.get_text()
    # print("추출2:", text)

    '''
    #s_content > div.section > ul
    검색결과 10개가 일정한 패턴으로 출력되므로 상위태그를 선택하면 
    항목의 갯수만큼 반복해서 파싱할 수 있다. 
    '''
    ul = soup.select_one('#s_content > div.section > ul')
    # print("추출3:", ul)

    '''
    검색 항목이 반복되는 ul을 앞에서 선택했으므로, 여기서는 하위의 
    a태그를 선택하고, 갯수만큼 반복하여 텍스트만 파싱한다. 
    '''
    print("추출4")
    titles2 = ul.select('li > dl > dt > a')
    for tit in titles2:
        print(tit.get_text())
else:
    print(response.status_code)

