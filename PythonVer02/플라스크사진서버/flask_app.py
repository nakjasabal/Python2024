'''
pip install flask

질문
파이썬 플라스크 이용해서 사진을 보여주는 간단한 웹 서비스 만들어줘
'''

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# 사진 디렉토리 경로
IMAGE_DIR = 'static'
IMAGE_DIR = os.path.join('../../PythonVer02/플라스크사진서버/static')
print('zz', IMAGE_DIR)

@app.route('/')
def index():
    # index.html을 렌더링하여 홈 페이지를 표시합니다.
    return render_template('index.html')


@app.route('/list')
def list():
    # 이미지 디렉토리에서 모든 파일의 목록을 가져옵니다.
    images = [img for img in os.listdir(IMAGE_DIR) if img.endswith(('jpg', 'jpeg', 'png', 'gif'))]

    # index.html을 렌더링하여 홈 페이지를 표시합니다.
    return render_template('index2.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
