import requests
from bs4 import BeautifulSoup

def currency_converter(amount, from_currency, to_currency):
    """
    웹 크롤링을 이용한 환율 변환 함수

    파라미터:
    amount (float): 변환할 금액.
    from_currency (str): 원래 통화 코드 (예: 'USD' - 미국 달러).
    to_currency (str): 변환할 통화 코드 (예: 'KRW' - 한국 원).

    반환:
    float: 변환된 금액.

    사용 예:
    converted_amount = currency_converter(100, 'USD', 'KRW')
    print(f"100 USD to KRW: {converted_amount:.2f}")
    """
    # 환율 정보가 제공되는 웹사이트 URL
    url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={from_currency}&To={to_currency}"

    # 웹사이트에서 HTML 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 환율을 포함하는 요소 찾기
    #rate_element = soup.find('span', class_='uccResultAmount')

    

    result1 = soup.select_one('#__next > div:nth-child(4) > div.sc-2b1c5c79-0.frAgUY > section > div:nth-child(2) > div > main > div > div:nth-child(2) > div:nth-child(1) > div > p.sc-1c293993-0.hnFRxk').get_text()
    # print(result1)
    
    result2 = soup.select_one('#__next > div:nth-child(4) > div.sc-2b1c5c79-0.frAgUY > section > div:nth-child(2) > div > main > div > div:nth-child(2) > div:nth-child(1) > div > p.sc-1c293993-1.fxoXHw').get_text()
    # print(result2)

    return f'{result1} {result2}'




    # if rate_element:
    #     # 환율 추출
    #     exchange_rate = float(rate_element.text)
    #     # 금액 변환
    #     converted_amount = amount * exchange_rate
    #     return converted_amount
    # else:
    #     print("환율 정보를 찾을 수 없습니다.")
    #     return None

# 함수 사용 예:
# 100 USD를 KRW로 변환하는 예제
converted_amount = currency_converter(100, 'USD', 'KRW')
print(f"결과 : {converted_amount}")
