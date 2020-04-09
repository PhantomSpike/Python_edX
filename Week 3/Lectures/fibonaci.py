#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 22:18:31 2019

@author: aleksandar
"""
from time import time as now

def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n==2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
def fib_efficient(n,d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1,d) + fib_efficient(n-2,d)
        d[n] = ans
        return ans
d = {1:1,2:2}

arg = 34
print('')
print('using fib')
t0 = now()
numFibCalls = 0
print(fib(arg))
print(now() - t0)
print('function calls',numFibCalls)
print('')
t0 = now()
print('using fib_efficient')
numFibCalls = 0
print(now() - t0)
print(fib_efficient(arg,d))
print('function calls',numFibCalls)
    