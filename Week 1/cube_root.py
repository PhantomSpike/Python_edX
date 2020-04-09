#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 14:58:24 2019

@author: aleksandar
"""

x = int(input("Enter an integer: "))
ans = 0
while ans**3<x:
    ans = ans+1
if ans**3 != x:
    print(str(x)+' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))
        