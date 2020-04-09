#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 15:35:20 2019

@author: aleksandar
"""

count = 0
move = 3
for j in range(len(s)-2):
    if 'bob' in s[j:j+move]:
        count += 1
print('Number of times bob occurs is: ' + str(count))