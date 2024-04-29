'''
spaCy는 강력하고 효율적인 자연어 처리 라이브러리입니다. 문장 토큰화, 품사 태깅, 개체명 인식, 구문 분석 등의 다양한 기능을 제공합니다.
pip install spacy

이후, 한국어 언어 모델을 사용할 수 있도록 모델을 다운로드합니다.
python -m spacy download ko_core_news_sm


위 코드에서는 입력된 텍스트를 nlp 객체로 분석하여 다양한 NLP 기능을 수행합니다. 코드의 각 부분 설명:

토큰화 및 품사 태깅
: 입력된 텍스트를 토큰(단어 단위로 분리)하고 각 토큰의 품사 및 태그를 출력합니다.
개체명 인식
: 텍스트에서 사람, 장소, 조직 등 개체명 및 개체 유형을 인식하여 출력합니다.
구문 분석
: 텍스트의 각 문장을 파싱하여 구문 트리를 생성하고, 각 토큰의 부모 및 관계를 출력합니다.
구문 트리 시각화
: displacy를 사용하여 문장 구문 트리를 시각화합니다.

위 코드를 실행하면 사용자가 입력한 텍스트에 대한 분석 결과를 출력합니다. NLP 기능을 이용하여 입력된 텍스트를 이해하고 처리하는 데 사용할 수 있습니다.
'''
import spacy
from spacy import displacy

# 한국어 모델 로드
nlp = spacy.load('ko_core_news_sm')

def analyze_text(text):
    # 텍스트 분석
    doc = nlp(text)

    # 토큰화 및 품사 태깅
    print("토큰화 및 품사 태깅:")
    for token in doc:
        print(f"단어: {token.text}, 품사: {token.pos_}, 태그: {token.tag_}")

    # 개체명 인식
    print("\n개체명 인식:")
    for ent in doc.ents:
        print(f"텍스트: {ent.text}, 개체 유형: {ent.label_}")

    # 구문 분석
    print("\n구문 분석:")
    for sent in doc.sents:
        print(f"문장: {sent}")
        for token in sent:
            print(f"  단어: {token.text}, 품사: {token.pos_}, 부모: {token.head.text}, 관계: {token.dep_}")

    # 구문 트리 시각화
    displacy.render(doc, style='dep', jupyter=True)

# 메인 프로그램 실행
def main():
    # 분석할 텍스트 입력
    text = input("분석할 텍스트를 입력하세요: ")

    # 텍스트 분석
    analyze_text(text)

if __name__ == '__main__':
    main()
