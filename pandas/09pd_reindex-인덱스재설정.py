# -*- coding: utf-8 -*-
import pandas as pd 

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 
             'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
 
new_index = ['r0', 'r1', 'r2', 'r3', 'r4'] 
ndf = df.reindex(new_index)
print(ndf)
 
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf2 = df.reindex(new_index, fill_value=0)
print(ndf2)
 
ndf3 = ndf2.reset_index()
print(ndf3)
 
ndf4 = ndf3.sort_index(ascending=False)
print(ndf4) 

ndf5 = ndf4.sort_values(by='c3', ascending=True)
print(ndf5)









