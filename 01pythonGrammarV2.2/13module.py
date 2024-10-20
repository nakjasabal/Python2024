'''
모듈
    : 다른 파이썬 프로그램을 불러와서 사용할 수 있도록 만든 파일로
    함수나 변수 또는 클래스를 모아놓은것을 말한다. 
    모듈을 여러개 모아놓은 것을 패키지라고 한다. 
    형식]
        import 모듈명;
        import 모듈명 from 함수 
'''

'''
모듈 사용방법1 : 모듈명만 임포트한다. 이 경우 사용할때 모듈명과
함수명을 같이 기술해야한다. 
'''
import mod1
print("모듈의 함수호출1 :", mod1.add(3, 4))
print("모듈의 함수호출2 :", mod1.sub(4, 2))

'''
모듈 사용방법2 : 모듈에서 특정한 함수만 임포트한다. 이 경우에는 
    함수명만 명시하면 된다. 
'''
from mod1 import add
result = add(3, 4)
print("결과 :", result)

# 방법2와 동일하지만 모든 함수를 한꺼번에 임포트 하는 방식이다. 
from mod1 import *
result1 = add(3, 4)
print("결과 :", result1)
result2 = sub(3, 4)
print("결과 :", result2)

'''
__name__ 변수를 사용한 모듈로 이와같이 임포트하면 "mod2"가 
저장되므로 if문의 블럭은 실행되지 않는다. 
''' 
import mod2  
result = mod2.mul(3, 4)
print(result)
 
#모듈을 나눠서 관리할때는 패키지를 사용한다. 여러개의 모듈을
#업무에 맞게 나눠서 저장하는 것을 패키지라고 한다.  
import tjoeun.mod3   
#패키지명까지 포함한 형태로 함수를 호출한다. 
tjoeun.mod3.sum1To10()  

#이와같이 특정함수만 임포트하면 패키지명은 생략할 수 있다. 
from tjoeun.mod3 import sum1To10
sum1To10()  
    