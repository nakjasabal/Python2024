from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 초기 투표 항목
poll_options = {
    "짜장면": 0,
    "탕수육": 0,
    "짬뽕": 0
}

@app.route('/')
def index():
    return render_template('index.html', options=poll_options)

@app.route('/vote', methods=['POST'])
def vote():
    selected_option = request.form['option']
    poll_options[selected_option] += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
