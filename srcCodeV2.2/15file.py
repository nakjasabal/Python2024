'''
open()
  : 파일을 다룰때 사용되는 내장함수로 첫번째 인자인 file경로만 
  필수요소이다. 
  형식] open(파일경로, mode, buffering, encoding)
  
mode : 파일열기모드
  r : 읽기모드
  w : 쓰기모드
  a : 추가모드. 파일의 마지막 부분에 새로운 내용을 추가한다. 
  b : 2진모드(바이너리모드)로 컴퓨터가 알아볼수 있는 파일을 생성한다.  
  t : 텍스트모드로 defalut값이다. 사람이 알아볼 수 있는 형태의 텍스트
    파일을 생성한다. 메모장으로 열어서 보거나 편집할 수 있다. 

'''
print("="*30)
print("새파일01.txt")
print("="*30)

'''
새로운 파일을 생성한 후 반복문으로 내용을 입력한다. wt이므로 쓰기/텍스트
모드로 파일을 오픈한다. 인코딩 방식은 다국어를 지원하는 utf-8을 기본으로 
한다.
''' 
f_open = open("새파일01.txt", mode='wt', encoding='utf-8') 
#1~20까지 반복하여 문자열을 입력한다. 
for i in range(1, 21): 
    #서식문자를 이용해서 문장을 생성한다. 
    data = "%d번째 줄입니다.\n" % i
    f_open.write(data)      
#파일 객체를 닫아준다. 
f_open.close()

### 여기까지 실행하면 새파일01.txt 이 생성된다. ###

#파일 읽기 : rt이므로 텍스트파일을 읽기모드로 오픈한다.  
f_read = open("새파일01.txt", mode='rt', encoding='utf-8')
#모든 내용을 읽기전에는 몇줄인지 알수 없으므로 while문을 사용한다. 
while True: 
    #파일 내용 한줄을 읽는다. 
    line = f_read.readline()  
    #만약 더 이상 읽을내용이 없다면 반복문을 탈출한다.   
    #반복문 내에서 break를 만나면 반복문을 탈출한다. 
    if not line: break    
    #출력
    print(line)  
f_read.close()

### 새파일01.txt의 모든 내용이 출력된다. ###
 
# 기존 파일에 내용을 추가한다. 
f_add = open('새파일01.txt', mode='at', encoding='utf-8') 
# 한줄을 추가한다. 개행문자가 없으므로 줄바꿈 처리는 되지않는다.
f_add.write("추가하는 내용입니다.")  
# 리스트를 통해 여러줄의 내용을 추가한다. \n은 줄바꿈 기능을 하는 특수문자이다.
f_add.writelines(["줄바꿈은 되나요?\n", "안되면 개행문자를 넣어주세요."]) 
f_add.write("마지막 라인입니다.")
f_add.close()



print("="*30)
print("새파일02.txt")
print("="*30)  
'''
자동으로 파일객체를 닫기 위해  with open()과 같이 사용할 수 있다. 
파일에 15줄의 내용을 입력한 후 자동으로 close 해준다. 
'''
with open("새파일02.txt", mode='wt', encoding='utf-8') as myfile:
    for i in range(1, 16):
        data = "%d라인 입력합니다.\n" % i
        myfile.write(data)

# 파일의 내용을 읽어서 출력한다.          
with open("새파일02.txt", mode='rt', encoding='utf-8') as myfile:    
	line = None
	while line != '':
		line = myfile.readline()
		print(line.strip('\n'))

### 새파일02.txt 파일이 생성되고 내용을 읽어 출력한다. ###



'''
피클링(Pickling)
  : 파이썬 객체를 파일에 저장하는 과정을 의미한다. 반대로
  복원하는것을 언피클링이라고 한다. 
'''
#피클링을 위한 모듈 임포트 
import pickle 
 
#파일에 저장한 내용을 준비. 문자열, 숫자, 딕셔너리 등  
name = '개발자'  
age = 99   
address = '서울시 중구 세종대로'
times = {'JAVA': 20, 'HTML': 2, 'Oracle': 10, 'Python': 3} 

#쓰기모드로 바이너리 파일을 오픈한다. 이때 파일은 새롭게 생성된다. 
with open('developer.p', 'wb') as file: 
    #dump() 함수를 통해 데이터를 저장한다. 
    pickle.dump(name, file)  
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(times, file)
    
#바이너리 파일을 읽기모드로 오픈한 후 load()함수를 통해 복원한다.     
with open('developer.p', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    times = pickle.load(file)
    #복원한 내용을 출력한다. 
    print("이름", name)
    print("나이", age)
    print("주소", address)
    print("배당시간", times)
    
    
