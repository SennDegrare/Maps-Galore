# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:08:15 2021

@author: user
"""

#Two sequences as mentioned
s1 = '12233344456223566146'
s2 = '23322145614552234456'

#dictionary
d = {}


for i in range(0,len(s1)-2):
   #taking trigrams in s1
    ta = (s1[i], s1[i+1], s1[i+2])
    if ta in d:
        d[ta] +=1
    else:
        d[ta] = 1
        
for i in range(0,len(s2)-2):
    #taking trigrams in s2
    tb = (s2[i], s2[i+1], s2[i+2])
    if tb in d:
        d[tb] +=1
    else:
        d[tb] = 1


s3 = input("Enter a bigram: ")

#two digits of the bigram separated
num1 = s3[0]
num2 = s3[1]

b=[]
c=[]

#comparing bigram (given) to dictionary
for x in d:
    if(x[0] == num1 and x[1] == num2):
        b.append(x[2])
        c.append(d[x])

print("The most probable number that follows is", b[c.index(max(c))],
      "with probabilty", max(c)/sum(c))
