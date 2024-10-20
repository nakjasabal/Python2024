import requests
from bs4 import BeautifulSoup

def currency_converter(amount, from_currency, to_currency):
    # 환율 정보가 제공되는 웹사이트 URL
    url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={from_currency}&To={to_currency}"

    # 웹사이트에서 HTML 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    result1 = soup.select_one('#__next > div:nth-child(4) > div.sc-2b1c5c79-0.frAgUY > section > div:nth-child(2) > div > main > div > div:nth-child(2) > div:nth-child(1) > div > p.sc-1c293993-0.hnFRxk').get_text()
    # print(result1)
    
    result2 = soup.select_one('#__next > div:nth-child(4) > div.sc-2b1c5c79-0.frAgUY > section > div:nth-child(2) > div > main > div > div:nth-child(2) > div:nth-child(1) > div > p.sc-1c293993-1.fxoXHw').get_text()
    # print(result2)

    return f'{result1} {result2}'

# 함수 사용 예:
# 100 USD를 KRW로 변환하는 예제
converted_amount = currency_converter(100, 'USD', 'KRW')
print(f"결과 : {converted_amount}")

