import cv2

# 이미지 로드
def load_image(image_path):
    return cv2.imread(image_path)

# 얼굴 탐지 및 모자이크 처리 함수
def mosaic_faces(image, scaleFactor=1.1, minNeighbors=5):
    # 얼굴 탐지를 위한 Haar Cascade 로드
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 이미지를 그레이스케일로 변환 (얼굴 탐지 성능 향상)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이미지에서 얼굴을 탐지
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

    # 탐지된 얼굴에 대해 모자이크 처리
    for (x, y, w, h) in faces:
        # 얼굴 부분만 잘라서 작은 사이즈로 축소
        face_region = image[y:y+h, x:x+w]
        mosaic_face = cv2.resize(face_region, (w // 15, h // 15))
        
        # 다시 원래 크기로 확대 (모자이크 효과)
        mosaic_face = cv2.resize(mosaic_face, (w, h), interpolation=cv2.INTER_LINEAR)
        
        # 모자이크 처리된 얼굴을 원래 이미지에 덮어씌움
        image[y:y+h, x:x+w] = mosaic_face

    return image

# 결과 이미지 저장
def save_image(image, output_path):
    cv2.imwrite(output_path, image)

# 메인 함수
def main(input_image_path, output_image_path):
    # 이미지 로드
    image = load_image(input_image_path)
    
    # 얼굴 모자이크 처리
    image_with_mosaic = mosaic_faces(image)
    
    # 결과 이미지 저장
    save_image(image_with_mosaic, output_image_path)
    print(f"처리 완료: {output_image_path}")

# 실행 예시
input_image_path = 'aespa.jpg'  # 입력 이미지 경로
output_image_path = 'aespa-output.jpg'  # 출력 이미지 경로
main(input_image_path, output_image_path)
