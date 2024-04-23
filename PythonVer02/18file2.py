'''
피클링(pickling)
    : 파이썬 객체를 파일에 저장하는 과정을 의미한다. 
    복원하는것은 언피클링이라고 한다. 
'''
import pickle #모듈 임포트
 
name = '국비교육' #문자열
days = 150 #숫자
times = {'JAVA': 20, 'HTML': 2, 'Oracle': 10, 'Python': 3} #딕셔너리
 
# 파일을 바이너리 쓰기(wb)로 오픈한다.
with open('study.p', 'wb') as file:
    pickle.dump(name, file) #dump()를 통해 저장
    pickle.dump(days, file)
    pickle.dump(times, file)
'''
앞에서 study.p 파일을 저장할때 dump()를 3번 사용하므로
복원할때는 load()를 3번 사용해야한다. 
저장한 순서 그대로 복원한다. 
'''
# 파일을 바이러너 읽기 모드로 오픈한다. 
with open('study.p', 'rb') as file:
    name = pickle.load(file)
    days = pickle.load(file)
    times = pickle.load(file)
    print("명칭", name)
    print("날짜", days)
    print("시수", times)