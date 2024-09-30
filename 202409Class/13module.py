'''
모듈
: 별도의 파이썬 파일로 생성해둔 프로그램을 불러와서 사용할 수 
있도록 함수나 변수 혹은 클래스를 모아둔것을 말한다. 
이런 모듈을 여러개 모아놓은 폴더를 패키지라고 한다. 
'''
'''
모듈 사용법1 : 모듈명만 임포트한다. 이 경우 사용할때 모듈명과
    함수명을 같이 기술해야한다. 
'''
import mod1
print("모듈의 함수호출1 :", mod1.add(3, 4))
print("모듈의 함수호출2 :", mod1.sub(4, 2))

'''
모듈 사용법2 : 모듈에서 특정한 함수만 임포트한다. 이 경우에는 
    함수명만 명시하여 호출하면된다. 
'''
from mod1 import add
result = add(3, 4)
print("결과 :", result)

'''
사용법3 : 방법2와 동일하지만 모든 함수를 한꺼번에 임포트하는
    방식이다. 모듈명 없이 함수를 호출할 수 있다. 
'''
from mod1 import *
result1 = add(3, 4)
print("결과 :", result1)
result2 = sub(3, 4)
print("결과 :", result2)

#mod2.py 를 임포트한다. 
import mod2  
result = mod2.mul(3, 4)
print(result)

'''
모듈을 업무의 목적에 맞게 나눠서 관리할때는 패키지를 사용한다. 
패키지는 윈도우에서 하나의 디렉토리(폴더)로 생성할 수 있다. 
''' 
#패키지명까지 포함한 형태로 함수를 호출
import commons.mod3   
commons.mod3.sum1To10()  

#특정함수만 임포트하는 경우에는 패키지명은 생략 가능 
from commons.mod3 import sum1To10
sum1To10()
