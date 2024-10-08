# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
 
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1)
 
percentage = student1 / 200
print(percentage)
 
student2 = pd.Series({'수학':80, '국어':np.nan, '영어':80})
print(student2)
 
addition = student1 + student2 
subtraction = student1 - student2
multiplication = student1.mul(student2, fill_value=0) 
division = student1.div(student2, fill_value=0) 
 
result = pd.DataFrame([addition, subtraction, multiplication, division], 
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)

