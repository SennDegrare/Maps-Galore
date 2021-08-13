# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 10:58:09 2021

@author: user
"""

#Since all points on the timeline are not equispaced, we use 
#Lagrange interpolation

#The arrays of x and y are as follows
x = [2009,2010,2011,2012,2013,2015]
y = [166.6, 473.2, 426.7, 318.3, 389.5, 458.5]

value = 2014
result = 0.0
for i in range(len(x)):

	# Computing individual terms of Lagrange interpolation
	term = y[i]
	for j in range(len(x)):
		if j != i:
			term = term * (value - x[j]) / (x[i] - x[j])

	# Result is appended by the term
	result += term

print("\nAnnual Rainfall in Rajasthan in", value,
	"is", round(result, 6), "mm")