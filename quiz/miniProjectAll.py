#폰북 리스트
pList = []

while True:
    print("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
    no = int(input("선택: "))
    if no == 1 :
        print("{:-^50}".format(" 입력기능 "))
        people = {}
        people["name"] = input("성명>>> ")
        people["phone"] = input("전화>>> ")
        people["addr"] = input("주소>>> ")
        pList.append(people)
        print("주소 입력 완료!")
    elif no == 2 :
        print("{:-^50}".format(" 출력기능 "))
        print("{:^3}{:^10}{:^15}{:^20}".format("번호", "성명", "전화", "주소") )
        print("-"*53)
        for i, p in enumerate(pList) :
            print("{:^3}{:^10}{:^15}{:^20}".format(i+1,p["name"],p["phone"],p["addr"]))
    elif no == 3 :
        print("{:-^50}".format(" 검색기능 "))
        searchFlag = False
        searchName = input("검색할성명>>> ")
        print("{:^3}{:^10}{:^15}{:^20}"
              .format("번호", "성명", "전화", "주소") )
        print("-"*53)
        i = 1
        for p in pList:
            if p['name'] == searchName:
                searchFlag = True
                print("{:^3}{:^10}{:^15}{:^20}"
                      .format(i+1,p["name"],p["phone"],p["addr"]))
        if searchFlag == False:
            print('검색결과가 없습니다')
    elif no == 4 :
        print("{:-^50}".format(" 수정기능 "))
        searchFlag = False
        searchName = input("수정할성명>>> ")
        #인덱스와 값 동시 인출
        for i, v in enumerate(pList):
            #일치하는 이름을 찾음
            if v['name'] == searchName:
                searchFlag = True
                #수정할 내용을 딕셔너리로 생성
                people = {}
                people["name"] = input("성명>>> ")
                people["phone"] = input("전화>>> ")
                people["addr"] = input("주소>>> ")
                #리스트에서 인덱스로 수정 
                pList[i] = people
                print('정보가 수정되었습니다.')
        if searchFlag == False:
            print('수정할 항목이 없습니다')
    elif no == 5 :
        print("{:-^50}".format(" 삭제기능 "))
        searchFlag = False
        searchName = input("삭제할성명>>> ")
        for i, v in enumerate(pList):
            if v['name'] == searchName:
                searchFlag = True
                del pList[i]
                print('정보가 삭제되었습니다.')
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












