import requests
from bs4 import BeautifulSoup

def get_exchange_rate(base_currency, target_currency):
    # 웹사이트 URL 설정
    url = f"https://www.x-rates.com/calculator/?from={base_currency}&to={target_currency}&amount=1"

    # 요청 보내기
    response = requests.get(url)
    
    # HTML 파싱
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 환율 정보 추출
    # 웹사이트 구조에 따라 적절한 태그와 속성을 찾기
    rate_tag = soup.find('span', class_='ccOutputRslt')
    
    # 환율 변환 후 값 반환
    if rate_tag:
        rate_text = rate_tag.text.strip()
        rate = float(rate_text.split()[0])
        return rate
    else:
        print("환율 정보를 찾을 수 없습니다.")
        return None

def convert_currency(base_currency, target_currency, amount):
    # 환율을 얻습니다.
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    
    if exchange_rate is not None:
        # 금액을 환율에 따라 변환합니다.
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return None

def main():
    # 예시로 USD에서 EUR로 환율 변환을 합니다.
    base_currency = 'USD'
    target_currency = 'EUR'
    amount = 100  # 변환할 금액
    
    # 환율 변환을 수행합니다.
    converted_amount = convert_currency(base_currency, target_currency, amount)
    
    if converted_amount is not None:
        print(f'{amount} {base_currency}는 {converted_amount:.2f} {target_currency} 입니다.')
    else:
        print('환율 변환에 실패했습니다.')

if __name__ == "__main__":
    main()
