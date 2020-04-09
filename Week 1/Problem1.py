#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 15:26:39 2019

@author: aleksandar
"""

count = 0
vowels = 'aeiou'
for letter in s:
    if letter in vowels:
        count += 1
print('Number of vowels: ' + str(count))