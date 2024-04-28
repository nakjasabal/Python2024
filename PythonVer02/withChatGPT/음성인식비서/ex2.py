'''
pip install pyttsx3


'''

import speech_recognition as sr
import datetime
import webbrowser
import pyttsx3  # 텍스트를 음성으로 변환하기 위해 pyttsx3 사용

# 음성 인식기 및 텍스트를 음성으로 변환하는 엔진 생성
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# 마이크를 통해 음성 입력 받기
def listen_to_voice():
    with sr.Microphone() as source:
        print("음성을 인식 중입니다. 말씀해주세요...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    return audio

# 음성을 인식하여 텍스트로 변환
def recognize_voice(audio):
    try:
        text = recognizer.recognize_google(audio, language='ko-KR')
        return text
    except sr.UnknownValueError:
        return "음성을 인식할 수 없습니다."
    except sr.RequestError as e:
        return f"요청 에러: {e}"

# 사용자 명령에 따라 동작을 수행하는 함수
def execute_command(command):
    command = command.lower()  # 소문자로 변환
    if '안녕' in command:
        print("안녕하세요!")
        engine.say("안녕하세요!")
    elif '시간' in command:
        current_time = datetime.datetime.now().strftime('%H:%M')
        print(f"현재 시간은 {current_time}입니다.")
        engine.say(f"현재 시간은 {current_time}입니다.")
    elif '검색' in command:
        search_query = command.split('검색')[1].strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        print(f"{search_query} 검색을 시작합니다.")
        engine.say(f"{search_query} 검색을 시작합니다.")
    elif '계산' in command:
        # 간단한 수학 계산 기능 (예: "2 더하기 3 계산")
        try:
            expression = command.split('계산')[1].strip()
            result = eval(expression)
            print(f"계산 결과는 {result}입니다.")
            engine.say(f"계산 결과는 {result}입니다.")
        except:
            print("계산을 할 수 없습니다.")
            engine.say("계산을 할 수 없습니다.")
    else:
        print("지원하지 않는 명령입니다.")
        engine.say("지원하지 않는 명령입니다.")
    
    engine.runAndWait()

# 메인 프로그램 실행
def main():
    while True:
        audio = listen_to_voice()
        command = recognize_voice(audio)
        print(f"인식된 명령: {command}")
        execute_command(command)

if __name__ == '__main__':
    main()
