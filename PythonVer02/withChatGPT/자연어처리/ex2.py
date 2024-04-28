'''
nltk
: 자연어 처리를 위한 라이브러리입니다. 
pip install nltk

konlpy
한글 자연어 처리를 위한 라이브러리
한글 형태소 분석기를 제공하여，한글 문서에서 단어 단위로 분리하고 품사를 태깅할 수 있도록 도와줍니다. 
pip install konlpy
'''
from konlpy.tag import Okt
from nltk import FreqDist
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# 한글 글꼴 경로 설정
font_path = '../../PythonVer02/font/malgun.ttf'  # 예시 글꼴 경로
# 글꼴 설정 적용
font_prop = fm.FontProperties(fname=font_path, size=12)
plt.rcParams['font.family'] = font_prop.get_name()

# 형태소 분석기 생성
okt = Okt()

# 한글 텍스트 분석
def analyze_korean_text(text):
    # 형태소 분석을 통한 토큰화
    tokens = okt.morphs(text)

    # 토큰 빈도 분포 생성
    freq_dist = FreqDist(tokens)

    # 가장 빈도가 높은 토큰 10개 출력
    print("가장 빈도가 높은 토큰 10개:")
    for token, count in freq_dist.most_common(10):
        print(f"{token}: {count}회")

    # 토큰 빈도 분포 그래프 출력
    freq_dist.plot(30, title='토큰 빈도 분포')

# 메인 프로그램 실행
def main():
    # 분석할 텍스트 입력
    text = input("분석할 한글 텍스트를 입력하세요: ")

    # 한글 텍스트 분석
    analyze_korean_text(text)

if __name__ == '__main__':
    main()
