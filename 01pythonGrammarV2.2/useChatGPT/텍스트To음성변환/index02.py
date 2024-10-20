from gtts import gTTS
import os

def text_to_speech(text, lang='ko'):
    tts = gTTS(text=text, lang=lang)
    tts.save("./output.mp3")
    os.system("start ./output.mp3")

# 텍스트 입력
text = input("음성으로 변환할 텍스트를 입력하세요: ")

# 텍스트를 한글 음성으로 변환하여 출력
text_to_speech(text)
