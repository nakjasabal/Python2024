import requests
from bs4 import BeautifulSoup

def get_samsung_stock_price(myCode):
    # 네이버 증권
    url = f'https://finance.naver.com/item/main.naver?code={myCode}'
    
    # 페이지 요청
    response = requests.get(url)
    
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 주가 데이터를 포함하는 HTML 요소 선택
    # price_element = soup.select_one('.no_today .blind')
    price_element = soup.select_one('div > p.no_today > em')
    
    # 주가 데이터를 텍스트로 추출
    if price_element:
        current_price = price_element.get_text()
        # 금액이 2개씩 나오는 문제가 있음
        # print("결과:", current_price)
        # return current_price
        # 금액을 \n으로 split(분리)한 후 하나의 금액만 반환하도록 수정
        currList = current_price.split('\n')
        # print("결과:", currList[1])
        return currList[1]
    
    return None

# 나의 관심종목
myStockList = []
myStockList.append({'삼성전자':'005930'})
myStockList.append({'에코프로비엠':'247540'})
myStockList.append({'네이버':'035420'})
myStockList.append({'카카오':'035720'})

for dics in myStockList:
    #print(dics, dics.keys())
    for key, value in dics.items():
        # print(f"{key} : {value}")
        stockPrice = get_samsung_stock_price(value)
        if stockPrice:
            print(f"{key}의 현재가 : {stockPrice}원")
        else:
            print("{key}의 주가를 가져오는 데 실패했습니다.")
