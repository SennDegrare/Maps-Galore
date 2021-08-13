# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:48:08 2021

@author: user
"""

import random

list0 = [0,1,2]
ls = []
n="0"

while(len(ls)<4):
    

    index = random.randint(0,len(list0)-1)
    #print(index)

    if index ==0:
        n = str(random.randint(0,10))
    elif index == 1:
        n = str(chr(random.randint(97,123)))
    elif index == 2:
        n = str(chr(random.randint(65,91)))
    else:
        continue
    #print(n)
    ls.append(n)
    


#print(ls)

sr = "".join(ls)
print("Captcha is:", sr)
