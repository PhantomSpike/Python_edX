#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 15:45:14 2019

@author: aleksandar
"""
L = [1,2,3,4]
total = 0

for i in range(len(L)):
    total += L[i]
    
print(total)

total = 0
for i in L:
    total += i

print(total)