from googletrans import Translator

def translate_file(file_path):
    # 텍스트 파일 읽기
    with open(file_path, 'r') as file:
        english_text = file.read()

    # 번역기 생성
    translator = Translator()
    
    # 영어 텍스트를 한글로 번역
    translated_text = translator.translate(english_text, src='en', dest='ko')

    # 번역된 텍스트 출력
    print("번역된 한글 텍스트:")
    print(translated_text.text)

translate_file('./resData/Aegukga.txt')

