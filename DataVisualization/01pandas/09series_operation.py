# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(f"{'학생1':-^30}")
print(student1)
 
add_stu = student1 + 30
print(f"{'30 더한 후':-^30}")
print(add_stu)

student2 = pd.Series({'수학':80, '국어':np.nan, '영어':80})
print(f"{'학생2':-^30}")
print(student2)

addition = student1 + student2 # add() 함수로 대체 가능
subtraction = student1 - student2 # sub() 함수로 대체 가능
multiplication = student1.mul(student2, fill_value=0) 
division = student1.div(student2, fill_value=0) 

result = pd.DataFrame([addition, subtraction, multiplication, division], 
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(f"{'최종 데이터프레임':-^30}")
print(result)

