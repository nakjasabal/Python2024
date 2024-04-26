def chatbot():
    print("챗봇: 안녕하세요! 무엇을 도와드릴까요?")

    while True:
        user_input = input("사용자: ")  # 사용자 입력 받기
        
        # 입력된 메시지에 따라 응답을 정의합니다.
        if user_input in ["안녕", "안녕하세요"]:
            print("챗봇: 안녕하세요! 반갑습니다.")
        elif user_input in ["어때", "어떻게 지내?"]:
            print("챗봇: 잘 지내고 있어요! 당신은요?")
        elif user_input in ["고마워", "감사합니다"]:
            print("챗봇: 천만에요! 도와드릴 일이 또 있나요?")
        elif user_input in ["잘가", "안녕히 가세요"]:
            print("챗봇: 안녕히 가세요! 다음에 또 봐요.")
            break  # 대화를 종료합니다.
        else:
            print("챗봇: 죄송해요, 이해하지 못했어요. 다시 말씀해 주시겠어요?")

if __name__ == "__main__":
    chatbot()