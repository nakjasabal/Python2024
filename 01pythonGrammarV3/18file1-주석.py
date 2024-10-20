'''
open() 파일을 다룰때 사용되는 내장함수 첫번째 인자인 file경로만 필수사항
open(파일경로,mode,buffering,encoding)
mode:파일열기모드
r:읽기모드
w:쓰기모드
a:추가모드.파일의 마지막 부분에 새로운 내용을 추가한다.
b:2진모드(바이너리모드)로 컴퓨터가 알아볼 수 있는 파일을 생성한다.
t:텍스트모드로 디폴트값이다.사람이 알아볼 수 있는 텍스트파일을 생성한다.
'''
print("\n새파일01.txt 생성")
print("="*30)
'''
새로운 파일을 생성하여 반복문으로 내용을 입력한다.wt이므로 쓰기/텍스트 모드로 오픈한다.
'''
f_open=open("./saveFiles/새파일01.txt",mode='wt',encoding='utf-8')
#20번 반복하여 문자열 입력
for i in range(1,21):    
    #서식문자를 이용해서 문자열을 구성한다.
    data="%d번째 줄입니다.\n" % i
    #파일에 내용을 입력한다.
    f_open.write(data)
#파일 객체를 닫아준다.    
f_open.close()

### 여기까지 실행되면 파일은 생성된다. ###

#파일을 읽기/텍스트 모드로 오픈한다.(만약 파일이 없으면 에러발생됨)
f_read=open("./saveFiles/새파일01.txt",mode='rt',encoding='utf-8')    
while True:
    #파일 내용을 한줄씩 읽는다.
    line=f_read.readline()
    #더 이상 읽을 내용이 없다면 반복문을 탈출한다.
    if not line: break
    #내용 출력
    print(line)
f_read.close()

#기존 파일에 내용을 추가하기 위해 추가/텍스트 모드로 오픈한다.
f_add=open('./saveFiles/새파일01.txt',mode='at',encoding='utf-8')   
#한줄을 추가한다.개행문자가 없으므로 줄바꿈 처리는 되지 않는다. 
f_add.write("추가하는 내용입니다.")
f_add.writelines(["줄바꿈은 되나요?\n","안되면 개행문자를 넣어주세요."])           
f_add.write("마지막 라인입니다.")
f_add.close()


print("\n새파일02.txt 생성")
print("="*30)
#자동으로 파일객체를 open/close 할 수 있게 with~as를 사용한다.
with open("./saveFiles/새파일02.txt",mode='wt',encoding='utf-8') as myfile:
    #15줄의 문장을 입력하면 자동으로 close가 된다.
    for i in range(1,16):
        data="%d라인 입력합니다.\n" % i
        myfile.write(data)

#앞에서 생성된 파일을 읽기모드를 통해 내용을 출력한다.        
with open("./saveFiles/새파일02.txt",mode='rt',encoding='utf-8') as myfile:        
    line=None
    while line != '':
        line=myfile.readline()
        print(line.strip('\n'))        
