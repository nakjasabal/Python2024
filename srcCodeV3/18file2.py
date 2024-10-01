
'''피클링(Pickling)
    :파이썬 객체를 파일에 저장하는 과정을 의미.복원은 언피클링
'''        
import pickle

#파일에 저장한 내용을 준비,문자열,숫자,딕셔너리 등
name='개발자'        
age=99
address='서울시 중구 세종대로'
times={'JAVA':20,'HTML':2,'Oracle':10,'Python':3}

#쓰기모드로 바이너리 파일을 오픈.파일은 새롭게 생성.
with open('developer.p','wb') as file:
    #dump() 함수를 통해 데이터를 저장한다.
    pickle.dump(name,file)
    pickle.dump(age,file)
    pickle.dump(address,file)
    pickle.dump(times,file)

#바이너리 파일을 읽기모드로 오픈한 후 load()함수를 통해 복원.    
with open('developer.p','rb') as file:
    name=pickle.load(file)
    age=pickle.load(file)
    address=pickle.load(file)
    times=pickle.load(file)
    #복원된 내용을 출력.
    print("이름",name)
    print("나이",age)
    print("주소",address)
    print("배당시간",times)