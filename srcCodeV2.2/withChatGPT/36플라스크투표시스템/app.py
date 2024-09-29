from flask import Flask, render_template, request, redirect, url_for, send_file
import matplotlib.pyplot as plt
import io
from matplotlib import font_manager

#플라스크 앱 생성
app = Flask(__name__)

# 투표 항목과 그에 대한 투표 수를 저장할 딕셔너리
votes = {
    '아토스': 0,
    '포르토스': 0,
    '아라미스': 0,
    '달타냥': 0
}

# 한글 폰트 경로 지정
font_path = 'resData\malgun.ttf'

# 폰트 등록
font_manager.fontManager.addfont(font_path)
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = font_name

#루트경로 : http://127.0.0.1:5000/ 로 접속
@app.route('/')
def home():
    return render_template('vote.html', votes=votes)

'''
vote.html에서 항목을 선택한 후 '투표' 버튼을 누르면 
폼값은 post방식으로 /vote로 전달된다. 
'''
@app.route('/vote', methods=['POST'])
def vote():
    # 클라이언트에서 보낸 데이터를 수신
    selected_option = request.form.get('option')
    # 투표 수 증가
    if selected_option in votes:
        #만약 '아토스'를 선택했다면 votes[아토스]의 값을 1증가 시킨다. 
        votes[selected_option] += 1
    
    # 투표가 완료되면 결과 페이지로 리디렉션
    # return redirect(url_for('result1'))
    return redirect(url_for('result2'))

@app.route('/result1')
def result1():    
    # 투표 결과를 보여주는 페이지 렌더링
    return render_template('result1.html', votes=votes)

@app.route('/result2')
def result2():
    # 투표 결과를 그래프로 그리기 위해 투표 수와 항목을 가져옴
    labels = list(votes.keys())
    counts = list(votes.values())
    
    # 막대 그래프 생성
    plt.figure(figsize=(8, 6))
    plt.bar(labels, counts, color='blue')
    plt.xlabel('투표 항목')
    plt.ylabel('투표 수')
    plt.title('투표 결과')
    
    # 그래프를 메모리 버퍼에 저장
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    
    # 클라이언트에게 이미지 파일로 전송
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)