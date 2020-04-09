#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:07:21 2019

@author: aleksandar
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
final_count = [0]*len(s)
for i in range(len(s)-1):
    letter = s[i]
    ix = alphabet.index(letter)
    j = 1
    count = 0
    while s[i+j] in alphabet[ix:]:
        ix = alphabet.index(s[i+j])
        count += 1
        j += 1
        if i+j>=len(s):
            break
    final_count[i] = count
max_val = max(final_count)
max_ix = final_count.index(max_val)  
        
            
print('Longest substring in alphabetical order is: ',s[max_ix:max_ix+max_val+1])