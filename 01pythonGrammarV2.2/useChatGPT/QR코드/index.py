import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"./saveFiles/{file_name}")

# QR 코드 생성할 데이터 입력
data = input("QR 코드로 만들 텍스트를 입력하세요: ")

# 생성한 QR 코드 이미지 파일 이름 입력
file_name = input("저장할 QR 코드 이미지 파일의 이름을 입력하세요 (예: qrcode.png): ")

# QR 코드 생성
generate_qr_code(data, file_name)
print("QR 코드가 성공적으로 생성되었습니다.")
