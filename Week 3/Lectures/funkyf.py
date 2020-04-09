#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:38:17 2019

@author: aleksandar
"""

def applyToEach(L,f):
    '''assumes L is a list,  a function 
    mutates L by replacing each element,
    e, of L by f(e)'''
    for i in range(len(L)):
        L[i] = f(L[i])
        
def applyFuns(F,x):
    for f in F:
        print(f(x))

for elt in map(abs,[1,-2,3,-4]):
    print(elt)
    
L1 = [1,28,36]
L2 = [2,57,9]

for elt in map(min,L1,L2):
    print(elt)
    
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1