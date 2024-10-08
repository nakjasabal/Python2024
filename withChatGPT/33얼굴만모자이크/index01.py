import cv2
import numpy as np

def mosaic_face(image_path, output_path, mosaic_scale=0.05):
    # 이미지 불러오기
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"이미지를 불러올 수 없습니다: {image_path}")

    # 그레이스케일로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 얼굴 감지기 불러오기 (OpenCV의 pre-trained 모델)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        raise ValueError("이미지에서 얼굴을 찾을 수 없습니다.")

    # 얼굴마다 모자이크 처리
    for (x, y, w, h) in faces:
        # 얼굴 영역 추출
        face_region = image[y:y+h, x:x+w]

        # 모자이크 처리
        small = cv2.resize(face_region, (int(w * mosaic_scale), int(h * mosaic_scale)), interpolation=cv2.INTER_LINEAR)
        mosaic_face = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)

        # 원본 이미지에 모자이크된 얼굴 덮어쓰기
        image[y:y+h, x:x+w] = mosaic_face

    # 결과 이미지 저장
    cv2.imwrite(output_path, image)
    print(f"모자이크 처리된 이미지를 저장했습니다: {output_path}")

# 예시 사용
try:
    mosaic_face('resserafim.jpg', 'resserafim-output.jpg')
except ValueError as e:
    print(f"오류 발생: {e}")
