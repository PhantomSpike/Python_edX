#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 18:49:07 2019

@author: aleksandar
"""

x = 27
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high+low)/2.0

while abs(ans**3 - x)> epsilon:
    print("low = " + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses+=1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (low + high)/2.0
print('numGuesses = '+ str(numGuesses))
print(str(ans) + ' is close to the sqrt of ' + str(x))