#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 12:51:50 2019

@author: aleksandar
"""

def f(y):
    x = 1
    x += 1
    print(x)
    
x = 5
f(x)
print(x)

def g(y):
    print(x)
    print(x+1)
    
x = 5
g(x)
print(x)

def h(y):
    x = x + 1
    
x = 5
h(x)
print(x)
    