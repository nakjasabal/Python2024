'''
pip install googletrans==4.0.0-rc1

파이썬으로 영어로 작성된 txt 파일의 내용을 읽어서 한글로 번역하는 프로그램을 작성해줘

영화 명대사를 영어로 10개 보여줘. 영화제목과 주인공 이름은 한글로 함께 보여줘. 
여기서 명대사만 추출해줘
추출한 명대사를 한글로 번역해줘
'''

from googletrans import Translator

def translate_file(file_path):
    """
    영어로 작성된 텍스트 파일의 내용을 읽어서 한글로 번역하는 함수.

    파라미터:
    file_path (str): 파일 경로.

    사용 예:
    translate_file('english_text.txt')
    """
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

# 함수 사용 예:
# 영어로 작성된 'english_text.txt' 파일의 내용을 한글로 번역하는 예제
translate_file('saveFiles/Aegukga.txt')