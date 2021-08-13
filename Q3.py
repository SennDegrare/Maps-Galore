# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:11:02 2021

@author: user
"""

import pandas as pd

#We have three subjects S01,S02,S03 and three students
sub_marks = {'S01':[50,70,75], 'S02':[75,75,90], 'S03':[75,85,80]}


df = pd.DataFrame(sub_marks, index=["Satyabati","Ajit","Byomkesh"])

#Adding last marks row
marks4 = pd.Series(data = [70,80,75], index=df.columns, name="Anukul")
df = df.append(marks4)


df['sum'] = df['S01']+df['S02']+df['S03']


df['avg'] = df['sum']/3

print(df)

del df['sum']

import matplotlib.pyplot as plt

df.plot(kind='pie',y='avg', legend=None)
plt.show()