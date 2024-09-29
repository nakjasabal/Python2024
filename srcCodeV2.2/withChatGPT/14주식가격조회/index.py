import requests
from bs4 import BeautifulSoup

def get_samsung_stock_price():
    # 네이버 증권에서 삼성전자의 주가 페이지 URL
    url = 'https://finance.naver.com/item/main.naver?code=005930'
    
    # 페이지 요청
    response = requests.get(url)
    
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 주가 데이터를 포함하는 HTML 요소 선택
    # price_element = soup.select_one('.no_today .blind')
    price_element = soup.select_one('div > p.no_today > em')
    
    # 주가 데이터를 텍스트로 추출
    if price_element:
        current_price = price_element.text.strip()
        # print("결과:", current_price)
        return current_price
    
    return None

# 삼성전자의 현재 주가 조회
samsung_price = get_samsung_stock_price()
if samsung_price:
    print(f"삼성전자의 현재 주가: {samsung_price}원")
else:
    print("삼성전자의 주가를 가져오는 데 실패했습니다.")