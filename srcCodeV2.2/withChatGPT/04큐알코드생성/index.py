'''
패키지 설치
pip install qrcode

질문] 파이썬으로 qr 코드를 생성하는 코드를 작성해줘
'''

import qrcode

# QR 코드에 포함할 데이터
#data = "https://nakja.tistory.com/"
data = "Hello World"

# QR 코드 인스턴스 생성
qr = qrcode.QRCode(
    version=1,  # 버전 1 (1부터 40까지, 버전이 높을수록 더 많은 데이터를 포함할 수 있음)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 수정 레벨 (L, M, Q, H 중 선택)
    box_size=10,  # QR 코드의 각 박스 크기
    border=4,  # 경계선 크기
)

# 데이터 추가
qr.add_data(data)
qr.make(fit=True)

# QR 코드 이미지 생성
img = qr.make_image(fill="black", back_color="white")

# QR 코드 이미지 저장
img.save("./saveFiles/qrcode2.png")

print("QR 코드가 'qrcode.png'에 생성되었습니다.")