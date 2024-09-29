from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# 초기 투표 항목
poll_options = {
    "파타야": 0,
    "보라카이": 0,
    "세부": 0,
    "하노이": 0,
    "발리": 0
}

@app.route('/')
def index():
    return render_template('index.html', options=poll_options)

@app.route('/vote', methods=['POST'])
def vote():
    selected_option = request.form['option']
    poll_options[selected_option] += 1
    return redirect(url_for('index'))

@app.route('/result')
def result():
    # 그래프 생성
    options = list(poll_options.keys())
    votes = list(poll_options.values())

    plt.figure(figsize=(8, 6))
    plt.bar(options, votes)
    plt.xlabel('투표 항목')
    plt.ylabel('투표 수')
    plt.title('투표 결과')

    # 그래프를 이미지로 변환
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()

    # HTML 페이지에 그래프 이미지 삽입
    return render_template('result.html', graph_url=graph_url)

if __name__ == '__main__':
    app.run(debug=True)
