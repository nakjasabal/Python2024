import pyttsx3

def text_to_speech(text):
    # pyttsx3 엔진 초기화
    engine = pyttsx3.init()

    # 텍스트를 음성으로 변환하여 출력
    engine.say(text)
    engine.runAndWait()

# 변환할 텍스트 입력
text = input("음성으로 변환할 텍스트를 입력하세요: ")

# 텍스트를 음성으로 변환하여 출력
text_to_speech(text)
