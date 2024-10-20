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
        
        #검색결과 출력을 위한 변수 
        searchFlag = False
        searchName = input('검색할이름>> ')
        #list에 저장된 딕셔너리의 갯수만큼 반복
        i = 1
        for p in pList:
            #해당 회차의 딕셔너리에서 이름을 비교 
            if p['name'] == searchName:
                #검색할 이름이 있다면 True로 변경 
                searchFlag = True
                #찾는 이름이 있으면 출력 
                print("{:^3}{:^10}{:^15}{:^20}"
                    .format(i, p["name"], p["phone"], p["addr"]))
        #검색한 이름이 없다면 False를 유지하게 됨 
        if searchFlag == False:
            print('검색 결과가 없습니다.')        
        
    elif no == 4 :
        print("{:-^50}".format(" 수정기능 "))
        searchName = input('수정할이름 >> ')
        searchFlag = False
        #List에 저장된 데이터의 갯수만큼 반복. 인덱스까지 같이 반환.
        for i, v in enumerate(pList):
            #i:인덱스, v:딕셔너리가 회차마다 인출됨 
            #해당 회차의 이름과 비교 
            if v['name'] == searchName:
                searchFlag = True 
                #수정할 내용을 입력받아 딕셔너리로 정의 
                person = {}
                person['name'] = input('이름>>')
                person['phone'] = input ('전화>>')
                person['addr'] = input('주소>>')
                #생성된 딕셔너리를 리스트에서 수정(인덱스 사용함)
                pList[i] = person
                print('정보가 수정되었습니다.')
        if searchFlag == False:
            print('수정할 항목을 찾지 못했습니다.')
        
    elif no == 5 :
        print("{:-^50}".format(" 삭제기능 "))
        searchFlag = False
        searchName = input('삭제할이름 >>')
        for i, v in enumerate(pList):
            if v['name'] == searchName:
                searchFlag = True
                #해당 인덱스의 요소를 삭제 
                del pList[i]
                print('정보가 삭제되었습니다')
        if searchFlag == False:
            print('삭제할 항목이 없습니다')
        
    elif no == 6 :
        print("{:-^50}".format(" 종료합니다 "))
        break
    else :
        print("{:-^50}".format(" 번호를 잘못 입력하셨습니다 "))

    print() #공백 라인 추가

# end of while
print("프로그램종료~")
