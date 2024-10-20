'''
음성인식 비서 만들기

패키지설치
pip3 install SpeechRecognition pyaudio

질문
파이썬으로 음성을 인식하여 텍스트로 변환하는 코드를 작성해줘. 한국어 음성이야. speech_recognition을 사용해서 만들어줘.
'''
import speech_recognition as sr

# 인식기 생성
recognizer = sr.Recognizer()

# 마이크 사용하여 음성 입력
with sr.Microphone() as source:
    print("음성을 인식 중입니다. 말씀해주세요...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    # 한국어로 음성을 인식하여 텍스트로 변환
    text = recognizer.recognize_google(audio, language='ko-KR')
    print("인식된 텍스트:", text)

except sr.UnknownValueError:
    print("음성을 인식할 수 없습니다.")
    
except sr.RequestError as e:
    print("요청 에러:", e)