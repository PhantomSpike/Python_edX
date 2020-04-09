#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 12:43:12 2019

@author: aleksandar
"""

def func_a():
    print('Inside func_a')
def func_b(y):
    print('Inside func_b')
    return y
def func_c(z):
    print('Inside func_c')
    return z()

print(func_a())
print(5 + func_b(2))
print(func_c(func_a))