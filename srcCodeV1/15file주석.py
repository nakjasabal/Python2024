'''
파일명 : 15file.py

파일을 다룰때 사용되는 내장함수로 첫번째 인자 file경로만 필수인자임
형식]
    open(File경로, mode='', buffering=-1, encoding='')
mode : 파일열기 모드
    r : 읽기모드.
    w : 쓰기모드.
    a : 추가모드. 파일의 마지막 부분에 새로운 내용을 추가할때 사용.

    b : 2진모드. 바이너리모드 라고도 하는데, 컴퓨터가 알아볼수 있는
        파일형식으로 생성한다. 
    t : 텍스트모드. 기본값. 사람이 알아볼 수 있는 형태의 텍스트
        파일을 생성한다. 차후 메모장으로 열수 있다. 
파일 객체는 반드시 열고 작업이 완료되면 닫아야한다.         
'''


print("="*30)
print("내파일01.txt")
print("="*30)

# 새로운 파일을 생성하여 반복문으로 내용 입력
# wt : 읽기모드. 텍스트모드 
f_open = open("./saveFiles/내파일01.txt", mode='wt', encoding='utf-8')
for i in range(1, 21):
    data = "%d번째 줄입니다.\n" % i
    f_open.write(data)
f_open.close()

#파일 읽기 
f_read = open("./saveFiles/내파일01.txt", mode='rt', encoding='utf-8')
while True:    
    line = f_read.readline() #파일 내용 한줄을 읽는다.
    if not line: break #더이상 읽을 내용을 없을때 반복문 탈출.
    print(line) #읽은 내용을 print()로 출력
f_read.close()

#기존파일에 내용 추가하기 
f_add = open('./saveFiles/내파일01.txt', mode='at', encoding='utf-8')
#한줄을 추가한다. 개행문자가 없어 줄바꿈처리가 되지 않는다. 
f_add.write("추가하는 내용입니다.") 
#리스트를 인자로 여러줄의 내용을 추가한다. 
f_add.writelines(["줄바꿈은 되나요?\n", "안되면 개행문자를 넣어주세요."]) 
f_add.write("마지막 라인입니다.")
f_add.close()


print("="*30)
print("내파일02.txt")
print("="*30)
#자동으로 파일 객체 닫기 및 여러줄 쓰기/읽기
#쓰기
with open("./saveFiles/내파일02.txt", mode='wt', encoding='utf-8') as myfile:
	for i in range(1, 16):
		data = "%d라인 입력합니다.\n" % i
		myfile.write(data)
#읽기
with open("./saveFiles/내파일02.txt", mode='rt', encoding='utf-8') as myfile:
	line = None
	while line != '':
		line = myfile.readline()
        #줄바꿈을 제거하지 않으면 두줄이 띄워진다.
		print(line.strip('\n'))


'''
피클링(pickling)
    : 파이썬 객체를 파일에 저장하는 과정을 의미한다. 
    복원하는것은 언피클링이라고 한다. 
'''
import pickle #모듈 임포트
 
name = '종각' # 문자열
age = 99    # 숫자
address = '서울시 종로구 관철동'
times = {'JAVA': 20, 'HTML': 2, 'Oracle': 10, 'Python': 3} #딕셔너리
 
# kosmo.p 파일을 바이너리 쓰기(wb)로 오픈한다.
with open('./saveFiles/jong-ro.p', 'wb') as file:
    pickle.dump(name, file) #dump()를 통해 저장
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(times, file)
'''
앞에서 kosmo.p 파일을 저장할때 dump()를 4번 사용하므로
복원할때는 load()를 4번 사용해야한다. 
저장한 순서 그대로 복원한다. 
'''
# 파일을 바이러너 읽기 모드로 오픈한다. 
with open('./saveFiles/jong-ro.p', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    times = pickle.load(file)
    print("이름", name)
    print("나이", age)
    print("주소", address)
    print("배당시간", times)