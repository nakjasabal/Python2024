'''
여러 장의 사진을 보여주는 플라스크 서비스를 만들어줘. static 폴더의 사진을 모두 보여줘.
'''

from flask import Flask, render_template
import os

app = Flask(__name__)

# static 폴더의 이미지 디렉토리 경로
IMAGE_DIR = os.path.join('../../PythonVer02/플라스크사진서버/static')
print('zz', IMAGE_DIR)

@app.route('/')
def index():
    # 이미지 디렉토리에서 모든 파일의 목록을 가져옵니다.
    images = [img for img in os.listdir(IMAGE_DIR) if img.endswith(('jpg', 'jpeg', 'png', 'gif'))]

    # index.html을 렌더링하여 홈 페이지를 표시합니다.
    return render_template('index2.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
