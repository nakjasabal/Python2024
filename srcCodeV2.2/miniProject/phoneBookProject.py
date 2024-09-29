'''
미니프로젝트] 폰북 만들기 
'''
#연락처를 저장하기 위한 List 생성 
pList = []
#조건을 True로 지정하여 무한루프로 반복문 구성 
while True:
    #제일 먼저 메뉴를 출력 
    print("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
    #번호를 입력 
    no = int(input("선택: "))
    if no == 1 :
        print("{:-^50}".format(" 입력기능 "))
        #딕셔너리 생성 
        people = {}
        #각 key에 입력값을 추가한다. 
        people["name"] = input("성명>>> ")
        people["phone"] = input("전화>>> ")
        people["addr"] = input("주소>>> ")
        #append()로 List에 딕셔너리 추가 
        pList.append(people)
        print("주소 입력 완료!")
    elif no == 2 :
        # format()함수를 통해 출력 : {인덱스:정렬 확보할공간}
        # 만약 인덱스를 생략하면 순서대로 0, 1, 2...으로 지정된다.
        # {:-^50} => 50칸을 확보한 후 -을 채우고, 텍스트를 가운데 출력한다. 
        print("{:-^50}".format(" 출력기능 "))
        # {:^3} : 3칸 확보 후 텍스트를 가운데 출력한
        print("{:^3}{:^10}{:^15}{:^20}"
              .format("번호", "성명", "전화", "주소") )
        # -을 53번 반복 출력
        print("-"*53)
        # enumerate() 함수는 집합형 자료를 받아서 갯수만큼 반복해준다.
        # 단, 자료의 인덱스까지 같이 반환해준다. 0부터 시작한다. 
        # 즉 i는 인덱스, p는 저장된 딕셔너리를 가리킨다. 
        for i, p in enumerate(pList) :
            #각 딕셔너리는 key를 통해 value를 출력한다. 
            print("{:^3}{:^10}{:^15}{:^20}"
                  .format(i+1,p["name"],p["phone"],p["addr"]))
    elif no == 3 :
        print("{:-^50}".format(" 검색기능 "))
        #1.검색할 이름을 입력
        #2.List의 크기만큼 반복한 후 검색할 이름이 있는지 확인
        #3.일치하는 이름이 있다면 출력
        
        
        
        
    elif no == 4 :
        print("{:-^50}".format(" 수정기능 "))
    elif no == 5 :
        print("{:-^50}".format(" 삭제기능 "))
    elif no == 6 :
        print("{:-^50}".format(" 종료합니다 "))
        break
    else :
        print("{:-^50}".format(" 번호를 잘못 입력하셨습니다 "))

    print() #공백 라인 추가

# end of while
print("프로그램종료~")



